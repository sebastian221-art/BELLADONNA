"""
Módulo de razonamiento de Belladonna.

Procesa en lenguaje interno y toma decisiones basadas en grounding real.
"""

from razonamiento.evaluador_capacidades import EvaluadorCapacidades
from razonamiento.motor_razonamiento import MotorRazonamiento

__all__ = [
    'EvaluadorCapacidades',
    'MotorRazonamiento'
]