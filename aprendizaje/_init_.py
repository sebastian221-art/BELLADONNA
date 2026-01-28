"""
Sistema de Aprendizaje Autónomo v0.4
Belladonna aprende del mundo por sí misma.
"""

from .detector_lagunas import DetectorLagunas
from .investigador_web import InvestigadorWeb
from .integrador_conocimiento import IntegradorConocimiento
from .orquestador_aprendizaje import OrquestadorAprendizaje

__all__ = [
    'DetectorLagunas',
    'InvestigadorWeb', 
    'IntegradorConocimiento',
    'OrquestadorAprendizaje'
]