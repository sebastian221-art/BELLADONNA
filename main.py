#!/usr/bin/env python3
"""
Belladonna - Sistema Cognitivo Autónomo
Punto de entrada principal

Ejecutar: python main.py
"""

import sys
from pathlib import Path

# Asegura que el directorio raíz esté en el path
sys.path.insert(0, str(Path(__file__).parent))

from core.sistema_autonomo import Belladonna
from capacidades.comunicacion import InterfazCLI

def main():
    """Función principal"""
    try:
        # Crea el sistema
        sistema = Belladonna()
        
        # Despierta (activa bucles cognitivos)
        sistema.despertar()
        
        # Inicia interfaz de comunicación
        interfaz = InterfazCLI(sistema)
        interfaz.iniciar()
        
        # Al salir de la interfaz, pone el sistema a dormir
        sistema.dormir()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupción del usuario")
        if 'sistema' in locals():
            sistema.dormir()
    
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()