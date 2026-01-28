"""
Orquestador de Aprendizaje
Coordina TODO el proceso de aprendizaje autónomo.
"""

from .detector_lagunas import DetectorLagunas
from .investigador_web import InvestigadorWeb
from .integrador_conocimiento import IntegradorConocimiento
import logging

class OrquestadorAprendizaje:
    """
    Coordina detección → investigación → integración.
    """
    
    def __init__(self):
        self.detector = DetectorLagunas()
        self.investigador = InvestigadorWeb()
        self.integrador = IntegradorConocimiento(self.detector)
        
        logging.info("Orquestador de Aprendizaje inicializado")
    
    def procesar_mensaje_y_aprender(self, mensaje):
        """
        Pipeline completo de aprendizaje.
        
        1. Detecta lagunas
        2. Investiga palabras desconocidas
        3. Integra conocimiento
        
        Args:
            mensaje: Mensaje del usuario
            
        Returns:
            {
                'lagunas_detectadas': int,
                'palabras_aprendidas': int,
                'palabras_fallidas': [...]
            }
        """
        # 1. DETECTAR
        analisis = self.detector.analizar_mensaje(mensaje)
        
        if analisis['total_desconocidas'] == 0:
            return {
                'lagunas_detectadas': 0,
                'palabras_aprendidas': 0,
                'palabras_fallidas': []
            }
        
        logging.info(f"Detectadas {analisis['total_desconocidas']} palabras desconocidas")
        
        # 2. INVESTIGAR (máximo 5 a la vez para no saturar)
        palabras_investigar = analisis['palabras_desconocidas'][:5]
        
        aprendidas = 0
        fallidas = []
        
        for item in palabras_investigar:
            palabra = item['palabra']
            
            try:
                # Investiga
                investigacion = self.investigador.investigar_palabra(palabra)
                
                # Integra
                if self.integrador.integrar_palabra(investigacion):
                    aprendidas += 1
                else:
                    fallidas.append({
                        'palabra': palabra,
                        'razon': 'confianza_baja'
                    })
                    
            except Exception as e:
                logging.error(f"Error aprendiendo '{palabra}': {e}")
                fallidas.append({
                    'palabra': palabra,
                    'razon': str(e)
                })
        
        return {
            'lagunas_detectadas': analisis['total_desconocidas'],
            'palabras_aprendidas': aprendidas,
            'palabras_fallidas': fallidas
        }
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas completas de aprendizaje.
        """
        return self.integrador.obtener_estadisticas()
    
    def obtener_palabras_aprendidas_hoy(self):
        """
        Obtiene palabras aprendidas hoy.
        """
        return self.integrador.obtener_palabras_aprendidas_hoy()