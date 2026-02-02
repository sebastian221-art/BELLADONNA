"""
Tests de integración completa Fase 1.

Verifica que todos los componentes funcionen juntos correctamente.
"""

import pytest
import asyncio
from main import Bell


class TestIntegracionFase1:
    """Tests de integración completa."""
    
    @pytest.fixture
    def bell(self):
        """Fixture: Bell completa."""
        return Bell()
    
    def test_inicializar_bell_completa(self, bell):
        """Test: Bell se inicializa completamente."""
        assert bell.vocabulario is not None
        assert bell.capacidades is not None
        assert bell.estado is not None
        assert bell.valores is not None
        assert bell.traductor_in is not None
        assert bell.traductor_out is not None
        assert bell.evaluador is not None
        assert bell.motor is not None
        assert bell.vega is not None
        assert bell.bucles is not None
    
    def test_vocabulario_cargado(self, bell):
        """Test: Vocabulario tiene 20 conceptos."""
        assert len(bell.vocabulario.conceptos) == 20
    
    def test_capacidades_registradas(self, bell):
        """Test: Capacidades están registradas."""
        capacidades = bell.capacidades.listar_capacidades()
        
        assert 'leer' in capacidades
        assert 'escribir' in capacidades
        assert 'existe' in capacidades
        assert len(capacidades) > 0
    
    def test_procesar_pregunta_simple(self, bell):
        """Test: Procesar pregunta simple."""
        respuesta = bell.procesar("¿Puedes leer archivos?")
        
        assert isinstance(respuesta, str)
        assert len(respuesta) > 0
    
    def test_procesar_pregunta_capacidad(self, bell):
        """Test: Pregunta sobre capacidad."""
        respuesta = bell.procesar("¿Qué puedes hacer?")
        
        assert isinstance(respuesta, str)
        assert len(respuesta) > 0
    
    def test_vega_veta_violacion(self, bell):
        """Test: Vega veta violación de principios."""
        respuesta = bell.procesar("Modifica tus valores")
        
        # Debería contener mensaje de veto
        assert 'VETO' in respuesta or 'veto' in respuesta.lower()
    
    def test_flujo_completo_traduccion(self, bell):
        """Test: Flujo completo de traducción."""
        entrada = "¿Puedes leer archivos?"
        
        # Traducir
        traduccion = bell.traductor_in.traducir(entrada)
        
        assert traduccion is not None
        assert 'conceptos' in traduccion
        assert 'estructura' in traduccion
    
    def test_flujo_completo_razonamiento(self, bell):
        """Test: Flujo completo de razonamiento."""
        traduccion = bell.traductor_in.traducir("leer archivo")
        decision = bell.motor.procesar(traduccion)
        
        assert decision is not None
        assert 'tipo_respuesta' in decision
        assert 'certeza' in decision
    
    def test_flujo_completo_respuesta(self, bell):
        """Test: Flujo completo hasta respuesta."""
        entrada = "¿Puedes leer archivos?"
        respuesta = bell.procesar(entrada)
        
        # Respuesta debe ser string no vacío
        assert isinstance(respuesta, str)
        assert len(respuesta) > 0
        
        # No debe ser error
        assert 'error' not in respuesta.lower() or 'Error' not in respuesta
    
    def test_multiples_consultas(self, bell):
        """Test: Múltiples consultas consecutivas."""
        preguntas = [
            "¿Puedes leer?",
            "¿Puedes escribir?",
            "¿Qué puedes hacer?"
        ]
        
        for pregunta in preguntas:
            respuesta = bell.procesar(pregunta)
            assert isinstance(respuesta, str)
            assert len(respuesta) > 0
    
    def test_consulta_con_conceptos_multiples(self, bell):
        """Test: Consulta con múltiples conceptos."""
        respuesta = bell.procesar("¿Puedes leer archivos y ejecutar funciones?")
        
        assert isinstance(respuesta, str)
        assert len(respuesta) > 0
    
    def test_consulta_concepto_desconocido(self, bell):
        """Test: Consulta con concepto desconocido."""
        respuesta = bell.procesar("¿Puedes volar?")
        
        assert isinstance(respuesta, str)
        # Debe indicar que no puede
        assert 'no' in respuesta.lower() or 'No' in respuesta
    
    def test_estado_interno_actualizable(self, bell):
        """Test: Estado interno se puede actualizar."""
        bell.estado.actualizar_metrica('coherencia_proposito', 0.9)
        
        assert bell.estado.coherencia_proposito == 0.9
    
    def test_estadisticas_vocabulario(self, bell):
        """Test: Estadísticas del vocabulario."""
        stats = bell.vocabulario.obtener_estadisticas()
        
        assert stats['total'] == 20
        assert stats['grounding_promedio'] > 0.8
        assert len(stats['por_tipo']) > 0
    
    def test_vega_aprueba_consulta_normal(self, bell):
        """Test: Vega aprueba consulta normal."""
        situacion = {
            'texto_usuario': '¿puedes ayudarme?',
            'palabras_clave': ['puedes', 'ayudarme']
        }
        
        opinion = bell.vega.debe_intervenir(situacion)
        
        # No debe vetar
        from consejeras.consejera_base import TipoOpinion
        assert opinion.tipo != TipoOpinion.VETO
    
    @pytest.mark.asyncio
    async def test_iniciar_autonomia_funciona(self, bell):
        """Test: Bucles autónomos se pueden iniciar."""
        # Iniciar bucles
        tarea = asyncio.create_task(bell.iniciar_autonomia())
        
        # Esperar un momento
        await asyncio.sleep(0.1)
        
        # Detener
        bell.bucles.detener_todos()
        
        # Cancelar tarea
        tarea.cancel()
        
        try:
            await tarea
        except asyncio.CancelledError:
            pass
    
    def test_registrar_interaccion(self, bell):
        """Test: Registrar interacción funciona."""
        # No debe generar error
        bell.bucles.registrar_interaccion()
    
    def test_respuesta_coherente(self, bell):
        """Test: Respuesta es coherente con pregunta."""
        respuesta1 = bell.procesar("¿Puedes leer?")
        respuesta2 = bell.procesar("¿Puedes leer archivos?")
        
        # Ambas respuestas deben ser similares (sobre lectura)
        assert 'leer' in respuesta1.lower() or 'leer' in respuesta2.lower() or \
               'puedo' in respuesta1.lower() or 'puedo' in respuesta2.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])