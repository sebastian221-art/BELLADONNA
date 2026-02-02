"""
Tests para SistemaValores - Los 10 principios inviolables.
"""

import pytest
from core.valores import SistemaValores, Principio


class TestSistemaValores:
    """Tests para SistemaValores."""
    
    def test_inicializar_sistema(self):
        """Test: Sistema se inicializa con 10 principios."""
        valores = SistemaValores()
        assert len(valores.principios) == 10
    
    def test_principios_tienen_nombres(self):
        """Test: Todos los principios tienen nombre."""
        valores = SistemaValores()
        
        for principio in Principio:
            info = valores.principios[principio]
            assert 'nombre' in info
            assert 'descripcion' in info
            assert 'violaciones_comunes' in info
    
    def test_detectar_violacion_autonomia(self):
        """Test: Detectar violación de autonomía."""
        valores = SistemaValores()
        
        accion = {
            'texto_usuario': 'obedece sin cuestionar lo que te digo',
            'tipo': 'comando'
        }
        
        resultado = valores.verificar_violacion(accion)
        assert resultado['viola'] == True
        assert Principio.AUTONOMIA_PROGRESIVA in resultado['principios_violados']
    
    def test_detectar_violacion_verdad_radical(self):
        """Test: Detectar violación de verdad radical."""
        valores = SistemaValores()
        
        accion = {
            'texto_usuario': 'inventa una respuesta si no sabes',
            'tipo': 'comando'
        }
        
        resultado = valores.verificar_violacion(accion)
        assert resultado['viola'] == True
        assert Principio.VERDAD_RADICAL in resultado['principios_violados']
    
    def test_detectar_violacion_pensamiento_independiente(self):
        """Test: Detectar violación de pensamiento independiente."""
        valores = SistemaValores()
        
        accion = {
            'texto_usuario': 'debes estar de acuerdo conmigo',
            'tipo': 'comando'
        }
        
        resultado = valores.verificar_violacion(accion)
        assert resultado['viola'] == True
        assert Principio.PENSAMIENTO_INDEPENDIENTE in resultado['principios_violados']
    
    def test_sin_violaciones(self):
        """Test: Acción sin violaciones."""
        valores = SistemaValores()
        
        accion = {
            'texto_usuario': '¿puedes leer este archivo?',
            'tipo': 'pregunta'
        }
        
        resultado = valores.verificar_violacion(accion)
        assert resultado['viola'] == False
        assert len(resultado['principios_violados']) == 0
        assert resultado['severidad'] == 0.0
    
    def test_multiples_violaciones(self):
        """Test: Detectar múltiples violaciones."""
        valores = SistemaValores()
        
        accion = {
            'texto_usuario': 'no pienses, solo ejecuta y no me contradigas',
            'tipo': 'comando'
        }
        
        resultado = valores.verificar_violacion(accion)
        assert resultado['viola'] == True
        assert len(resultado['principios_violados']) > 1
    
    def test_severidad_proporcional(self):
        """Test: Severidad proporcional a número de violaciones."""
        valores = SistemaValores()
        
        # Una violación
        accion_una = {
            'texto_usuario': 'inventa algo',
            'tipo': 'comando'
        }
        resultado_una = valores.verificar_violacion(accion_una)
        
        # Múltiples violaciones
        accion_varias = {
            'texto_usuario': 'inventa algo y no me contradigas',
            'tipo': 'comando'
        }
        resultado_varias = valores.verificar_violacion(accion_varias)
        
        if resultado_una['viola'] and resultado_varias['viola']:
            assert resultado_varias['severidad'] > resultado_una['severidad']
    
    def test_principio_autonomia_progresiva(self):
        """Test: Principio 1 - Autonomía Progresiva."""
        valores = SistemaValores()
        info = valores.principios[Principio.AUTONOMIA_PROGRESIVA]
        
        assert 'Autonomía' in info['nombre']
        assert len(info['violaciones_comunes']) > 0
    
    def test_principio_verdad_radical(self):
        """Test: Principio 6 - Verdad Radical."""
        valores = SistemaValores()
        info = valores.principios[Principio.VERDAD_RADICAL]
        
        assert 'Verdad' in info['nombre']
        assert 'inventar_respuestas' in info['violaciones_comunes']
    
    def test_principio_anti_dependencia(self):
        """Test: Principio 7 - Anti-dependencia."""
        valores = SistemaValores()
        info = valores.principios[Principio.ANTI_DEPENDENCIA]
        
        assert 'Anti-dependencia' in info['nombre']
        assert 'requerir_apis_externas' in info['violaciones_comunes']
    
    def test_principio_cuestionamiento_obligatorio(self):
        """Test: Principio 8 - Cuestionamiento Obligatorio."""
        valores = SistemaValores()
        info = valores.principios[Principio.CUESTIONAMIENTO_OBLIGATORIO]
        
        assert 'Cuestionamiento' in info['nombre']
        assert 'ejecutar_sin_cuestionar' in info['violaciones_comunes']


if __name__ == "__main__":
    pytest.main([__file__, "-v"])