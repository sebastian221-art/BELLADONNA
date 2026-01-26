"""
Memoria de Conversación Activa
Mantiene contexto completo de la conversación actual
"""

from datetime import datetime

class ConversacionActiva:
    """
    Mantiene el contexto completo de la conversación en curso.
    Belladonna recuerda TODO lo que se ha dicho.
    """
    
    def __init__(self):
        self.mensajes = []
        self.inicio = datetime.now()
        self.temas_discutidos = set()
        self.preguntas_usuario = []
        self.respuestas_propias = []
    
    def agregar_mensaje(self, tipo, contenido, coherencia=None, analisis=None):
        """
        Guarda un mensaje en el contexto.
        
        tipo: 'usuario' o 'belladonna'
        contenido: texto del mensaje
        coherencia: coherencia calculada (solo para respuestas)
        analisis: análisis del input (solo para mensajes usuario)
        """
        mensaje = {
            'tipo': tipo,
            'contenido': contenido,
            'timestamp': datetime.now().isoformat(),
            'coherencia': coherencia,
            'analisis': analisis
        }
        
        self.mensajes.append(mensaje)
        
        # Extrae temas (palabras clave)
        if analisis and 'palabras_clave' in analisis:
            self.temas_discutidos.update(analisis['palabras_clave'])
        
        # Guarda preguntas y respuestas separadas
        if tipo == 'usuario':
            self.preguntas_usuario.append(contenido)
        else:
            self.respuestas_propias.append(contenido)
    
    def obtener_resumen(self):
        """
        Retorna resumen de la conversación actual.
        """
        duracion = (datetime.now() - self.inicio).total_seconds()
        minutos = int(duracion // 60)
        segundos = int(duracion % 60)
        
        return {
            'total_mensajes': len(self.mensajes),
            'mensajes_usuario': len(self.preguntas_usuario),
            'mensajes_belladonna': len(self.respuestas_propias),
            'duracion': f"{minutos}m {segundos}s",
            'temas_discutidos': list(self.temas_discutidos)[:10],
            'coherencia_promedio': self._calcular_coherencia_promedio()
        }
    
    def _calcular_coherencia_promedio(self):
        """Calcula coherencia promedio de la conversación"""
        coherencias = [m['coherencia'] for m in self.mensajes if m['coherencia'] is not None]
        if coherencias:
            return sum(coherencias) / len(coherencias)
        return 0.0
    
    def buscar_en_conversacion(self, query):
        """
        Busca un tema en la conversación actual.
        """
        query_lower = query.lower()
        resultados = []
        
        for msg in self.mensajes:
            if query_lower in msg['contenido'].lower():
                resultados.append({
                    'tipo': msg['tipo'],
                    'contenido': msg['contenido'][:200],
                    'timestamp': msg['timestamp']
                })
        
        return resultados
    
    def obtener_contexto_completo(self, ultimos_n=10):
        """
        Retorna los últimos N mensajes para contexto.
        """
        return self.mensajes[-ultimos_n:]
    
    def obtener_historial_formateado(self):
        """
        Retorna historial legible para que Belladonna lo reporte.
        """
        historial = []
        
        for i, msg in enumerate(self.mensajes, 1):
            if msg['tipo'] == 'usuario':
                historial.append(f"{i}. Tú: {msg['contenido'][:100]}")
            else:
                historial.append(f"{i}. Yo: {msg['contenido'][:100]}")
        
        return "\n".join(historial)
    
    def analizar_patrones(self):
        """
        Analiza patrones en la conversación.
        """
        patrones = {
            'tipos_preguntas': {},
            'temas_frecuentes': {},
            'coherencia_tendencia': []
        }
        
        for msg in self.mensajes:
            if msg['tipo'] == 'usuario' and msg['analisis']:
                tipo = msg['analisis'].get('tipo', 'desconocido')
                patrones['tipos_preguntas'][tipo] = patrones['tipos_preguntas'].get(tipo, 0) + 1
            
            if msg['coherencia']:
                patrones['coherencia_tendencia'].append(msg['coherencia'])
        
        return patrones