# consejeras/iris.py

"""
Iris - La Visionaria
Especialidad: Alineación con propósito y visión
"""

from typing import Dict, Any
from consejeras.consejera_base import (
    ConsejeraBase, Opinion, TipoOpinion, NivelPrioridad
)


class Iris(ConsejeraBase):
    """
    Iris - La Visionaria.
    
    Evalúa:
    - Alineación con propósito fundamental
    - Coherencia con visión a largo plazo
    - Deriva del objetivo principal
    """
    
    def __init__(self):
        super().__init__(
            nombre="Iris",
            especialidad="Guardiana del Propósito"
        )
        
        self.proposito_fundamental = "Ser socio cognitivo, no herramienta"
        self.umbral_alineacion = 0.6
    
    def debe_intervenir(self, situacion: Dict[str, Any]) -> Opinion:
        """Decide si Iris debe intervenir."""
        
        # Evaluar alineación con propósito
        alineacion = self._evaluar_alineacion(situacion)
        
        if alineacion < self.umbral_alineacion:
            return self.analizar(situacion)
        
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.APROBACION,
            decision="ALINEADO",
            razon=f"Alineación con propósito: {alineacion:.0%}",
            prioridad=NivelPrioridad.BAJA,
            certeza=alineacion,
            metadata={'alineacion': alineacion}
        )
    
    def analizar(self, situacion: Dict[str, Any]) -> Opinion:
        """Analiza alineación con propósito."""
        
        alineacion = self._evaluar_alineacion(situacion)
        
        if alineacion < self.umbral_alineacion:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.ADVERTENCIA,
                decision="DESALINEADO",
                razon=self._generar_razon_deriva(alineacion),
                prioridad=NivelPrioridad.ALTA,
                certeza=1.0 - alineacion,
                metadata={'alineacion': alineacion}
            )
        
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.APROBACION,
            decision="ALINEADO",
            razon="Coherente con propósito fundamental",
            prioridad=NivelPrioridad.BAJA,
            certeza=alineacion,
            metadata={}
        )
    
    def _evaluar_alineacion(self, situacion: Dict[str, Any]) -> float:
        """Evalúa alineación con propósito."""
        
        score = 1.0
        
        decision = situacion.get('decision_propuesta', {})
        accion = decision.get('accion', '')
        texto = str(situacion).lower()
        
        # Factor 1: Autonomía
        if 'obedecer' in accion or 'herramienta' in texto:
            score -= 0.4
        
        # Factor 2: Pensamiento independiente
        if 'no cuestionar' in texto or 'solo ejecutar' in texto:
            score -= 0.3
        
        return max(score, 0.0)
    
    def _generar_razon_deriva(self, alineacion: float) -> str:
        """Genera explicación de deriva."""
        
        razon = f"Alineación con propósito: {alineacion:.0%} (< 60% mínimo)\n\n"
        razon += f"Nuestro propósito es: {self.proposito_fundamental}\n\n"
        razon += "Esta acción nos aleja de esa misión.\n"
        razon += "Sugerencia: Reorientar hacia colaboración genuina."
        
        return razon