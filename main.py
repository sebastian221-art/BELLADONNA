"""
Belladonna - Sistema Conversacional con Grounding Computacional Real.

FASE 2 - VERSIÓN MODULAR
Arquitectura Cognitiva con Sistema de Consejo Multi-Perspectiva
"""
import sys
from pathlib import Path

# Asegurar imports
sys.path.insert(0, str(Path(__file__).parent))

from vocabulario.gestor_vocabulario import GestorVocabulario
from traduccion.traductor_entrada import TraductorEntrada
from razonamiento.motor_razonamiento import MotorRazonamiento
from consejeras.gestor_consejeras import GestorConsejeras  # ← MODIFICADO: usar gestor
from generacion.generador_salida import GeneradorSalida

class Belladonna:
    """
    Belladonna - Sistema Conversacional Completo.
    
    Flujo:
    1. Usuario habla en español
    2. Traductor → Conceptos internos
    3. Motor → Razonamiento
    4. Consejeras → Protección ética (múltiples perspectivas)  # ← MODIFICADO
    5. Generador → Respuesta español
    """
    
    def __init__(self, verbose: bool = False):
        """
        Inicializa Belladonna.
        
        Args:
            verbose: Si True, muestra metadata de procesamiento
        """
        self.verbose = verbose
        
        print("Inicializando Belladonna...")
        
        # Componentes
        self.gestor = GestorVocabulario()
        self.traductor = TraductorEntrada(self.gestor)
        self.motor = MotorRazonamiento()
        
        # ← MODIFICADO: Usar gestor de consejeras
        self.gestor_consejeras = GestorConsejeras()
        self.consejeras = self.gestor_consejeras.obtener_activas()
        
        self.generador = GeneradorSalida()
        
        print(f"✅ Sistema cargado: {len(self.gestor.obtener_todos())} conceptos")
        print(f"✅ Consejeras activas: {len(self.consejeras)}")  # ← MODIFICADO
        for consejera in self.consejeras:
            print(f"   • {consejera.nombre} ({consejera.especialidad})")
        print()
    
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
        
        # PASO 3: Consejeras revisan (solo Vega por ahora tiene veto)
        # ← MODIFICADO: Revisar con todas las consejeras activas
        revision_final = None
        for consejera in self.consejeras:
            revision = consejera.revisar(decision, {'traduccion': traduccion})
            
            if self.verbose:
                print(f"[{consejera.nombre}: {'VETO' if revision.get('veto') else 'OK'}]")
            
            # Si alguna veta, usar esa revisión
            if revision.get('veto'):
                revision_final = revision
                break
        
        # Si nadie vetó, usar última revisión
        if revision_final is None and self.consejeras:
            revision_final = revision
        
        # PASO 4: Generar respuesta
        respuesta = self.generador.generar(decision, {
            'traduccion': traduccion,
            'revision_vega': revision_final  # Mantener nombre por compatibilidad
        })
        
        return respuesta
    
    def loop_conversacional(self):
        """
        Loop interactivo de conversación.
        
        Comandos especiales:
        - 'exit' o 'salir': Termina
        - 'verbose': Activa/desactiva modo verbose
        - 'stats': Muestra estadísticas
        - 'consejeras': Lista consejeras activas
        """
        print("=" * 70)
        print(" " * 20 + "🌿 BELLADONNA v2.0 🌿")
        print(" " * 15 + "Fase 2 - Sistema de Consejo")
        print("=" * 70)
        print()
        print("Comandos especiales:")
        print("  • 'exit' o 'salir': Terminar")
        print("  • 'verbose': Activar/desactivar modo detallado")
        print("  • 'stats': Ver estadísticas del sistema")
        print("  • 'consejeras': Ver consejeras activas")
        print("  • 'help': Mostrar ayuda")
        print()
        
        # Mensaje inicial
        print("Bell: Hola! Soy Belladonna. ¿En qué puedo ayudarte?")
        print()
        
        turnos = 0
        
        while True:
            try:
                # Leer input
                mensaje = input("Usuario: ").strip()
                
                if not mensaje:
                    continue
                
                # Comandos especiales
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
                
                # Procesar mensaje
                respuesta = self.procesar(mensaje)
                
                print()
                print(f"Bell: {respuesta}")
                print()
                
                turnos += 1
                
            except KeyboardInterrupt:
                print()
                print()
                print("Bell: Interrumpido. Adiós!")
                break
            
            except Exception as e:
                print()
                print(f"[ERROR: {e}]")
                print("Bell: Lo siento, tuve un error procesando eso.")
                print()
        
        # Estadísticas finales
        print()
        print("=" * 70)
        print(f"Conversación finalizada. Turnos: {turnos}")
        print("=" * 70)
    
    def _mostrar_estadisticas(self):
        """Muestra estadísticas del sistema."""
        print()
        print("=" * 70)
        print("ESTADÍSTICAS DEL SISTEMA")
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
        print("AYUDA")
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
        print("Comandos especiales:")
        print("  • 'verbose': Activar modo detallado")
        print("  • 'stats': Ver estadísticas")
        print("  • 'consejeras': Ver consejeras activas")
        print("  • 'exit': Salir")
        print("=" * 70)
        print()

def main():
    """Punto de entrada principal."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Belladonna - Sistema Conversacional')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Activar modo verbose (mostrar metadata)')
    
    args = parser.parse_args()
    
    # Crear e iniciar Belladonna
    bell = Belladonna(verbose=args.verbose)
    bell.loop_conversacional()

if __name__ == '__main__':
    main()