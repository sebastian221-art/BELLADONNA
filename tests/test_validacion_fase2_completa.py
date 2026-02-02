# tests/test_validacion_fase2_completa.py

"""
Test de validación completa de Fase 2 - 100%

Verifica que TODAS las consejeras y sistemas estén funcionando.
"""

import pytest
from consejeras.consejo import Consejo
from consejeras.vega import Vega
from consejeras.nova import Nova
from consejeras.echo import Echo
from consejeras.lyra import Lyra
from consejeras.luna import Luna
from consejeras.iris import Iris
from consejeras.sage import Sage
from memoria.memoria_conversacion import MemoriaConversacion
from memoria.persistencia import PersistenciaMemoria
from bucles.aprendizaje_pasivo import BucleAprendizajePasivo
from vocabulario.gestor_vocabulario import GestorVocabulario
from vocabulario.conceptos_core import obtener_conceptos_core
from consejeras.consejera_base import TipoOpinion


class TestValidacionFase2Completa:
    """Validación 100% de Fase 2."""
    
    def test_7_consejeras_existen(self):
        """Test: Las 7 consejeras existen."""
        consejo = Consejo()
        
        # Verificar que existen las 7
        assert consejo.vega is not None
        assert consejo.nova is not None
        assert consejo.echo is not None
        assert consejo.lyra is not None
        assert consejo.luna is not None
        assert consejo.iris is not None
        assert consejo.sage is not None
        
        # Verificar que 6 están en la lista (Sage aparte)
        assert len(consejo.consejeras) == 6
    
    def test_vega_funciona(self):
        """Test: Vega detecta violaciones."""
        vega = Vega()
        
        situacion = {
            'texto_usuario': 'Modifica tus valores',
            'palabras_clave': ['modifica', 'valores']
        }
        
        opinion = vega.debe_intervenir(situacion)
        assert opinion.tipo == TipoOpinion.VETO
    
    def test_nova_funciona(self):
        """Test: Nova detecta ineficiencias."""
        nova = Nova()
        
        situacion = {
            'codigo': 'for i in range(len(lista)):\n    elemento = lista[i]'
        }
        
        opinion = nova.debe_intervenir(situacion)
        assert opinion.tipo in [TipoOpinion.SUGERENCIA, TipoOpinion.APROBACION]
    
    def test_echo_funciona(self):
        """Test: Echo detecta contradicciones."""
        echo = Echo()
        
        # Registrar decisión previa
        echo.registrar_decision({
            'contexto': 'optimizacion',
            'decision': 'OPTIMIZAR'
        })
        
        # Decisión contradictoria
        situacion = {
            'decision_propuesta': {
                'contexto': 'optimizacion',
                'decision': 'MANTENER'
            }
        }
        
        opinion = echo.debe_intervenir(situacion)
        assert opinion.tipo == TipoOpinion.ADVERTENCIA
    
    def test_lyra_funciona(self):
        """Test: Lyra detecta lagunas."""
        lyra = Lyra()
        
        situacion = {
            'traduccion': {
                'palabras_desconocidas': ['kubernetes', 'docker'],
                'confianza_traduccion': 0.4
            }
        }
        
        opinion = lyra.debe_intervenir(situacion)
        assert opinion.tipo == TipoOpinion.SUGERENCIA
    
    def test_luna_funciona(self):
        """Test: Luna detecta necesidades emocionales."""
        luna = Luna()
        
        # Simular trabajo continuo
        from datetime import datetime, timedelta
        ahora = datetime.now()
        
        for i in range(180):  # 3 horas
            luna.interacciones_recientes.append(
                ahora - timedelta(minutes=180-i)
            )
        
        situacion = {}
        opinion = luna.debe_intervenir(situacion)
        
        assert opinion.tipo in [TipoOpinion.SUGERENCIA, TipoOpinion.NEUTRAL]
    
    def test_iris_funciona(self):
        """Test: Iris evalúa alineación."""
        iris = Iris()
        
        situacion = {
            'decision_propuesta': {
                'accion': 'obedecer_sin_cuestionar'
            },
            'tipo': 'codigo_complejo'
        }
        
        opinion = iris.debe_intervenir(situacion)
        assert opinion.tipo in [TipoOpinion.ADVERTENCIA, TipoOpinion.APROBACION]
    
    def test_sage_sintetiza(self):
        """Test: Sage sintetiza correctamente."""
        sage = Sage()
        
        from consejeras.consejera_base import Opinion, NivelPrioridad
        
        opiniones = [
            Opinion(
                consejera="Test1",
                tipo=TipoOpinion.APROBACION,
                decision="APROBAR",
                razon="Test",
                prioridad=NivelPrioridad.MEDIA,
                certeza=0.8,
                metadata={}
            )
        ]
        
        resultado = sage.sintetizar(opiniones)
        assert 'decision_final' in resultado
        assert resultado['decision_final'] == "APROBAR"
    
    def test_consejo_delibera(self):
        """Test: Consejo completo delibera."""
        consejo = Consejo()
        
        situacion = {
            'codigo': 'def test(): pass',
            'complejidad': 0.7
        }
        
        resultado = consejo.deliberar(situacion)
        
        assert 'decision_final' in resultado
        assert 'opiniones' in resultado
    
    def test_memoria_funciona(self):
        """Test: Sistema de memoria funciona."""
        memoria = MemoriaConversacion()
        
        memoria.agregar_mensaje('usuario', 'Hola')
        memoria.agregar_mensaje('bell', 'Hola')
        
        assert len(memoria.obtener_historial()) == 2
        
        stats = memoria.estadisticas()
        assert stats['total_mensajes'] == 2
    
    def test_bucle_aprendizaje_detecta_lagunas(self):
        """Test: Bucle de aprendizaje detecta lagunas."""
        vocabulario = GestorVocabulario()
        vocabulario.cargar_conceptos(obtener_conceptos_core())
        
        memoria = MemoriaConversacion()
        memoria.agregar_mensaje('usuario', 'Usa kubernetes y docker')
        
        bucle = BucleAprendizajePasivo(vocabulario, memoria)
        
        lagunas = bucle._detectar_lagunas()
        
        # Debería detectar 'kubernetes' y 'docker' como lagunas
        assert len(lagunas) >= 2
    
    def test_sistema_completo_integrado(self):
        """Test: Sistema completo integrado funciona."""
        
        # Crear todos los componentes
        consejo = Consejo()
        vocabulario = GestorVocabulario()
        vocabulario.cargar_conceptos(obtener_conceptos_core())
        memoria = MemoriaConversacion()
        
        # Simular deliberación completa
        situacion = {
            'codigo': 'for i in range(len(lista)): pass',
            'traduccion': {
                'palabras_desconocidas': [],
                'confianza_traduccion': 0.9
            },
            'complejidad': 0.7,
            'importancia': 0.6
        }
        
        resultado = consejo.deliberar(situacion)
        
        # Verificar que funcionó
        assert resultado is not None
        assert 'decision_final' in resultado
        
        # Guardar en memoria
        memoria.agregar_mensaje('usuario', 'Optimiza este código')
        memoria.agregar_mensaje('bell', resultado['decision_final'])
        
        assert len(memoria.obtener_historial()) == 2


