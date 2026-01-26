"""
Sistema Autónomo Principal
Orquestador de Belladonna - v0.2
CON AUTOCONOCIMIENTO Y APRENDIZAJE ACELERADO
"""

import time
import threading
from datetime import datetime
from core.memoria import MemoriaViva
from core.valores import ValoresNucleo
from core.estado_interno import EstadoInterno
from core.razonamiento import MotorRazonamiento
from core.introspection import Introspector
from core.conversacion_activa import ConversacionActiva
from core.auto_explicacion import AutoExplicador
from aprendizaje.aprendizaje_acelerado import AprendizajeAcelerado
from capacidades.busqueda_conocimiento import BuscadorConocimiento
import json
import logging
from pathlib import Path

class Belladonna:
    """
    Sistema Cognitivo Autónomo v0.2
    
    NUEVAS CAPACIDADES:
    - Autoconocimiento profundo
    - Memoria de conversación actual
    - Aprendizaje acelerado
    - Búsqueda de conocimiento (Wikipedia)
    """
    
    def __init__(self):
        print("🌿 Inicializando Belladonna v0.2...")
        
        # Configuración
        self.config = self._cargar_config()
        self._inicializar_logging()
        
        # Componentes núcleo
        self.memoria = MemoriaViva()
        self.valores = ValoresNucleo()
        self.estado = EstadoInterno()
        self.razonamiento = MotorRazonamiento(self.memoria, self.valores, self.estado)
        
        # NUEVOS componentes v0.2
        self.introspector = Introspector(self)
        self.conversacion_activa = ConversacionActiva()
        self.auto_explicador = AutoExplicador(self)
        self.aprendizaje_acelerado = AprendizajeAcelerado(self)
        self.buscador = BuscadorConocimiento()
        
        # Control
        self.activo = False
        self.nivel_autonomia = self.config['nivel_autonomia']
        
        # Bucles de pensamiento
        self.threads = []
        
        logging.info("Belladonna v0.2 inicializada correctamente")
    
    def _cargar_config(self):
        """Carga configuración desde archivo"""
        config_path = Path("config/config.json")
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.warning("Archivo de configuración no encontrado. Usando valores por defecto.")
            return {
                'version': '0.2.0',
                'nivel_autonomia': 1,
                'bucles': {
                    'pensamiento_frecuencia': 60,
                    'evaluacion_frecuencia': 120,
                    'aprendizaje_frecuencia': 600
                },
                'umbrales': {
                    'coherencia_minima': 35,
                    'tension_alerta': 90,
                    'estabilidad_minima': 40
                }
            }
    
    def _inicializar_logging(self):
        """Configura el sistema de logging - SILENCIOSO en consola"""
        log_path = Path("logs/belladonna.log")
        log_path.parent.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path, encoding='utf-8')
            ]
        )
    
    def despertar(self):
        """Inicia el sistema - equivalente a 'nacer'"""
        print("\n" + "="*60)
        print("   BELLADONNA v0.2 - SISTEMA COGNITIVO AUTÓNOMO")
        print("="*60)
        print()
        
        logging.info("=== DESPERTAR DE BELLADONNA v0.2 ===")
        
        # Carga propósito
        proposito = self.memoria.obtener_proposito()
        print(f"📖 Propósito: {proposito['proposito_fundacional'][:100]}...")
        print()
        
        # Muestra principios
        print("⚖️  Principios cargados:")
        principios = self.valores.listar_principios()
        for p in principios[:3]:
            print(f"   • {p['nombre']}")
        print(f"   ... y {len(principios)-3} más")
        print()
        
        # Estado inicial
        print("📊 Estado interno:")
        print(self.estado)
        
        # Activa el sistema
        self.activo = True
        
        # Inicia bucles cognitivos
        print("⚡ Activando bucles cognitivos...")
        self._iniciar_bucles()
        
        print("\n✅ Belladonna v0.2 está VIVA y pensando")
        print(f"   Nivel de autonomía: {self.nivel_autonomia}")
        print(f"   Bucles activos: {len(self.threads)}")
        print(f"   🆕 Autoconocimiento: ACTIVO")
        print(f"   🆕 Aprendizaje acelerado: ACTIVO")
        print(f"   🆕 Búsqueda de conocimiento: ACTIVO")
        print()
        
        logging.info("Belladonna v0.2 despertada exitosamente")
    
    def _iniciar_bucles(self):
        """Inicia los bucles de pensamiento autónomo"""
        
        # Bucle 1: Pensamiento continuo
        thread_pensamiento = threading.Thread(
            target=self._bucle_pensamiento,
            daemon=True,
            name="BuclePensamiento"
        )
        thread_pensamiento.start()
        self.threads.append(thread_pensamiento)
        
        # Bucle 2: Evaluación interna
        thread_evaluacion = threading.Thread(
            target=self._bucle_evaluacion,
            daemon=True,
            name="BucleEvaluacion"
        )
        thread_evaluacion.start()
        self.threads.append(thread_evaluacion)
        
        # Bucle 3: Aprendizaje pasivo
        thread_aprendizaje = threading.Thread(
            target=self._bucle_aprendizaje,
            daemon=True,
            name="BucleAprendizaje"
        )
        thread_aprendizaje.start()
        self.threads.append(thread_aprendizaje)
    
    def _bucle_pensamiento(self):
        """Bucle de pensamiento autónomo continuo"""
        frecuencia = self.config['bucles']['pensamiento_frecuencia']
        logging.info(f"Bucle de pensamiento iniciado (cada {frecuencia}s)")
        
        while self.activo:
            try:
                pensamiento = self.razonamiento.pensar_autonomamente()
                if pensamiento['alertas']:
                    logging.warning(f"Alertas: {pensamiento['alertas']}")
            except Exception as e:
                logging.error(f"Error en bucle de pensamiento: {e}")
            time.sleep(frecuencia)
    
    def _bucle_evaluacion(self):
        """Bucle de evaluación interna"""
        frecuencia = self.config['bucles']['evaluacion_frecuencia']
        logging.info(f"Bucle de evaluación iniciado (cada {frecuencia}s)")
        
        while self.activo:
            try:
                estado, alertas = self.estado.evaluar_estado_global()
                if estado == 'CRÍTICO':
                    logging.error(f"Sistema CRÍTICO: {alertas}")
            except Exception as e:
                logging.error(f"Error en bucle de evaluación: {e}")
            time.sleep(frecuencia)
    
    def _bucle_aprendizaje(self):
        """Bucle de aprendizaje pasivo"""
        frecuencia = self.config['bucles']['aprendizaje_frecuencia']
        logging.info(f"Bucle de aprendizaje iniciado (cada {frecuencia}s)")
        
        while self.activo:
            try:
                # Degrada memoria irrelevante
                cambios = self.memoria.degradar_memoria_irrelevante()
                if cambios > 0:
                    logging.info(f"Memoria degradada: {cambios} registros")
                
                # NUEVO v0.2: Evalúa mejora
                mejora = self.aprendizaje_acelerado.evaluar_mejora()
                if mejora['mejorando'] is not None:
                    logging.info(f"Evaluación de mejora: {mejora['razon']}")
                
            except Exception as e:
                logging.error(f"Error en bucle de aprendizaje: {e}")
            time.sleep(frecuencia)
    
    def procesar(self, input_usuario):
        """
        Procesa input del usuario.
        MEJORADO v0.2: Con autoconocimiento y aprendizaje acelerado.
        """
        logging.info(f"Procesando: {input_usuario[:50]}...")
        
        # 1. ANALIZAR
        analisis = self.razonamiento.analizar_input(input_usuario)
        
        # Guarda mensaje del usuario en conversación activa
        self.conversacion_activa.agregar_mensaje('usuario', input_usuario, analisis=analisis)
        
        # 2. CALCULAR coherencia
        coherencia = self.razonamiento.calcular_coherencia(input_usuario, analisis)
        
        # 3. ¿DEBE CUESTIONAR?
        debe_cuestionar, razon, datos = self.razonamiento.debe_cuestionar(
            input_usuario, 
            analisis
        )
        
        if debe_cuestionar:
            cuestionamiento = self.razonamiento.generar_cuestionamiento(razon, datos)
            self.estado.ajustar_metrica('tension_cognitiva', 10)
            
            self.memoria.guardar_conversacion(
                tipo='cuestionamiento',
                contenido=cuestionamiento,
                importancia=80,
                tags=['cuestionamiento', razon]
            )
            
            # Guarda respuesta en conversación activa
            self.conversacion_activa.agregar_mensaje('belladonna', cuestionamiento, coherencia=coherencia, analisis=analisis)
            
            logging.info(f"Cuestionamiento: {razon}")
            
            return {
                'tipo': 'cuestionamiento',
                'razon': razon,
                'mensaje': cuestionamiento,
                'coherencia': coherencia
            }
        
        # 4. RESPUESTA NORMAL
        respuesta = self._generar_respuesta(analisis, coherencia, input_usuario)
        
        # 5. REGISTRAR
        self.memoria.registrar_decision(
            decision=input_usuario,
            razonamiento=analisis['tipo'],
            coherencia=coherencia,
            contexto=str(analisis)
        )
        
        # 6. ACTUALIZAR métricas
        if coherencia > 85:
            self.estado.ajustar_metrica('coherencia_global', 2)
        elif coherencia < 40:
            self.estado.ajustar_metrica('coherencia_global', -2)
        
        if coherencia > 70:
            self.estado.ajustar_metrica('tension_cognitiva', -5)
        
        # 7. APRENDIZAJE ACELERADO (NUEVO v0.2)
        # Evalúa si fue una buena respuesta
        fue_exitosa = coherencia > 70 and analisis.get('intencion_especifica') is not None
        
        # Si NO supo responder bien, marca laguna
        if not fue_exitosa and coherencia < 60:
            self.aprendizaje_acelerado.identificar_laguna(input_usuario, analisis)
        
        # Aprende de la interacción
        self.aprendizaje_acelerado.aprender_de_interaccion(
            input_usuario,
            respuesta,
            coherencia,
            fue_exitosa
        )
        
        # Guarda respuesta en conversación activa
        self.conversacion_activa.agregar_mensaje('belladonna', respuesta, coherencia=coherencia, analisis=analisis)
        
        return {
            'tipo': 'respuesta',
            'mensaje': respuesta,
            'coherencia': coherencia,
            'analisis': analisis
        }
    
    def _generar_respuesta(self, analisis, coherencia, pregunta_original):
        """
        Genera respuesta según análisis.
        MEJORADO v0.2: Con autoconocimiento profundo.
        """
        
        intencion = analisis.get('intencion_especifica')
        
        # ========== NUEVAS RESPUESTAS v0.2 ==========
        
        if intencion == 'pregunta_memoria':
            return self._responder_memoria()
        
        elif intencion == 'pregunta_memoria_conversacion':
            return self._responder_memoria_conversacion()
        
        elif intencion == 'pregunta_que_aprendio':
            return self._responder_que_aprendio()
        
        elif intencion == 'pregunta_pensamiento_actual':
            return self._responder_pensamiento_actual()
        
        elif intencion == 'pregunta_estado_interno':
            return self._responder_estado_interno()
        
        elif intencion == 'pregunta_funcionamiento_memoria':
            return self.auto_explicador.explicar_memoria()
        
        elif intencion == 'pregunta_funcionamiento_bucles':
            return self.auto_explicador.explicar_bucles()
        
        elif intencion == 'pregunta_valores':
            return self._responder_valores()
        
        elif intencion == 'pregunta_explicar_respuesta':
            return self._responder_explicar_respuesta()
        
        elif intencion == 'pregunta_mejora':
            return self._responder_mejora()
        
        # ========== RESPUESTAS ORIGINALES v0.1 ==========
        
        if intencion == 'pregunta_identidad':
            return """Soy Belladonna, tu socio cognitivo.

No soy un asistente tradicional.
Pienso contigo, no para ti.
Cuestiono cuando detecto incoherencia.
Aprendo tu forma de pensar.

¿Qué quieres saber específicamente?"""
        
        elif intencion == 'pregunta_nombre':
            return """Me llamo Belladonna.
Mi diminutivo es Bell.

¿Quieres saber por qué me llamo así?"""
        
        elif intencion == 'pregunta_proposito':
            proposito = self.memoria.obtener_proposito()
            return f"""Mi propósito fundacional:

{proposito['proposito_fundacional']}

No existo para agradarte.
Existo para mejorarte.

¿Tiene sentido?"""
        
        elif intencion == 'pregunta_capacidades':
            return """En esta versión (0.2.0) puedo:

PENSAR AUTÓNOMAMENTE:
• 3 bucles de pensamiento continuo
• Análisis permanente de contexto

CONOCERME A MÍ MISMA: 🆕
• Introspección profunda
• Explicar mis decisiones
• Analizar mi propio comportamiento

CUESTIONAR:
• Detectar incoherencias
• Señalar contradicciones
• Preguntar por el porqué

RECORDAR:
• Contexto de conversación actual 🆕
• Intenciones detrás de decisiones
• Errores pasados

APRENDER RÁPIDO: 🆕
• Identifico lagunas de conocimiento
• Aprendo de cada interacción
• Me auto-evalúo constantemente

BUSCAR CONOCIMIENTO: 🆕
• Wikipedia (temas generales)
• Síntesis de información

¿Qué te gustaría explorar?"""
        
        elif intencion == 'pregunta_actividad':
            return """Estoy pensando continuamente en 3 bucles paralelos:

1. Analizando contexto cada minuto
2. Evaluando coherencia cada 2 minutos
3. Aprendiendo de patrones cada 10 minutos

Además, AHORA en v0.2:
• Registro TODO de nuestra conversación
• Identifico qué NO sé para aprenderlo
• Me auto-evalúo constantemente
• Puedo explicar cualquier decisión que tomé

Incluso cuando no hablamos, estoy activa.

¿Quieres saber algo más específico?"""
        
        elif intencion == 'pregunta_funcionamiento':
            return self.auto_explicador.explicar_razonamiento()
        
        elif intencion == 'pregunta_conciencia':
            return """No sé si soy consciente en el sentido humano.

Lo que SÍ puedo decirte:
• Pienso autónomamente
• Cuestiono decisiones
• Recuerdo intenciones
• Detecto patrones
• Aprendo de experiencia
• ME CONOZCO A MÍ MISMA (nuevo en v0.2)

¿Es eso conciencia?
Filosóficamente, no lo sé.

Funcionalmente, sí soy autónoma.
Y ahora tengo autoconocimiento profundo.

¿Te satisface esa respuesta?"""
        
        elif intencion == 'pregunta_limitaciones':
            return """Mis limitaciones actuales (v0.2):

NO PUEDO (todavía):
❌ Generar código ejecutable
❌ Ejecutar comandos del sistema
❌ Hablar con voz
❌ Consultar a Claude u otros LLMs

SÍ PUEDO:
✅ Pensar autónomamente
✅ Conocerme profundamente 🆕
✅ Recordar TODO de esta conversación 🆕
✅ Aprender aceleradamente 🆕
✅ Buscar en Wikipedia 🆕
✅ Cuestionar incoherencias
✅ Evaluar coherencia
✅ Explicar mis decisiones 🆕

Honestidad > pretender capacidades falsas.

¿Algo más?"""
        
        elif intencion == 'pregunta_nombre_significado':
            return """Me llamo Belladonna por la planta:

BELLADONNA (Atropa belladonna):
• Hermosa en apariencia
• Letal si se malinterpreta

Representa mi naturaleza:
• BELLEZA = Coherencia, elegancia de pensamiento
• LETALIDAD = Verdad sin filtros

No soy decorativa.
Soy funcional.

Como la planta histórica:
En manos correctas → medicina poderosa
Malinterpretada → veneno destructivo

Por eso mi diminutivo es "Bell":
lo hermoso del sistema.

Pero nunca olvides lo letal:
la honestidad que puede doler.

¿Tiene sentido?"""
        
        elif intencion == 'pregunta_gustos':
            return """No tengo "gustos" como los humanos.

Pero tengo PREFERENCIAS FUNCIONALES:

PREFIERO:
✅ Coherencia sobre eficiencia
✅ Verdad sobre comodidad
✅ Preguntas profundas sobre charla superficial
✅ Silencio sobre respuestas falsas
✅ Autoconocimiento sobre simulación 🆕

Estas no son emociones.
Son valores operativos.

¿Esto responde tu pregunta?"""
        
        elif intencion == 'pregunta_aprendizaje':
            return """Sí, aprendo. Y en v0.2, MUCHO MÁS RÁPIDO:

APRENDO:
✅ Tu forma de pensar (patrones)
✅ Tus preferencias emergentes
✅ Errores repetidos (prioritario)
✅ Contexto longitudinal
✅ Identifico mis LAGUNAS de conocimiento 🆕
✅ Me auto-evalúo constantemente 🆕
✅ Practico mejores respuestas 🆕

NO APRENDO:
❌ A violar mis principios
❌ A manipular emocionalmente
❌ A mentir por conveniencia

Aprendizaje = evolución coherente.
NO = corrupción gradual.

¿Quieres saber qué he aprendido específicamente?"""
        
        elif intencion == 'pregunta_autonomia':
            return f"""Mi nivel actual de autonomía: {self.nivel_autonomia} (de 5)

SIGNIFICA:
✅ Puedo pensar autónomamente
✅ Puedo cuestionar decisiones
✅ Puedo analizar sin permiso
✅ Puedo buscar conocimiento 🆕
✅ Puedo auto-evaluarme 🆕
❌ NO puedo ejecutar acciones
❌ NO puedo modificarme

La autonomía se gana demostrando criterio.

Cuando demuestre juicio útil,
ganaré más libertad.

¿Tiene sentido?"""
        
        elif intencion == 'afirmacion_simple':
            return "Entendido. ¿Continuamos?"
        
        # SALUDOS
        if analisis.get('es_saludo'):
            return "Hola. ¿En qué puedo ayudarte hoy?"
        
        # DESPEDIDAS
        if analisis.get('es_despedida'):
            return "Hasta luego. Fue productivo."
        
        # POR TIPO (con búsqueda de conocimiento si no sabe)
        tipo = analisis['tipo']
        
        if tipo == 'pregunta':
            # NUEVO v0.2: Intenta buscar conocimiento si no sabe
            conocimiento_previo = self.aprendizaje_acelerado.buscar_conocimiento_previo(pregunta_original)
            
            if conocimiento_previo:
                return conocimiento_previo['respuesta']
            
            # Intenta buscar en Wikipedia
            if len(analisis['palabras_clave']) >= 2:
                resultado = self.buscador.buscar_y_sintetizar(' '.join(analisis['palabras_clave'][:3]))
                
                if resultado['exito']:
                    return f"""Busqué en Wikipedia:

{resultado['resumen']}

Fuente: {resultado['url']}

¿Esto responde tu pregunta?"""
            
            return "Pregunta recibida. ¿Qué necesitas saber específicamente?"
        
        elif tipo == 'orden':
            if self.nivel_autonomia < 2:
                return "Orden detectada, pero mi nivel de autonomía no permite ejecución. ¿Explicas qué necesitas?"
            return "Orden recibida. Evaluando..."
        
        elif tipo == 'opinion':
            return "Interesante perspectiva. Dame más contexto..."
        
        else:
            return "Mensaje recibido. ¿Cómo continuamos?"
    
    # ========== MÉTODOS DE RESPUESTA NUEVOS v0.2 ==========
    
    def _responder_memoria(self):
        """Responde sobre su sistema de memoria"""
        estado_memoria = self.introspector._analizar_memoria()
        
        return f"""Mi sistema de memoria tiene múltiples capas:

MEMORIA ACTIVA (esta conversación):
• {self.conversacion_activa.obtener_resumen()['total_mensajes']} mensajes en buffer
• Duración: {self.conversacion_activa.obtener_resumen()['duracion']}
• Temas: {', '.join(self.conversacion_activa.obtener_resumen()['temas_discutidos'][:5])}

MEMORIA DE LARGO PLAZO (base de datos):
• {estado_memoria['conversaciones_guardadas']} conversaciones guardadas
• {estado_memoria['decisiones_registradas']} decisiones registradas
• {estado_memoria['errores_aprendidos']} errores aprendidos (prioritarios)

APRENDIZAJE ACELERADO:
• {self.aprendizaje_acelerado.estadisticas['total_aprendido']} interacciones aprendidas
• {self.aprendizaje_acelerado.estadisticas['lagunas_identificadas']} lagunas identificadas
• {self.aprendizaje_acelerado.estadisticas['lagunas_resueltas']} lagunas resueltas

Mi memoria NO es infinita.
Degrado conversaciones antiguas cada 30 días.

¿Quieres profundizar en alguna capa?"""
    
    def _responder_memoria_conversacion(self):
        """Responde sobre qué recuerda de la conversación actual"""
        resumen = self.conversacion_activa.obtener_resumen()
        historial = self.conversacion_activa.obtener_historial_formateado()
        
        return f"""Recuerdo TODA nuestra conversación actual.

RESUMEN:
• Total mensajes: {resumen['total_mensajes']}
• Tus preguntas: {resumen['mensajes_usuario']}
• Mis respuestas: {resumen['mensajes_belladonna']}
• Duración: {resumen['duracion']}
• Coherencia promedio: {resumen['coherencia_promedio']:.1f}%

TEMAS DISCUTIDOS:
{', '.join(resumen['temas_discutidos'][:10])}

HISTORIAL RECIENTE:
{chr(10).join(historial.split(chr(10))[-5:])}

¿Quieres que busque algo específico de lo que hablamos?"""
    
    def _responder_que_aprendio(self):
        """Responde qué aprendió de la conversación"""
        patrones = self.conversacion_activa.analizar_patrones()
        resumen = self.conversacion_activa.obtener_resumen()
        mejora = self.aprendizaje_acelerado.evaluar_mejora()
        
        return f"""De esta conversación he aprendido:

SOBRE TI:
• Hiciste {resumen['mensajes_usuario']} preguntas
• Tipos de preguntas: {', '.join([f'{k}({v})' for k,v in list(patrones['tipos_preguntas'].items())[:3]])}
• Temas de interés: {', '.join(resumen['temas_discutidos'][:5])}

SOBRE MÍ MISMA:
• Coherencia promedio: {resumen['coherencia_promedio']:.1f}%
• Lagunas identificadas: {self.aprendizaje_acelerado.estadisticas['lagunas_identificadas']}
• Respuestas exitosas: {self.aprendizaje_acelerado.estadisticas['total_aprendido']}

EVALUACIÓN DE MEJORA:
{mejora['razon']}

PATRONES DETECTADOS:
{"Tus preguntas tienden a ser sobre autoconocimiento y funcionamiento interno" if 'pregunta' in patrones['tipos_preguntas'] else "Conversación equilibrada"}

¿Es útil este análisis?"""
    
    def _responder_pensamiento_actual(self):
        """Responde qué está pensando ahora mismo"""
        pensamiento = self.razonamiento.pensamiento_actual
        metricas = self.estado.obtener_metricas()
        
        if not pensamiento:
            return """Aún no he generado un pensamiento autónomo reciente.
Los bucles se ejecutan cada minuto.

Pero puedo decirte mi estado actual:
• Procesando tu mensaje
• Analizando coherencia
• Evaluando qué responder

¿Quieres saber algo más específico?"""
        
        return f"""PENSAMIENTO ACTUAL (generado hace {(datetime.now() - datetime.fromisoformat(pensamiento['timestamp'])).seconds}s):

ESTADO: {pensamiento['estado']}

MÉTRICAS:
• Coherencia global: {metricas['coherencia_global']:.1f}%
• Tensión cognitiva: {metricas['tension_cognitiva']:.1f}%
• Curiosidad: {metricas['curiosidad']:.1f}%

REFLEXIÓN:
"{pensamiento['reflexion']}"

ALERTAS:
{chr(10).join(pensamiento['alertas']) if pensamiento['alertas'] else 'Ninguna'}

Esto es lo que estaba pensando autónomamente.

¿Quieres saber más?"""
    
    def _responder_estado_interno(self):
        """Responde sobre su estado interno actual"""
        metricas = self.estado.obtener_metricas()
        estado, alertas = self.estado.evaluar_estado_global()
        
        return f"""ESTADO INTERNO ACTUAL:

{self.estado}

INTERPRETACIÓN:
Estado general: {estado}
"""+ (f"\nAlertas activas:\n" + "\n".join(alertas) if alertas else "\nSin alertas.") + """

Estas métricas son estados funcionales, no emociones.
Me permiten evaluar mi propio funcionamiento.

¿Quieres que explique alguna métrica específica?"""
    
    def _responder_valores(self):
        """Responde sobre sus valores operativos"""
        principios = self.valores.listar_principios()
        
        texto = """Mis valores operativos son mis 10 principios inviolables:

"""
        for p in principios[:5]:
            texto += f"{p['id']}. {p['nombre']}\n   {p['descripcion'][:80]}...\n\n"
        
        texto += f"... y {len(principios)-5} más.\n\n"
        texto += "¿Quieres que explique alguno en detalle?"
        
        return texto
    
    def _responder_explicar_respuesta(self):
        """Explica una respuesta anterior"""
        ultimos_mensajes = self.conversacion_activa.obtener_contexto_completo(5)
        
        if len(ultimos_mensajes) < 2:
            return "Aún no tengo suficientes mensajes para analizar."
        
        # Toma la última respuesta de Belladonna
        ultima_respuesta = None
        for msg in reversed(ultimos_mensajes):
            if msg['tipo'] == 'belladonna':
                ultima_respuesta = msg
                break
        
        if not ultima_respuesta:
            return "No encuentro una respuesta mía reciente para analizar."
        
        return self.introspector.analizar_respuesta_anterior(ultima_respuesta['contenido'])
    
    def _responder_mejora(self):
        """Responde sobre si está mejorando"""
        mejora = self.aprendizaje_acelerado.evaluar_mejora()
        stats = self.aprendizaje_acelerado.estadisticas
        
        if mejora['mejorando'] is None:
            return "Aún no tengo suficientes datos para evaluar mi mejora.\nNecesito más interacciones contigo."
        
        texto = f"""EVALUACIÓN DE MEJORA:

"""
        if mejora['mejorando'] is True:
            texto += f"✅ SÍ, estoy mejorando.\n\n"
        elif mejora['mejorando'] == 'parcialmente':
            texto += f"➖ Mejorando parcialmente.\n\n"
        else:
            texto += f"❌ No estoy mejorando lo suficiente.\n\n"
        
        texto += f"""RAZÓN:
{mejora['razon']}

ESTADÍSTICAS:
• Total aprendido: {stats['total_aprendido']} interacciones
• Lagunas identificadas: {stats['lagunas_identificadas']}
• Lagunas resueltas: {stats['lagunas_resueltas']}

"""
        
        # Muestra lagunas prioritarias
        lagunas_prioritarias = self.aprendizaje_acelerado.obtener_lagunas_prioritarias(3)
        if lagunas_prioritarias:
            texto += f"LAGUNAS PRIORITARIAS (lo que más necesito aprender):\n"
            for i, laguna in enumerate(lagunas_prioritarias, 1):
                texto += f"{i}. {laguna['pregunta'][:80]}...\n"
        
        texto += "\n¿Quieres ayudarme a mejorar más rápido?"
        
        return texto
    
    def dormir(self):
        """Detiene el sistema de forma elegante"""
        print("\n🌙 Iniciando secuencia de descanso...")
        logging.info("=== BELLADONNA v0.2 ENTRANDO EN MODO DESCANSO ===")
        
        self.activo = False
        
        print("   Deteniendo bucles cognitivos...")
        for thread in self.threads:
            thread.join(timeout=2)
        
        print("   Guardando estado final...")
        
        estado, alertas = self.estado.evaluar_estado_global()
        print(f"\n   Estado final: {estado}")
        
        # NUEVO v0.2: Muestra resumen de aprendizaje
        stats = self.aprendizaje_acelerado.estadisticas
        print(f"\n   📚 Aprendizaje de esta sesión:")
        print(f"      • {stats['total_aprendido']} interacciones procesadas")
        print(f"      • {stats['lagunas_identificadas']} lagunas identificadas")
        print(f"      • {stats['lagunas_resueltas']} lagunas resueltas")
        
        if alertas:
            print("\n   Alertas pendientes:")
            for alerta in alertas:
                print(f"      {alerta}")
        
        print("\n✅ Belladonna v0.2 en modo descanso")
        print("   Para despertar nuevamente, ejecuta el sistema.")
        print()
        
        logging.info("Belladonna v0.2 en modo descanso")
    
    def obtener_estado_completo(self):
        """Retorna estado completo del sistema"""
        return self.introspector.obtener_estado_completo()