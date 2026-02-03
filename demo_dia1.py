"""
Demo del primer día de Belladonna.
"""
from vocabulario.conceptos_core import obtener_conceptos_core

def main():
    print("=" * 50)
    print("   DEMO DÍA 1: BELLADONNA")
    print("=" * 50)
    print()
    
    # Cargar conceptos
    conceptos = obtener_conceptos_core()
    print(f"✅ Conceptos cargados: {len(conceptos)}\n")
    
    # Mostrar cada concepto
    for concepto in conceptos:
        print(f"ID: {concepto.id}")
        print(f"  Tipo: {concepto.tipo.name}")
        print(f"  Palabras: {concepto.palabras_español}")
        print(f"  Grounding: {concepto.confianza_grounding}")
        print(f"  Operaciones: {list(concepto.operaciones.keys())}")
        print()
    
    # Estadísticas
    grounding_promedio = sum(c.confianza_grounding for c in conceptos) / len(conceptos)
    print(f"📊 Grounding promedio: {grounding_promedio:.2f}")
    print()
    
    # Test de operación REAL
    print("=" * 50)
    print("   TEST: Leer archivo")
    print("=" * 50)
    print()
    
    concepto_leer = conceptos[0]  # CONCEPTO_LEER
    
    # Crear archivo de prueba
    import tempfile
    import os
    archivo_temp = os.path.join(tempfile.gettempdir(), 'test_bell.txt')
    
    with open(archivo_temp, 'w', encoding='utf-8') as f:
        f.write("¡Hola desde Belladonna!")
    
    print(f"Archivo creado: {archivo_temp}")
    
    # Leer con Bell
    contenido = concepto_leer.ejecutar('ejecutar', archivo_temp)
    print(f"Contenido leído: {contenido}")
    print(f"Veces usado: {concepto_leer.metadata['veces_usado']}")
    
    print()
    print("=" * 50)
    print("   ✅ DEMO EXITOSO")
    print("=" * 50)

if __name__ == '__main__':
    main()