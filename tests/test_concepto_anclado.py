"""
Tests para ConceptoAnclado.
"""
import pytest
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def test_creacion_concepto_basico():
    """Test: Crear concepto con datos mínimos."""
    concepto = ConceptoAnclado(
        id="CONCEPTO_TEST",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["test"]
    )
    
    assert concepto.id == "CONCEPTO_TEST"
    assert concepto.tipo == TipoConcepto.OPERACION_SISTEMA
    assert concepto.confianza_grounding == 0.0
    print("✅ Test 1 pasó")

def test_validacion_id_invalido():
    """Test: ID debe empezar con CONCEPTO_."""
    with pytest.raises(ValueError):
        ConceptoAnclado(
            id="TEST_INVALIDO",
            tipo=TipoConcepto.OPERACION_SISTEMA,
            palabras_español=["test"]
        )
    print("✅ Test 2 pasó")

def test_ejecucion_operacion():
    """Test: Ejecutar operación disponible."""
    concepto = ConceptoAnclado(
        id="CONCEPTO_SUMAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["sumar"],
        operaciones={
            'ejecutar': lambda a, b: a + b
        },
        accesible_directamente=True,
        confianza_grounding=1.0
    )
    
    resultado = concepto.ejecutar('ejecutar', 2, 3)
    assert resultado == 5
    assert concepto.metadata['veces_usado'] == 1
    print("✅ Test 3 pasó")

if __name__ == '__main__':
    pytest.main([__file__, '-v'])