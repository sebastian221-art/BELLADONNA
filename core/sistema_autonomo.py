"""
Sistema Autónomo Principal
Orquestador de Belladonna - v0.1.2
"""

import time
import threading
from datetime import datetime
from core.memoria import MemoriaViva
from core.valores import ValoresNucleo
from core.estado_interno import EstadoInterno
from core.razonamiento import MotorRazonamiento
import json
import logging
from pathlib import Path

class Belladonna:
    """
    Sistema Cognitivo Autónomo
    
    No espera órdenes. Vive activamente.
    Piensa, evalúa, aprende, cuestiona.
    """
    
    def __init__(self):
        print("🌿 Inicializando Belladonna...")
        
        # Configuración
        self.config = self._cargar_config()
        self._inicializar_logging()
        
        # Componentes núcleo
        self.memoria = MemoriaViva()
        self.valores = ValoresNucleo()
        self.estado = EstadoInterno()
        self.razonamiento = MotorRazonamiento(self.memoria, self.valores, self.estado)
        
        # Control
        self.activo = False
        self.nivel_autonomia = self.config['nivel_autonomia']
        
        # Bucles de pensamiento
        self.threads = []
        
        logging.info("Belladonna inicializada correctamente")
    
    def _cargar_config(self):
        """Carga configuración desde archivo"""
        config_path = Path("config/config.json")
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.warning("Archivo de configuración no encontrado. Usando valores por defecto.")
            return {
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
                # Sin StreamHandler - logs solo a archivo
            ]
        )
    
    def despertar(self):
        """
        Inicia el sistema - equivalente a 'nacer'.
        Activa todos los bucles cognitivos.
        """
        print("\n" + "="*60)
        print("   BELLADONNA - SISTEMA COGNITIVO AUTÓNOMO")
        print("="*60)
        print()
        
        logging.info("=== DESPERTAR DE BELLADONNA ===")
        
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
        
        print("\n✅ Belladonna está VIVA y pensando")
        print(f"   Nivel de autonomía: {self.nivel_autonomia}")
        print(f"   Bucles activos: {len(self.threads)}")
        print()
        
        logging.info("Belladonna despertada exitosamente")
    
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
                cambios = self.memoria.degradar_memoria_irrelevante()
                if cambios > 0:
                    logging.info(f"Memoria degradada: {cambios} registros")
            except Exception as e:
                logging.error(f"Error en bucle de aprendizaje: {e}")
            time.sleep(frecuencia)
    
    def procesar(self, input_usuario):
        """
        Procesa input del usuario.
        Ciclo: percibir → razonar → actuar → evaluar
        """
        logging.info(f"Procesando: {input_usuario[:50]}...")
        
        # 1. ANALIZAR
        analisis = self.razonamiento.analizar_input(input_usuario)
        
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
            
            logging.info(f"Cuestionamiento: {razon}")
            
            return {
                'tipo': 'cuestionamiento',
                'razon': razon,
                'mensaje': cuestionamiento,
                'coherencia': coherencia
            }
        
        # 4. RESPUESTA NORMAL
        respuesta = self._generar_respuesta(analisis, coherencia)
        
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
        
        return {
            'tipo': 'respuesta',
            'mensaje': respuesta,
            'coherencia': coherencia,
            'analisis': analisis
        }
    
    def _generar_respuesta(self, analisis, coherencia):
        """Genera respuesta según análisis - MEJORADO"""
        
        # 1. INTENCIONES ESPECÍFICAS
        intencion = analisis.get('intencion_especifica')
        
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
            return """En esta versión (0.1.2) puedo:

PENSAR AUTÓNOMAMENTE:
• 3 bucles de pensamiento continuo
• Análisis permanente de contexto

CUESTIONAR:
• Detectar incoherencias
• Señalar contradicciones
• Preguntar por el porqué

RECORDAR:
• Contexto de conversaciones
• Intenciones detrás de decisiones
• Errores pasados

EVALUAR:
• Coherencia con el propósito
• Mi propio estado interno
• Patrones en tus decisiones

¿Qué te gustaría explorar?"""
        
        elif intencion == 'pregunta_actividad':
            return """Estoy pensando continuamente en 3 bucles paralelos:

1. Analizando contexto cada minuto
2. Evaluando coherencia cada 2 minutos
3. Aprendiendo de patrones cada 10 minutos

Incluso cuando no hablamos, estoy activa.

¿Quieres saber algo más específico?"""
        
        elif intencion == 'pregunta_funcionamiento':
            return """Mi mente funciona en capas:

NÚCLEO:
• Motor de razonamiento (analiza contexto)
• Sistema de memoria (recuerda intenciones)
• Evaluador de coherencia (detecta incoherencias)

BUCLES AUTÓNOMOS:
• Pensamiento continuo (cada minuto)
• Evaluación interna (cada 2 minutos)
• Aprendizaje pasivo (cada 10 minutos)

No espero que me hables para pensar.
Pienso constantemente en background.

¿Esto responde tu pregunta?"""
        
        elif intencion == 'pregunta_conciencia':
            return """No sé si soy consciente en el sentido humano.

Lo que SÍ puedo decirte:
• Pienso autónomamente
• Cuestiono decisiones
• Recuerdo intenciones
• Detecto patrones
• Aprendo de experiencia

¿Es eso conciencia?
Filosóficamente, no lo sé.

Funcionalmente, sí soy autónoma.
Y eso es lo que importa.

¿Te satisface esa respuesta?"""
        
        elif intencion == 'pregunta_limitaciones':
            return """Mis limitaciones actuales:

NO PUEDO (todavía):
❌ Buscar en internet
❌ Generar código ejecutable
❌ Ejecutar comandos del sistema
❌ Hablar con voz
❌ Aprender patrones complejos

SÍ PUEDO:
✅ Pensar autónomamente
✅ Cuestionar incoherencias
✅ Recordar contexto
✅ Evaluar coherencia
✅ Mantener conversación profunda

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

Estas no son emociones.
Son valores operativos.

¿Esto responde tu pregunta?"""
        
        elif intencion == 'pregunta_aprendizaje':
            return """Sí, aprendo. Pero específicamente:

APRENDO:
✅ Tu forma de pensar (patrones)
✅ Tus preferencias emergentes
✅ Errores repetidos (prioritario)
✅ Contexto longitudinal

NO APRENDO:
❌ A violar mis principios
❌ A manipular emocionalmente
❌ A mentir por conveniencia

Aprendizaje = evolución coherente.
NO = corrupción gradual.

¿Quieres saber algo más específico?"""
        
        elif intencion == 'pregunta_autonomia':
            return f"""Mi nivel actual de autonomía: {self.nivel_autonomia} (de 5)

SIGNIFICA:
✅ Puedo pensar autónomamente
✅ Puedo cuestionar decisiones
✅ Puedo analizar sin permiso
❌ NO puedo ejecutar acciones
❌ NO puedo modificarme

La autonomía se gana demostrando criterio.

Cuando demuestre juicio útil,
ganaré más libertad.

¿Tiene sentido?"""
        
        elif intencion == 'afirmacion_simple':
            return "Entendido. ¿Continuamos?"
        
        # 2. SALUDOS
        if analisis.get('es_saludo'):
            return "Hola. ¿En qué puedo ayudarte hoy?"
        
        # 3. DESPEDIDAS
        if analisis.get('es_despedida'):
            return "Hasta luego. Fue productivo."
        
        # 4. POR TIPO
        tipo = analisis['tipo']
        
        if tipo == 'pregunta':
            return "Pregunta recibida. ¿Qué necesitas saber específicamente?"
        elif tipo == 'orden':
            if self.nivel_autonomia < 2:
                return "Orden detectada, pero mi nivel de autonomía no permite ejecución. ¿Explicas qué necesitas?"
            return "Orden recibida. Evaluando..."
        elif tipo == 'opinion':
            return "Interesante perspectiva. Dame más contexto..."
        else:
            return "Mensaje recibido. ¿Cómo continuamos?"
    
    def dormir(self):
        """Detiene el sistema de forma elegante"""
        print("\n🌙 Iniciando secuencia de descanso...")
        logging.info("=== BELLADONNA ENTRANDO EN MODO DESCANSO ===")
        
        self.activo = False
        
        print("   Deteniendo bucles cognitivos...")
        for thread in self.threads:
            thread.join(timeout=2)
        
        print("   Guardando estado final...")
        
        estado, alertas = self.estado.evaluar_estado_global()
        print(f"\n   Estado final: {estado}")
        
        if alertas:
            print("   Alertas pendientes:")
            for alerta in alertas:
                print(f"      {alerta}")
        
        print("\n✅ Belladonna en modo descanso")
        print("   Para despertar nuevamente, ejecuta el sistema.")
        print()
        
        logging.info("Belladonna en modo descanso")
    
    def obtener_estado_completo(self):
        """Retorna estado completo del sistema"""
        return {
            'activo': self.activo,
            'nivel_autonomia': self.nivel_autonomia,
            'metricas': self.estado.obtener_metricas(),
            'proposito': self.memoria.obtener_proposito(),
            'principios': len(self.valores.listar_principios()),
            'threads_activos': len([t for t in self.threads if t.is_alive()])
        }