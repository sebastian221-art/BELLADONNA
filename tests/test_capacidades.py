"""
Tests para CapacidadesBell - Registro de capacidades ejecutables.
"""

import pytest
from core.capacidades_bell import CapacidadesBell


class TestCapacidadesBell:
    """Tests para CapacidadesBell."""
    
    def test_crear_registro_vacio(self):
        """Test: Crear registro vacío."""
        capacidades = CapacidadesBell()
        assert len(capacidades.listar_capacidades()) == 0
    
    def test_registrar_capacidad_simple(self):
        """Test: Registrar capacidad simple."""
        capacidades = CapacidadesBell()
        
        def sumar(a, b):
            return a + b
        
        capacidades.registrar_capacidad('sumar', sumar)
        
        assert capacidades.tiene_capacidad('sumar')
        assert 'sumar' in capacidades.listar_capacidades()
    
    def test_ejecutar_capacidad(self):
        """Test: Ejecutar capacidad registrada."""
        capacidades = CapacidadesBell()
        
        capacidades.registrar_capacidad(
            'multiplicar',
            lambda a, b: a * b
        )
        
        resultado = capacidades.ejecutar_capacidad('multiplicar', 3, 4)
        assert resultado == 12
    
    def test_ejecutar_capacidad_sin_args(self):
        """Test: Ejecutar capacidad sin argumentos."""
        capacidades = CapacidadesBell()
        
        capacidades.registrar_capacidad(
            'obtener_pi',
            lambda: 3.14159
        )
        
        resultado = capacidades.ejecutar_capacidad('obtener_pi')
        assert resultado == 3.14159
    
    def test_ejecutar_capacidad_con_kwargs(self):
        """Test: Ejecutar capacidad con kwargs."""
        capacidades = CapacidadesBell()
        
        def crear_persona(nombre, edad=0):
            return {'nombre': nombre, 'edad': edad}
        
        capacidades.registrar_capacidad('crear_persona', crear_persona)
        
        resultado = capacidades.ejecutar_capacidad('crear_persona', 'Bell', edad=1)
        assert resultado['nombre'] == 'Bell'
        assert resultado['edad'] == 1
    
    def test_capacidad_inexistente(self):
        """Test: Ejecutar capacidad inexistente debe fallar."""
        capacidades = CapacidadesBell()
        
        with pytest.raises(KeyError):
            capacidades.ejecutar_capacidad('volar')
    
    def test_verificar_capacidad_existente(self):
        """Test: Verificar existencia de capacidad."""
        capacidades = CapacidadesBell()
        
        capacidades.registrar_capacidad('leer', lambda x: x)
        
        assert capacidades.tiene_capacidad('leer')
        assert not capacidades.tiene_capacidad('escribir')
    
    def test_sobrescribir_capacidad(self):
        """Test: Sobrescribir capacidad existente."""
        capacidades = CapacidadesBell()
        
        capacidades.registrar_capacidad('test', lambda: 1)
        capacidades.registrar_capacidad('test', lambda: 2)
        
        resultado = capacidades.ejecutar_capacidad('test')
        assert resultado == 2
    
    def test_listar_multiples_capacidades(self):
        """Test: Listar múltiples capacidades."""
        capacidades = CapacidadesBell()
        
        capacidades.registrar_capacidad('leer', lambda: None)
        capacidades.registrar_capacidad('escribir', lambda: None)
        capacidades.registrar_capacidad('ejecutar', lambda: None)
        
        lista = capacidades.listar_capacidades()
        assert len(lista) == 3
        assert 'leer' in lista
        assert 'escribir' in lista
        assert 'ejecutar' in lista
    
    def test_capacidad_con_estado(self):
        """Test: Capacidad que mantiene estado."""
        capacidades = CapacidadesBell()
        
        contador = {'valor': 0}
        
        def incrementar():
            contador['valor'] += 1
            return contador['valor']
        
        capacidades.registrar_capacidad('incrementar', incrementar)
        
        assert capacidades.ejecutar_capacidad('incrementar') == 1
        assert capacidades.ejecutar_capacidad('incrementar') == 2
        assert capacidades.ejecutar_capacidad('incrementar') == 3
    
    def test_repr(self):
        """Test: Representación en string."""
        capacidades = CapacidadesBell()
        
        capacidades.registrar_capacidad('test1', lambda: None)
        capacidades.registrar_capacidad('test2', lambda: None)
        
        repr_str = repr(capacidades)
        assert 'CapacidadesBell' in repr_str
        assert '2' in repr_str


if __name__ == "__main__":
    pytest.main([__file__, "-v"])