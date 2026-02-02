# consejeras/sage.py

"""
Sage - La Mediadora
Especialidad: Síntesis y resolución de conflictos
"""

from typing import Dict, List
from consejeras.consejera_base import (
    ConsejeraBase, Opinion, TipoOpinion, NivelPrioridad
)
from collections import Counter


class Sage(ConsejeraBase):
    """
    Sage - La Mediadora.
    
    Rol: Sintetizar opiniones del consejo en decisión final
    """
    
    def __init__(self):
        super().__init__(
            nombre="Sage",
            especialidad="Sintetizadora del Consejo"
        )
    
    def debe_intervenir(self, situacion: Dict) -> Opinion:
        """Sage siempre sintetiza, no interviene individualmente."""
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.NEUTRAL,
            decision="SINTETIZAR",
            razon="Sage sintetiza opiniones",
            prioridad=NivelPrioridad.BAJA,
            certeza=1.0,
            metadata={}
        )
    
    def analizar(self, situacion: Dict) -> Opinion:
        """Sage no analiza individualmente."""
        return self.debe_intervenir(situacion)
    
    def sintetizar(self, opiniones: List[Opinion]) -> Dict:
        """
        Sintetiza opiniones en decisión final.
        
        Reglas:
        1. Veto → automático
        2. Consenso → usar
        3. Conflicto → votación ponderada
        """
        
        # Regla 1: Veto
        vetos = [op for op in opiniones if op.tipo == TipoOpinion.VETO]
        if vetos:
            veto = vetos[0]
            return {
                'decision_final': veto.decision,
                'tipo': veto.tipo,
                'razon': f"[{veto.consejera} VETO] {veto.razon}",
                'opiniones': opiniones,
                'consenso': False,
                'metodo': 'VETO'
            }
        
        # Filtrar activas
        activas = [op for op in opiniones if op.tipo != TipoOpinion.NEUTRAL]
        
        if not activas:
            return {
                'decision_final': "APROBAR",
                'tipo': TipoOpinion.APROBACION,
                'razon': "Sin objeciones del consejo",
                'opiniones': opiniones,
                'consenso': True,
                'metodo': 'SIN_OBJECIONES'
            }
        
        # Regla 2: Consenso
        decisiones = [op.decision for op in activas]
        
        if len(set(decisiones)) == 1:
            return {
                'decision_final': decisiones[0],
                'tipo': activas[0].tipo,
                'razon': self._razon_consenso(activas),
                'opiniones': opiniones,
                'consenso': True,
                'metodo': 'CONSENSO'
            }
        
        # Regla 3: Votación
        return self._votacion_ponderada(activas, opiniones)
    
    def _razon_consenso(self, opiniones: List[Opinion]) -> str:
        """Genera razón de consenso."""
        consejeras = [op.consejera for op in opiniones]
        return f"Consenso entre {', '.join(consejeras)}: {opiniones[0].razon[:100]}"
    
    def _votacion_ponderada(self, activas: List[Opinion], todas: List[Opinion]) -> Dict:
        """Votación ponderada por prioridad."""
        
        votos = Counter()
        
        for op in activas:
            peso = op.prioridad.value
            votos[op.decision] += peso
        
        decision_ganadora = votos.most_common(1)[0][0]
        
        op_ganadora = next(op for op in activas if op.decision == decision_ganadora)
        
        return {
            'decision_final': decision_ganadora,
            'tipo': op_ganadora.tipo,
            'razon': f"Votación: {dict(votos)}. {op_ganadora.razon[:100]}",
            'opiniones': todas,
            'consenso': False,
            'metodo': 'VOTACION'
        }