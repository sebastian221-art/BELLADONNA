"""
Belladonna - Sistema Conversacional con Grounding Computacional Real.

FASE 1 - VERSIÓN COMPLETA
Arquitectura Cognitiva con Lenguaje Interno Explícito
"""
import sys
from pathlib import Path

# Asegurar imports
sys.path.insert(0, str(Path(__file__).parent))

from vocabulario.gestor_vocabulario import GestorVocabulario
from traduccion.traductor_entrada import TraductorEntrada
from razonamiento.motor_razonamiento import MotorRazonamiento
from consejeras.vega import Vega
from generacion.generador_salida import GeneradorSalida

class Belladonna:
    """
    Belladonna - Sistema Conversacional Completo.
    
    Flujo:
    1. Usuario habla en español
    2. Traductor → Conceptos internos
    3. Motor → Razonamiento
    4. Vega → Protección ética
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
        self.vega = Vega()
        self.generador = GeneradorSalida()
        
        print(f"✅ Sistema cargado: {len(self.gestor.obtener_todos())} conceptos")
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
        
        # PASO 3: Vega revisa
        revision = self.vega.revisar(decision, {'traduccion': traduccion})
        
        if self.verbose and revision['veto']:
            print(f"[Vega: VETO - {revision['principio_violado'].name}]")
        
        # PASO 4: Generar respuesta
        respuesta = self.generador.generar(decision, {
            'traduccion': traduccion,
            'revision_vega': revision
        })
        
        return respuesta
    
    def loop_conversacional(self):
        """
        Loop interactivo de conversación.
        
        Comandos especiales:
        - 'exit' o 'salir': Termina
        - 'verbose': Activa/desactiva modo verbose
        - 'stats': Muestra estadísticas
        """
        print("=" * 70)
        print(" " * 20 + "🌿 BELLADONNA v1.0 🌿")
        print(" " * 15 + "Fase 1 - Sistema Conversacional")
        print("=" * 70)
        print()
        print("Comandos especiales:")
        print("  • 'exit' o 'salir': Terminar")
        print("  • 'verbose': Activar/desactivar modo detallado")
        print("  • 'stats': Ver estadísticas del sistema")
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
        
        vega_stats = self.vega.estadisticas()
        print(f"Vega - Revisiones: {vega_stats['revisiones']}")
        print(f"Vega - Vetos: {vega_stats['vetos']}")
        print(f"Vega - Tasa veto: {vega_stats['tasa_veto']:.0%}")
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