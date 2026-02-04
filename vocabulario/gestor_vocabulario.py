"""
Gestor de Vocabulario de Belladonna.

Este archivo coordina la carga de todos los conceptos.
Arquitectura MODULAR: cada categoría en su propio archivo.
"""
from typing import List, Optional
from core.concepto_anclado import ConceptoAnclado

class GestorVocabulario:
    """
    Administra TODO el vocabulario de Bell de forma modular.
    
    Ventajas:
    - Cada categoría en su archivo
    - Fácil expandir sin modificar archivos existentes
    - Organización clara por semanas/temas
    """
    
    def __init__(self):
        self.conceptos: List[ConceptoAnclado] = []
        self._cargar_todos_los_conceptos()
    
    def _cargar_todos_los_conceptos(self):
        """
        Carga conceptos de todos los módulos.
        
        PATRÓN: Importar y extender, nunca modificar.
        """
        
        # SEMANA 1: Fundamentos (30 conceptos)
        from vocabulario.semana1_operaciones import obtener_conceptos_operaciones
        from vocabulario.semana1_conversacion import obtener_conceptos_conversacion
        from vocabulario.semana1_cognitivos import obtener_conceptos_cognitivos
        from vocabulario.semana1_acciones import obtener_conceptos_acciones
        
        self.conceptos.extend(obtener_conceptos_operaciones())    # 5 conceptos
        self.conceptos.extend(obtener_conceptos_conversacion())   # 10 conceptos
        self.conceptos.extend(obtener_conceptos_cognitivos())     # 10 conceptos
        self.conceptos.extend(obtener_conceptos_acciones())       # 5 conceptos
        
        # SEMANA 2: Traducción (40 conceptos)
        from vocabulario.semana2_python import obtener_conceptos_python
        from vocabulario.semana2_verbos import obtener_conceptos_verbos
        from vocabulario.semana2_conectores import obtener_conceptos_conectores
        from vocabulario.semana2_adjetivos import obtener_conceptos_adjetivos
        
        self.conceptos.extend(obtener_conceptos_python())         # 15
        self.conceptos.extend(obtener_conceptos_verbos())         # 10
        self.conceptos.extend(obtener_conceptos_conectores())     # 10
        self.conceptos.extend(obtener_conceptos_adjetivos())      # 5
        
        # SEMANA 2.5: Python Avanzado (40 conceptos)
        from vocabulario.semana3_python_avanzado import obtener_conceptos_python_avanzado
        
        self.conceptos.extend(obtener_conceptos_python_avanzado())  # 40
        
        # SEMANA 3: Vocabulario Expandido (80 conceptos) ← AGREGAR ESTAS 6 LÍNEAS
        from vocabulario.semana3_sistema_avanzado import obtener_conceptos_sistema_avanzado
        from vocabulario.semana3_matematicas import obtener_conceptos_matematicas
        from vocabulario.semana3_conversacion_expandida import obtener_conceptos_conversacion_expandida
        
        self.conceptos.extend(obtener_conceptos_sistema_avanzado())        # 30
        self.conceptos.extend(obtener_conceptos_matematicas())             # 20
        self.conceptos.extend(obtener_conceptos_conversacion_expandida())  # 30
    
    def obtener_todos(self) -> List[ConceptoAnclado]:
        """Retorna todos los conceptos cargados."""
        return self.conceptos
    
    def buscar_por_palabra(self, palabra: str) -> Optional[ConceptoAnclado]:
        """
        Busca un concepto por palabra en español.
        
        Ejemplo:
            gestor.buscar_por_palabra("leer") → CONCEPTO_LEER
        """
        palabra_lower = palabra.lower()
        for concepto in self.conceptos:
            if palabra_lower in [p.lower() for p in concepto.palabras_español]:
                return concepto
        return None
    
    def buscar_por_id(self, concepto_id: str) -> Optional[ConceptoAnclado]:
        """
        Busca un concepto por su ID.
        
        Ejemplo:
            gestor.buscar_por_id("CONCEPTO_LEER") → ConceptoAnclado(...)
        """
        for concepto in self.conceptos:
            if concepto.id == concepto_id:
                return concepto
        return None
    
    def filtrar_por_tipo(self, tipo_concepto) -> List[ConceptoAnclado]:
        """
        Filtra conceptos por tipo.
        
        Ejemplo:
            gestor.filtrar_por_tipo(TipoConcepto.OPERACION_SISTEMA)
        """
        return [c for c in self.conceptos if c.tipo == tipo_concepto]
    
    def estadisticas(self) -> dict:
        """
        Retorna estadísticas del vocabulario.
        
        Útil para validar que el vocabulario está bien balanceado.
        """
        total = len(self.conceptos)
        if total == 0:
            return {
                'total_conceptos': 0,
                'grounding_promedio': 0.0,
                'por_tipo': {},
                'con_operaciones': 0
            }
        
        grounding_promedio = sum(c.confianza_grounding for c in self.conceptos) / total
        
        # Contar por tipo
        por_tipo = {}
        for concepto in self.conceptos:
            tipo = concepto.tipo.name
            por_tipo[tipo] = por_tipo.get(tipo, 0) + 1
        
        return {
            'total_conceptos': total,
            'grounding_promedio': round(grounding_promedio, 2),
            'por_tipo': por_tipo,
            'con_operaciones': sum(1 for c in self.conceptos if len(c.operaciones) > 0),
            'grounding_1_0': sum(1 for c in self.conceptos if c.confianza_grounding == 1.0)
        }