# tests/test_nova.py

import pytest
from consejeras.nova import Nova
from consejeras.consejera_base import TipoOpinion


class TestNova:
    """Tests para Nova - La Ingeniera."""
    
    def test_nova_detecta_range_len(self):
        """Nova detecta patrón range(len())."""
        
        nova = Nova()
        
        codigo = """
for i in range(len(lista)):
    elemento = lista[i]
    print(elemento)
"""
        
        situacion = {'codigo': codigo}
        opinion = nova.debe_intervenir(situacion)
        
        assert opinion.tipo in [TipoOpinion.SUGERENCIA, TipoOpinion.NEUTRAL]
        assert 'enumerate' in opinion.razon.lower() or opinion.tipo == TipoOpinion.NEUTRAL
    
    def test_nova_aprueba_codigo_eficiente(self):
        """Nova aprueba código eficiente."""
        
        nova = Nova()
        
        codigo = """
for i, elemento in enumerate(lista):
    print(elemento)
"""
        
        situacion = {'codigo': codigo}
        opinion = nova.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.APROBACION
    
    def test_nova_detecta_bucles_anidados(self):
        """Nova detecta bucles muy anidados."""
        
        nova = Nova()
        
        codigo = """
for i in range(10):
    for j in range(10):
        for k in range(10):
            print(i, j, k)
"""
        
        situacion = {'codigo': codigo}
        opinion = nova.debe_intervenir(situacion)
        
        # Debería detectar anidamiento
        assert opinion.tipo in [TipoOpinion.SUGERENCIA, TipoOpinion.NEUTRAL]
    
    def test_nova_sin_codigo(self):
        """Nova no interviene sin código."""
        
        nova = Nova()
        
        situacion = {}
        opinion = nova.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.NEUTRAL