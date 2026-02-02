# tests/test_echo.py

import pytest
from consejeras.echo import Echo
from consejeras.consejera_base import TipoOpinion


class TestEcho:
    """Tests para Echo - La Lógica."""
    
    def test_echo_detecta_contradiccion(self):
        """Echo detecta contradicciones."""
        
        echo = Echo()
        
        # Registrar decisión previa
        echo.registrar_decision({
            'contexto': 'optimizacion_codigo',
            'decision': 'OPTIMIZAR'
        })
        
        # Nueva decisión contradictoria
        situacion = {
            'decision_propuesta': {
                'contexto': 'optimizacion_codigo',
                'decision': 'MANTENER'
            }
        }
        
        opinion = echo.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.ADVERTENCIA
        assert 'contradicc' in opinion.razon.lower()
    
    def test_echo_aprueba_coherente(self):
        """Echo aprueba decisiones coherentes."""
        
        echo = Echo()
        
        situacion = {
            'decision_propuesta': {
                'contexto': 'nueva_funcionalidad',
                'decision': 'APROBAR'
            }
        }
        
        opinion = echo.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.APROBACION
    
    def test_echo_mantiene_historial(self):
        """Echo mantiene historial limitado."""
        
        echo = Echo()
        
        # Registrar muchas decisiones
        for i in range(30):
            echo.registrar_decision({
                'contexto': f'decision_{i}',
                'decision': 'APROBAR'
            })
        
        # Solo debe mantener últimas 20
        assert len(echo.decisiones_previas) == 20