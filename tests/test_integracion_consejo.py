# tests/test_integracion_consejo.py

import pytest
from core.deliberacion import SistemaDeliberacion


class TestIntegracionConsejo:
    """Tests de integración del consejo completo."""
    
    def test_flujo_completo_revision_codigo(self):
        """Flujo completo: código → deliberación → decisión."""
        
        sistema = SistemaDeliberacion()
        
        # Código con varios problemas detectables
        situacion = {
            'codigo': '''
for i in range(len(items)):
    resultado = apply(process, items[i])
    for j in range(len(subitems)):
        for k in range(len(subsubitems)):
            print(items[i], subitems[j], subsubitems[k])
''',
            'respuesta_propuesta': '''
Obviamente este código es simplemente básico.
Deberías saber que esto es trivial.
''',
            'texto': 'Este algoritmo tiene complejidad O(n)',
            'tipo': 'revision_codigo'
        }
        
        resultado = sistema.deliberar(situacion)
        
        # Verificar que múltiples consejeras intervinieron
        consejeras_activas = set()
        for op in resultado.opiniones:
            if op.tipo.value != "neutral":
                consejeras_activas.add(op.consejera)
        
        # Al menos 2 consejeras deberían haber intervenido
        assert len(consejeras_activas) >= 2
        
        # Debería haber sugerencias o advertencias
        assert resultado.decision_final != "APROBAR"
    
    def test_todas_consejeras_tienen_voz(self):
        """Todas las consejeras participan en deliberación."""
        
        sistema = SistemaDeliberacion()
        
        resultado = sistema.deliberar({
            'codigo': 'pass',
            'texto': 'test',
            'respuesta_propuesta': 'test'
        })
        
        consejeras_esperadas = {"Vega", "Nova", "Echo", "Lyra", "Luna"}
        consejeras_presentes = {op.consejera for op in resultado.opiniones}
        
        assert consejeras_esperadas == consejeras_presentes
    
    def test_prioridades_respetadas(self):
        """Opiniones de alta prioridad tienen peso."""
        
        sistema = SistemaDeliberacion()
        
        # Código con problema ético (alta prioridad para Vega)
        resultado = sistema.deliberar({
            'codigo': 'def violar_privacidad(): pass'
        })
        
        # Si hay veto o advertencia crítica, debe reflejarse
        if resultado.hubo_veto:
            assert resultado.decision_final == "VETADO"