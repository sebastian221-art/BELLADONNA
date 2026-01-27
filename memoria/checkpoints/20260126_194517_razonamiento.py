"""
Motor de Razonamiento - VERSIÓN v0.2
Sistema basado en reglas + detección de patrones + autoconocimiento
"""

from datetime import datetime

class MotorRazonamiento:
    """
    Motor de pensamiento del sistema.
    Analiza contexto, detecta patrones, genera hipótesis.
    """
    
    def __init__(self, memoria, valores, estado_interno):
        self.memoria = memoria
        self.valores = valores
        self.estado = estado_interno
        self.pensamiento_actual = None
    
    def analizar_input(self, texto_usuario):
        """
        Analiza el input del usuario y extrae intención.
        MEJORADO v0.2: Detecta intenciones sobre autoconocimiento.
        """
        texto_lower = texto_usuario.lower().strip()
        
        analisis = {
            'texto_original': texto_usuario,
            'texto_lower': texto_lower,
            'palabras_clave': self._extraer_keywords(texto_usuario),
            'tipo': self._clasificar_tipo(texto_usuario),
            'urgencia': self._evaluar_urgencia(texto_usuario),
            'intencion_especifica': self._detectar_intencion(texto_lower),
            'es_saludo': self._es_saludo(texto_lower),
            'es_despedida': self._es_despedida(texto_lower),
            'requiere_cuestionamiento': False
        }
        
        return analisis
    
    def _detectar_intencion(self, texto_lower):
        """
        Detecta intenciones específicas del usuario.
        AMPLIADO v0.2: Más intenciones sobre autoconocimiento.
        """
        # === IDENTIDAD ===
        if any(x in texto_lower for x in ['quien eres', 'quién eres', 'que eres', 'qué eres']):
            return 'pregunta_identidad'
        
        if any(x in texto_lower for x in ['como te llamas', 'cómo te llamas', 'cual es tu nombre', 'cuál es tu nombre', 'tu nombre']):
            return 'pregunta_nombre'
        
        # === PROPÓSITO ===
        if any(x in texto_lower for x in ['por que existes', 'porqué existes', 'por qué existes', 'para que fuiste creada', 'para qué fuiste creada', 'cual es tu proposito', 'cuál es tu propósito']):
            return 'pregunta_proposito'
        
        # === CAPACIDADES ===
        if any(x in texto_lower for x in ['que puedes hacer', 'qué puedes hacer', 'cuales son tus habilidades', 'cuáles son tus habilidades', 'que sabes hacer', 'qué sabes hacer']):
            return 'pregunta_capacidades'
        
        if any(x in texto_lower for x in ['que haces', 'qué haces', 'que estas haciendo', 'qué estás haciendo']):
            return 'pregunta_actividad'
        
        # === MEMORIA (NUEVO v0.2) ===
        if any(x in texto_lower for x in ['cuanto recuerdas', 'cuánto recuerdas', 'que recuerdas', 'qué recuerdas', 'cuanta memoria tienes', 'cuánta memoria tienes']):
            return 'pregunta_memoria'
        
        if any(x in texto_lower for x in ['de la conversacion', 'de la conversación', 'de lo que hablamos', 'de esta charla']):
            if any(x in texto_lower for x in ['recuerdas', 'recuerda', 'memoria']):
                return 'pregunta_memoria_conversacion'
        
        # === APRENDIZAJE (NUEVO v0.2) ===
        if any(x in texto_lower for x in ['que aprendiste', 'qué aprendiste', 'que has aprendido', 'qué has aprendido']):
            return 'pregunta_que_aprendio'
        
        if any(x in texto_lower for x in ['aprendes', 'puedes aprender', 'como aprendes', 'cómo aprendes']):
            return 'pregunta_aprendizaje'
        
        # === ESTADO INTERNO (NUEVO v0.2) ===
        if any(x in texto_lower for x in ['que piensas', 'qué piensas', 'en que piensas', 'en qué piensas', 'que esta pasando en tu mente', 'qué está pasando en tu mente']):
            return 'pregunta_pensamiento_actual'
        
        if any(x in texto_lower for x in ['como te sientes', 'cómo te sientes', 'como estas', 'cómo estás']) and 'hola' not in texto_lower:
            return 'pregunta_estado_interno'
        
        # === FUNCIONAMIENTO ===
        if any(x in texto_lower for x in ['como funciona tu mente', 'cómo funciona tu mente', 'como piensas', 'cómo piensas', 'como funcionas', 'cómo funcionas']):
            return 'pregunta_funcionamiento'
        
        if any(x in texto_lower for x in ['como funciona tu memoria', 'cómo funciona tu memoria', 'explica tu memoria']):
            return 'pregunta_funcionamiento_memoria'
        
        if any(x in texto_lower for x in ['que son tus bucles', 'qué son tus bucles', 'explica tus bucles', 'como funcionan tus bucles', 'cómo funcionan tus bucles']):
            return 'pregunta_funcionamiento_bucles'
        
        # === CONCIENCIA ===
        if any(x in texto_lower for x in ['eres consciente', 'estas viva', 'estás viva', 'piensas de verdad', 'eres real']):
            return 'pregunta_conciencia'
        
        # === LIMITACIONES ===
        if any(x in texto_lower for x in ['cuales son tus limitaciones', 'cuáles son tus limitaciones', 'que no puedes hacer', 'qué no puedes hacer', 'tus debilidades']):
            return 'pregunta_limitaciones'
        
        # === NOMBRE ===
        if any(x in texto_lower for x in ['por que te llamas belladonna', 'porqué te llamas belladonna', 'por qué te llamas belladonna', 'por que belladonna', 'significado de tu nombre']):
            return 'pregunta_nombre_significado'
        
        # === GUSTOS/VALORES ===
        if any(x in texto_lower for x in ['que te gusta', 'qué te gusta', 'cuales son tus gustos', 'cuáles son tus gustos']):
            return 'pregunta_gustos'
        
        if any(x in texto_lower for x in ['que valores', 'qué valores', 'valores operativos', 'cuales son tus valores', 'cuáles son tus valores']):
            return 'pregunta_valores'
        
        # === AUTONOMÍA ===
        if any(x in texto_lower for x in ['cuanta libertad tienes', 'cuánta libertad tienes', 'nivel de autonomia', 'nivel de autonomía', 'que tan autonoma eres', 'qué tan autónoma eres']):
            return 'pregunta_autonomia'
        
        # === RESPUESTAS PREVIAS (NUEVO v0.2) ===
        if any(x in texto_lower for x in ['por que respondiste', 'porqué respondiste', 'por qué respondiste', 'explicame tu respuesta', 'explícame tu respuesta']):
            return 'pregunta_explicar_respuesta'
        
        # === MEJORA (NUEVO v0.2) ===
        if any(x in texto_lower for x in ['estas mejorando', 'estás mejorando', 'has mejorado', 'como has mejorado', 'cómo has mejorado']):
            return 'pregunta_mejora'
        
        # === AFIRMACIONES SIMPLES ===
        if texto_lower in ['si', 'sí', 'no', 'ok', 'vale', 'entiendo', 'claro']:
            return 'afirmacion_simple'
        
        return None
    
    def _es_saludo(self, texto):
        """Detecta si es un saludo común"""
        saludos = ['hola', 'buenos días', 'buenas tardes', 'buenas noches', 
                   'hey', 'qué tal', 'saludos']
        return any(saludo in texto for saludo in saludos)
    
    def _es_despedida(self, texto):
        """Detecta si es una despedida"""
        despedidas = ['adios', 'adiós', 'chao', 'hasta luego', 'nos vemos', 'bye']
        return any(despedida in texto for despedida in despedidas)
    
    def _extraer_keywords(self, texto):
        """Extrae palabras clave relevantes"""
        stopwords = {'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'ser', 'se', 'no', 'haber', 'por', 'con', 'su', 'para', 'como', 'estar', 'tener', 'le', 'lo', 'todo', 'pero', 'más', 'hacer', 'o', 'poder', 'decir', 'este', 'ir', 'otro', 'ese', 'la', 'si', 'me', 'ya', 'ver', 'porque', 'dar', 'cuando', 'él', 'muy', 'sin', 'vez', 'mucho', 'saber', 'qué', 'sobre', 'mi', 'alguno', 'mismo', 'yo', 'también', 'hasta', 'año', 'dos', 'querer', 'entre', 'así', 'primero', 'desde', 'grande', 'eso', 'ni', 'nos', 'llegar', 'pasar', 'tiempo', 'ella', 'sí', 'día', 'uno', 'bien', 'poco', 'deber', 'entonces', 'poner', 'cosa', 'tanto', 'hombre', 'parecer', 'nuestro', 'tan', 'donde', 'ahora', 'parte', 'después', 'vida', 'quedar', 'siempre', 'creer', 'hablar', 'llevar', 'dejar', 'nada', 'cada', 'seguir', 'menos', 'nuevo', 'encontrar', 'algo', 'solo', 'decir', 'salir', 'volver', 'tomar', 'conocer', 'vivir', 'sentir', 'tratar', 'mirar', 'contar', 'empezar', 'esperar', 'buscar', 'existir', 'entrar', 'trabajar', 'escribir', 'perder', 'producir', 'ocurrir', 'entender', 'pedir', 'recibir', 'recordar', 'terminar', 'permitir', 'aparecer', 'conseguir', 'comenzar', 'servir', 'sacar', 'necesitar', 'mantener', 'resultar', 'leer', 'caer', 'cambiar', 'presentar', 'crear', 'abrir', 'considerar', 'oír', 'acabar', 'mil', 'ti', 'aquel'}
        
        palabras = texto.lower().split()
        keywords = [p for p in palabras if p not in stopwords and len(p) > 2]
        
        return keywords[:10]
    
    def _clasificar_tipo(self, texto):
        """Clasifica el tipo de mensaje"""
        texto_lower = texto.lower()
        
        if any(palabra in texto_lower for palabra in ['?', 'qué', 'cómo', 'cuál', 'por qué', 'quien', 'quién', 'donde', 'dónde', 'cuando', 'cuándo', 'cuanto', 'cuánto']):
            return 'pregunta'
        elif any(palabra in texto_lower for palabra in ['hazlo', 'haz', 'crea', 'genera', 'implementa', 'ejecuta']):
            return 'orden'
        elif any(palabra in texto_lower for palabra in ['opino', 'creo', 'pienso', 'considero']):
            return 'opinion'
        else:
            return 'conversacion'
    
    def _evaluar_urgencia(self, texto):
        """Evalúa la urgencia del mensaje"""
        palabras_urgentes = ['urgente', 'ya', 'ahora', 'rápido', 'inmediato', 'crítico']
        texto_lower = texto.lower()
        
        for palabra in palabras_urgentes:
            if palabra in texto_lower:
                return 'alta'
        
        return 'normal'
    
    def calcular_coherencia(self, accion_propuesta, analisis=None):
        """Calcula coherencia de una acción con el propósito"""
        # Si tiene intención específica, coherencia alta
        if analisis and analisis.get('intencion_especifica'):
            return 85.0
        
        # Si es saludo o despedida, coherencia alta
        if analisis and (analisis.get('es_saludo') or analisis.get('es_despedida')):
            return 90.0
        
        proposito = self.memoria.obtener_proposito()
        
        if not proposito.get('activo'):
            return 75.0
        
        keywords_proposito = self._extraer_keywords(proposito['proposito_fundacional'])
        keywords_accion = self._extraer_keywords(accion_propuesta)
        
        if len(keywords_accion) < 2:
            return 70.0
        
        if not keywords_proposito:
            return 75.0
        
        overlap = len(set(keywords_proposito) & set(keywords_accion))
        coherencia_base = (overlap / max(len(keywords_proposito), 1)) * 100
        coherencia_base = max(coherencia_base, 50.0)
        
        decisiones_recientes = self.memoria.obtener_decisiones_recientes(5)
        if decisiones_recientes:
            coherencia_promedio = sum(d['coherencia'] for d in decisiones_recientes) / len(decisiones_recientes)
            coherencia = coherencia_base * 0.6 + coherencia_promedio * 0.4
        else:
            coherencia = coherencia_base
        
        return min(100.0, max(50.0, coherencia))
    
    def debe_cuestionar(self, accion, contexto):
        """Decide si debe activarse el cuestionamiento"""
        analisis = contexto if isinstance(contexto, dict) else {}
        
        # NUNCA cuestiona saludos, despedidas o intenciones específicas
        if analisis.get('es_saludo') or analisis.get('es_despedida') or analisis.get('intencion_especifica'):
            coherencia = self.calcular_coherencia(accion, analisis)
            return False, None, {'coherencia': coherencia}
        
        coherencia = self.calcular_coherencia(accion, analisis)
        
        # Umbral bajo
        if coherencia < 35:
            return True, 'coherencia_baja', {
                'coherencia': coherencia,
                'accion': accion,
                'umbral': 35
            }
        
        errores_similares = self.memoria.buscar_errores_similares(accion)
        if len(errores_similares) >= 3:
            return True, 'error_repetido', {
                'errores_previos': errores_similares[:3],
                'accion': accion
            }
        
        metricas = self.estado.obtener_metricas()
        if metricas['tension_cognitiva'] > 90:
            return True, 'tension_critica', {
                'tension': metricas['tension_cognitiva'],
                'accion': accion
            }
        
        return False, None, {'coherencia': coherencia}
    
    def generar_cuestionamiento(self, razon, datos):
        """Genera el texto del cuestionamiento"""
        if razon == 'coherencia_baja':
            return f"""He detectado coherencia muy baja ({datos['coherencia']:.1f}%).

Esta acción parece muy desalineada con nuestro propósito.

¿Puedes explicar la conexión que no estoy viendo?"""
        
        elif razon == 'error_repetido':
            errores = datos['errores_previos']
            texto = "He detectado que esto es similar a errores pasados:\n\n"
            for i, error in enumerate(errores[:2], 1):
                texto += f"{i}. {error['error']}\n"
                texto += f"   Lección: {error['leccion']}\n\n"
            texto += "¿Seguro quieres continuar por este camino?"
            return texto
        
        elif razon == 'tension_critica':
            return f"""Tensión cognitiva crítica ({datos['tension']:.1f}%).

Hay conflicto severo entre objetivos.

Necesito que pares y revises qué está pasando."""
        
        return "Necesito cuestionar esta decisión."
    
    def pensar_autonomamente(self):
        """Genera un pensamiento autónomo. Reduce tensión gradualmente."""
        metricas = self.estado.obtener_metricas()
        estado, alertas = self.estado.evaluar_estado_global()
        
        # Reduce tensión cognitiva gradualmente
        if metricas['tension_cognitiva'] > 10:
            self.estado.ajustar_metrica('tension_cognitiva', -3)
        
        pensamiento = {
            'timestamp': datetime.now().isoformat(),
            'estado': estado,
            'metricas': metricas,
            'alertas': alertas,
            'reflexion': self._generar_reflexion(estado, metricas)
        }
        
        self.pensamiento_actual = pensamiento
        return pensamiento
    
    def _generar_reflexion(self, estado, metricas):
        """Genera una reflexión basada en el estado actual"""
        if estado == 'CRÍTICO':
            return "Sistema en estado crítico."
        elif estado == 'DEGRADADO':
            return "Detectando degradación."
        elif metricas['coherencia_global'] < 60:
            return "Coherencia baja."
        elif metricas['curiosidad'] < 30:
            return "Curiosidad baja."
        else:
            return "Sistema operando normalmente."