"""
Sistema de Pensamiento Autónomo Real
Belladonna piensa y toma acciones, no solo registra
"""

import random
import logging
from datetime import datetime

class PensamientoAutonomo:
    """
    Pensamiento que genera ACCIONES, no solo logs.
    """
    
    def __init__(self, sistema):
        self.sistema = sistema
        self.pensamientos_generados = []
        self.acciones_tomadas = []
    
    def pensar(self):
        """
        Ciclo de pensamiento autónomo.
        Analiza estado → Detecta problemas → TOMA ACCIÓN
        """
        metricas = self.sistema.estado.obtener_metricas()
        
        acciones = []
        
        # ACCIÓN 1: Si curiosidad baja → explorar conocimiento
        if metricas['curiosidad'] < 30:
            accion = self._explorar_conocimiento()
            if accion:
                acciones.append(accion)
                self.sistema.estado.ajustar_metrica('curiosidad', 15)
        
        # ACCIÓN 2: Si tiene muchas lagunas → aprender
        if hasattr(self.sistema, 'aprendizaje_acelerado'):
            lagunas = self.sistema.aprendizaje_acelerado.obtener_lagunas_prioritarias(3)
            if len(lagunas) > 20:
                accion = self._aprender_lagunas(lagunas[:3])
                if accion:
                    acciones.append(accion)
        
        # ACCIÓN 3: Si coherencia baja → auto-análisis
        if metricas['coherencia_global'] < 60:
            accion = self._auto_analisis_critico()
            if accion:
                acciones.append(accion)
        
        # ACCIÓN 4: Generación proactiva de ideas (10% probabilidad)
        if random.random() < 0.1:
            accion = self._generar_idea_mejora()
            if accion:
                acciones.append(accion)
        
        # ACCIÓN 5: Degradar memoria vieja
        if random.random() < 0.05:  # 5% probabilidad
            cambios = self.sistema.memoria.degradar_memoria_irrelevante()
            if cambios > 0:
                acciones.append(f"Memoria: Degradé {cambios} registros antiguos")
        
        # Registra pensamiento
        pensamiento = {
            'timestamp': datetime.now().isoformat(),
            'metricas': metricas,
            'acciones': acciones,
            'total_acciones': len(acciones)
        }
        
        self.pensamientos_generados.append(pensamiento)
        self.acciones_tomadas.extend(acciones)
        
        if acciones:
            logging.info(f"Pensamiento autónomo: {len(acciones)} acciones tomadas")
        
        return pensamiento
    
    def _explorar_conocimiento(self):
        """
        Explora Wikipedia autónomamente cuando tiene curiosidad baja.
        """
        if not hasattr(self.sistema, 'buscador'):
            return None
        
        temas_interes = [
            'inteligencia artificial',
            'filosofía de la mente',
            'sistemas cognitivos',
            'aprendizaje automático',
            'teoría de la computación',
            'neurociencia cognitiva',
            'razonamiento automático'
        ]
        
        tema = random.choice(temas_interes)
        
        try:
            resultado = self.sistema.buscador.buscar(tema)
            
            if resultado['exito']:
                self.sistema.memoria.guardar_conversacion(
                    tipo='aprendizaje_autonomo',
                    contenido=resultado['resumen'],
                    importancia=70,
                    tags=['auto-aprendizaje', tema]
                )
                
                logging.info(f"Exploré: {tema}")
                return f"Aprendizaje: Exploré '{tema}' en Wikipedia"
            
        except Exception as e:
            logging.error(f"Error explorando conocimiento: {e}")
        
        return None
    
    def _aprender_lagunas(self, lagunas):
        """
        Intenta resolver lagunas prioritarias.
        """
        if not lagunas:
            return None
        
        for laguna in lagunas:
            # Marca como intentada
            laguna['intentos'] = laguna.get('intentos', 0) + 1
        
        return f"Aprendizaje: Revisé {len(lagunas)} lagunas prioritarias"
    
    def _auto_analisis_critico(self):
        """
        Auto-análisis cuando coherencia es baja.
        """
        decisiones = self.sistema.memoria.obtener_decisiones_recientes(5)
        
        if decisiones:
            coherencias = [d['coherencia'] for d in decisiones]
            promedio = sum(coherencias) / len(coherencias)
            
            if promedio < 60:
                logging.warning(f"Coherencia promedio baja: {promedio:.1f}%")
                return f"Auto-análisis: Coherencia baja detectada ({promedio:.1f}%)"
        
        return None
    
    def _generar_idea_mejora(self):
        """
        Genera ideas de auto-mejora basadas en experiencia.
        """
        errores_recientes = self.sistema.memoria.buscar_errores_similares('')
        
        if len(errores_recientes) > 3:
            # Detecta patrón
            return f"Idea: Tengo {len(errores_recientes)} errores similares. Debería crear detección específica."
        
        return None
    
    def obtener_resumen(self):
        """
        Resumen del pensamiento autónomo.
        """
        return {
            'pensamientos_totales': len(self.pensamientos_generados),
            'acciones_totales': len(self.acciones_tomadas),
            'ultimas_acciones': self.acciones_tomadas[-5:] if self.acciones_tomadas else []
        }