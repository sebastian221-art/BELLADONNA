"""
Belladonna - Sistema Conversacional con Grounding Computacional Real.

FASE 2 COMPLETA - VERSIÓN INTEGRADA
Arquitectura Cognitiva con:
- Sistema de Consejo Multi-Perspectiva
- Bucles Autónomos (pensamiento en segundo plano)
- Memoria Persistente (recuerda entre sesiones)
- Aprendizaje Básico (mejora automáticamente)
"""
import sys
from pathlib import Path
from datetime import datetime

# Asegurar imports
sys.path.insert(0, str(Path(__file__).parent))

from vocabulario.gestor_vocabulario import GestorVocabulario
from traduccion.traductor_entrada import TraductorEntrada
from razonamiento.motor_razonamiento import MotorRazonamiento
from consejeras.gestor_consejeras import GestorConsejeras
from generacion.generador_salida import GeneradorSalida

# ===== FASE 2: NUEVOS IMPORTS =====
from bucles import GestorBucles
from memoria import GestorMemoria
from aprendizaje import MotorAprendizaje

class Belladonna:
    """
    Belladonna - Sistema Conversacional Completo.
    
    Flujo Fase 1:
    1. Usuario habla en español
    2. Traductor → Conceptos internos
    3. Motor → Razonamiento
    4. Consejeras → Protección ética (7 perspectivas)
    5. Generador → Respuesta español
    
    Flujo Fase 2 (Paralelo):
    - Bucles analizan uso en segundo plano
    - Memoria persiste entre sesiones
    - Aprendizaje ajusta grounding automáticamente
    """
    
    def __init__(self, verbose: bool = False):
        """
        Inicializa Belladonna con todos los subsistemas.
        
        Args:
            verbose: Si True, muestra metadata de procesamiento
        """
        self.verbose = verbose
        
        print("Inicializando Belladonna Fase 2...")
        print()
        
        # ===== COMPONENTES FASE 1 =====
        self.gestor = GestorVocabulario()
        self.traductor = TraductorEntrada(self.gestor)
        self.motor = MotorRazonamiento()
        self.gestor_consejeras = GestorConsejeras()
        self.consejeras = self.gestor_consejeras.obtener_activas()
        self.generador = GeneradorSalida()
        
        print(f"✅ Fase 1: {len(self.gestor.obtener_todos())} conceptos cargados")
        print(f"✅ Consejeras: {len(self.consejeras)} activas")
        for consejera in self.consejeras:
            print(f"   • {consejera.nombre} ({consejera.especialidad})")
        print()
        
        # ===== COMPONENTES FASE 2 =====
        print("Inicializando subsistemas Fase 2...")
        
        # Bucles autónomos
        self.gestor_bucles = GestorBucles()
        print("✅ Bucles: 3 bucles configurados (corto, medio, largo)")
        
        # Memoria persistente
        self.gestor_memoria = GestorMemoria()
        print("✅ Memoria: Sistema de persistencia activo")
        
        # Aprendizaje básico
        self.motor_aprendizaje = MotorAprendizaje()
        self.motor_aprendizaje.configurar_integraciones(
            vocabulario=self.gestor,
            memoria=self.gestor_memoria,
            bucles=self.gestor_bucles
        )
        print("✅ Aprendizaje: Motor configurado e integrado")
        print()
        
        # Estadísticas
        self.turnos_conversacion = 0
        self.fase2_inicializado = False
    
    def iniciar_fase2(self):
        """Inicia los subsistemas de Fase 2."""
        if self.fase2_inicializado:
            return
        
        print("🚀 Iniciando subsistemas Fase 2...")
        
        # Iniciar sesión de memoria
        self.id_sesion = self.gestor_memoria.iniciar_sesion()
        print(f"   • Memoria: Sesión iniciada ({self.id_sesion[:8]}...)")
        
        # Iniciar bucles autónomos
        self.gestor_bucles.iniciar_todos()
        print(f"   • Bucles: 3 bucles en ejecución")
        
        print("✅ Fase 2 activa")
        print()
        
        self.fase2_inicializado = True
    
    def detener_fase2(self):
        """Detiene los subsistemas de Fase 2."""
        if not self.fase2_inicializado:
            return
        
        print()
        print("⏹️  Deteniendo subsistemas Fase 2...")
        
        # Detener bucles
        self.gestor_bucles.detener_todos()
        print("   • Bucles detenidos")
        
        # Finalizar sesión de memoria
        self.gestor_memoria.finalizar_sesion()
        print("   • Memoria guardada y sesión finalizada")
        
        self.fase2_inicializado = False
    
    def procesar(self, mensaje_usuario: str) -> str:
        """
        Procesa un mensaje del usuario.
        
        Args:
            mensaje_usuario: Texto en español
            
        Returns:
            Respuesta de Bell en español
        """
        # PASO 1: Traducir
        traduccion = self.traductor.traducir(mensaje_usuario)
        
        if self.verbose:
            print(f"[Traducción: {len(traduccion['conceptos'])} conceptos, "
                  f"confianza {traduccion['confianza']:.0%}]")
        
        # PASO 2: Razonar
        decision = self.motor.razonar(traduccion)
        
        if self.verbose:
            print(f"[Decisión: {decision.tipo.name}, certeza {decision.certeza:.0%}]")
        
        # PASO 3: Consejeras revisan
        revision_final = None
        for consejera in self.consejeras:
            revision = consejera.revisar(decision, {'traduccion': traduccion})
            
            if self.verbose:
                print(f"[{consejera.nombre}: {'VETO' if revision.get('veto') else 'OK'}]")
            
            if revision.get('veto'):
                revision_final = revision
                break
        
        if revision_final is None and self.consejeras:
            revision_final = revision
        
        # ===== FASE 2: REGISTRAR EN BUCLES Y MEMORIA =====
        if self.fase2_inicializado:
            # Registrar conceptos usados
            for concepto in traduccion['conceptos']:
                self.gestor_bucles.registrar_concepto_usado(concepto.id)
                self.gestor_memoria.guardar_concepto_usado(
                    concepto.id,
                    concepto.confianza_grounding
                )
            
            # Registrar decisión
            decision_info = {
                'tipo': decision.tipo.name,
                'puede_ejecutar': decision.puede_ejecutar,
                'certeza': decision.certeza,
                'conceptos_principales': [c.id for c in traduccion['conceptos'][:3]],
                'grounding_promedio': decision.grounding_promedio
            }
            self.gestor_bucles.registrar_decision(decision_info)
            self.gestor_memoria.guardar_decision(decision_info)
            
            # Procesar aprendizaje en tiempo real
            for concepto in traduccion['conceptos']:
                self.motor_aprendizaje.procesar_uso_concepto(
                    concepto.id,
                    exitoso=decision.puede_ejecutar,
                    certeza=concepto.confianza_grounding
                )
        
        # PASO 4: Generar respuesta
        respuesta = self.generador.generar(decision, {
            'traduccion': traduccion,
            'revision_vega': revision_final
        })
        
        return respuesta
    
    def loop_conversacional(self):
        """
        Loop interactivo de conversación.
        
        Comandos especiales Fase 1:
        - 'exit' o 'salir': Termina
        - 'verbose': Activa/desactiva modo verbose
        - 'stats': Muestra estadísticas
        - 'consejeras': Lista consejeras activas
        - 'help': Muestra ayuda
        
        Comandos especiales Fase 2:
        - 'bucles': Estado de bucles autónomos
        - 'memoria': Estadísticas de memoria
        - 'aprendizaje': Estado del motor de aprendizaje
        - 'fase2': Dashboard completo Fase 2
        """
        print("=" * 70)
        print(" " * 20 + "🌿 BELLADONNA v2.0 🌿")
        print(" " * 12 + "Fase 2 - Autonomía y Aprendizaje")
        print("=" * 70)
        print()
        print("Comandos especiales:")
        print("  Fase 1:")
        print("    • 'exit' o 'salir': Terminar")
        print("    • 'verbose': Activar/desactivar modo detallado")
        print("    • 'stats': Ver estadísticas del sistema")
        print("    • 'consejeras': Ver consejeras activas")
        print("    • 'help': Mostrar ayuda")
        print()
        print("  Fase 2:")
        print("    • 'bucles': Estado de bucles autónomos")
        print("    • 'memoria': Estadísticas de memoria")
        print("    • 'aprendizaje': Estado del motor de aprendizaje")
        print("    • 'fase2': Dashboard completo Fase 2")
        print()
        
        # Iniciar Fase 2
        self.iniciar_fase2()
        
        # Mensaje inicial
        print("Bell: ¡Hola! Soy Belladonna Fase 2. ¿En qué puedo ayudarte?")
        print()
        
        try:
            while True:
                try:
                    # Leer input
                    mensaje = input("Usuario: ").strip()
                    
                    if not mensaje:
                        continue
                    
                    # ===== COMANDOS FASE 1 =====
                    if mensaje.lower() in ['exit', 'salir', 'quit']:
                        print()
                        print("Bell: Adiós! Fue un placer ayudarte.")
                        break
                    
                    elif mensaje.lower() == 'verbose':
                        self.verbose = not self.verbose
                        estado = "activado" if self.verbose else "desactivado"
                        print(f"[Modo verbose {estado}]")
                        continue
                    
                    elif mensaje.lower() == 'stats':
                        self._mostrar_estadisticas()
                        continue
                    
                    elif mensaje.lower() == 'consejeras':
                        self._mostrar_consejeras()
                        continue
                    
                    elif mensaje.lower() == 'help':
                        self._mostrar_ayuda()
                        continue
                    
                    # ===== COMANDOS FASE 2 =====
                    elif mensaje.lower() == 'bucles':
                        self._mostrar_bucles()
                        continue
                    
                    elif mensaje.lower() == 'memoria':
                        self._mostrar_memoria()
                        continue
                    
                    elif mensaje.lower() == 'aprendizaje':
                        self._mostrar_aprendizaje()
                        continue
                    
                    elif mensaje.lower() == 'fase2':
                        self._mostrar_dashboard_fase2()
                        continue
                    
                    # Procesar mensaje normal
                    respuesta = self.procesar(mensaje)
                    
                    print()
                    print(f"Bell: {respuesta}")
                    print()
                    
                    self.turnos_conversacion += 1
                    
                except KeyboardInterrupt:
                    print()
                    print()
                    print("Bell: Interrumpido. Adiós!")
                    break
                
                except Exception as e:
                    print()
                    print(f"[ERROR: {e}]")
                    if self.verbose:
                        import traceback
                        traceback.print_exc()
                    print("Bell: Lo siento, tuve un error procesando eso.")
                    print()
        
        finally:
            # Detener Fase 2 al salir
            self.detener_fase2()
            
            # Estadísticas finales
            print()
            print("=" * 70)
            print(f"Conversación finalizada. Turnos: {self.turnos_conversacion}")
            print("=" * 70)
    
    # ===== MÉTODOS DE VISUALIZACIÓN FASE 1 =====
    
    def _mostrar_estadisticas(self):
        """Muestra estadísticas del sistema Fase 1."""
        print()
        print("=" * 70)
        print("ESTADÍSTICAS DEL SISTEMA - FASE 1")
        print("=" * 70)
        
        stats = self.gestor.estadisticas()
        print(f"Conceptos totales: {stats['total_conceptos']}")
        print(f"Grounding promedio: {stats['grounding_promedio']:.2f}")
        print(f"Conceptos ejecutables: {stats['con_operaciones']}")
        print()
        
        print("Consejeras:")
        for consejera in self.consejeras:
            stats_consejera = consejera.estadisticas()
            print(f"  {stats_consejera['nombre']}:")
            print(f"    - Revisiones: {stats_consejera['revisiones']}")
            print(f"    - Vetos: {stats_consejera.get('vetos', 0)}")
        print("=" * 70)
        print()
    
    def _mostrar_consejeras(self):
        """Muestra consejeras activas."""
        print()
        print("=" * 70)
        print("CONSEJERAS ACTIVAS")
        print("=" * 70)
        for consejera in self.consejeras:
            print(f"\n{consejera.nombre} - {consejera.especialidad}")
            print(f"  Estado: {'Activa' if consejera.activa else 'Inactiva'}")
            stats = consejera.estadisticas()
            print(f"  Revisiones: {stats['revisiones']}")
        print("=" * 70)
        print()
    
    def _mostrar_ayuda(self):
        """Muestra ayuda."""
        print()
        print("=" * 70)
        print("AYUDA - BELLADONNA FASE 2")
        print("=" * 70)
        print()
        print("Belladonna es un sistema conversacional con grounding real.")
        print()
        print("Puedes preguntarme sobre mis capacidades:")
        print("  • ¿Puedes leer archivos?")
        print("  • ¿Qué puedes hacer?")
        print("  • ¿Puedes ayudarme con Python?")
        print()
        print("También puedo conversar:")
        print("  • Hola")
        print("  • Gracias")
        print()
        print("Comandos Fase 1:")
        print("  • 'verbose': Activar modo detallado")
        print("  • 'stats': Ver estadísticas")
        print("  • 'consejeras': Ver consejeras activas")
        print("  • 'exit': Salir")
        print()
        print("Comandos Fase 2 (NUEVOS):")
        print("  • 'bucles': Ver estado de bucles autónomos")
        print("  • 'memoria': Ver estadísticas de memoria")
        print("  • 'aprendizaje': Ver estado del aprendizaje")
        print("  • 'fase2': Dashboard completo de Fase 2")
        print("=" * 70)
        print()
    
    # ===== MÉTODOS DE VISUALIZACIÓN FASE 2 =====
    
    def _mostrar_bucles(self):
        """Muestra estado de bucles autónomos."""
        print()
        print("=" * 70)
        print("BUCLES AUTÓNOMOS - ESTADO")
        print("=" * 70)
        
        estado = self.gestor_bucles.estado_sistema()
        
        print(f"\nEstado general: {'🟢 Activos' if estado['bucles_activos'] else '🔴 Detenidos'}")
        print()
        
        for bucle_nombre, bucle_stats in estado['bucles'].items():
            print(f"{bucle_nombre}:")
            print(f"  Estado: {'🟢 Activo' if bucle_stats['activo'] else '🔴 Detenido'}")
            print(f"  Intervalo: {bucle_stats['intervalo_segundos']}s")
            print(f"  Ciclos ejecutados: {bucle_stats['ciclos_ejecutados']}")
            print(f"  Última ejecución: {bucle_stats.get('ultimo_ciclo', 'Nunca')}")
            print()
        
        # Conceptos calientes
        conceptos_calientes = self.gestor_bucles.obtener_conceptos_calientes()
        if conceptos_calientes:
            print("Conceptos más usados recientemente:")
            for concepto, info in conceptos_calientes[:5]:
                print(f"  • {concepto}: {info['porcentaje']:.1f}% ({info['veces']} usos)")
            print()
        
        # Patrones detectados
        patrones = self.gestor_bucles.obtener_patrones()
        if patrones:
            print("Patrones detectados:")
            for patron in patrones[:3]:
                print(f"  • {patron['tipo']}: {patron['descripcion']}")
            print()
        
        # Insights
        insights = self.gestor_bucles.obtener_insights()
        if insights:
            print(f"Insights generados: {len(insights)}")
            for insight in insights[-2:]:
                print(f"  • {insight['tipo']}: {insight['descripcion']}")
            print()
        
        print("=" * 70)
        print()
    
    def _mostrar_memoria(self):
        """Muestra estadísticas de memoria."""
        print()
        print("=" * 70)
        print("MEMORIA PERSISTENTE - ESTADÍSTICAS")
        print("=" * 70)
        
        stats = self.gestor_memoria.obtener_estadisticas_globales()
        
        print(f"\nSesión actual: {self.id_sesion[:8]}... (activa)")
        print()
        print(f"Sesiones totales: {stats['total_sesiones']}")
        print(f"Conceptos guardados: {stats['total_conceptos_usados']}")
        print(f"Decisiones guardadas: {stats['total_decisiones']}")
        print(f"Patrones guardados: {stats['total_patrones']}")
        print(f"Insights guardados: {stats['total_insights']}")
        print(f"Ajustes guardados: {stats['total_ajustes']}")
        print()
        
        # Conceptos más usados
        if stats['conceptos_mas_usados']:
            print("Conceptos más usados (histórico):")
            for concepto in stats['conceptos_mas_usados'][:5]:
                print(f"  • {concepto['concepto_id']}: {concepto['usos']} usos")
            print()
        
        # Estadísticas de decisiones
        stats_dec = stats['estadisticas_decisiones']
        if stats_dec['total'] > 0:
            print("Estadísticas de decisiones:")
            print(f"  Total: {stats_dec['total']}")
            print(f"  Tasa de ejecución: {stats_dec['tasa_ejecucion']:.1f}%")
            print(f"  Certeza promedio: {stats_dec['certeza_promedio']:.2f}")
            print()
        
        # Info del almacén
        almacen = stats['almacen']
        print(f"Almacenamiento:")
        print(f"  Archivos: {almacen['total_archivos']}")
        print(f"  Tamaño: {almacen['tamano_mb']:.2f} MB")
        
        print("=" * 70)
        print()
    
    def _mostrar_aprendizaje(self):
        """Muestra estado del motor de aprendizaje."""
        print()
        print("=" * 70)
        print("MOTOR DE APRENDIZAJE - ESTADO")
        print("=" * 70)
        
        stats = self.motor_aprendizaje.obtener_estadisticas()
        
        print(f"\nCiclos ejecutados: {stats['ciclos_ejecutados']}")
        print(f"Estado: {'🟢 Activo' if stats['activo'] else '⚪ En espera'}")
        print()
        
        # Estadísticas del ajustador
        stats_ajustador = stats['ajustador']
        print("Ajustador de Grounding:")
        print(f"  Total ajustes propuestos: {stats_ajustador['total_ajustes']}")
        print(f"  Ajustes aplicados: {stats_ajustador['ajustes_aplicados']}")
        if stats_ajustador['total_ajustes'] > 0:
            print(f"  Tasa de aplicación: {stats_ajustador['tasa_aplicacion']:.1f}%")
            print(f"  Cambio promedio: {stats_ajustador['cambio_promedio']:.3f}")
        print(f"  Conceptos ajustados: {stats_ajustador['conceptos_ajustados']}")
        print()
        
        # Estadísticas del aplicador
        stats_aplicador = stats['aplicador']
        print("Aplicador de Insights:")
        print(f"  Insights procesados: {stats_aplicador['insights_procesados']}")
        print(f"  Acciones generadas: {stats_aplicador['acciones_generadas']}")
        print(f"  Acciones aplicadas: {stats_aplicador['acciones_aplicadas']}")
        print()
        
        # Historial de ajustes recientes
        historial = self.motor_aprendizaje.obtener_historial_ajustes()
        if historial:
            print(f"Ajustes recientes ({len(historial[-5:])}):")
            for ajuste in historial[-5:]:
                print(f"  • {ajuste['concepto_id']}: "
                      f"{ajuste['grounding_anterior']:.2f} → {ajuste['grounding_nuevo']:.2f} "
                      f"({ajuste['razon']})")
            print()
        
        # Integraciones
        integs = stats['integraciones']
        print("Integraciones:")
        print(f"  Vocabulario: {'✅' if integs['vocabulario'] else '❌'}")
        print(f"  Memoria: {'✅' if integs['memoria'] else '❌'}")
        print(f"  Bucles: {'✅' if integs['bucles'] else '❌'}")
        
        print("=" * 70)
        print()
    
    def _mostrar_dashboard_fase2(self):
        """Muestra dashboard completo de Fase 2."""
        print()
        print("=" * 70)
        print("DASHBOARD COMPLETO - FASE 2")
        print("=" * 70)
        print()
        
        # Resumen general
        print("📊 RESUMEN GENERAL")
        print(f"  Sesión actual: {self.id_sesion[:8]}...")
        print(f"  Turnos de conversación: {self.turnos_conversacion}")
        print(f"  Fase 2 activa: {'✅ Sí' if self.fase2_inicializado else '❌ No'}")
        print()
        
        # Bucles (compacto)
        estado_bucles = self.gestor_bucles.estado_sistema()
        print("🔄 BUCLES AUTÓNOMOS")
        for nombre, stats in estado_bucles['bucles'].items():
            print(f"  {nombre}: {stats['ciclos_ejecutados']} ciclos "
                  f"({'🟢 activo' if stats['activo'] else '🔴 detenido'})")
        print()
        
        # Memoria (compacto)
        stats_mem = self.gestor_memoria.obtener_estadisticas_globales()
        print("💾 MEMORIA")
        print(f"  Conceptos: {stats_mem['total_conceptos_usados']}")
        print(f"  Decisiones: {stats_mem['total_decisiones']}")
        print(f"  Insights: {stats_mem['total_insights']}")
        print(f"  Tamaño: {stats_mem['almacen']['tamano_mb']:.2f} MB")
        print()
        
        # Aprendizaje (compacto)
        stats_apr = self.motor_aprendizaje.obtener_estadisticas()
        print("🧠 APRENDIZAJE")
        print(f"  Ciclos: {stats_apr['ciclos_ejecutados']}")
        print(f"  Ajustes aplicados: {stats_apr['ajustador']['ajustes_aplicados']}")
        print(f"  Conceptos ajustados: {stats_apr['ajustador']['conceptos_ajustados']}")
        print()
        
        print("💡 Para ver detalles, usa:")
        print("  • 'bucles' - Ver estado de bucles")
        print("  • 'memoria' - Ver estadísticas de memoria")
        print("  • 'aprendizaje' - Ver estado del aprendizaje")
        
        print("=" * 70)
        print()

def main():
    """Punto de entrada principal."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Belladonna - Sistema Conversacional Fase 2'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Activar modo verbose (mostrar metadata)'
    )
    
    args = parser.parse_args()
    
    # Crear e iniciar Belladonna
    bell = Belladonna(verbose=args.verbose)
    bell.loop_conversacional()

if __name__ == '__main__':
    main()