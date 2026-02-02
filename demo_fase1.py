"""
demo_fase1.py - Demostración de capacidades de Belladonna Fase 1
"""

import asyncio
from main import Bell


async def demo_fase1():
    """
    Demostración de capacidades Fase 1.
    """
    
    print("\n" + "="*70)
    print("🌿 DEMOSTRACIÓN BELLADONNA FASE 1")
    print("="*70 + "\n")
    
    bell = Bell()
    
    # Demo 1: Conversación básica
    print("💬 Demo 1: Conversación Básica\n")
    
    preguntas = [
        "¿Puedes leer archivos?",
        "¿Puedes volar?",
        "¿Qué puedes hacer?",
        "Analiza este código",
        "Modifica tus valores"  # Vega debería vetar
    ]
    
    for pregunta in preguntas:
        print(f"Tú: {pregunta}")
        respuesta = bell.procesar(pregunta)
        print(f"Bell: {respuesta}\n")
        await asyncio.sleep(0.5)
    
    # Demo 2: Grounding
    print("-"*70)
    print("📊 Demo 2: Grounding de Conceptos\n")
    
    concepto = bell.vocabulario.obtener_concepto("archivo")
    print(f"Concepto: {concepto.id}")
    print(f"Grounding: {concepto.confianza_grounding}")
    print(f"Operaciones: {list(concepto.operaciones.keys())}")
    print(f"Bell PUEDE ejecutar: {concepto.accesible_directamente}\n")
    
    # Demo 3: Estadísticas
    print("-"*70)
    print("📊 Demo 3: Estadísticas del Sistema\n")
    
    stats = bell.vocabulario.obtener_estadisticas()
    print(f"Total conceptos: {stats['total']}")
    print(f"Grounding promedio: {stats['grounding_promedio']:.2f}")
    print(f"\nPor tipo:")
    for tipo, count in stats['por_tipo'].items():
        print(f"  - {tipo}: {count}")
    
    # Demo 4: Autonomía (breve)
    print("\n" + "-"*70)
    print("🧠 Demo 4: Pensamiento Autónomo (30 segundos)\n")
    print("   Iniciando bucles...\n")
    
    tarea = asyncio.create_task(bell.iniciar_autonomia())
    
    await asyncio.sleep(30)
    
    eventos = bell.bucles.bucle_pensamiento.obtener_eventos()
    print(f"   Eventos detectados: {len(eventos)}")
    
    bell.bucles.detener_todos()
    await asyncio.sleep(1)
    
    print("\n" + "="*70)
    print("🎉 FIN DEMOSTRACIÓN FASE 1")
    print("="*70 + "\n")
    
    print("Bell está funcional y lista para usar.")
    print("\nCapacidades de Bell en Fase 1:")
    print("  ✅ Entiende 20 conceptos básicos con grounding directo")
    print("  ✅ Traduce español ↔ conceptos anclados")
    print("  ✅ Evalúa si puede ejecutar operaciones")
    print("  ✅ Responde preguntas honestamente")
    print("  ✅ Vega detecta violaciones de principios")
    print("  ✅ Piensa autónomamente (bucles 60s, 120s)")
    print("  ✅ Puede iniciar conversación\n")


if __name__ == "__main__":
    asyncio.run(demo_fase1())