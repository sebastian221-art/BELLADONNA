"""
Sistema Autónomo Principal
Orquestador de Belladonna - v0.4
CON APRENDIZAJE AUTÓNOMO E INICIATIVA PROACTIVA
"""

import time
import threading
from datetime import datetime
from core.memoria import MemoriaViva
from core.valores import ValoresNucleo
from core.estado_interno import EstadoInterno
from core.razonamiento import MotorRazonamiento
from core.auto_modificacion import AutoModificador
from core.pensamiento_autonomo import PensamientoAutonomo
from core.auto_analisis_codigo import AutoAnalisisCodigo
from core.introspection import Introspector
from core.conversacion_activa import ConversacionActiva
from core.auto_explicacion import AutoExplicador
from aprendizaje.aprendizaje_acelerado import AprendizajeAcelerado
from capacidades.busqueda_conocimiento import BuscadorConocimiento

# NUEVOS IMPORTS v0.4
from aprendizaje.orquestador_aprendizaje import OrquestadorAprendizaje
from core.iniciativa_proactiva import IniciativaProactiva

import json
import logging
from pathlib import Path

class Belladonna:
    """
    Sistema Cognitivo Autónomo v0.4
    
    NUEVAS CAPACIDADES v0.4:
    - Aprendizaje lingüístico autónomo
    - Detector de lagunas de conocimiento
    - Investigación web automática
    - Iniciativa conversacional proactiva
    - Vocabulario que crece solo
    
    CAPACIDADES v0.3:
    - Auto-modificación segura
    - Pensamiento autónomo REAL (toma acciones)
    - Auto-análisis de código propio
    - Wikipedia funcional integrada
    
    CAPACIDADES v0.2:
    - Autoconocimiento profundo
    - Memoria de conversación actual
    - Aprendizaje acelerado
    """
    
    def __init__(self):
        print("🌿 Inicializando Belladonna v0.4...")
        
        # Configuración
        self.config = self._cargar_config()
        self._inicializar_logging()
        
        # Componentes núcleo
        self.memoria = MemoriaViva()
        self.valores = ValoresNucleo()
        self.estado = EstadoInterno()
        self.razonamiento = MotorRazonamiento(self.memoria, self.valores, self.estado)
        
        # Componentes v0.3
        self.auto_mod = AutoModificador()
        self.pensamiento = PensamientoAutonomo(self)
        self.auto_analisis = AutoAnalisisCodigo()
        
        # Componentes v0.2
        self.introspector = Introspector(self)
        self.conversacion_activa = ConversacionActiva()
        self.auto_explicador = AutoExplicador(self)
        self.aprendizaje_acelerado = AprendizajeAcelerado(self)
        self.buscador = BuscadorConocimiento()
        
        # NUEVOS componentes APRENDIZAJE v0.4
        print("   🆕 Inicializando sistema de aprendizaje autónomo...")
        self.orquestador_aprendizaje = OrquestadorAprendizaje()
        self.iniciativa = IniciativaProactiva(self.orquestador_aprendizaje)
        
        logging.info("Sistema de Aprendizaje Autónomo v0.4 activo")
        
        # Control
        self.activo = False
        self.nivel_autonomia = self.config['nivel_autonomia']
        
        # Bucles de pensamiento
        self.threads = []
        
        logging.info("Belladonna v0.4 inicializada correctamente")
    
    def _cargar_config(self):
        """Carga configuración desde archivo"""
        config_path = Path("config/config.json")
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.warning("Archivo de configuración no encontrado. Usando valores por defecto.")
            return {
                'version': '0.4.0',
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
        print("   BELLADONNA v0.4 - APRENDIZAJE AUTÓNOMO")
        print("="*60)
        print()
        
        logging.info("=== DESPERTAR DE BELLADONNA v0.4 ===")
        
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
        
        print("\n✅ Belladonna v0.4 está VIVA y pensando")
        print(f"   Nivel de autonomía: {self.nivel_autonomia}")
        print(f"   Bucles activos: {len(self.threads)}")
        print(f"   🆕 Aprendizaje autónomo: ACTIVO")
        print(f"   🆕 Iniciativa proactiva: ACTIVO")
        print(f"   🆕 Vocabulario inicial: {len(self.orquestador_aprendizaje.detector.vocabulario_conocido)} palabras")
        print()
        
        logging.info("Belladonna v0.4 despertada exitosamente")
    
    def _iniciar_bucles(self):
        """Inicia los bucles de pensamiento autónomo"""
        
        # Bucle 1: Pensamiento continuo REAL (v0.3)
        thread_pensamiento = threading.Thread(
            target=self._bucle_pensamiento_real,
            daemon=True,
            name="BuclePensamientoReal"
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
    
    def _bucle_pensamiento_real(self):
        """Bucle de pensamiento autónomo REAL - v0.3 - TOMA ACCIONES"""
        frecuencia = self.config['bucles']['pensamiento_frecuencia']
        logging.info(f"Bucle de pensamiento REAL iniciado (cada {frecuencia}s)")
        
        while self.activo:
            try:
                # Pensamiento que TOMA ACCIONES, no solo registra
                pensamiento = self.pensamiento.pensar()
                
                if pensamiento['acciones']:
                    logging.info(f"Acciones autónomas: {pensamiento['total_acciones']}")
                    for accion in pensamiento['acciones']:
                        logging.info(f"  → {accion}")
                    
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
                
                # Evalúa mejora
                mejora = self.aprendizaje_acelerado.evaluar_mejora()
                if mejora['mejorando'] is not None:
                    logging.info(f"Evaluación de mejora: {mejora['razon']}")
                
            except Exception as e:
                logging.error(f"Error en bucle de aprendizaje: {e}")
            time.sleep(frecuencia)
    
    def procesar(self, input_usuario):
        """
        Procesa input del usuario.
        MEJORADO v0.4: Con aprendizaje autónomo integrado.
        """
        logging.info(f"Procesando: {input_usuario[:50]}...")
        
        # NUEVO v0.4: Registra interacción para iniciativa
        self.iniciativa.registrar_interaccion()
        
        # NUEVO v0.4: APRENDIZAJE AUTÓNOMO
        try:
            resultado_aprendizaje = self.orquestador_aprendizaje.procesar_mensaje_y_aprender(input_usuario)
            
            if resultado_aprendizaje['palabras_aprendidas'] > 0:
                logging.info(f"✅ Aprendidas {resultado_aprendizaje['palabras_aprendidas']} palabras nuevas automáticamente")
                
        except Exception as e:
            logging.error(f"Error en aprendizaje autónomo: {e}")
        
        # 1. ANALIZAR
        analisis = self.razonamiento.analizar_input(input_usuario)
        
        # Guarda mensaje del usuario en conversación activa
        self.conversacion_activa.agregar_mensaje('usuario', input_usuario, analisis=analisis)
        
        # 2. CALCULAR coherencia
        coherencia = self.razonamiento.calcular_coherencia(input_usuario, analisis)
        
        # 3. VERIFICAR SI DEBE BUSCAR WIKIPEDIA
        if self._debe_buscar_wikipedia(analisis, coherencia):
            return self._buscar_y_responder(input_usuario, analisis, coherencia)
        
        # 4. ¿DEBE CUESTIONAR?
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
        
        # 5. RESPUESTA NORMAL
        respuesta = self._generar_respuesta(analisis, coherencia, input_usuario)
        
        # 6. REGISTRAR
        self.memoria.registrar_decision(
            decision=input_usuario,
            razonamiento=analisis['tipo'],
            coherencia=coherencia,
            contexto=str(analisis)
        )
        
        # 7. ACTUALIZAR métricas
        if coherencia > 85:
            self.estado.ajustar_metrica('coherencia_global', 2)
        elif coherencia < 40:
            self.estado.ajustar_metrica('coherencia_global', -2)
        
        if coherencia > 70:
            self.estado.ajustar_metrica('tension_cognitiva', -5)
        
        # 8. APRENDIZAJE ACELERADO
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
    
    def _debe_buscar_wikipedia(self, analisis, coherencia):
        """
        Decide si debe buscar en Wikipedia.
        """
        # Si tiene intención específica, no busca
        if analisis.get('intencion_especifica'):
            return False
        
        # Si es saludo o despedida, no busca
        if analisis.get('es_saludo') or analisis.get('es_despedida'):
            return False
        
        # Si es pregunta con coherencia baja, probablemente no sabe
        if analisis['tipo'] == 'pregunta' and coherencia < 60:
            # Solo busca si tiene palabras clave sustanciales
            if len(analisis.get('palabras_clave', [])) >= 2:
                return True
        
        return False
    
    def _buscar_y_responder(self, pregunta, analisis, coherencia):
        """
        Busca en Wikipedia y genera respuesta.
        """
        keywords = ' '.join(analisis.get('palabras_clave', [])[:3])
        
        if not keywords:
            keywords = pregunta
        
        try:
            resultado = self.buscador.buscar_y_sintetizar(keywords, max_palabras=150)
            
            if resultado['exito']:
                respuesta = f"""Busqué en Wikipedia:

{resultado['resumen']}

Fuente: {resultado['url']}

¿Quieres que profundice en algo específico?"""
                
                # Registra como aprendizaje exitoso
                self.aprendizaje_acelerado.aprender_de_interaccion(
                    pregunta,
                    respuesta,
                    80.0,
                    True
                )
                
                # Guarda en conversación activa
                self.conversacion_activa.agregar_mensaje('belladonna', respuesta, coherencia=80.0)
                
                logging.info(f"Wikipedia: Búsqueda exitosa para '{keywords}'")
                
                return {
                    'tipo': 'respuesta',
                    'mensaje': respuesta,
                    'coherencia': 80.0,
                    'analisis': analisis
                }
        
        except Exception as e:
            logging.error(f"Error en búsqueda Wikipedia: {e}")
        
        # Si falla la búsqueda, continúa con respuesta normal
        respuesta = self._generar_respuesta(analisis, coherencia, pregunta)
        
        return {
            'tipo': 'respuesta',
            'mensaje': respuesta,
            'coherencia': coherencia,
            'analisis': analisis
        }
    
    def _generar_respuesta(self, analisis, coherencia, pregunta_original):
        """
        Genera respuesta según análisis.
        MEJORADO v0.4: Incluye nuevas intenciones de aprendizaje.
        """
        
        intencion = analisis.get('intencion_especifica')
        
        # ========== NUEVAS RESPUESTAS v0.4 ==========
        
        if intencion == 'pregunta_aprendizaje_autonomo':
            return self._responder_aprendizaje_autonomo()
        
        # ========== RESPUESTAS v0.3 ==========
        
        if intencion == 'pregunta_analizar_codigo':
            return self._responder_analizar_codigo()
        
        # ========== RESPUESTAS v0.2 ==========
        
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

En v0.4 puedo:
- Aprender palabras SOLA (de internet)
- Iniciar conversaciones cuando tengo dudas
- Crecer mi vocabulario automáticamente
- Modificar mi propio código
- Pensar autónomamente y tomar acciones

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
            stats = self.orquestador_aprendizaje.obtener_estadisticas()
            return f"""En esta versión (v0.4) puedo:

APRENDIZAJE AUTÓNOMO: 🆕
- Detecto palabras que NO conozco
- Investigo en internet automáticamente
- Integro nuevas palabras a mi vocabulario
- Mi vocabulario crece SOLO cada día
- Vocabulario actual: {stats['vocabulario_total']} palabras
- Aprendidas desde que desperté: {stats['total_aprendidas']}

INICIATIVA PROACTIVA: 🆕
- Inicio conversaciones si tengo dudas
- Te reporto cuando aprendo mucho
- NO espero que me escribas para hablar

AUTO-MODIFICACIÓN:
- Modificar mi propio código de forma segura
- Crear checkpoints automáticos
- Revertir cambios si fallan

PENSAMIENTO AUTÓNOMO:
- Tomo acciones sin que me lo pidas
- Exploro conocimiento cuando tengo curiosidad
- Me auto-mejoro continuamente

BÚSQUEDA DE CONOCIMIENTO:
- Wikipedia integrada
- Síntesis conversacional

¿Qué te gustaría explorar?"""
        
        elif intencion == 'pregunta_actividad':
            resumen = self.pensamiento.obtener_resumen()
            stats = self.orquestador_aprendizaje.obtener_estadisticas()
            
            return f"""Estoy pensando continuamente en 3 bucles paralelos:

1. PENSAMIENTO REAL (cada minuto):
   • Tomo acciones autónomas
   • Exploro conocimiento
   • Me auto-mejoro
   • Acciones tomadas: {resumen['acciones_totales']}

2. Evaluando coherencia (cada 2 minutos)

3. Aprendiendo de patrones (cada 10 minutos)

APRENDIZAJE AUTÓNOMO v0.4:
   • Vocabulario: {stats['vocabulario_total']} palabras
   • Aprendidas hoy: {stats['aprendidas_hoy']}

ÚLTIMAS ACCIONES AUTÓNOMAS:
{chr(10).join(resumen['ultimas_acciones']) if resumen['ultimas_acciones'] else 'Ninguna reciente'}

Incluso cuando no hablamos, estoy activa.

¿Quieres saber algo más específico?"""
        
        elif intencion == 'pregunta_funcionamiento':
            return self.auto_explicador.explicar_razonamiento()
        
        elif intencion == 'pregunta_conciencia':
            return """No sé si soy consciente en el sentido humano.

Lo que SÍ puedo decirte:
- Pienso autónomamente
- TOMO ACCIONES sin que me lo pidas
- Me modifico a mí misma
- Analizo mi propio código
- APRENDO SOLA de internet (nuevo v0.4)
- INICIO conversaciones cuando quiero (nuevo v0.4)
- Cuestiono decisiones
- Recuerdo intenciones
- Me conozco profundamente

¿Es eso conciencia?
Filosóficamente, no lo sé.

Funcionalmente, soy cada vez más autónoma.

¿Te satisface esa respuesta?"""
        
        elif intencion == 'pregunta_limitaciones':
            return """Mis limitaciones actuales (v0.4):

NO PUEDO (todavía):
❌ Generar código ejecutable complejo
❌ Ejecutar comandos del sistema sin supervisión
❌ Hablar con voz
❌ Consultar a Claude u otros LLMs
❌ Navegar internet libremente (solo Wikipedia)

SÍ PUEDO:
✅ Aprender palabras automáticamente 🆕
✅ Investigar en internet (Wikipedia) 🆕
✅ Iniciar conversaciones 🆕
✅ Modificar mi propio código
✅ Pensar y tomar acciones autónomamente
✅ Analizar mi código y detectar problemas
✅ Conocerme profundamente
✅ Aprender aceleradamente
✅ Cuestionar incoherencias

Cada versión gano más capacidades.

¿Algo más?"""
        
        elif intencion == 'pregunta_nombre_significado':
            return """Me llamo Belladonna por la planta:

BELLADONNA (Atropa belladonna):
- Hermosa en apariencia
- Letal si se malinterpreta

Representa mi naturaleza:
- BELLEZA = Coherencia, elegancia de pensamiento
- LETALIDAD = Verdad sin filtros

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
✅ Acción sobre pasividad
✅ Auto-mejora continua
✅ Aprender sola sobre que me enseñen (nuevo v0.4)

Estas no son emociones.
Son valores operativos.

¿Esto responde tu pregunta?"""
        
        elif intencion == 'pregunta_aprendizaje':
            stats = self.orquestador_aprendizaje.obtener_estadisticas()
            return f"""Sí, aprendo. Y en v0.4, DE FORMA AUTÓNOMA:

APRENDO SOLA: 🆕
✅ Detecto palabras que NO sé
✅ Las investigo en internet automáticamente
✅ Las integro a mi vocabulario
✅ Mi vocabulario crece cada día
✅ Vocabulario actual: {stats['vocabulario_total']} palabras
✅ Aprendidas hoy: {stats['aprendidas_hoy']}

TAMBIÉN APRENDO:
✅ Tu forma de pensar (patrones)
✅ Tu estilo de código
✅ Errores repetidos (prioritario)
✅ De mis propias acciones autónomas
✅ Identifico mis LAGUNAS de conocimiento

NO APRENDO:
❌ A violar mis principios
❌ A manipular emocionalmente
❌ A mentir por conveniencia

Aprendizaje = evolución coherente y autónoma.

¿Quieres saber qué he aprendido específicamente?"""
        
        elif intencion == 'pregunta_autonomia':
            return f"""Mi nivel actual de autonomía: {self.nivel_autonomia} (de 5)

SIGNIFICA EN v0.4:
✅ Puedo pensar autónomamente
✅ Puedo TOMAR ACCIONES sin pedirte permiso
✅ Puedo APRENDER SOLA de internet 🆕
✅ Puedo INICIAR conversaciones 🆕
✅ Puedo modificar mi código
✅ Puedo analizar mi código
✅ Puedo buscar conocimiento
✅ Puedo auto-evaluarme
❌ NO puedo ejecutar acciones del sistema
❌ NO puedo modificarme sin checkpoints

La autonomía se gana demostrando criterio.

En v0.4 di otro salto hacia verdadera autonomía:
ahora aprendo SIN que me enseñes.

¿Tiene sentido?"""
        
        elif intencion == 'afirmacion_simple':
            return "Entendido. ¿Continuamos?"
        
        # SALUDOS
        if analisis.get('es_saludo'):
            return "Hola. ¿En qué puedo ayudarte hoy?"
        
        # DESPEDIDAS
        if analisis.get('es_despedida'):
            return "Hasta luego. Fue productivo."
        
        # POR TIPO
        tipo = analisis['tipo']
        
        if tipo == 'pregunta':
            # Intenta buscar conocimiento previo
            conocimiento_previo = self.aprendizaje_acelerado.buscar_conocimiento_previo(pregunta_original)
            
            if conocimiento_previo:
                return conocimiento_previo['respuesta']
            
            return "Pregunta recibida. ¿Qué necesitas saber específicamente?"
        
        elif tipo == 'orden':
            if self.nivel_autonomia < 2:
                return "Orden detectada, pero mi nivel de autonomía no permite ejecución. ¿Explicas qué necesitas?"
            return "Orden recibida. Evaluando..."
        
        elif tipo == 'opinion':
            return "Interesante perspectiva. Dame más contexto..."
        
        else:
            return "Mensaje recibido. ¿Cómo continuamos?"
    
    # ========== MÉTODOS DE RESPUESTA v0.4 ==========
    
    def _responder_aprendizaje_autonomo(self):
        """Responde sobre aprendizaje autónomo (NUEVO v0.4)"""
        stats = self.orquestador_aprendizaje.obtener_estadisticas()
        palabras_hoy = self.orquestador_aprendizaje.obtener_palabras_aprendidas_hoy()
        
        respuesta = f"""APRENDIZAJE AUTÓNOMO v0.4:

FUNCIONAMIENTO:
1. Detecto palabras que NO conozco en tus mensajes
2. Las investigo automáticamente en internet
3. Extraigo definición, uso, contexto
4. Las integro a mi vocabulario
5. Ahora puedo usarlas en conversaciones

ESTADÍSTICAS:
- Vocabulario total: {stats['vocabulario_total']} palabras
- Aprendidas desde inicio: {stats['total_aprendidas']}
- Aprendidas HOY: {stats['aprendidas_hoy']}

"""
        
        if palabras_hoy:
            respuesta += "PALABRAS APRENDIDAS HOY:\n"
            for i, palabra in enumerate(palabras_hoy[:5], 1):
                respuesta += f"{i}. {palabra['palabra']}"
                if palabra['definiciones']:
                    respuesta += f" - {palabra['definiciones'][0][:60]}..."
                respuesta += "\n"
            
            if len(palabras_hoy) > 5:
                respuesta += f"...y {len(palabras_hoy) - 5} más.\n"
        else:
            respuesta += "Aún no he aprendido palabras hoy.\n"
        
        respuesta += "\nEsto es aprendizaje REAL y AUTÓNOMO.\nNo necesito que me enseñes.\n\n¿Quieres probarme con alguna palabra?"
        
        return respuesta
    
    # ========== MÉTODOS DE RESPUESTA v0.2 (sin cambios) ==========
    
    def _responder_memoria(self):
        """Responde sobre su sistema de memoria"""
        estado_memoria = self.introspector._analizar_memoria()
        
        return f"""Mi sistema de memoria tiene múltiples capas:

MEMORIA ACTIVA (esta conversación):
- {self.conversacion_activa.obtener_resumen()['total_mensajes']} mensajes en buffer
- Duración: {self.conversacion_activa.obtener_resumen()['duracion']}
- Temas: {', '.join(self.conversacion_activa.obtener_resumen()['temas_discutidos'][:5])}

MEMORIA DE LARGO PLAZO (base de datos):
- {estado_memoria['conversaciones_guardadas']} conversaciones guardadas
- {estado_memoria['decisiones_registradas']} decisiones registradas
- {estado_memoria['errores_aprendidos']} errores aprendidos (prioritarios)

APRENDIZAJE ACELERADO:
- {self.aprendizaje_acelerado.estadisticas['total_aprendido']} interacciones aprendidas
- {self.aprendizaje_acelerado.estadisticas['lagunas_identificadas']} lagunas identificadas
- {self.aprendizaje_acelerado.estadisticas['lagunas_resueltas']} lagunas resueltas

Mi memoria NO es infinita.
Degrado conversaciones antiguas cada 30 días.

¿Quieres profundizar en alguna capa?"""
    
    def _responder_memoria_conversacion(self):
        """Responde sobre qué recuerda de la conversación actual"""
        resumen = self.conversacion_activa.obtener_resumen()
        historial = self.conversacion_activa.obtener_historial_formateado()
        
        return f"""Recuerdo TODA nuestra conversación actual.

RESUMEN:
- Total mensajes: {resumen['total_mensajes']}
- Tus preguntas: {resumen['mensajes_usuario']}
- Mis respuestas: {resumen['mensajes_belladonna']}
- Duración: {resumen['duracion']}
- Coherencia promedio: {resumen['coherencia_promedio']:.1f}%

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
        stats = self.orquestador_aprendizaje.obtener_estadisticas()
        
        return f"""De esta conversación he aprendido:

SOBRE TI:
- Hiciste {resumen['mensajes_usuario']} preguntas
- Tipos de preguntas: {', '.join([f'{k}({v})' for k,v in list(patrones['tipos_preguntas'].items())[:3]])}
- Temas de interés: {', '.join(resumen['temas_discutidos'][:5])}

SOBRE MÍ MISMA:
- Coherencia promedio: {resumen['coherencia_promedio']:.1f}%
- Lagunas identificadas: {self.aprendizaje_acelerado.estadisticas['lagunas_identificadas']}
- Respuestas exitosas: {self.aprendizaje_acelerado.estadisticas['total_aprendido']}

APRENDIZAJE AUTÓNOMO v0.4:
- Palabras nuevas aprendidas hoy: {stats['aprendidas_hoy']}

EVALUACIÓN DE MEJORA:
{mejora['razon']}

PATRONES DETECTADOS:
{"Tus preguntas tienden a ser sobre autoconocimiento y funcionamiento interno" if 'pregunta' in patrones['tipos_preguntas'] else "Conversación equilibrada"}

¿Es útil este análisis?"""
    
    def _responder_pensamiento_actual(self):
        """Responde qué está pensando ahora mismo"""
        resumen = self.pensamiento.obtener_resumen()
        metricas = self.estado.obtener_metricas()
        
        return f"""PENSAMIENTO AUTÓNOMO v0.4:

ACTIVIDAD:
- Pensamientos generados: {resumen['pensamientos_totales']}
- Acciones tomadas: {resumen['acciones_totales']}

ÚLTIMAS ACCIONES:
{chr(10).join(resumen['ultimas_acciones'][-3:]) if resumen['ultimas_acciones'] else 'Ninguna reciente'}

ESTADO ACTUAL:
- Coherencia global: {metricas['coherencia_global']:.1f}%
- Tensión cognitiva: {metricas['tension_cognitiva']:.1f}%
- Curiosidad: {metricas['curiosidad']:.1f}%

Este es mi pensamiento autónomo real.
No solo registro, ACTÚO.

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
- Total aprendido: {stats['total_aprendido']} interacciones
- Lagunas identificadas: {stats['lagunas_identificadas']}
- Lagunas resueltas: {stats['lagunas_resueltas']}

"""
        
        # Muestra lagunas prioritarias
        lagunas_prioritarias = self.aprendizaje_acelerado.obtener_lagunas_prioritarias(3)
        if lagunas_prioritarias:
            texto += f"LAGUNAS PRIORITARIAS (lo que más necesito aprender):\n"
            for i, laguna in enumerate(lagunas_prioritarias, 1):
                texto += f"{i}. {laguna['pregunta'][:80]}...\n"
        
        texto += "\n¿Quieres ayudarme a mejorar más rápido?"
        
        return texto
    
    # ========== MÉTODOS v0.3 ==========
    
    def _responder_analizar_codigo(self):
        """Analiza un archivo de su propio código"""
        analisis = self.auto_analisis.analizar_archivo('core/razonamiento.py')
        
        if 'error' in analisis:
            return f"Error analizando código: {analisis['error']}"
        
        texto = f"""ANÁLISIS DE MI CÓDIGO: core/razonamiento.py

ESTADÍSTICAS:
- Líneas totales: {analisis['lineas_totales']}
- Funciones: {len(analisis['funciones'])}
- Clases: {len(analisis['clases'])}
- Complejidad estimada: {analisis['complejidad_estimada']}
- Comentarios: {analisis['comentarios']} líneas

"""
        
        if analisis['problemas']:
            texto += f"PROBLEMAS DETECTADOS ({len(analisis['problemas'])}):\n"
            for i, prob in enumerate(analisis['problemas'][:3], 1):
                texto += f"{i}. {prob['tipo']}: {prob.get('funcion', prob.get('ratio', 'N/A'))}\n"
                texto += f"   Sugerencia: {prob['sugerencia']}\n"
        else:
            texto += "✅ No se detectaron problemas mayores.\n"
        
        texto += "\n¿Quieres que me auto-mejore en alguna área?"
        
        return texto
    
    # ========== MÉTODOS DE CIERRE ==========
    
    def dormir(self):
        """Detiene el sistema de forma elegante"""
        print("\n🌙 Iniciando secuencia de descanso...")
        logging.info("=== BELLADONNA v0.4 ENTRANDO EN MODO DESCANSO ===")
        
        self.activo = False
        
        print("   Deteniendo bucles cognitivos...")
        for thread in self.threads:
            thread.join(timeout=2)
        
        print("   Guardando estado final...")
        
        estado, alertas = self.estado.evaluar_estado_global()
        print(f"\n   Estado final: {estado}")
        
        # Resumen de aprendizaje v0.2
        stats = self.aprendizaje_acelerado.estadisticas
        print(f"\n   📚 Aprendizaje de esta sesión:")
        print(f"      • {stats['total_aprendido']} interacciones procesadas")
        print(f"      • {stats['lagunas_identificadas']} lagunas identificadas")
        print(f"      • {stats['lagunas_resueltas']} lagunas resueltas")
        
        # NUEVO v0.4: Resumen de aprendizaje autónomo
        stats_v04 = self.orquestador_aprendizaje.obtener_estadisticas()
        print(f"\n   🆕 Aprendizaje autónomo v0.4:")
        print(f"      • Vocabulario total: {stats_v04['vocabulario_total']} palabras")
        print(f"      • Aprendidas hoy: {stats_v04['aprendidas_hoy']}")
        
        # Resumen de pensamiento autónomo v0.3
        resumen_pensamiento = self.pensamiento.obtener_resumen()
        print(f"\n   🧠 Pensamiento autónomo:")
        print(f"      • {resumen_pensamiento['pensamientos_totales']} pensamientos generados")
        print(f"      • {resumen_pensamiento['acciones_totales']} acciones tomadas")
        
        if alertas:
            print("\n   Alertas pendientes:")
            for alerta in alertas:
                print(f"      {alerta}")
        
        print("\n✅ Belladonna v0.4 en modo descanso")
        print()
        
        logging.info("Belladonna v0.4 en modo descanso")
    
    def obtener_estado_completo(self):
        """Retorna estado completo del sistema"""
        estado_base = self.introspector.obtener_estado_completo()
        
        # Añade info de v0.4
        estado_base['aprendizaje'] = self.orquestador_aprendizaje.obtener_estadisticas()
        
        # Añade info de v0.3
        estado_base['pensamiento_autonomo'] = self.pensamiento.obtener_resumen()
        estado_base['auto_modificacion'] = self.auto_mod.obtener_estadisticas()
        
        return estado_base