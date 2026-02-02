# tests/verificar_fase2.py

"""
Script de verificación completa de la Fase 2.
"""

import subprocess
import sys


def ejecutar_tests():
    """Ejecuta todos los tests de la Fase 2."""
    
    print("🧪 VERIFICACIÓN FASE 2 - CONSEJO COMPLETO")
    print("=" * 60)
    
    tests = [
        ("Nova", "tests/test_nova.py"),
        ("Echo", "tests/test_echo.py"),
        ("Lyra", "tests/test_lyra.py"),
        ("Luna", "tests/test_luna.py"),
        ("Deliberación", "tests/test_deliberacion_completa.py"),
        ("Integración", "tests/test_integracion_consejo.py"),
    ]
    
    resultados = []
    
    for nombre, archivo in tests:
        print(f"\n📋 Ejecutando tests de {nombre}...")
        
        resultado = subprocess.run(
            ["pytest", archivo, "-v"],
            capture_output=True,
            text=True
        )
        
        exito = resultado.returncode == 0
        resultados.append((nombre, exito))
        
        if exito:
            print(f"✅ {nombre}: PASÓ")
        else:
            print(f"❌ {nombre}: FALLÓ")
            print(resultado.stdout)
            print(resultado.stderr)
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN FASE 2:")
    print("=" * 60)
    
    total = len(resultados)
    exitosos = sum(1 for _, exito in resultados if exito)
    
    for nombre, exito in resultados:
        emoji = "✅" if exito else "❌"
        print(f"{emoji} {nombre}")
    
    print(f"\n🎯 {exitosos}/{total} grupos pasaron")
    
    if exitosos == total:
        print("\n🎉 ¡FASE 2 COMPLETADA!")
        return 0
    else:
        print("\n⚠️  Algunos tests fallaron")
        return 1


if __name__ == "__main__":
    sys.exit(ejecutar_tests())