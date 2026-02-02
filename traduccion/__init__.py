"""
Módulo de traducción de Belladonna.

Traduce entre español natural y conceptos anclados (lenguaje interno de Bell).
"""

from traduccion.analizador_gramatical import AnalizadorGramatical
from traduccion.traductor_entrada import TraductorEntrada
from traduccion.traductor_salida import TraductorSalida

__all__ = [
    'AnalizadorGramatical',
    'TraductorEntrada',
    'TraductorSalida'
]