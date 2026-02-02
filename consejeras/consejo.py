# consejeras/consejo.py

"""
Consejo de las 7 Consejeras - Sistema de Deliberación Completo
"""

from typing import Dict, Any, List
from consejeras.consejera_base import Opinion, TipoOpinion
from consejeras.vega import Vega
from consejeras.nova import Nova
from consejeras.echo import Echo
from consejeras.lyra import Lyra
from consejeras.luna import Luna
from consejeras.iris import Iris
from consejeras.sage import Sage


class Consejo:
    """
    El Consejo de las 7 Consejeras.
    
    Gestiona deliberación multi-perspectiva para decisiones importantes.
    """
    
    def __init__(self):
        # Las 7 consejeras
        self.vega = Vega()
        self.nova = Nova()
        self.echo = Echo()
        self.lyra = Lyra()
        self.luna = Luna()
        self.iris = Iris()
        self.sage = Sage()
        
        # Lista de consejeras (sin Sage - ella sintetiza)
        self.consejeras = [
            self.vega,
            self.nova,
            self.echo,
            self.lyra,
            self.luna,
            self.iris
        ]
        
        self.historial = []
    
    def deliberar(self, situacion: Dict[str, Any]) -> Dict:
        """
        Proceso completo de deliberación.
        
        Args:
            situacion: Contexto a analizar
            
        Returns:
            Decisión del consejo
        """
        
        print("🗣️  Consejo deliberando...")
        
        # Fase 1: Cada consejera opina
        opiniones = []
        
        for consejera in self.consejeras:
            opinion = consejera.debe_intervenir(situacion)
            opiniones.append(opinion)
            
            # Mostrar opiniones relevantes
            if opinion.tipo != TipoOpinion.NEUTRAL:
                print(f"   {consejera.nombre}: {opinion.tipo.value}")
            
            # Vega puede vetar inmediatamente
            if consejera.nombre == "Vega" and opinion.tipo == TipoOpinion.VETO:
                resultado = {
                    'decision_final': "VETADO",
                    'tipo': TipoOpinion.VETO,
                    'razon': opinion.razon,
                    'opiniones': opiniones,
                    'hubo_veto': True,
                    'consejera_veto': 'Vega'
                }
                
                self.historial.append(resultado)
                return resultado
        
        # Fase 2: Sage sintetiza
        resultado = self.sage.sintetizar(opiniones)
        
        # Agregar metadata
        resultado['situacion'] = situacion
        
        # Registrar en historial
        self.historial.append(resultado)
        
        return resultado
    
    def obtener_resumen(self, resultado: Dict) -> str:
        """Genera resumen legible de la deliberación."""
        
        resumen = f"\n📊 Decisión del Consejo: {resultado['decision_final']}\n\n"
        
        if resultado.get('hubo_veto'):
            resumen += f"🚫 VETO de {resultado['consejera_veto']}\n"
            resumen += f"Razón: {resultado['razon']}\n"
            return resumen
        
        resumen += "Opiniones del consejo:\n"
        for op in resultado['opiniones']:
            if op.tipo != TipoOpinion.NEUTRAL:
                emoji = self._emoji_para_tipo(op.tipo)
                resumen += f"{emoji} {op.consejera}: {op.decision}\n"
        
        resumen += f"\n✅ {resultado['razon']}"
        
        return resumen
    
    def _emoji_para_tipo(self, tipo: TipoOpinion) -> str:
        """Emoji para tipo de opinión."""
        return {
            TipoOpinion.APROBACION: "✅",
            TipoOpinion.SUGERENCIA: "💡",
            TipoOpinion.ADVERTENCIA: "⚠️",
            TipoOpinion.VETO: "🚫",
            TipoOpinion.NEUTRAL: "➖"
        }.get(tipo, "❓")