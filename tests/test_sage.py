# tests/test_sage.py

"""
Tests para Sage - La Mediadora.
"""

import pytest
from consejeras.sage import Sage
from consejeras.consejera_base import Opinion, TipoOpinion, NivelPrioridad


class TestSage:
    """Tests para Sage."""
    
    def test_sage_sintetiza_consenso(self):
        """Test: Sage sintetiza consenso cuando todas están de acuerdo."""
        sage = Sage()
        
        opiniones = [
            Opinion(
                consejera="Consejera1",
                tipo=TipoOpinion.APROBACION,
                decision="APROBAR",
                razon="Razón 1",
                prioridad=NivelPrioridad.MEDIA,
                certeza=0.9,
                metadata={}
            ),
            Opinion(
                consejera="Consejera2",
                tipo=TipoOpinion.APROBACION,
                decision="APROBAR",
                razon="Razón 2",
                prioridad=NivelPrioridad.MEDIA,
                certeza=0.8,
                metadata={}
            )
        ]
        
        resultado = sage.sintetizar(opiniones)
        
        assert resultado['decision_final'] == "APROBAR"
        assert resultado['consenso'] == True
        assert resultado['metodo'] == 'CONSENSO'
    
    def test_sage_aplica_veto(self):
        """Test: Sage aplica veto correctamente."""
        sage = Sage()
        
        opiniones = [
            Opinion(
                consejera="Vega",
                tipo=TipoOpinion.VETO,
                decision="VETO_ABSOLUTO",
                razon="Violación crítica",
                prioridad=NivelPrioridad.CRITICA,
                certeza=0.95,
                metadata={}
            ),
            Opinion(
                consejera="Nova",
                tipo=TipoOpinion.APROBACION,
                decision="APROBAR",
                razon="Técnicamente correcto",
                prioridad=NivelPrioridad.MEDIA,
                certeza=0.8,
                metadata={}
            )
        ]
        
        resultado = sage.sintetizar(opiniones)
        
        assert resultado['decision_final'] == "VETO_ABSOLUTO"
        assert resultado['consenso'] == False
        assert resultado['metodo'] == 'VETO_ABSOLUTO'
    
    def test_sage_votacion_ponderada(self):
        """Test: Sage usa votación ponderada cuando hay desacuerdo."""
        sage = Sage()
        
        opiniones = [
            Opinion(
                consejera="Consejera1",
                tipo=TipoOpinion.APROBACION,
                decision="APROBAR",
                razon="Razón 1",
                prioridad=NivelPrioridad.ALTA,  # Valor 3
                certeza=0.9,
                metadata={}
            ),
            Opinion(
                consejera="Consejera2",
                tipo=TipoOpinion.ADVERTENCIA,
                decision="RECHAZAR",
                razon="Razón 2",
                prioridad=NivelPrioridad.MEDIA,  # Valor 2
                certeza=0.8,
                metadata={}
            )
        ]
        
        resultado = sage.sintetizar(opiniones)
        
        # APROBAR debería ganar (3 vs 2)
        assert resultado['decision_final'] == "APROBAR"
        assert resultado['metodo'] == 'VOTACION_PONDERADA'