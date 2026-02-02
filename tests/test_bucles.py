"""
Tests para bucles autónomos de pensamiento.
"""

import pytest
import asyncio
from bucles.pensamiento_continuo import BuclePensamientoContinuo
from bucles.evaluacion_interna import BucleEvaluacionInterna
from bucles.gestor_bucles import GestorBucles
from core.estado_interno import EstadoInterno


class TestBuclePensamientoContinuo:
    """Tests para BuclePensamientoContinuo."""
    
    def test_crear_bucle(self):
        """Test: Crear bucle."""
        bucle = BuclePensamientoContinuo()
        
        assert bucle.activo == False
        assert bucle.intervalo == 60
        assert len(bucle.eventos_detectados) == 0
    
    def test_registrar_interaccion(self):
        """Test: Registrar interacción actualiza timestamp."""
        bucle = BuclePensamientoContinuo()
        
        import time
        time.sleep(0.01)
        
        bucle.registrar_interaccion()
        
        tiempo_inactivo = bucle._calcular_tiempo_inactividad()
        assert tiempo_inactivo < 1.0
    
    def test_detectar_eventos_inactividad(self):
        """Test: Detectar eventos de inactividad."""
        bucle = BuclePensamientoContinuo()
        
        # Simular inactividad larga
        contexto = {
            'timestamp': None,
            'tiempo_desde_ultima_interaccion': 7300  # Más de 2 horas
        }
        
        eventos = bucle._detectar_eventos(contexto)
        
        assert len(eventos) > 0
        assert eventos[0]['tipo'] == 'INACTIVIDAD_LARGA'
    
    def test_debe_intervenir_severidad_alta(self):
        """Test: Intervenir cuando severidad es alta."""
        bucle = BuclePensamientoContinuo()
        
        evento = {
            'tipo': 'TEST',
            'severidad': 0.8
        }
        
        debe = bucle._debe_intervenir(evento)
        
        assert debe == True
    
    def test_no_intervenir_severidad_baja(self):
        """Test: No intervenir cuando severidad es baja."""
        bucle = BuclePensamientoContinuo()
        
        evento = {
            'tipo': 'TEST',
            'severidad': 0.3
        }
        
        debe = bucle._debe_intervenir(evento)
        
        assert debe == False
    
    def test_obtener_eventos(self):
        """Test: Obtener eventos detectados."""
        bucle = BuclePensamientoContinuo()
        
        bucle._programar_intervencion({
            'tipo': 'TEST',
            'descripcion': 'Evento de prueba'
        })
        
        eventos = bucle.obtener_eventos()
        
        assert len(eventos) == 1
        assert eventos[0]['tipo'] == 'TEST'
    
    def test_detener_bucle(self):
        """Test: Detener bucle."""
        bucle = BuclePensamientoContinuo()
        bucle.activo = True
        
        bucle.detener()
        
        assert bucle.activo == False


class TestBucleEvaluacionInterna:
    """Tests para BucleEvaluacionInterna."""
    
    def test_crear_bucle(self):
        """Test: Crear bucle."""
        estado = EstadoInterno()
        bucle = BucleEvaluacionInterna(estado)
        
        assert bucle.activo == False
        assert bucle.intervalo == 120
        assert len(bucle.historial_metricas) == 0
    
    def test_calcular_metricas(self):
        """Test: Calcular métricas."""
        estado = EstadoInterno(
            coherencia_proposito=0.8,
            confianza_conocimiento=0.7,
            carga_cognitiva=0.4
        )
        bucle = BucleEvaluacionInterna(estado)
        
        metricas = bucle._calcular_metricas()
        
        assert metricas['coherencia'] == 0.8
        assert metricas['confianza'] == 0.7
        assert metricas['carga'] == 0.4
    
    def test_detectar_sobrecarga(self):
        """Test: Detectar sobrecarga cognitiva."""
        estado = EstadoInterno(carga_cognitiva=0.9)
        bucle = BucleEvaluacionInterna(estado)
        
        metricas = bucle._calcular_metricas()
        problemas = bucle._detectar_problemas(metricas)
        
        assert len(problemas) > 0
        assert any(p['tipo'] == 'SOBRECARGA' for p in problemas)
    
    def test_detectar_deriva_proposito(self):
        """Test: Detectar deriva de propósito."""
        estado = EstadoInterno(coherencia_proposito=0.5)
        bucle = BucleEvaluacionInterna(estado)
        
        metricas = bucle._calcular_metricas()
        problemas = bucle._detectar_problemas(metricas)
        
        assert len(problemas) > 0
        assert any(p['tipo'] == 'DERIVA_PROPOSITO' for p in problemas)
    
    def test_sin_problemas(self):
        """Test: Sin problemas cuando métricas son normales."""
        estado = EstadoInterno(
            coherencia_proposito=0.9,
            carga_cognitiva=0.3
        )
        bucle = BucleEvaluacionInterna(estado)
        
        metricas = bucle._calcular_metricas()
        problemas = bucle._detectar_problemas(metricas)
        
        assert len(problemas) == 0
    
    def test_obtener_historial(self):
        """Test: Obtener historial de métricas."""
        estado = EstadoInterno()
        bucle = BucleEvaluacionInterna(estado)
        
        # Simular registro
        bucle.historial_metricas.append({
            'timestamp': None,
            'metricas': {},
            'problemas': []
        })
        
        historial = bucle.obtener_historial()
        
        assert len(historial) == 1
    
    def test_detener_bucle(self):
        """Test: Detener bucle."""
        estado = EstadoInterno()
        bucle = BucleEvaluacionInterna(estado)
        bucle.activo = True
        
        bucle.detener()
        
        assert bucle.activo == False


class TestGestorBucles:
    """Tests para GestorBucles."""
    
    def test_crear_gestor(self):
        """Test: Crear gestor."""
        estado = EstadoInterno()
        gestor = GestorBucles(estado)
        
        assert gestor.bucle_pensamiento is not None
        assert gestor.bucle_evaluacion is not None
    
    def test_registrar_interaccion(self):
        """Test: Registrar interacción propaga a bucles."""
        estado = EstadoInterno()
        gestor = GestorBucles(estado)
        
        gestor.registrar_interaccion()
        
        # Verificar que se registró
        tiempo = gestor.bucle_pensamiento._calcular_tiempo_inactividad()
        assert tiempo < 1.0
    
    def test_detener_todos(self):
        """Test: Detener todos los bucles."""
        estado = EstadoInterno()
        gestor = GestorBucles(estado)
        
        # Activar bucles
        gestor.bucle_pensamiento.activo = True
        gestor.bucle_evaluacion.activo = True
        
        gestor.detener_todos()
        
        assert gestor.bucle_pensamiento.activo == False
        assert gestor.bucle_evaluacion.activo == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])