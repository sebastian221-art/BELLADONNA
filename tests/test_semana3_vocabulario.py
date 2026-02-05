"""
Tests para Vocabulario Semana 3 - 80 conceptos adicionales.

Total esperado: 110 (previo) + 80 (semana 3) + 34 (semana 4) = 224
"""
import pytest
from vocabulario.gestor_vocabulario import GestorVocabulario

@pytest.fixture
def gestor():
    """Gestor con vocabulario completo."""
    return GestorVocabulario()

def test_total_190_conceptos(gestor):
    """Test: Total debe ser 225 (110 + 80 + 35)."""
    conceptos = gestor.obtener_todos()
    assert len(conceptos) == 225, f"Esperados 225, encontrados {len(conceptos)}"

def test_sistema_avanzado(gestor):
    """Test: Conceptos de sistema avanzado presentes."""
    # Sistema avanzado (30 conceptos)
    assert gestor.buscar_por_palabra("copiar") is not None
    assert gestor.buscar_por_palabra("mover") is not None
    assert gestor.buscar_por_palabra("ejecutar") is not None
    assert gestor.buscar_por_palabra("proceso") is not None

def test_matematicas(gestor):
    """Test: Conceptos matemáticos presentes."""
    # Matemáticas (20 conceptos) - NOMBRES CORREGIDOS
    assert gestor.buscar_por_palabra("suma") is not None  # ← CORREGIDO
    assert gestor.buscar_por_palabra("resta") is not None  # ← CORREGIDO
    assert gestor.buscar_por_palabra("entero") is not None  # ← CORREGIDO (antes "número")
    assert gestor.buscar_por_palabra("potencia") is not None

def test_conversacion_expandida(gestor):
    """Test: Conceptos de conversación expandida presentes."""
    # Conversación expandida (30 conceptos)
    assert gestor.buscar_por_palabra("ahora") is not None
    assert gestor.buscar_por_palabra("después") is not None
    assert gestor.buscar_por_palabra("mucho") is not None
    assert gestor.buscar_por_palabra("poco") is not None

def test_grounding_mantiene_calidad(gestor):
    """Test: Grounding promedio se mantiene >= 0.70."""
    stats = gestor.estadisticas()
    
    assert stats['grounding_promedio'] >= 0.70, \
        f"Grounding: {stats['grounding_promedio']}"

def test_sin_duplicados(gestor):
    """Test: No debe haber IDs duplicados después de correcciones."""
    conceptos = gestor.obtener_todos()
    ids = [c.id for c in conceptos]
    
    # Identificar duplicados si existen
    if len(ids) != len(set(ids)):
        duplicados = [id for id in set(ids) if ids.count(id) > 1]
        pytest.fail(f"IDs duplicados encontrados: {duplicados}")
    
    assert len(ids) == len(set(ids)), "Hay IDs duplicados"

if __name__ == '__main__':
    pytest.main([__file__, '-v'])