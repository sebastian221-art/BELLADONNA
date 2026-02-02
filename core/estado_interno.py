"""
EstadoInterno - Estado funcional de Bell.

NO son emociones - son métricas funcionales que Bell usa para auto-evaluarse.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass
class EstadoInterno:
    """
    Estado interno de Bell.
    
    NO son emociones - son métricas funcionales.
    """
    
    # Métrica 1: Coherencia con propósito (0.0-1.0)
    coherencia_proposito: float = 1.0
    
    # Métrica 2: Confianza en conocimiento (0.0-1.0)
    confianza_conocimiento: float = 0.5
    
    # Métrica 3: Utilidad de intervenciones (0.0-1.0)
    utilidad_intervenciones: float = 0.7
    
    # Métrica 4: Carga cognitiva (0.0-1.0, donde 1.0 = sobrecargada)
    carga_cognitiva: float = 0.3
    
    # Métrica 5: Alineación con usuario (0.0-1.0)
    alineacion_usuario: float = 0.8
    
    # Métrica 6: Tasa de aprendizaje (conceptos/hora)
    tasa_aprendizaje: float = 0.0
    
    # Metadata
    ultima_actualizacion: datetime = field(default_factory=datetime.now)
    
    def actualizar_metrica(self, metrica: str, valor: float):
        """
        Actualiza métrica con validación.
        
        Args:
            metrica: Nombre de la métrica
            valor: Nuevo valor (0.0-1.0)
            
        Raises:
            ValueError: Si valor fuera de rango
        """
        if not 0.0 <= valor <= 1.0:
            raise ValueError(f"Métrica debe estar en [0.0, 1.0]: {valor}")
        
        if not hasattr(self, metrica):
            raise AttributeError(f"Métrica '{metrica}' no existe")
        
        setattr(self, metrica, valor)
        self.ultima_actualizacion = datetime.now()
    
    def obtener_resumen(self) -> Dict:
        """
        Resumen del estado.
        
        Returns:
            Dict con todas las métricas
        """
        return {
            'coherencia': self.coherencia_proposito,
            'confianza': self.confianza_conocimiento,
            'utilidad': self.utilidad_intervenciones,
            'carga': self.carga_cognitiva,
            'alineacion': self.alineacion_usuario,
            'aprendizaje': self.tasa_aprendizaje,
            'ultima_actualizacion': self.ultima_actualizacion.isoformat()
        }
    
    def __repr__(self) -> str:
        return (
            f"EstadoInterno(coherencia={self.coherencia_proposito:.2f}, "
            f"confianza={self.confianza_conocimiento:.2f})"
        )