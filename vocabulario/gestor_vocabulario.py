"""
GestorVocabulario - Gestiona el vocabulario de conceptos de Bell.
"""

from typing import Dict, Optional, List
from core.concepto_anclado import ConceptoAnclado


class GestorVocabulario:
    """
    Gestiona todos los conceptos que Bell conoce.
    """
    
    def __init__(self):
        self.conceptos: Dict[str, ConceptoAnclado] = {}
    
    def cargar_conceptos(self, conceptos: Dict[str, ConceptoAnclado]):
        """
        Carga conceptos iniciales.
        
        Args:
            conceptos: Diccionario de conceptos
        """
        self.conceptos.update(conceptos)
    
    def agregar_concepto(self, concepto: ConceptoAnclado):
        """
        Agrega concepto nuevo.
        
        Args:
            concepto: Concepto a agregar
        """
        self.conceptos[concepto.id] = concepto
    
    def obtener_concepto(self, palabra: str) -> Optional[ConceptoAnclado]:
        """
        Busca concepto por palabra en español.
        
        Args:
            palabra: Palabra a buscar
            
        Returns:
            ConceptoAnclado si existe, None si no
        """
        palabra_lower = palabra.lower()
        
        # Buscar por palabras en español
        for concepto in self.conceptos.values():
            if palabra_lower in [p.lower() for p in concepto.palabras_español]:
                return concepto
        
        return None
    
    def listar_conceptos(self) -> List[str]:
        """
        Lista IDs de todos los conceptos.
        
        Returns:
            Lista de IDs
        """
        return list(self.conceptos.keys())
    
    def calcular_grounding_promedio(self) -> float:
        """
        Calcula grounding promedio de todos los conceptos.
        
        Returns:
            Grounding promedio (0.0-1.0)
        """
        if not self.conceptos:
            return 0.0
        
        total = sum(c.confianza_grounding for c in self.conceptos.values())
        return total / len(self.conceptos)
    
    def obtener_estadisticas(self) -> Dict:
        """
        Obtiene estadísticas del vocabulario.
        
        Returns:
            Dict con estadísticas
        """
        if not self.conceptos:
            return {
                'total': 0,
                'grounding_promedio': 0.0,
                'por_tipo': {}
            }
        
        por_tipo = {}
        for concepto in self.conceptos.values():
            tipo = concepto.tipo.value
            por_tipo[tipo] = por_tipo.get(tipo, 0) + 1
        
        return {
            'total': len(self.conceptos),
            'grounding_promedio': self.calcular_grounding_promedio(),
            'por_tipo': por_tipo
        }
    
    def __repr__(self) -> str:
        return f"GestorVocabulario(conceptos={len(self.conceptos)})"