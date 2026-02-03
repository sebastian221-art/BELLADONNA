"""
Tests para el sistema de vocabulario modular.
"""
import pytest
from vocabulario.gestor_vocabulario import GestorVocabulario
from core.tipos import TipoConcepto

@pytest.fixture
def gestor():
    """Crea gestor de vocabulario para tests."""
    return GestorVocabulario()

def test_total_conceptos(gestor):
    """Test: Total de conceptos cargados."""
    conceptos = gestor.obtener_todos()
    # CORREGIDO: 30 (Semana 1) + 15 (Semana 2 Python) + 10 (Semana 2 Verbos) + 10 (Semana 2 Conectores) + 5 (Semana 2 Adjetivos) = 70
    assert len(conceptos) == 70, f"Esperados 70, encontrados {len(conceptos)}"

def test_estadisticas_basicas(gestor):
    """Test: Estadísticas del vocabulario."""
    stats = gestor.estadisticas()
    
    # CORREGIDO: 70 conceptos totales
    assert stats['total_conceptos'] == 70
    assert stats['grounding_promedio'] >= 0.70
    assert stats['con_operaciones'] >= 5
    assert 'por_tipo' in stats

def test_buscar_por_palabra(gestor):
    """Test: Buscar concepto por palabra."""
    # Debe encontrar
    concepto_leer = gestor.buscar_por_palabra("leer")
    assert concepto_leer is not None
    assert concepto_leer.id == "CONCEPTO_LEER"
    
    concepto_hola = gestor.buscar_por_palabra("hola")
    assert concepto_hola is not None
    assert concepto_hola.id == "CONCEPTO_HOLA"
    
    # No debe encontrar
    concepto_inexistente = gestor.buscar_por_palabra("xyz123")
    assert concepto_inexistente is None

def test_buscar_por_id(gestor):
    """Test: Buscar concepto por ID."""
    concepto = gestor.buscar_por_id("CONCEPTO_LEER")
    assert concepto is not None
    assert concepto.id == "CONCEPTO_LEER"
    
    inexistente = gestor.buscar_por_id("CONCEPTO_INEXISTENTE")
    assert inexistente is None

def test_filtrar_por_tipo(gestor):
    """Test: Filtrar conceptos por tipo."""
    operaciones = gestor.filtrar_por_tipo(TipoConcepto.OPERACION_SISTEMA)
    assert len(operaciones) >= 3  # Mínimo LEER, ESCRIBIR, EXISTE
    
    conversacion = gestor.filtrar_por_tipo(TipoConcepto.PALABRA_CONVERSACION)
    assert len(conversacion) >= 4  # Interrogativos, saludos, etc.

def test_conceptos_con_grounding_1_0(gestor):
    """Test: Conceptos con grounding perfecto."""
    stats = gestor.estadisticas()
    assert stats['grounding_1_0'] >= 5  # Las 5 operaciones

def test_todos_ids_validos(gestor):
    """Test: Todos los IDs empiezan con CONCEPTO_."""
    conceptos = gestor.obtener_todos()
    for concepto in conceptos:
        assert concepto.id.startswith("CONCEPTO_")

def test_sin_conceptos_duplicados(gestor):
    """Test: No hay conceptos duplicados."""
    conceptos = gestor.obtener_todos()
    ids = [c.id for c in conceptos]
    assert len(ids) == len(set(ids)), "Hay IDs duplicados"

if __name__ == '__main__':
    pytest.main([__file__, '-v'])