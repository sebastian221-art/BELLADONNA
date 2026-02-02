"""
ConceptoAnclado - Estructura fundamental de conocimiento en Belladonna.

Un concepto anclado es conocimiento con grounding computacional real.
Bell solo "entiende" lo que puede ejecutar, medir o relacionar.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set, Any, Callable
from enum import Enum
from datetime import datetime


class TipoConcepto(Enum):
    """Tipos de conceptos que Bell puede manejar."""
    ENTIDAD_DIGITAL = "entidad_digital"
    ENTIDAD_CODIGO = "entidad_codigo"
    OPERACION_CODIGO = "operacion_codigo"
    OPERACION_SISTEMA = "operacion_sistema"
    OPERACION_LOGICA = "operacion_logica"
    CONCEPTO_ABSTRACTO = "concepto_abstracto"


@dataclass
class ConceptoAnclado:
    """
    Representación fundamental de conocimiento con grounding real.
    
    Bell entiende X si y solo si puede EJECUTAR operaciones relacionadas con X.
    """
    
    # ========== IDENTIFICACIÓN ==========
    id: str
    tipo: TipoConcepto
    palabras_español: List[str]
    
    # ========== GROUNDING 1: OPERACIONES EJECUTABLES ==========
    operaciones: Dict[str, Callable] = field(default_factory=dict)
    
    # ========== GROUNDING 2: RELACIONES ==========
    relaciones: Dict[str, Set[str]] = field(default_factory=dict)
    
    # ========== GROUNDING 3: PROPIEDADES ==========
    propiedades: Dict[str, Any] = field(default_factory=dict)
    
    # ========== GROUNDING 4: DATOS ==========
    datos: Dict[str, Any] = field(default_factory=dict)
    
    # ========== EVALUACIÓN DE GROUNDING ==========
    accesible_directamente: bool = False
    confianza_grounding: float = 0.0
    
    # ========== METADATA ==========
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validaciones post-inicialización."""
        
        # Validar ID
        if not self.id:
            raise ValueError("ID no puede estar vacío")
        
        # Validar palabras en español
        if not self.palabras_español:
            raise ValueError("Debe tener al menos una palabra en español")
        
        # Validar confianza
        if not 0.0 <= self.confianza_grounding <= 1.0:
            raise ValueError("Confianza debe estar entre 0.0 y 1.0")
        
        # Agregar metadata por defecto
        if 'fecha_creacion' not in self.metadata:
            self.metadata['fecha_creacion'] = datetime.now().isoformat()
        
        if 'veces_usado' not in self.metadata:
            self.metadata['veces_usado'] = 0
        
        # Calcular grounding automático si no se especificó
        if self.confianza_grounding == 0.0:
            self.confianza_grounding = self.calcular_grounding_automatico()
    
    def ejecutar_operacion(self, nombre_operacion: str, *args, **kwargs) -> Any:
        """
        Ejecuta una operación del concepto.
        
        Args:
            nombre_operacion: Nombre de la operación
            *args, **kwargs: Argumentos para la operación
            
        Returns:
            Resultado de la operación
            
        Raises:
            KeyError: Si la operación no existe
        """
        if nombre_operacion not in self.operaciones:
            raise KeyError(f"Operación '{nombre_operacion}' no existe en {self.id}")
        
        self.metadata['veces_usado'] += 1
        
        return self.operaciones[nombre_operacion](*args, **kwargs)
    
    def tiene_relacion(self, tipo_relacion: str, concepto_destino: str) -> bool:
        """
        Verifica si existe relación con otro concepto.
        
        Args:
            tipo_relacion: Tipo de relación (es_un, requiere, etc.)
            concepto_destino: ID del concepto destino
            
        Returns:
            True si existe la relación
        """
        if tipo_relacion not in self.relaciones:
            return False
        
        return concepto_destino in self.relaciones[tipo_relacion]
    
    def agregar_relacion(self, tipo_relacion: str, concepto_destino: str):
        """
        Agrega relación con otro concepto.
        
        Args:
            tipo_relacion: Tipo de relación
            concepto_destino: ID del concepto destino
        """
        if tipo_relacion not in self.relaciones:
            self.relaciones[tipo_relacion] = set()
        
        self.relaciones[tipo_relacion].add(concepto_destino)
    
    def calcular_grounding_automatico(self) -> float:
        """
        Calcula nivel de grounding automáticamente.
        
        Returns:
            Score de grounding (0.0-1.0)
        """
        score = 0.0
        
        # Factor 1: Operaciones ejecutables (40%)
        if self.operaciones:
            num_ops = len(self.operaciones)
            score += min(num_ops / 5.0, 0.4)
        
        # Factor 2: Accesibilidad directa (30%)
        if self.accesible_directamente:
            score += 0.3
        
        # Factor 3: Relaciones (20%)
        if self.relaciones:
            num_rels = sum(len(rels) for rels in self.relaciones.values())
            score += min(num_rels / 10.0, 0.2)
        
        # Factor 4: Datos estructurados (10%)
        if self.datos:
            score += min(len(self.datos) / 5.0, 0.1)
        
        return min(score, 1.0)
    
    def __repr__(self) -> str:
        return (
            f"ConceptoAnclado(id='{self.id}', "
            f"tipo={self.tipo.value}, "
            f"grounding={self.confianza_grounding:.2f})"
        )