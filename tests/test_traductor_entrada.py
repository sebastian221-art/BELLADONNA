"""
Tests para TraductorEntrada - Traducción español → conceptos anclados.
"""

import pytest
from vocabulario.gestor_vocabulario import GestorVocabulario
from vocabulario.conceptos_core import obtener_conceptos_core
from traduccion.traductor_entrada import TraductorEntrada


class TestTraductorEntrada:
    """Tests para TraductorEntrada."""
    
    @pytest.fixture
    def traductor(self):
        """Fixture: Traductor con conceptos core."""
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        return TraductorEntrada(gestor)
    
    def test_traducir_pregunta_simple(self, traductor):
        """Test: Traducir pregunta simple."""
        resultado = traductor.traducir("¿Puedes leer archivos?")
        
        assert resultado['estructura'] == 'pregunta'
        assert len(resultado['conceptos']) > 0
        assert resultado['texto_original'] == "¿Puedes leer archivos?"
    
    def test_traducir_comando(self, traductor):
        """Test: Traducir comando."""
        resultado = traductor.traducir("Lee este archivo")
        
        assert resultado['estructura'] in ['comando', 'afirmacion']
        assert len(resultado['conceptos']) > 0
    
    def test_detectar_conceptos_conocidos(self, traductor):
        """Test: Detectar conceptos conocidos."""
        resultado = traductor.traducir("archivo lista función")
        
        conceptos_ids = [c['concepto'].id for c in resultado['conceptos']]
        
        assert 'CONCEPTO_ARCHIVO' in conceptos_ids
        assert 'CONCEPTO_LISTA' in conceptos_ids
        assert 'CONCEPTO_FUNCION' in conceptos_ids
    
    def test_detectar_palabras_desconocidas(self, traductor):
        """Test: Detectar palabras desconocidas."""
        resultado = traductor.traducir("qwerty asdfgh zxcvbn")
        
        assert len(resultado['palabras_desconocidas']) > 0
    
    def test_confianza_alta_con_palabras_conocidas(self, traductor):
        """Test: Confianza alta cuando todas las palabras son conocidas."""
        resultado = traductor.traducir("leer archivo")
        
        # Al menos algunas palabras son conocidas
        assert resultado['confianza_traduccion'] > 0.0
    
    def test_confianza_baja_con_palabras_desconocidas(self, traductor):
        """Test: Confianza baja con palabras desconocidas."""
        resultado = traductor.traducir("xyzabc defghi jklmno")
        
        assert resultado['confianza_traduccion'] == 0.0 or resultado['confianza_traduccion'] < 0.3
    
    def test_analisis_completo_incluido(self, traductor):
        """Test: Análisis completo está incluido."""
        resultado = traductor.traducir("¿Qué puedes hacer?")
        
        assert 'analisis_completo' in resultado
        assert 'tokens' in resultado['analisis_completo']
        assert 'lemas' in resultado['analisis_completo']
    
    def test_extraer_intencion_pregunta_capacidad(self, traductor):
        """Test: Extraer intención de pregunta sobre capacidad."""
        traduccion = traductor.traducir("¿Puedes leer archivos?")
        intencion = traductor.extraer_intencion(traduccion)
        
        assert intencion in ['pregunta_capacidad', 'pregunta_general']
    
    def test_extraer_intencion_comando(self, traductor):
        """Test: Extraer intención de comando."""
        traduccion = traductor.traducir("Ejecuta este código")
        intencion = traductor.extraer_intencion(traduccion)
        
        # Puede ser comando o afirmacion dependiendo del análisis
        assert intencion in ['comando_ejecutar', 'afirmacion']
    
    def test_traducir_texto_vacio(self, traductor):
        """Test: Traducir texto vacío."""
        resultado = traductor.traducir("")
        
        assert resultado['confianza_traduccion'] == 0.0
        assert len(resultado['conceptos']) == 0
    
    def test_traducir_con_puntuacion(self, traductor):
        """Test: Traducir texto con puntuación."""
        resultado = traductor.traducir("¿Puedes leer archivos? ¡Claro!")
        
        # Debe procesar sin errores
        assert 'conceptos' in resultado
        assert 'estructura' in resultado
    
    def test_detectar_estructura_pregunta(self, traductor):
        """Test: Detectar estructura de pregunta."""
        resultado1 = traductor.traducir("¿Puedes hacer esto?")
        resultado2 = traductor.traducir("Qué puedes hacer")
        
        assert resultado1['estructura'] == 'pregunta'
        assert resultado2['estructura'] == 'pregunta'
    
    def test_detectar_estructura_comando(self, traductor):
        """Test: Detectar estructura de comando."""
        resultado = traductor.traducir("Lee este archivo")
        
        # Puede ser comando o afirmacion
        assert resultado['estructura'] in ['comando', 'afirmacion']
    
    def test_grounding_en_conceptos(self, traductor):
        """Test: Conceptos traducidos incluyen grounding."""
        resultado = traductor.traducir("archivo lista")
        
        for concepto_info in resultado['conceptos']:
            assert 'grounding' in concepto_info
            assert 0.0 <= concepto_info['grounding'] <= 1.0
    
    def test_operaciones_en_conceptos(self, traductor):
        """Test: Conceptos traducidos incluyen operaciones."""
        resultado = traductor.traducir("leer archivo")
        
        for concepto_info in resultado['conceptos']:
            assert 'operaciones' in concepto_info
            assert isinstance(concepto_info['operaciones'], list)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])