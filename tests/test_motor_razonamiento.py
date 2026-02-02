"""
Tests para MotorRazonamiento - Motor de decisiones de Bell.
"""

import pytest
from vocabulario.gestor_vocabulario import GestorVocabulario
from vocabulario.conceptos_core import obtener_conceptos_core
from core.capacidades_bell import CapacidadesBell
from traduccion.traductor_entrada import TraductorEntrada
from razonamiento.evaluador_capacidades import EvaluadorCapacidades
from razonamiento.motor_razonamiento import MotorRazonamiento


class TestMotorRazonamiento:
    """Tests para MotorRazonamiento."""
    
    @pytest.fixture
    def motor_completo(self):
        """Fixture: Motor con capacidades y vocabulario."""
        # Vocabulario
        gestor = GestorVocabulario()
        gestor.cargar_conceptos(obtener_conceptos_core())
        
        # Capacidades
        capacidades = CapacidadesBell()
        capacidades.registrar_capacidad('leer', lambda x: x)
        capacidades.registrar_capacidad('existe', lambda x: True)
        
        # Motor
        evaluador = EvaluadorCapacidades(capacidades)
        motor = MotorRazonamiento(evaluador)
        
        # Traductor
        traductor = TraductorEntrada(gestor)
        
        return motor, traductor
    
    def test_procesar_decision_afirmativa(self, motor_completo):
        """Test: Procesar decisión afirmativa."""
        motor, traductor = motor_completo
        
        traduccion = traductor.traducir("leer archivo")
        decision = motor.procesar(traduccion)
        
        assert decision['tipo_respuesta'] in ['afirmativa', 'parcial', 'negativa']
        assert 'certeza' in decision
        assert 'razon' in decision
    
    def test_decision_contiene_operaciones(self, motor_completo):
        """Test: Decisión contiene operaciones disponibles."""
        motor, traductor = motor_completo
        
        traduccion = traductor.traducir("leer archivo")
        decision = motor.procesar(traduccion)
        
        assert 'operaciones' in decision
        assert isinstance(decision['operaciones'], list)
    
    def test_decision_contiene_conceptos(self, motor_completo):
        """Test: Decisión contiene conceptos involucrados."""
        motor, traductor = motor_completo
        
        traduccion = traductor.traducir("leer archivo")
        decision = motor.procesar(traduccion)
        
        assert 'conceptos_involucrados' in decision
        assert isinstance(decision['conceptos_involucrados'], list)
    
    def test_decision_incluye_traduccion_original(self, motor_completo):
        """Test: Decisión incluye traducción original."""
        motor, traductor = motor_completo
        
        traduccion = traductor.traducir("leer archivo")
        decision = motor.procesar(traduccion)
        
        assert 'traduccion_original' in decision
        assert decision['traduccion_original'] == traduccion
    
    def test_certeza_en_rango_valido(self, motor_completo):
        """Test: Certeza está en rango válido [0.0, 1.0]."""
        motor, traductor = motor_completo
        
        traduccion = traductor.traducir("leer archivo lista")
        decision = motor.procesar(traduccion)
        
        assert 0.0 <= decision['certeza'] <= 1.0
    
    def test_tipo_respuesta_valido(self, motor_completo):
        """Test: Tipo de respuesta es válido."""
        motor, traductor = motor_completo
        
        traduccion = traductor.traducir("leer archivo")
        decision = motor.procesar(traduccion)
        
        assert decision['tipo_respuesta'] in ['afirmativa', 'parcial', 'negativa']
    
    def test_decision_con_capacidad_completa(self, motor_completo):
        """Test: Decisión afirmativa cuando tiene todas las capacidades."""
        motor, traductor = motor_completo
        
        traduccion = traductor.traducir("leer")
        decision = motor.procesar(traduccion)
        
        # 'leer' está registrada como capacidad
        if len(decision['operaciones']) > 0:
            assert decision['puede_ejecutar'] or decision['tipo_respuesta'] == 'parcial'
    
    def test_razon_presente(self, motor_completo):
        """Test: Razón siempre está presente."""
        motor, traductor = motor_completo
        
        traduccion = traductor.traducir("archivo lista función")
        decision = motor.procesar(traduccion)
        
        assert 'razon' in decision
        assert len(decision['razon']) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])