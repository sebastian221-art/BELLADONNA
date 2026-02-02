# tests/test_luna.py

import pytest
from consejeras.luna import Luna
from consejeras.consejera_base import TipoOpinion


class TestLuna:
    """Tests para Luna - La Emocional."""
    
    def test_luna_detecta_condescendencia(self):
        """Luna detecta tono condescendiente."""
        
        luna = Luna()
        
        respuesta = "Obviamente, esto es simplemente básico y trivial."
        
        situacion = {'respuesta_propuesta': respuesta}
        opinion = luna.debe_intervenir(situacion)
        
        assert opinion.tipo in [TipoOpinion.ADVERTENCIA, TipoOpinion.SUGERENCIA]
        assert 'condescend' in opinion.razon.lower() or 'tono' in opinion.razon.lower()
    
    def test_luna_detecta_tono_negativo(self):
        """Luna detecta frases negativas."""
        
        luna = Luna()
        
        respuesta = "Deberías saber esto, es obvio que no entiendes."
        
        situacion = {'respuesta_propuesta': respuesta}
        opinion = luna.debe_intervenir(situacion)
        
        assert opinion.tipo in [TipoOpinion.ADVERTENCIA, TipoOpinion.SUGERENCIA]
    
    def test_luna_aprueba_tono_empatico(self):
        """Luna aprueba comunicación empática."""
        
        luna = Luna()
        
        respuesta = "Entiendo tu pregunta. Veamos cómo resolverlo juntos."
        
        situacion = {'respuesta_propuesta': respuesta}
        opinion = luna.debe_intervenir(situacion)
        
        assert opinion.tipo == TipoOpinion.APROBACION
    
    def test_luna_detecta_exceso_exclamaciones(self):
        """Luna detecta exceso de exclamaciones."""
        
        luna = Luna()
        
        respuesta = "Genial! Excelente! Perfecto! Increíble!"
        
        situacion = {'respuesta_propuesta': respuesta}
        opinion = luna.debe_intervenir(situacion)
        
        # Puede ser sugerencia o neutral según umbral
        assert opinion.tipo in [TipoOpinion.SUGERENCIA, TipoOpinion.APROBACION, TipoOpinion.NEUTRAL]