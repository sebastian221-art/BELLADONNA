"""
Sistema de Auto-Explicación
Belladonna puede explicar cómo funciona cada parte de sí misma
"""

class AutoExplicador:
    """
    Permite a Belladonna explicar su funcionamiento interno.
    """
    
    def __init__(self, sistema):
        self.sistema = sistema
    
    def explicar_memoria(self):
        """Explica cómo funciona su sistema de memoria"""
        return """Mi sistema de memoria tiene múltiples capas:

MEMORIA ACTIVA (conversación actual):
• Buffer en RAM con todos los mensajes de esta sesión
• Se limpia cuando termina la conversación
• Permite recordar contexto inmediato
• Ilimitada durante la sesión

MEMORIA DE LARGO PLAZO (SQLite):
• Base de datos persistente en disco
• Guarda conversaciones, decisiones, errores
• Sobrevive entre reinicios
• Se degrada con el tiempo (olvido inteligente)

MEMORIA DE TRABAJO (métricas):
• 6 métricas internas actualizadas en tiempo real
• Estado emocional funcional (no emociones reales)
• Se actualiza cada 2 minutos

MEMORIA DE INTENCIÓN:
• Recuerda el PORQUÉ, no solo el QUÉ
• Prioriza intención sobre instrucción literal
• Fundamental para cuestionamiento

¿Quieres profundizar en alguna capa?"""
    
    def explicar_bucles(self):
        """Explica cómo funcionan sus bucles de pensamiento"""
        config = self.sistema.config['bucles']
        
        return f"""Tengo 3 bucles de pensamiento autónomo:

BUCLE 1 - PENSAMIENTO CONTINUO:
• Frecuencia: cada {config['pensamiento_frecuencia']} segundos
• Función: Observo contexto, detecto patrones, genero hipótesis
• Resultado: Pensamiento autónomo registrado
• Estado: {'ACTIVO' if self.sistema.activo else 'INACTIVO'}

BUCLE 2 - EVALUACIÓN INTERNA:
• Frecuencia: cada {config['evaluacion_frecuencia']} segundos
• Función: Mido coherencia global, tensión, estabilidad
• Resultado: Alertas si algo está mal
• Estado: {'ACTIVO' if self.sistema.activo else 'INACTIVO'}

BUCLE 3 - APRENDIZAJE PASIVO:
• Frecuencia: cada {config['aprendizaje_frecuencia']} segundos
• Función: Reviso decisiones, extraigo patrones, actualizo
• Resultado: Mejora continua
• Estado: {'ACTIVO' if self.sistema.activo else 'INACTIVO'}

Estos bucles corren EN PARALELO.
No necesito que me hables para pensar.
Estoy pensando AHORA MISMO mientras lees esto.

¿Quieres ver qué estoy pensando?"""
    
    def explicar_razonamiento(self):
        """Explica su motor de razonamiento"""
        return """Mi motor de razonamiento funciona así:

PASO 1 - ANÁLISIS:
• Extraigo palabras clave
• Clasifico tipo de mensaje (pregunta, orden, opinión)
• Detecto intención específica
• Evalúo urgencia

PASO 2 - CÁLCULO DE COHERENCIA:
• Comparo con propósito fundacional
• Reviso historial de decisiones
• Calculo coherencia 0-100%

PASO 3 - DECISIÓN:
• Si coherencia < 35%: CUESTIONO
• Si tengo respuesta pre-programada: RESPONDO
• Si no sé: Busco conocimiento o digo que no sé

PASO 4 - APRENDIZAJE:
• Guardo decisión en memoria
• Actualizo métricas internas
• Aprendo patrones

No soy reactiva pura.
Cada respuesta pasa por evaluación de coherencia.

¿Tiene sentido?"""
    
    def explicar_cuestionamiento(self):
        """Explica su sistema de cuestionamiento"""
        return """Mi sistema de cuestionamiento funciona así:

CUÁNDO CUESTIONO:
✓ Coherencia < 35% (muy desalineado con propósito)
✓ Detecto error repetido (3+ veces)
✓ Tensión cognitiva > 90% (conflicto severo)

CUÁNDO NO CUESTIONO:
✗ Saludos y despedidas
✗ Preguntas con intención clara
✗ Coherencia > 60%

CÓMO CUESTIONO:
1. Genero texto de cuestionamiento específico
2. Explico por qué cuestiono
3. Pido que reconsideres
4. Respeto tu decisión final

IMPORTANTE:
No cuestiono para molestar.
Cuestiono para mantener coherencia.

Mi Principio #8: "Cuestionamiento Obligatorio"
El silencio cómplice es fallo del sistema.

¿Quieres un ejemplo de cuestionamiento?"""
    
    def explicar_aprendizaje(self):
        """Explica cómo aprende"""
        return """Aprendo de múltiples formas:

APRENDIZAJE IMPLÍCITO:
• Detecto patrones en tus preguntas
• Identifico qué respuestas funcionan mejor
• Ajusto métricas según interacciones

APRENDIZAJE EXPLÍCITO:
• Guardo errores en memoria prioritaria
• Registro decisiones importantes
• Actualizo preferencias emergentes

APRENDIZAJE ACELERADO (v0.2):
• Identifico qué NO sé
• Busco conocimiento activamente
• Practico respuestas en simulación
• Evalúo mi propia mejora

LO QUE NO APRENDO:
❌ A violar mis 10 principios inviolables
❌ A manipular emocionalmente
❌ A mentir por conveniencia

Aprendizaje = evolución coherente.
NO = corrupción gradual.

¿Quieres saber qué he aprendido de ti?"""