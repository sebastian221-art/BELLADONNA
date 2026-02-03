"""
Demo del Día 2 - 15 conceptos.
"""
from vocabulario.conceptos_core import obtener_conceptos_core, obtener_concepto_por_palabra

def main():
    print("=" * 60)
    print("   DEMO DÍA 2: BELLADONNA - 15 CONCEPTOS")
    print("=" * 60)
    print()
    
    conceptos = obtener_conceptos_core()
    print(f"✅ Total conceptos: {len(conceptos)}\n")
    
    # Agrupar por tipo
    por_tipo = {}
    for c in conceptos:
        tipo = c.tipo.name
        if tipo not in por_tipo:
            por_tipo[tipo] = []
        por_tipo[tipo].append(c)
    
    # Mostrar agrupados
    for tipo, lista in por_tipo.items():
        print(f"\n📂 {tipo}: {len(lista)} conceptos")
        for c in lista:
            print(f"  • {c.id} → {c.palabras_español} (grounding: {c.confianza_grounding})")
    
    # Estadísticas
    print("\n" + "=" * 60)
    print("   ESTADÍSTICAS")
    print("=" * 60)
    grounding_promedio = sum(c.confianza_grounding for c in conceptos) / len(conceptos)
    con_operaciones = sum(1 for c in conceptos if len(c.operaciones) > 0)
    
    print(f"Grounding promedio: {grounding_promedio:.2f}")
    print(f"Conceptos con operaciones ejecutables: {con_operaciones}")
    print(f"Conceptos con grounding 1.0: {sum(1 for c in conceptos if c.confianza_grounding == 1.0)}")
    
    # Test de búsqueda
    print("\n" + "=" * 60)
    print("   TEST: Búsqueda de conceptos")
    print("=" * 60)
    
    palabras_test = ["leer", "hola", "ayuda", "pensar", "xyz"]
    for palabra in palabras_test:
        concepto = obtener_concepto_por_palabra(palabra, conceptos)
        if concepto:
            print(f"✅ '{palabra}' → {concepto.id}")
        else:
            print(f"❌ '{palabra}' → No encontrado")
    
    print("\n" + "=" * 60)
    print("   ✅ DEMO DÍA 2 EXITOSO")
    print("=" * 60)

if __name__ == '__main__':
    main()