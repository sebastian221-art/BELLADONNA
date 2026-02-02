"""
Módulo core de Belladonna.

Contiene las estructuras fundamentales del sistema.
"""

__version__ = "0.1.0"

from core.concepto_anclado import ConceptoAnclado, TipoConcepto
from core.capacidades_bell import CapacidadesBell
from core.valores import SistemaValores, Principio
from core.estado_interno import EstadoInterno

__all__ = [
    'ConceptoAnclado',
    'TipoConcepto',
    'CapacidadesBell',
    'SistemaValores',
    'Principio',
    'EstadoInterno'
]