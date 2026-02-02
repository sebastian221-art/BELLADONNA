"""
Tests para EstadoInterno - Métricas funcionales de Bell.
"""

import pytest
from core.estado_interno import EstadoInterno


class TestEstadoInterno:
    """Tests para EstadoInterno."""
    
    def test_crear_estado_inicial(self):
        """Test: Crear estado con valores por defecto."""
        estado = EstadoInterno()
        
        assert estado.coherencia_proposito == 1.0
        assert estado.confianza_conocimiento == 0.5
        assert estado.utilidad_intervenciones == 0.7
        assert estado.carga_cognitiva == 0.3
        assert estado.alineacion_usuario == 0.8
        assert estado.tasa_aprendizaje == 0.0
    
    def test_crear_estado_personalizado(self):
        """Test: Crear estado con valores personalizados."""
        estado = EstadoInterno(
            coherencia_proposito=0.8,
            confianza_conocimiento=0.9,
            carga_cognitiva=0.5
        )
        
        assert estado.coherencia_proposito == 0.8
        assert estado.confianza_conocimiento == 0.9
        assert estado.carga_cognitiva == 0.5
    
    def test_actualizar_metrica_valida(self):
        """Test: Actualizar métrica con valor válido."""
        estado = EstadoInterno()
        
        estado.actualizar_metrica('coherencia_proposito', 0.6)
        assert estado.coherencia_proposito == 0.6
        
        estado.actualizar_metrica('carga_cognitiva', 0.9)
        assert estado.carga_cognitiva == 0.9
    
    def test_actualizar_metrica_fuera_rango(self):
        """Test: Actualizar métrica con valor fuera de rango debe fallar."""
        estado = EstadoInterno()
        
        with pytest.raises(ValueError):
            estado.actualizar_metrica('coherencia_proposito', 1.5)
        
        with pytest.raises(ValueError):
            estado.actualizar_metrica('confianza_conocimiento', -0.1)
    
    def test_actualizar_metrica_inexistente(self):
        """Test: Actualizar métrica inexistente debe fallar."""
        estado = EstadoInterno()
        
        with pytest.raises(AttributeError):
            estado.actualizar_metrica('metrica_inventada', 0.5)
    
    def test_obtener_resumen(self):
        """Test: Obtener resumen del estado."""
        estado = EstadoInterno()
        resumen = estado.obtener_resumen()
        
        assert 'coherencia' in resumen
        assert 'confianza' in resumen
        assert 'utilidad' in resumen
        assert 'carga' in resumen
        assert 'alineacion' in resumen
        assert 'aprendizaje' in resumen
        assert 'ultima_actualizacion' in resumen
    
    def test_resumen_valores_correctos(self):
        """Test: Resumen contiene valores correctos."""
        estado = EstadoInterno(
            coherencia_proposito=0.7,
            confianza_conocimiento=0.8
        )
        
        resumen = estado.obtener_resumen()
        
        assert resumen['coherencia'] == 0.7
        assert resumen['confianza'] == 0.8
    
    def test_ultima_actualizacion_cambia(self):
        """Test: Última actualización cambia al modificar métrica."""
        estado = EstadoInterno()
        
        import time
        time.sleep(0.01)
        
        estado.actualizar_metrica('coherencia_proposito', 0.9)
        
        # La última actualización debe ser reciente
        from datetime import datetime
        delta = datetime.now() - estado.ultima_actualizacion
        assert delta.total_seconds() < 1
    
    def test_metricas_en_rango_valido(self):
        """Test: Todas las métricas están en rango válido [0.0, 1.0]."""
        estado = EstadoInterno()
        resumen = estado.obtener_resumen()
        
        for metrica, valor in resumen.items():
            if metrica != 'ultima_actualizacion':
                assert 0.0 <= valor <= 1.0, f"Métrica {metrica} fuera de rango: {valor}"
    
    def test_repr(self):
        """Test: Representación en string."""
        estado = EstadoInterno(
            coherencia_proposito=0.85,
            confianza_conocimiento=0.75
        )
        
        repr_str = repr(estado)
        assert 'EstadoInterno' in repr_str
        assert '0.85' in repr_str
        assert '0.75' in repr_str
    
    def test_cambios_multiples_metricas(self):
        """Test: Cambiar múltiples métricas."""
        estado = EstadoInterno()
        
        estado.actualizar_metrica('coherencia_proposito', 0.6)
        estado.actualizar_metrica('confianza_conocimiento', 0.7)
        estado.actualizar_metrica('carga_cognitiva', 0.8)
        
        assert estado.coherencia_proposito == 0.6
        assert estado.confianza_conocimiento == 0.7
        assert estado.carga_cognitiva == 0.8
    
    def test_valores_limite(self):
        """Test: Valores en límites del rango."""
        estado = EstadoInterno()
        
        # Límite inferior
        estado.actualizar_metrica('coherencia_proposito', 0.0)
        assert estado.coherencia_proposito == 0.0
        
        # Límite superior
        estado.actualizar_metrica('confianza_conocimiento', 1.0)
        assert estado.confianza_conocimiento == 1.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])