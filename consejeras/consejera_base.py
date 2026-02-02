"""
ConsejeraBase - Clase base para todas las consejeras.

Cada consejera tiene una especialidad única y criterio de intervención.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Any, List
from enum import Enum
from datetime import datetime


class TipoOpinion(Enum):
    """Tipos de opinión que puede dar una consejera."""
    VETO = "veto"
    ADVERTENCIA = "advertencia"
    APROBACION = "aprobacion"
    SUGERENCIA = "sugerencia"
    NEUTRAL = "neutral"


class NivelPrioridad(Enum):
    """Nivel de prioridad de la opinión."""
    CRITICA = 4
    ALTA = 3
    MEDIA = 2
    BAJA = 1


@dataclass
class Opinion:
    """Opinión de una consejera."""
    consejera: str
    tipo: TipoOpinion
    decision: str
    razon: str
    prioridad: NivelPrioridad
    certeza: float  # 0.0 - 1.0
    metadata: Dict[str, Any]
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()


class ConsejeraBase(ABC):
    """
    Clase base para todas las consejeras.
    
    Cada consejera tiene:
    - Especialidad única
    - Criterio de cuándo intervenir
    - Método de análisis
    """
    
    def __init__(self, nombre: str, especialidad: str):
        self.nombre = nombre
        self.especialidad = especialidad
        self.intervenciones: List[Opinion] = []
    
    @abstractmethod
    def debe_intervenir(self, situacion: Dict[str, Any]) -> Opinion:
        """
        Decide si esta consejera debe intervenir.
        
        IMPORTANTE: Retorna Opinion, NO bool.
        Si no debe intervenir, retorna Opinion tipo NEUTRAL.
        
        Args:
            situacion: Contexto a evaluar
            
        Returns:
            Opinion con evaluación
        """
        pass
    
    @abstractmethod
    def analizar(self, situacion: Dict[str, Any]) -> Opinion:
        """
        Analiza situación y genera opinión detallada.
        
        Args:
            situacion: Contexto a analizar
            
        Returns:
            Opinion con análisis completo
        """
        pass
    
    def registrar_intervencion(self, opinion: Opinion):
        """Registra intervención para aprendizaje."""
        self.intervenciones.append(opinion)
    
    def obtener_historial(self, ultimas_n: int = 10) -> List[Opinion]:
        """
        Obtiene historial de intervenciones.
        
        Args:
            ultimas_n: Número de intervenciones a obtener
            
        Returns:
            Lista de opiniones recientes
        """
        return self.intervenciones[-ultimas_n:]
    
    def __repr__(self) -> str:
        return f"{self.nombre} ({self.especialidad})"