"""
Sistema de Valores Núcleo
Principios inviolables de Belladonna
"""

import json
from pathlib import Path

class ValoresNucleo:
    """
    Gestiona los principios inviolables del sistema.
    Estos valores NO pueden modificarse por aprendizaje.
    """
    
    def __init__(self):
        self.ruta_principios = Path("memoria/principios.json")
        self.principios = self._cargar_principios()
    
    def _cargar_principios(self):
        """Carga principios desde archivo"""
        try:
            with open(self.ruta_principios, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data['principios_inviolables']
        except FileNotFoundError:
            print("⚠️  Archivo de principios no encontrado")
            return []
    
    def obtener_principio(self, id_principio):
        """Obtiene un principio específico por ID"""
        for principio in self.principios:
            if principio['id'] == id_principio:
                return principio
        return None
    
    def listar_principios(self):
        """Lista todos los principios"""
        return self.principios
    
    def validar_accion(self, accion, contexto):
        """
        Valida si una acción respeta los valores núcleo.
        Retorna: (es_valida, principios_violados)
        """
        violaciones = []
        
        # Lógica de validación básica
        # TODO: Implementar validaciones específicas por principio
        
        return len(violaciones) == 0, violaciones
    
    def explicar_principio(self, id_principio):
        """Explica un principio en detalle"""
        principio = self.obtener_principio(id_principio)
        if principio:
            return f"{principio['nombre']}: {principio['descripcion']}"
        return "Principio no encontrado"