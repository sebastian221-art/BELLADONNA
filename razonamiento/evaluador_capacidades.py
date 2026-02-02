"""
EvaluadorCapacidades - Evalúa si Bell PUEDE ejecutar operaciones.

Grounding real = Bell solo dice que puede hacer algo si REALMENTE puede ejecutarlo.
"""

from typing import List, Dict
from core.concepto_anclado import ConceptoAnclado
from core.capacidades_bell import CapacidadesBell


class EvaluadorCapacidades:
    """
    Evalúa si Bell PUEDE ejecutar operaciones basándose en grounding real.
    """
    
    def __init__(self, capacidades: CapacidadesBell):
        self.capacidades = capacidades
    
    def evaluar(self, conceptos: List[Dict]) -> Dict:
        """
        Evalúa si Bell puede ejecutar los conceptos.
        
        Args:
            conceptos: Lista de conceptos detectados en entrada
            
        Returns:
            Dict con evaluación de capacidades
        """
        # 🔧 CORRECCIÓN: Si no hay conceptos, retornar evaluación negativa
        if not conceptos:
            return {
                'puede_ejecutar': False,
                'operaciones_disponibles': [],
                'operaciones_faltantes': [],
                'certeza': 0.0,
                'razon': 'No se detectaron conceptos con operaciones'
            }
        
        operaciones_necesarias = set()
        operaciones_disponibles = []
        operaciones_faltantes = []
        
        # Recopilar operaciones de todos los conceptos
        for concepto_info in conceptos:
            concepto = concepto_info['concepto']
            for nombre_op in concepto.operaciones.keys():
                operaciones_necesarias.add(nombre_op)
        
        # 🔧 CORRECCIÓN: Si los conceptos no tienen operaciones, no puede ejecutar
        if not operaciones_necesarias:
            return {
                'puede_ejecutar': False,
                'operaciones_disponibles': [],
                'operaciones_faltantes': [],
                'certeza': 0.3,
                'razon': 'Los conceptos detectados no tienen operaciones ejecutables'
            }
        
        # Verificar disponibilidad
        for operacion in operaciones_necesarias:
            if self.capacidades.tiene_capacidad(operacion):
                operaciones_disponibles.append(operacion)
            else:
                operaciones_faltantes.append(operacion)
        
        # 🔧 CORRECCIÓN CRÍTICA: Solo puede_ejecutar si NO faltan operaciones
        puede_ejecutar = len(operaciones_faltantes) == 0
        
        # Calcular certeza
        certeza = len(operaciones_disponibles) / len(operaciones_necesarias)
        
        # Generar razón
        if puede_ejecutar:
            razon = f"Tengo todas las capacidades: {operaciones_disponibles}"
        else:
            razon = f"Me faltan capacidades: {operaciones_faltantes}"
        
        return {
            'puede_ejecutar': puede_ejecutar,
            'operaciones_disponibles': operaciones_disponibles,
            'operaciones_faltantes': operaciones_faltantes,
            'certeza': certeza,
            'razon': razon
        }