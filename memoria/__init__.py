# memoria/__init__.py

"""
Sistema de Memoria de Belladonna.

Módulos:
- memoria_conversacion: Memoria de sesión actual
- persistencia: Persistencia en SQLite
"""

from memoria.memoria_conversacion import MemoriaConversacion, MensajeMemoria
from memoria.persistencia import PersistenciaMemoria

__all__ = [
    'MemoriaConversacion',
    'MensajeMemoria',
    'PersistenciaMemoria'
]