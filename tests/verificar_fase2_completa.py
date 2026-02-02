# tests/verificar_fase2_completa.py

"""
Script de verificación completa de Fase 2.

Ejecuta todos los tests y verifica que esté al 100%.
"""

import subprocess
import sys


def ejecutar_tests_grupo(nombre_grupo, archivo_test):
    """Ejecuta un grupo de tests."""
    print(f"📋 Ejecutando tests de {nombre_grupo}...")
    
    resultado = subprocess.run(
        [sys.executable, '-m', 'pytest', archivo_test, '-v'],
        capture_output=True,
        text=True
    )
    
    if resultado.returncode == 0:
        print(f"✅ {nombre_grupo}: PASÓ")
        return True
    else:
        print(f"❌ {nombre_grupo}: FALLÓ")
        print(resultado.stdout)
        print(resultado.stderr)
        return False


def main():
    """Función principal."""
    
    print("\n" + "="*70)
    print("🧪 VERIFICACIÓN FASE 2 - 100% COMPLETA")
    print("="*70 + "\n")
    
    grupos = [
        ("Vega", "tests/test_vega.py"),
        ("Nova", "tests/test_nova.py"),
        ("Echo", "tests/test_echo.py"),
        ("Lyra", "tests/test_lyra.py"),
        ("Luna", "tests/test_luna.py"),
        ("Iris", "tests/test_iris.py"),
        ("Sage", "tests/test_sage.py"),
        ("Memoria", "tests/test_memoria.py"),
        ("Deliberación", "tests/test_deliberacion_completa.py"),
        ("Integración Consejo", "tests/test_integracion_consejo.py"),
        ("Validación Completa", "tests/test_validacion_fase2_completa.py")
    ]
    
    resultados = []
    
    for nombre, archivo in grupos:
        resultado = ejecutar_tests_grupo(nombre, archivo)
        resultados.append((nombre, resultado))
    
    print("\n" + "="*70)
    print("📊 RESUMEN FASE 2:")
    print("="*70)
    
    for nombre, resultado in resultados:
        simbolo = "✅" if resultado else "❌"
        print(f"{simbolo} {nombre}")
    
    total_pasados = sum(1 for _, r in resultados if r)
    total_grupos = len(resultados)
    
    print(f"\n🎯 {total_pasados}/{total_grupos} grupos pasaron")
    
    if total_pasados == total_grupos:
        print("\n" + "="*70)
        print("🎉 ¡FASE 2 - 100% COMPLETADA!")
        print("="*70)
        print("\n📊 COMPONENTES VERIFICADOS:")
        print("   ✅ 7 Consejeras (Vega, Nova, Echo, Lyra, Luna, Iris, Sage)")
        print("   ✅ Sistema de Deliberación Multi-Perspectiva")
        print("   ✅ Sistema de Memoria (RAM + SQLite)")
        print("   ✅ Bucle de Aprendizaje Pasivo")
        print("   ✅ Integración Completa")
        print("\n🚀 Listo para Fase 3!")
        return 0
    else:
        print("\n⚠️  Algunos tests fallaron")
        print("Revisa los errores arriba y corrige antes de continuar.")
        return 1


if __name__ == "__main__":
    sys.exit(main())