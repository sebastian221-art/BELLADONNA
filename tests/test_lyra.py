# tests/test_lyra.py

import pytest
from consejeras.lyra import Lyra
from consejeras.consejera_base import TipoOpinion


class TestLyra:
    """Tests para Lyra - La Investigadora."""
    
    def test_lyra_detecta_funcion_deprecada(self):
        """Lyra detecta funciones deprecadas."""
        
        lyra = Lyra()
        
        codigo = """
resultado = apply(funcion, argumentos)
"""
        
        situacion = {'codigo': codigo}
        opinion = lyra.debe_intervenir(situacion)
        
        assert opinion.tipo in [TipoOpinion.ADVERTENCIA, TipoOpinion.SUGERENCIA]
        assert 'deprec' in opinion.razon.lower()
    
    def test_lyra_aprueba_codigo_moderno(self):
        """Lyra aprueba código moderno."""
        
        lyra = Lyra()
        
        codigo = """
def procesar(datos: list) -> dict:
    '''Procesa datos con type hints.'''
    return {x: x**2 for x in datos}
"""
        
        situacion = {'codigo': codigo}
        opinion = lyra.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.APROBACION
    
    def test_lyra_detecta_python2(self):
        """Lyra detecta referencias a Python 2."""
        
        lyra = Lyra()
        
        texto = "Este código usa Python 2 para el procesamiento"
        
        situacion = {'texto': texto}
        opinion = lyra.debe_intervenir(situacion)
        
        assert opinion.tipo in [TipoOpinion.ADVERTENCIA, TipoOpinion.SUGERENCIA]
    
    def test_lyra_sin_contenido(self):
        """Lyra no interviene sin contenido."""
        
        lyra = Lyra()
        
        situacion = {}
        opinion = lyra.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.NEUTRAL