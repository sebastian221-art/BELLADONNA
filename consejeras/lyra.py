# consejeras/lyra.py

"""
Lyra - La Investigadora
Especialidad: Detección de lagunas de conocimiento
"""

from typing import Dict, Any, List
from consejeras.consejera_base import (
    ConsejeraBase, Opinion, TipoOpinion, NivelPrioridad
)


class Lyra(ConsejeraBase):
    """
    Lyra - La Investigadora.
    
    Detecta:
    - Conceptos desconocidos
    - Lagunas de conocimiento
    - Necesidades de investigación
    """
    
    def __init__(self):
        super().__init__(
            nombre="Lyra",
            especialidad="Guardiana del Conocimiento"
        )
        
        self.umbral_confianza = 0.7
    
    def debe_intervenir(self, situacion: Dict[str, Any]) -> Opinion:
        """Decide si Lyra debe intervenir."""
        
        # CLAVE: Verificar traducción
        traduccion = situacion.get('traduccion', {})
        
        if not traduccion:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.NEUTRAL,
                decision="NO_RELEVANTE",
                razon="No hay contenido técnico para verificar",
                prioridad=NivelPrioridad.BAJA,
                certeza=1.0,
                metadata={}
            )
        
        # Verificar palabras desconocidas
        desconocidas = traduccion.get('palabras_desconocidas', [])
        confianza = traduccion.get('confianza_traduccion', 1.0)
        
        # INTERVENIR si hay lagunas
        if desconocidas or confianza < self.umbral_confianza:
            return self.analizar(situacion)
        
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.APROBACION,
            decision="CONOCIMIENTO_COMPLETO",
            razon="Conozco todos los conceptos necesarios",
            prioridad=NivelPrioridad.BAJA,
            certeza=confianza,
            metadata={}
        )
    
    def analizar(self, situacion: Dict[str, Any]) -> Opinion:
        """Analiza lagunas de conocimiento."""
        
        traduccion = situacion.get('traduccion', {})
        desconocidas = traduccion.get('palabras_desconocidas', [])
        confianza = traduccion.get('confianza_traduccion', 1.0)
        
        if not desconocidas and confianza >= self.umbral_confianza:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.APROBACION,
                decision="CONOCIMIENTO_ADECUADO",
                razon="Conocimiento suficiente para proceder",
                prioridad=NivelPrioridad.BAJA,
                certeza=confianza,
                metadata={}
            )
        
        # Hay lagunas → SUGERIR investigación
        razon = self._generar_razon_investigacion(desconocidas, confianza)
        
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.SUGERENCIA,  # Sugerir investigar
            decision="INVESTIGAR",
            razon=razon,
            prioridad=NivelPrioridad.ALTA if len(desconocidas) > 2 else NivelPrioridad.MEDIA,
            certeza=1.0 - confianza,
            metadata={
                'lagunas': desconocidas,
                'confianza': confianza
            }
        )
    
    def _generar_razon_investigacion(
        self, 
        desconocidas: List[str], 
        confianza: float
    ) -> str:
        """Genera explicación de lagunas."""
        
        if desconocidas:
            palabras_str = ", ".join(f"'{p}'" for p in desconocidas[:5])
            razon = f"Detecté conceptos desconocidos: {palabras_str}\n\n"
            razon += "Mi grounding es limitado aquí.\n\n"
            razon += "Opciones:\n"
            razon += "1. Puedo investigar en documentación\n"
            razon += "2. Puedes explicarme brevemente\n"
            razon += "3. Procedo con conocimiento parcial (arriesgado)"
        else:
            razon = f"Confianza de traducción baja: {confianza:.0%}\n\n"
            razon += "Necesito más contexto o información para proceder con certeza."
        
        return razon