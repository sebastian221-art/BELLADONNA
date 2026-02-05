"""
Tests para Vocabulario Expandido.

Verifica la expansión con Python avanzado, Semana 3 y Semana 4.
Total esperado: 224 conceptos.
"""
import pytest
from vocabulario.gestor_vocabulario import GestorVocabulario

@pytest.fixture
def gestor():
    """Gestor con vocabulario expandido."""
    return GestorVocabulario()

def test_total_conceptos_expandido(gestor):
    """Test: Total debe ser 225 (70 + 40 + 80 + 35)."""
    conceptos = gestor.obtener_todos()
    # Semana 1+2: 70 + Python Avanzado: 40 + Semana 3: 80 + Semana 4: 35 = 225
    assert len(conceptos) == 225, f"Esperados 225, encontrados {len(conceptos)}"

def test_conceptos_python_avanzado(gestor):
    """Test: Conceptos de Python avanzado presentes."""
    # Verificar algunos conceptos avanzados
    assert gestor.buscar_por_palabra("async") is not None
    assert gestor.buscar_por_palabra("await") is not None
    assert gestor.buscar_por_palabra("yield") is not None
    assert gestor.buscar_por_palabra("lambda") is not None

def test_grounding_promedio_expandido(gestor):
    """Test: Grounding promedio se mantiene >= 0.70 con expansión."""
    stats = gestor.estadisticas()
    assert stats['grounding_promedio'] >= 0.70, \
        f"Grounding degradado: {stats['grounding_promedio']}"

def test_sin_duplicados_expandido(gestor):
    """Test: No debe haber IDs duplicados en vocabulario expandido."""
    conceptos = gestor.obtener_todos()
    ids = [c.id for c in conceptos]
    assert len(ids) == len(set(ids)), "Hay IDs duplicados"

if __name__ == '__main__':
    pytest.main([__file__, '-v'])