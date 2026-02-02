"""
CapacidadesBell - Registro de capacidades ejecutables de Bell.

Bell solo puede decir que "puede hacer X" si realmente puede ejecutar X.
"""

from typing import Dict, Callable, List


class CapacidadesBell:
    """
    Registro de capacidades reales de Bell.
    
    Cada capacidad es una operación que Bell puede ejecutar.
    """
    
    def __init__(self):
        self.capacidades: Dict[str, Callable] = {}
    
    def registrar_capacidad(self, nombre: str, operacion: Callable):
        """
        Registra nueva capacidad.
        
        Args:
            nombre: Nombre de la capacidad
            operacion: Función ejecutable
        """
        self.capacidades[nombre] = operacion
    
    def tiene_capacidad(self, nombre: str) -> bool:
        """
        Verifica si Bell tiene una capacidad.
        
        Args:
            nombre: Nombre de la capacidad
            
        Returns:
            True si la capacidad existe
        """
        return nombre in self.capacidades
    
    def ejecutar_capacidad(self, nombre: str, *args, **kwargs):
        """
        Ejecuta capacidad.
        
        Args:
            nombre: Nombre de la capacidad
            *args, **kwargs: Argumentos
            
        Returns:
            Resultado de la ejecución
            
        Raises:
            KeyError: Si la capacidad no existe
        """
        if not self.tiene_capacidad(nombre):
            raise KeyError(f"Bell no tiene capacidad '{nombre}'")
        
        return self.capacidades[nombre](*args, **kwargs)
    
    def listar_capacidades(self) -> List[str]:
        """
        Lista todas las capacidades.
        
        Returns:
            Lista de nombres de capacidades
        """
        return list(self.capacidades.keys())
    
    def __repr__(self) -> str:
        return f"CapacidadesBell(capacidades={len(self.capacidades)})"