# consejeras/nova.py

"""
Nova - La Ingeniera
Especialidad: Optimización, refactorización, detección de código ineficiente
"""

from typing import Dict, Any, List
from consejeras.consejera_base import (
    ConsejeraBase, Opinion, TipoOpinion, NivelPrioridad
)
import ast
import re


class Nova(ConsejeraBase):
    """
    Nova - La Ingeniera.
    
    Detecta:
    - Código ineficiente
    - Patrones problemáticos
    - Oportunidades de optimización
    """
    
    def __init__(self):
        super().__init__(
            nombre="Nova",
            especialidad="Arquitecta del Código y Optimización"
        )
        
        self.umbral_intervencion = 0.4  # 40% de mejora potencial (REDUCIDO)
    
    def debe_intervenir(self, situacion: Dict[str, Any]) -> Opinion:
        """Decide si Nova debe intervenir."""
        
        # ¿Hay código para analizar?
        codigo = situacion.get('codigo', '')
        
        if not codigo:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.NEUTRAL,
                decision="NO_RELEVANTE",
                razon="No hay código para analizar",
                prioridad=NivelPrioridad.BAJA,
                certeza=1.0,
                metadata={}
            )
        
        # Detectar problemas
        problemas = self._detectar_problemas(codigo)
        
        if not problemas:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.APROBACION,
                decision="CODIGO_EFICIENTE",
                razon="No detecté problemas de eficiencia",
                prioridad=NivelPrioridad.BAJA,
                certeza=0.8,
                metadata={}
            )
        
        # Hay problemas → analizar
        return self.analizar(situacion)
    
    def analizar(self, situacion: Dict[str, Any]) -> Opinion:
        """Analiza código y propone optimizaciones."""
        
        codigo = situacion.get('codigo', '')
        problemas = self._detectar_problemas(codigo)
        
        if not problemas:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.APROBACION,
                decision="APROBAR",
                razon="Código eficiente",
                prioridad=NivelPrioridad.BAJA,
                certeza=0.8,
                metadata={}
            )
        
        # Calcular impacto
        impacto = self._calcular_impacto(problemas)
        
        # CAMBIO CLAVE: Siempre sugerir si hay problemas (no neutral)
        if impacto >= self.umbral_intervencion:
            # Problemas significativos
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.SUGERENCIA,
                decision="OPTIMIZAR",
                razon=self._generar_razon(problemas),
                prioridad=NivelPrioridad.MEDIA,
                certeza=0.8,
                metadata={
                    'problemas': problemas,
                    'impacto': impacto
                }
            )
        else:
            # Problemas menores pero aún sugerir
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.SUGERENCIA,  # CAMBIADO de NEUTRAL
                decision="MEJORA_MENOR",
                razon=self._generar_razon(problemas),
                prioridad=NivelPrioridad.BAJA,
                certeza=0.6,
                metadata={'problemas': problemas}
            )
    
    def _detectar_problemas(self, codigo: str) -> List[Dict]:
        """Detecta problemas de eficiencia."""
        
        problemas = []
        
        # Problema 1: range(len())
        if 'range(len(' in codigo:
            problemas.append({
                'tipo': 'RANGE_LEN',
                'severidad': 0.5,
                'sugerencia': 'Usar enumerate() en su lugar',
                'ejemplo': 'for i, item in enumerate(lista):'
            })
        
        # Problema 2: Bucles anidados profundos
        try:
            tree = ast.parse(codigo)
            nivel_max = self._max_anidamiento(tree)
            
            if nivel_max >= 3:
                problemas.append({
                    'tipo': 'BUCLES_ANIDADOS',
                    'severidad': 0.7,
                    'nivel': nivel_max,
                    'sugerencia': 'Considerar list comprehension o refactorizar'
                })
        except:
            pass
        
        # Problema 3: Operaciones en bucle que podrían estar fuera
        if re.search(r'for .+ in .+:\s+.+=.+\(', codigo):
            problemas.append({
                'tipo': 'OPERACION_EN_BUCLE',
                'severidad': 0.4,
                'sugerencia': 'Mover operaciones constantes fuera del bucle'
            })
        
        return problemas
    
    def _max_anidamiento(self, tree) -> int:
        """Calcula máximo nivel de anidamiento de bucles."""
        
        max_nivel = 0
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While)):
                nivel = self._calcular_nivel(node)
                max_nivel = max(max_nivel, nivel)
        
        return max_nivel
    
    def _calcular_nivel(self, node, nivel=1) -> int:
        """Calcula nivel de anidamiento recursivamente."""
        
        max_interno = nivel
        
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.For, ast.While)):
                nivel_child = self._calcular_nivel(child, nivel + 1)
                max_interno = max(max_interno, nivel_child)
        
        return max_interno
    
    def _calcular_impacto(self, problemas: List[Dict]) -> float:
        """Calcula impacto total de problemas."""
        
        if not problemas:
            return 0.0
        
        severidades = [p['severidad'] for p in problemas]
        return sum(severidades) / len(severidades)
    
    def _generar_razon(self, problemas: List[Dict]) -> str:
        """Genera explicación de problemas."""
        
        razon = "Detecté oportunidades de optimización:\n\n"
        
        for p in problemas:
            razon += f"• {p['tipo']}: {p['sugerencia']}\n"
            if 'ejemplo' in p:
                razon += f"  Ejemplo: {p['ejemplo']}\n"
        
        return razon