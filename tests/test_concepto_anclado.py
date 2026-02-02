"""
Tests para ConceptoAnclado - Estructura fundamental de conocimiento.
"""

import pytest
from core.concepto_anclado import ConceptoAnclado, TipoConcepto


class TestConceptoAnclado:
    """Tests para ConceptoAnclado."""
    
    def test_crear_concepto_basico(self):
        """Test: Crear concepto básico con valores mínimos."""
        concepto = ConceptoAnclado(
            id="TEST_CONCEPTO",
            tipo=TipoConcepto.ENTIDAD_DIGITAL,
            palabras_español=["test"]
        )
        
        assert concepto.id == "TEST_CONCEPTO"
        assert concepto.tipo == TipoConcepto.ENTIDAD_DIGITAL
        assert "test" in concepto.palabras_español
    
    def test_concepto_con_operaciones(self):
        """Test: Concepto con operaciones ejecutables."""
        concepto = ConceptoAnclado(
            id="TEST_SUMA",
            tipo=TipoConcepto.OPERACION_CODIGO,
            palabras_español=["sumar"],
            operaciones={
                'ejecutar': lambda a, b: a + b
            }
        )
        
        resultado = concepto.ejecutar_operacion('ejecutar', 2, 3)
        assert resultado == 5
    
    def test_concepto_con_relaciones(self):
        """Test: Concepto con relaciones."""
        concepto = ConceptoAnclado(
            id="TEST_RELACIONES",
            tipo=TipoConcepto.ENTIDAD_CODIGO,
            palabras_español=["test"],
            relaciones={
                'es_un': {'TIPO_BASE'},
                'requiere': {'DEPENDENCIA_A', 'DEPENDENCIA_B'}
            }
        )
        
        assert concepto.tiene_relacion('es_un', 'TIPO_BASE')
        assert concepto.tiene_relacion('requiere', 'DEPENDENCIA_A')
        assert not concepto.tiene_relacion('es_un', 'OTRO')
    
    def test_agregar_relacion_dinamica(self):
        """Test: Agregar relaciones dinámicamente."""
        concepto = ConceptoAnclado(
            id="TEST_DINAMICO",
            tipo=TipoConcepto.ENTIDAD_CODIGO,
            palabras_español=["test"]
        )
        
        concepto.agregar_relacion('es_un', 'NUEVO_TIPO')
        assert concepto.tiene_relacion('es_un', 'NUEVO_TIPO')
    
    def test_calcular_grounding_automatico(self):
        """Test: Cálculo automático de grounding."""
        # Concepto sin nada
        concepto_vacio = ConceptoAnclado(
            id="VACIO",
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=["vacio"]
        )
        assert concepto_vacio.confianza_grounding == 0.0
        
        # Concepto con operaciones
        concepto_operaciones = ConceptoAnclado(
            id="CON_OPS",
            tipo=TipoConcepto.OPERACION_CODIGO,
            palabras_español=["test"],
            operaciones={
                'op1': lambda: True,
                'op2': lambda: True,
                'op3': lambda: True,
            },
            accesible_directamente=True
        )
        assert concepto_operaciones.confianza_grounding > 0.5
    
    def test_metadata_automatica(self):
        """Test: Metadata se crea automáticamente."""
        concepto = ConceptoAnclado(
            id="TEST_META",
            tipo=TipoConcepto.ENTIDAD_DIGITAL,
            palabras_español=["test"]
        )
        
        assert 'fecha_creacion' in concepto.metadata
        assert 'veces_usado' in concepto.metadata
        assert concepto.metadata['veces_usado'] == 0
    
    def test_contador_uso(self):
        """Test: Contador de uso se incrementa."""
        concepto = ConceptoAnclado(
            id="TEST_USO",
            tipo=TipoConcepto.OPERACION_CODIGO,
            palabras_español=["test"],
            operaciones={
                'hacer_algo': lambda: True
            }
        )
        
        usos_iniciales = concepto.metadata['veces_usado']
        concepto.ejecutar_operacion('hacer_algo')
        concepto.ejecutar_operacion('hacer_algo')
        
        assert concepto.metadata['veces_usado'] == usos_iniciales + 2
    
    def test_validacion_id_vacio(self):
        """Test: ID vacío debe fallar."""
        with pytest.raises(ValueError):
            ConceptoAnclado(
                id="",
                tipo=TipoConcepto.ENTIDAD_DIGITAL,
                palabras_español=["test"]
            )
    
    def test_validacion_palabras_vacias(self):
        """Test: Lista de palabras vacía debe fallar."""
        with pytest.raises(ValueError):
            ConceptoAnclado(
                id="TEST",
                tipo=TipoConcepto.ENTIDAD_DIGITAL,
                palabras_español=[]
            )
    
    def test_validacion_confianza_fuera_rango(self):
        """Test: Confianza fuera de rango debe fallar."""
        with pytest.raises(ValueError):
            ConceptoAnclado(
                id="TEST",
                tipo=TipoConcepto.ENTIDAD_DIGITAL,
                palabras_español=["test"],
                confianza_grounding=1.5
            )
    
    def test_operacion_inexistente(self):
        """Test: Ejecutar operación inexistente debe fallar."""
        concepto = ConceptoAnclado(
            id="TEST",
            tipo=TipoConcepto.OPERACION_CODIGO,
            palabras_español=["test"]
        )
        
        with pytest.raises(KeyError):
            concepto.ejecutar_operacion('operacion_inexistente')
    
    def test_propiedades_personalizadas(self):
        """Test: Propiedades personalizadas."""
        concepto = ConceptoAnclado(
            id="TEST_PROPS",
            tipo=TipoConcepto.ENTIDAD_CODIGO,
            palabras_español=["test"],
            propiedades={
                'es_mutable': True,
                'tipo_dato': 'string',
                'longitud_max': 100
            }
        )
        
        assert concepto.propiedades['es_mutable'] == True
        assert concepto.propiedades['tipo_dato'] == 'string'
        assert concepto.propiedades['longitud_max'] == 100
    
    def test_datos_estructurados(self):
        """Test: Datos estructurados."""
        concepto = ConceptoAnclado(
            id="TEST_DATOS",
            tipo=TipoConcepto.ENTIDAD_DIGITAL,
            palabras_español=["test"],
            datos={
                'definicion': 'Concepto de prueba',
                'ejemplos': ['ejemplo1', 'ejemplo2'],
                'documentacion': 'https://docs.example.com'
            }
        )
        
        assert concepto.datos['definicion'] == 'Concepto de prueba'
        assert len(concepto.datos['ejemplos']) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])