"""
Define qué puede hacer Bell en la realidad.
"""
from pathlib import Path
from typing import Any

class CapacidadesBell:
    """
    Operaciones que Bell REALMENTE puede ejecutar.
    
    Si algo está aquí, Bell lo puede hacer.
    Si no está aquí, Bell NO puede hacerlo.
    """
    
    @staticmethod
    def leer_archivo(ruta: str) -> str:
        """Lee contenido de un archivo."""
        return Path(ruta).read_text(encoding='utf-8')
    
    @staticmethod
    def escribir_archivo(ruta: str, contenido: str) -> bool:
        """Escribe contenido en un archivo."""
        try:
            Path(ruta).write_text(contenido, encoding='utf-8')
            return True
        except Exception:
            return False
    
    @staticmethod
    def archivo_existe(ruta: str) -> bool:
        """Verifica si un archivo existe."""
        return Path(ruta).exists()
    
    @staticmethod
    def obtener_tamaño_archivo(ruta: str) -> int:
        """Obtiene tamaño de archivo en bytes."""
        return Path(ruta).stat().st_size
    
    @staticmethod
    def listar_directorio(ruta: str) -> list:
        """Lista archivos en un directorio."""
        return [str(p) for p in Path(ruta).iterdir()]