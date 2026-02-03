"""
Gestor de Consejeras de Belladonna.

Este archivo coordina la carga de todas las consejeras.
Arquitectura MODULAR: cada consejera en su propia carpeta.

PATRÓN IGUAL A vocabulario/gestor_vocabulario.py
"""
from typing import List, Optional
from consejeras.base_consejera import Consejera

class GestorConsejeras:
    """
    Administra TODAS las consejeras de Bell de forma modular.
    
    Ventajas:
    - Cada consejera en su carpeta
    - Fácil agregar sin modificar archivos existentes
    - Organización clara por especialidad
    - Consistencia con GestorVocabulario
    """
    
    def __init__(self):
        self.consejeras: List[Consejera] = []
        self._cargar_todas_las_consejeras()
    
    def _cargar_todas_las_consejeras(self):
        """
        Carga consejeras de todos los módulos.
        
        PATRÓN: Importar y extender, nunca modificar.
        
        FASE 2 - SEMANA 1: Vega, Nova, Echo
        """
        
        # SEMANA 1: Fundacionales (3 consejeras)
        from consejeras.vega import Vega
        from consejeras.nova import Nova
        from consejeras.echo import Echo
        
        self.consejeras.append(Vega())
        self.consejeras.append(Nova())
        self.consejeras.append(Echo())
        
        # SEMANA 2: Empáticas y Visionarias (4 consejeras - AGREGAR DESPUÉS)
        # from consejeras.lyra import Lyra
        # from consejeras.luna import Luna
        # from consejeras.iris import Iris
        # from consejeras.sage import Sage
        # 
        # self.consejeras.append(Lyra())
        # self.consejeras.append(Luna())
        # self.consejeras.append(Iris())
        # self.consejeras.append(Sage())
    
    def obtener_todas(self) -> List[Consejera]:
        """Retorna todas las consejeras cargadas."""
        return self.consejeras
    
    def obtener_activas(self) -> List[Consejera]:
        """Retorna solo las consejeras activas."""
        return [c for c in self.consejeras if c.activa]
    
    def buscar_por_nombre(self, nombre: str) -> Optional[Consejera]:
        """
        Busca una consejera por nombre.
        
        Ejemplo:
            gestor.buscar_por_nombre("Vega") → Vega
        """
        nombre_lower = nombre.lower()
        for consejera in self.consejeras:
            if consejera.nombre.lower() == nombre_lower:
                return consejera
        return None
    
    def activar(self, nombre: str) -> bool:
        """Activa una consejera por nombre."""
        consejera = self.buscar_por_nombre(nombre)
        if consejera:
            consejera.activar()
            return True
        return False
    
    def desactivar(self, nombre: str) -> bool:
        """Desactiva una consejera por nombre."""
        consejera = self.buscar_por_nombre(nombre)
        if consejera:
            consejera.desactivar()
            return True
        return False
    
    def estadisticas(self) -> dict:
        """
        Retorna estadísticas del sistema de consejeras.
        
        Útil para validar que el sistema está balanceado.
        """
        total = len(self.consejeras)
        activas = len([c for c in self.consejeras if c.activa])
        
        # Estadísticas agregadas
        total_revisiones = sum(c.revisiones_realizadas for c in self.consejeras)
        total_vetos = sum(c.vetos_aplicados for c in self.consejeras)
        
        return {
            'total_consejeras': total,
            'activas': activas,
            'inactivas': total - activas,
            'total_revisiones': total_revisiones,
            'total_vetos': total_vetos,
            'consejeras': [
                {
                    'nombre': c.nombre,
                    'especialidad': c.especialidad,
                    'activa': c.activa,
                    'revisiones': c.revisiones_realizadas,
                    'vetos': c.vetos_aplicados
                }
                for c in self.consejeras
            ]
        }