"""
Clase Base para Consejeras.

Todas las consejeras heredan de aquí.
"""
from abc import ABC, abstractmethod
from typing import Dict, Optional
from razonamiento.tipos_decision import Decision
from core.principios import Principio

class Consejera(ABC):
    """
    Clase abstracta para consejeras.
    
    Cada consejera especializa en proteger ciertos principios.
    """
    
    def __init__(self, nombre: str):
        """
        Args:
            nombre: Nombre de la consejera
        """
        self.nombre = nombre
        self.principios_vigilados = []  # Principios que vigila esta consejera
        self.vetos_aplicados = 0
        self.revisiones_realizadas = 0
    
    @abstractmethod
    def revisar(self, decision: Decision, contexto: Dict) -> Dict:
        """
        Revisa una decisión y determina si viola principios.
        
        Args:
            decision: Decision del motor de razonamiento
            contexto: Contexto adicional (traducción, etc.)
            
        Returns:
            {
                'aprobada': bool,
                'veto': bool,
                'principio_violado': Principio or None,
                'razon_veto': str or None,
                'recomendacion': str or None
            }
        """
        pass
    
    def registrar_revision(self, aprobada: bool):
        """Registra estadística de revisión."""
        self.revisiones_realizadas += 1
        if not aprobada:
            self.vetos_aplicados += 1
    
    def estadisticas(self) -> Dict:
        """Retorna estadísticas de la consejera."""
        if self.revisiones_realizadas == 0:
            tasa_veto = 0.0
        else:
            tasa_veto = self.vetos_aplicados / self.revisiones_realizadas
        
        return {
            'nombre': self.nombre,
            'revisiones': self.revisiones_realizadas,
            'vetos': self.vetos_aplicados,
            'tasa_veto': round(tasa_veto, 2),
            'principios_vigilados': [p.name for p in self.principios_vigilados]
        }