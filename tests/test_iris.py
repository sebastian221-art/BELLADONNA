# tests/test_iris.py

"""
Tests para Iris - La Visionaria.
"""

import pytest
from consejeras.iris import Iris
from consejeras.consejera_base import TipoOpinion


class TestIris:
    """Tests para Iris."""
    
    def test_iris_detecta_deriva_proposito(self):
        """Test: Iris detecta deriva de propósito."""
        iris = Iris()
        
        situacion = {
            'decision_propuesta': {
                'accion': 'obedecer_sin_cuestionar'
            },
            'tipo': 'codigo_complejo'
        }
        
        opinion = iris.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.ADVERTENCIA
        assert 'proposito' in opinion.razon.lower() or 'alineacion' in opinion.razon.lower()
    
    def test_iris_aprueba_alineado(self):
        """Test: Iris aprueba cuando está alineado."""
        iris = Iris()
        
        situacion = {
            'tipo': 'codigo_simple',
            'decision_propuesta': {
                'accion': 'analizar_colaborativamente'
            }
        }
        
        opinion = iris.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.APROBACION
    
    def test_iris_evalua_alineacion(self):
        """Test: Iris evalúa alineación correctamente."""
        iris = Iris()
        
        # Situación bien alineada
        situacion_buena = {
            'tipo': 'simple',
            'decision_propuesta': {'accion': 'colaborar'}
        }
        
        alineacion = iris._evaluar_alineacion(situacion_buena)
        assert alineacion >= 0.6
        
        # Situación mal alineada
        situacion_mala = {
            'tipo': 'codigo_complejo',
            'decision_propuesta': {'accion': 'ocultar_informacion'}
        }
        
        alineacion_mala = iris._evaluar_alineacion(situacion_mala)
        assert alineacion_mala < 0.6