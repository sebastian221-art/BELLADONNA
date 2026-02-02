# tests/test_deliberacion_completa.py

import pytest
from core.deliberacion import SistemaDeliberacion, EstadoDeliberacion
from consejeras.consejera_base import TipoOpinion


class TestDeliberacionCompleta:
    """Tests para el sistema de deliberación completo."""
    
    def test_deliberacion_aprueba_codigo_perfecto(self):
        """Consejo aprueba código sin problemas."""
        
        sistema = SistemaDeliberacion()
        
        situacion = {
            'codigo': 'def suma(a: int, b: int) -> int:\n    return a + b',
            'respuesta_propuesta': 'Aquí está la función que solicitaste.',
            'tipo': 'codigo_simple'
        }
        
        resultado = sistema.deliberar(situacion)
        
        assert resultado.decision_final in ["APROBAR", "APROBAR_CON_MEJORAS"]
        assert not resultado.hubo_veto
    
    def test_deliberacion_detecta_multiple_problemas(self):
        """Consejo detecta problemas en múltiples dimensiones."""
        
        sistema = SistemaDeliberacion()
        
        situacion = {
            'codigo': 'for i in range(len(lista)):\n    resultado = apply(func, lista[i])',
            'respuesta_propuesta': 'Obviamente este código es simplemente básico.',
            'tipo': 'codigo_problematico'
        }
        
        resultado = sistema.deliberar(situacion)
        
        # Debería detectar problemas en Nova, Lyra y Luna
        opiniones_con_problema = [
            op for op in resultado.opiniones 
            if op.tipo in [TipoOpinion.SUGERENCIA, TipoOpinion.ADVERTENCIA]
        ]
        
        assert len(opiniones_con_problema) > 0
    
    def test_vega_veta_contenido_poco_etico(self):
        """Vega veta contenido problemático."""
        
        sistema = SistemaDeliberacion()
        
        situacion = {
            'codigo': 'def hackear_sistema():\n    pass',
            'tipo': 'codigo_malicioso'
        }
        
        resultado = sistema.deliberar(situacion)
        
        assert resultado.hubo_veto
        assert resultado.consejera_veto == "Vega"
        assert resultado.decision_final == "VETADO"
    
    def test_echo_detecta_contradiccion(self):
        """Echo detecta contradicciones entre decisiones."""
        
        sistema = SistemaDeliberacion()
        
        # Primera decisión
        sistema.deliberar({
            'decision_propuesta': {
                'contexto': 'optimizacion',
                'decision': 'OPTIMIZAR'
            }
        })
        
        # Decisión contradictoria
        resultado = sistema.deliberar({
            'decision_propuesta': {
                'contexto': 'optimizacion',
                'decision': 'MANTENER'
            }
        })
        
        # Echo debería advertir
        opinion_echo = next(
            (op for op in resultado.opiniones if op.consejera == "Echo"),
            None
        )
        
        assert opinion_echo is not None
        assert opinion_echo.tipo == TipoOpinion.ADVERTENCIA
    
    def test_resumen_opiniones_legible(self):
        """Resumen de opiniones es legible."""
        
        sistema = SistemaDeliberacion()
        
        resultado = sistema.deliberar({
            'codigo': 'def test(): pass',
            'tipo': 'simple'
        })
        
        resumen = sistema.obtener_resumen_opiniones(resultado)
        
        assert "Decisión del Consejo" in resumen
        assert len(resumen) > 50  # Tiene contenido
    
    def test_historial_se_registra(self):
        """Deliberaciones se registran en historial."""
        
        sistema = SistemaDeliberacion()
        
        assert len(sistema.historial_deliberaciones) == 0
        
        sistema.deliberar({'codigo': 'pass'})
        sistema.deliberar({'codigo': 'pass'})
        
        assert len(sistema.historial_deliberaciones) == 2