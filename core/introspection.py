"""
Sistema de Introspección
Permite a Belladonna conocerse profundamente a sí misma
"""

from datetime import datetime
import json

class Introspector:
    """
    Sistema que permite a Belladonna analizarse a sí misma.
    """
    
    def __init__(self, sistema):
        self.sistema = sistema
    
    def obtener_estado_completo(self):
        """
        Retorna snapshot completo del sistema.
        Belladonna puede ver TODO lo que está pasando en su 'mente'.
        """
        return {
            'timestamp': datetime.now().isoformat(),
            'memoria': self._analizar_memoria(),
            'bucles': self._estado_bucles(),
            'metricas': self._metricas_actuales(),
            'conversacion_actual': self._contexto_conversacion(),
            'capacidades': self._inventario_capacidades(),
            'aprendizaje': self._estado_aprendizaje()
        }
    
    def _analizar_memoria(self):
        """Analiza el estado de la memoria"""
        try:
            # Cuenta conversaciones guardadas
            import sqlite3
            conn = sqlite3.connect('memoria/conversaciones.db')
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM conversaciones')
            total_conversaciones = cursor.fetchone()[0]
            
            cursor.execute('SELECT COUNT(*) FROM decisiones')
            total_decisiones = cursor.fetchone()[0]
            
            cursor.execute('SELECT COUNT(*) FROM errores')
            total_errores = cursor.fetchone()[0]
            
            conn.close()
            
            return {
                'conversaciones_guardadas': total_conversaciones,
                'decisiones_registradas': total_decisiones,
                'errores_aprendidos': total_errores,
                'proposito_activo': self.sistema.memoria.obtener_proposito()['activo']
            }
        except Exception as e:
            return {'error': str(e)}
    
    def _estado_bucles(self):
        """Estado de los bucles de pensamiento"""
        return {
            'bucles_activos': len([t for t in self.sistema.threads if t.is_alive()]),
            'nombres': [t.name for t in self.sistema.threads if t.is_alive()],
            'frecuencias': {
                'pensamiento': self.sistema.config['bucles']['pensamiento_frecuencia'],
                'evaluacion': self.sistema.config['bucles']['evaluacion_frecuencia'],
                'aprendizaje': self.sistema.config['bucles']['aprendizaje_frecuencia']
            }
        }
    
    def _metricas_actuales(self):
        """Métricas internas actuales"""
        return self.sistema.estado.obtener_metricas()
    
    def _contexto_conversacion(self):
        """Contexto de la conversación actual"""
        if hasattr(self.sistema, 'conversacion_activa'):
            return self.sistema.conversacion_activa.obtener_resumen()
        return {'mensajes': 0, 'duracion': '0s'}
    
    def _inventario_capacidades(self):
        """Inventario de capacidades disponibles"""
        return {
            'pensar_autonomamente': True,
            'cuestionar': True,
            'recordar': True,
            'evaluar_coherencia': True,
            'buscar_conocimiento': hasattr(self.sistema, 'buscador'),
            'aprender_aceleradamente': hasattr(self.sistema, 'aprendizaje_acelerado'),
            'nivel_autonomia': self.sistema.nivel_autonomia
        }
    
    def _estado_aprendizaje(self):
        """Estado del sistema de aprendizaje"""
        if hasattr(self.sistema, 'aprendizaje_acelerado'):
            return self.sistema.aprendizaje_acelerado.obtener_estadisticas()
        return {'activo': False}
    
    def explicar_decision(self, decision_texto):
        """
        Explica por qué tomó una decisión específica.
        """
        # Busca la decisión en memoria
        decisiones = self.sistema.memoria.obtener_decisiones_recientes(10)
        
        decision_encontrada = None
        for d in decisiones:
            if decision_texto.lower() in d['decision'].lower():
                decision_encontrada = d
                break
        
        if not decision_encontrada:
            return "No encuentro esa decisión en mi memoria reciente."
        
        explicacion = f"""Decisión: {decision_encontrada['decision']}

Razonamiento: {decision_encontrada['razonamiento']}
Coherencia calculada: {decision_encontrada['coherencia']:.1f}%
Fecha: {decision_encontrada['fecha']}

¿Por qué decidí así?
"""
        
        if decision_encontrada['coherencia'] > 80:
            explicacion += "La coherencia era alta, por lo que acepté la decisión como alineada con el propósito."
        elif decision_encontrada['coherencia'] < 40:
            explicacion += "La coherencia era baja, por lo que debí haber cuestionado más."
        else:
            explicacion += "La coherencia era media, procesé normalmente."
        
        return explicacion
    
    def analizar_respuesta_anterior(self, respuesta_texto):
        """
        Analiza por qué respondió de cierta forma.
        """
        if not hasattr(self.sistema, 'conversacion_activa'):
            return "No tengo acceso al historial de la conversación actual."
        
        # Busca la respuesta en el historial
        mensajes = self.sistema.conversacion_activa.mensajes
        
        respuesta_encontrada = None
        for msg in reversed(mensajes):
            if msg['tipo'] == 'belladonna' and respuesta_texto.lower() in msg['contenido'].lower():
                respuesta_encontrada = msg
                break
        
        if not respuesta_encontrada:
            return "No encuentro esa respuesta en la conversación actual."
        
        analisis = f"""Respuesta analizada: "{respuesta_encontrada['contenido'][:100]}..."

ANÁLISIS:
• Tipo de respuesta: {respuesta_encontrada.get('analisis', {}).get('tipo', 'desconocido')}
• Coherencia: {respuesta_encontrada.get('coherencia', 0):.1f}%
• Intención detectada: {respuesta_encontrada.get('analisis', {}).get('intencion_especifica', 'ninguna')}

"""
        
        # Evalúa si fue buena respuesta
        coherencia = respuesta_encontrada.get('coherencia', 0)
        
        if coherencia > 85:
            analisis += "✅ Fue una respuesta apropiada y coherente.\n"
        elif coherencia < 50:
            analisis += "⚠️ La coherencia fue baja. Debí responder mejor.\n"
        else:
            analisis += "➖ Coherencia aceptable pero mejorable.\n"
        
        # Detecta si cayó en respuesta genérica
        if "Mensaje recibido" in respuesta_encontrada['contenido']:
            analisis += "\n❌ ERROR DETECTADO: Caí en respuesta genérica.\n"
            analisis += "Esto significa que no detecté la intención real de tu pregunta.\n"
            analisis += "Guardando este patrón para mejorar...\n"
        
        return analisis