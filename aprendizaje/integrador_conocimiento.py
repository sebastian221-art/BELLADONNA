"""
Integrador de Conocimiento
Integra conocimiento nuevo al sistema de Belladonna.
"""

import json
from pathlib import Path
from datetime import datetime

class IntegradorConocimiento:
    """
    Integra palabras aprendidas al vocabulario de Belladonna.
    """
    
    def __init__(self, detector_lagunas):
        self.detector = detector_lagunas
        self.palabras_aprendidas_path = Path("data/palabras_aprendidas.json")
        self.palabras_aprendidas = self._cargar_palabras_aprendidas()
    
    def _cargar_palabras_aprendidas(self):
        """
        Carga historial de palabras aprendidas.
        """
        if self.palabras_aprendidas_path.exists():
            with open(self.palabras_aprendidas_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def _guardar_palabras_aprendidas(self):
        """
        Guarda historial de palabras aprendidas.
        """
        self.palabras_aprendidas_path.parent.mkdir(exist_ok=True)
        with open(self.palabras_aprendidas_path, 'w', encoding='utf-8') as f:
            json.dump(self.palabras_aprendidas, f, ensure_ascii=False, indent=2)
    
    def integrar_palabra(self, investigacion):
        """
        Integra palabra investigada al vocabulario.
        
        Args:
            investigacion: Resultado de investigador_web
        """
        palabra = investigacion['palabra']
        
        # Valida confianza mínima
        if investigacion['confianza'] < 30:
            print(f"[Integrador] '{palabra}' tiene confianza muy baja ({investigacion['confianza']}%). No se integra.")
            return False
        
        # Añade al vocabulario conocido
        self.detector.agregar_palabra_conocida(palabra)
        
        # Registra aprendizaje
        aprendizaje = {
            'palabra': palabra,
            'definiciones': investigacion['definiciones'],
            'tipo': investigacion['tipo'],
            'fuentes': investigacion['fuentes'],
            'confianza': investigacion['confianza'],
            'fecha_aprendida': datetime.now().isoformat()
        }
        
        self.palabras_aprendidas.append(aprendizaje)
        self._guardar_palabras_aprendidas()
        
        # Marca laguna como resuelta
        self.detector.marcar_laguna_resuelta(palabra)
        
        print(f"✅ '{palabra}' integrada al vocabulario (confianza: {investigacion['confianza']}%)")
        
        return True
    
    def obtener_palabras_aprendidas_hoy(self):
        """
        Obtiene palabras aprendidas hoy.
        """
        hoy = datetime.now().date().isoformat()
        
        return [
            p for p in self.palabras_aprendidas
            if p['fecha_aprendida'].startswith(hoy)
        ]
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas de aprendizaje.
        """
        return {
            'total_aprendidas': len(self.palabras_aprendidas),
            'aprendidas_hoy': len(self.obtener_palabras_aprendidas_hoy()),
            'vocabulario_total': len(self.detector.vocabulario_conocido)
        }