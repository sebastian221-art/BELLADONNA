"""
Tests para GestorVocabulario - Gestión de conceptos anclados.
"""

import pytest
from vocabulario.gestor_vocabulario import GestorVocabulario
from vocabulario.conceptos_core import obtener_conceptos_core
from core.concepto_anclado import ConceptoAnclado, TipoConcepto


class TestGestorVocabulario:
    """Tests para GestorVocabulario."""
    
    def test_crear_gestor_vacio(self):
        """Test: Crear gestor vacío."""
        gestor = GestorVocabulario()
        assert len(gestor.conceptos) == 0
    
    def test_cargar_conceptos_core(self):
        """Test: Cargar conceptos core (20 conceptos)."""
        gestor = GestorVocabulario()
        conceptos_core = obtener_conceptos_core()
        
        gestor.cargar_conceptos(conceptos_core)
        
        assert len(gestor.conceptos) == 20
    
    def test_agregar_concepto_individual(self):
        """Test: Agregar concepto individualmente."""
        gestor = GestorVocabulario()
        
        concepto = ConceptoAnclado(
            id="TEST_CONCEPTO",
            tipo=TipoConcepto.ENTIDAD_DIGITAL,
            palabras_español=["test"]
        )
        
        gestor.agregar_concepto(concepto)
        
        assert "TEST_CONCEPTO" in gestor.conceptos
        assert len(gestor.conceptos) == 1
    
    def test_obtener_concepto_por_palabra(self):
        """Test: Obtener concepto por palabra en español."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        concepto = gestor.obtener_concepto("archivo")
        
        assert concepto is not None
        assert concepto.id == "CONCEPTO_ARCHIVO"
    
    def test_obtener_concepto_case_insensitive(self):
        """Test: Búsqueda no distingue mayúsculas/minúsculas."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        concepto1 = gestor.obtener_concepto("ARCHIVO")
        concepto2 = gestor.obtener_concepto("archivo")
        concepto3 = gestor.obtener_concepto("Archivo")
        
        assert concepto1 == concepto2 == concepto3
    
    def test_obtener_concepto_inexistente(self):
        """Test: Buscar concepto inexistente retorna None."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        concepto = gestor.obtener_concepto("volador")
        
        assert concepto is None
    
    def test_listar_conceptos(self):
        """Test: Listar IDs de conceptos."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        lista = gestor.listar_conceptos()
        
        assert len(lista) == 20
        assert "CONCEPTO_ARCHIVO" in lista
        assert "CONCEPTO_FUNCION" in lista
    
    def test_calcular_grounding_promedio(self):
        """Test: Calcular grounding promedio."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        promedio = gestor.calcular_grounding_promedio()
        
        assert 0.0 <= promedio <= 1.0
        assert promedio > 0.8  # Conceptos core deben tener alto grounding
    
    def test_grounding_promedio_gestor_vacio(self):
        """Test: Grounding promedio de gestor vacío es 0."""
        gestor = GestorVocabulario()
        
        promedio = gestor.calcular_grounding_promedio()
        
        assert promedio == 0.0
    
    def test_obtener_estadisticas(self):
        """Test: Obtener estadísticas del vocabulario."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        stats = gestor.obtener_estadisticas()
        
        assert 'total' in stats
        assert 'grounding_promedio' in stats
        assert 'por_tipo' in stats
        
        assert stats['total'] == 20
        assert stats['grounding_promedio'] > 0.0
    
    def test_estadisticas_por_tipo(self):
        """Test: Estadísticas incluyen conteo por tipo."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        stats = gestor.obtener_estadisticas()
        por_tipo = stats['por_tipo']
        
        assert 'entidad_codigo' in por_tipo
        assert 'operacion_codigo' in por_tipo
        assert sum(por_tipo.values()) == 20
    
    def test_estadisticas_gestor_vacio(self):
        """Test: Estadísticas de gestor vacío."""
        gestor = GestorVocabulario()
        
        stats = gestor.obtener_estadisticas()
        
        assert stats['total'] == 0
        assert stats['grounding_promedio'] == 0.0
        assert stats['por_tipo'] == {}
    
    def test_concepto_con_multiples_palabras(self):
        """Test: Concepto con múltiples palabras en español."""
        gestor = GestorVocabulario()
        
        concepto = ConceptoAnclado(
            id="TEST_MULTI",
            tipo=TipoConcepto.ENTIDAD_CODIGO,
            palabras_español=["funcion", "función", "def", "método"]
        )
        
        gestor.agregar_concepto(concepto)
        
        # Todas las palabras deben encontrar el mismo concepto
        assert gestor.obtener_concepto("funcion") == concepto
        assert gestor.obtener_concepto("función") == concepto
        assert gestor.obtener_concepto("def") == concepto
        assert gestor.obtener_concepto("método") == concepto
    
    def test_repr(self):
        """Test: Representación en string."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        repr_str = repr(gestor)
        
        assert 'GestorVocabulario' in repr_str
        assert '20' in repr_str


if __name__ == "__main__":
    pytest.main([__file__, "-v"])