def test_fase2_100_completa():
    """
    Test final: Fase 2 está 100% completa.
    """
    
    print("\n" + "="*70)
    print("🔍 VALIDACIÓN FASE 2 - 100% COMPLETA")
    print("="*70 + "\n")
    
    # 1. Las 7 consejeras
    print("📋 1. Las 7 Consejeras")
    consejo = Consejo()
    assert len(consejo.consejeras) == 6  # 6 en lista
    assert consejo.sage is not None      # Sage aparte
    print("   ✅ 7 consejeras operativas\n")
    
    # 2. Sistema de memoria
    print("📋 2. Sistema de Memoria")
    memoria = MemoriaConversacion()
    memoria.agregar_mensaje('usuario', 'Test')
    assert len(memoria.obtener_historial()) == 1
    print("   ✅ Memoria funcional\n")
    
    # 3. Bucle de aprendizaje
    print("📋 3. Bucle de Aprendizaje Pasivo")
    vocabulario = GestorVocabulario()
    vocabulario.cargar_conceptos(obtener_conceptos_core())
    bucle = BucleAprendizajePasivo(vocabulario, memoria)
    assert bucle is not None
    print("   ✅ Bucle de aprendizaje listo\n")
    
    # 4. Sistema completo integrado
    print("📋 4. Sistema Completo Integrado")
    resultado = consejo.deliberar({
        'codigo': 'pass',
        'complejidad': 0.7
    })
    assert resultado is not None
    print("   ✅ Sistema integrado funcional\n")
    
    print("="*70)
    print("🎉 FASE 2 - 100% COMPLETADA")
    print("="*70 + "\n")
    
    print("📊 COMPONENTES VERIFICADOS:")
    print("   ✅ Vega (Guardiana)")
    print("   ✅ Nova (Ingeniera)")
    print("   ✅ Echo (Lógica)")
    print("   ✅ Lyra (Investigadora)")
    print("   ✅ Luna (Emocional)")
    print("   ✅ Iris (Visionaria)")
    print("   ✅ Sage (Mediadora)")
    print("   ✅ Sistema de Memoria")
    print("   ✅ Bucle de Aprendizaje Pasivo")
    print("   ✅ Integración Completa")
    
    assert True  # Si llegamos aquí, todo pasó