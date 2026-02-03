"""
Tests para el vocabulario expandido.
"""
import pytest
from vocabulario.conceptos_core import obtener_conceptos_core, obtener_concepto_por_palabra

def test_total_conceptos():
    """Test: Debe haber 15 conceptos en Día 2."""
    conceptos = obtener_conceptos_core()
    assert len(conceptos) == 15, f"Esperados 15, encontrados {len(conceptos)}"

def test_todos_tienen_id_valido():
    """Test: Todos los IDs deben empezar con CONCEPTO_."""
    conceptos = obtener_conceptos_core()
    for concepto in conceptos:
        assert concepto.id.startswith("CONCEPTO_"), f"ID inválido: {concepto.id}"

def test_grounding_promedio():
    """Test: Grounding promedio debe ser >= 0.80."""
    conceptos = obtener_conceptos_core()
    promedio = sum(c.confianza_grounding for c in conceptos) / len(conceptos)
    assert promedio >= 0.80, f"Grounding promedio: {promedio:.2f}"

def test_busqueda_por_palabra():
    """Test: Buscar conceptos por palabra."""
    conceptos = obtener_conceptos_core()
    
    # Debe encontrar
    concepto_leer = obtener_concepto_por_palabra("leer", conceptos)
    assert concepto_leer is not None
    assert concepto_leer.id == "CONCEPTO_LEER"
    
    concepto_hola = obtener_concepto_por_palabra("hola", conceptos)
    assert concepto_hola is not None
    
    # No debe encontrar
    concepto_inexistente = obtener_concepto_por_palabra("xyz123", conceptos)
    assert concepto_inexistente is None

def test_operaciones_ejecutables():
    """Test: Conceptos con grounding 1.0 deben tener operaciones."""
    conceptos = obtener_conceptos_core()
    for concepto in conceptos:
        if concepto.confianza_grounding == 1.0:
            assert len(concepto.operaciones) > 0, f"{concepto.id} sin operaciones"

if __name__ == '__main__':
    pytest.main([__file__, '-v'])