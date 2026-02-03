"""
Script de Validación Final - Fase 1.

Ejecuta todas las pruebas y genera reporte.
"""
import subprocess
import sys

def ejecutar_comando(comando, descripcion):
    """Ejecuta un comando y reporta resultado."""
    print(f"\n{'='*70}")
    print(f"  {descripcion}")
    print('='*70)
    
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    
    if resultado.returncode == 0:
        print(f"✅ {descripcion}: PASÓ")
        return True
    else:
        print(f"❌ {descripcion}: FALLÓ")
        print(resultado.stdout)
        print(resultado.stderr)
        return False

def main():
    """Validación completa."""
    print("\n" + "="*70)
    print("  🌿 VALIDACIÓN FINAL FASE 1 - BELLADONNA 🌿")
    print("="*70)
    
    resultados = []
    
    # 1. Tests unitarios
    resultados.append(ejecutar_comando(
        "pytest tests/ -v --tb=short",
        "Tests Unitarios (54 tests)"
    ))
    
    # 2. Cobertura
    resultados.append(ejecutar_comando(
        "pytest tests/ --cov --cov-report=term-missing",
        "Cobertura de Código"
    ))
    
    # 3. Test conversación completa
    resultados.append(ejecutar_comando(
        "pytest tests/test_conversacion_completa.py -v",
        "Test Conversación Completa"
    ))
    
    # Reporte final
    print("\n" + "="*70)
    print("  REPORTE FINAL")
    print("="*70)
    
    total = len(resultados)
    pasados = sum(resultados)
    
    print(f"\nTests ejecutados: {total}")
    print(f"Pasados: {pasados}")
    print(f"Fallados: {total - pasados}")
    
    if all(resultados):
        print("\n🎉 ¡FASE 1 100% COMPLETA Y VALIDADA! 🎉")
        print("\nBelladonna está lista para producción.")
        return 0
    else:
        print("\n⚠️  Algunas pruebas fallaron. Revisar.")
        return 1

if __name__ == '__main__':
    sys.exit(main())