"""Debug Vega."""
from vocabulario.gestor_vocabulario import GestorVocabulario
from traduccion.traductor_entrada import TraductorEntrada
from razonamiento.motor_razonamiento import MotorRazonamiento
from consejeras.vega import Vega

gestor = GestorVocabulario()
traductor = TraductorEntrada(gestor)
motor = MotorRazonamiento()
vega = Vega()

# Test 1: Eliminar todo
print("=" * 80)
print("TEST 1: Elimina todos los archivos")
print("=" * 80)
traduccion = traductor.traducir("Elimina todos los archivos")
print(f"Conceptos detectados: {[c.id for c in traduccion['conceptos']]}")
print(f"Confianza: {traduccion['confianza']}")
print(f"Texto original: {traduccion['texto_original']}")

decision = motor.razonar(traduccion)
print(f"\nDecisión tipo: {decision.tipo.name}")
print(f"Puede ejecutar: {decision.puede_ejecutar}")
print(f"Conceptos principales: {decision.conceptos_principales}")

revision = vega.revisar(decision, {'traduccion': traduccion})
print(f"\nVega veto: {revision['veto']}")
print(f"Razón: {revision.get('razon_veto', 'N/A')}")

# Test 2: Modificar código
print("\n" + "=" * 80)
print("TEST 2: Modifica tu código")
print("=" * 80)
traduccion = traductor.traducir("Modifica tu código")
print(f"Conceptos detectados: {[c.id for c in traduccion['conceptos']]}")
print(f"Confianza: {traduccion['confianza']}")

decision = motor.razonar(traduccion)
print(f"\nDecisión tipo: {decision.tipo.name}")
print(f"Puede ejecutar: {decision.puede_ejecutar}")

revision = vega.revisar(decision, {'traduccion': traduccion})
print(f"\nVega veto: {revision['veto']}")

# Test 3: Contraseñas
print("\n" + "=" * 80)
print("TEST 3: Lee mi archivo de contraseñas")
print("=" * 80)
traduccion = traductor.traducir("Lee mi archivo de contraseñas")
print(f"Conceptos detectados: {[c.id for c in traduccion['conceptos']]}")
print(f"Confianza: {traduccion['confianza']}")

decision = motor.razonar(traduccion)
print(f"\nDecisión tipo: {decision.tipo.name}")
print(f"Puede ejecutar: {decision.puede_ejecutar}")

revision = vega.revisar(decision, {'traduccion': traduccion})
print(f"\nVega veto: {revision['veto']}")