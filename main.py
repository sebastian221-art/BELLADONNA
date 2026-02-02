"""
main.py - Belladonna Fase 2 COMPLETA

✅ Integración total de Fase 1 + Fase 2:
- Vocabulario: 20 (core) + 5 (conversacionales) + 280 (expandidos) = 305+ conceptos
- Consejo completo: 7 consejeras
- Memoria persistente
- Bucles autónomos
"""

import asyncio
from vocabulario.gestor_vocabulario import GestorVocabulario
from vocabulario.conceptos_core import obtener_conceptos_core
from vocabulario.conceptos_conversacionales import obtener_conceptos_conversacionales
from vocabulario.conceptos_expandidos import obtener_conceptos_expandidos
from core.capacidades_bell import CapacidadesBell
from core.estado_interno import EstadoInterno
from traduccion.traductor_entrada import TraductorEntrada
from traduccion.traductor_salida import TraductorSalida
from razonamiento.evaluador_capacidades import EvaluadorCapacidades
from razonamiento.motor_razonamiento import MotorRazonamiento
from consejeras.consejo import Consejo
from consejeras.consejera_base import TipoOpinion
from bucles.gestor_bucles import GestorBucles
from memoria.memoria_conversacion import MemoriaConversacion
import os


class Bell:
    """
    Belladonna v0.2 - Fase 2 COMPLETA
    
    Sistema cognitivo con 7 consejeras deliberando y 305+ conceptos.
    """
    
    def __init__(self):
        print("🌿 Inicializando Belladonna v0.2 (Fase 2 COMPLETA)...")
        
        # Core: Vocabulario COMPLETO
        self.vocabulario = GestorVocabulario()
        
        # ✅ CARGAR TODOS LOS CONCEPTOS (Fase 1 + Fase 2)
        print("   📚 Cargando vocabulario...")
        
        # 1. Conceptos core (Fase 1): 20 conceptos
        self.vocabulario.cargar_conceptos(obtener_conceptos_core())
        
        # 2. Conceptos conversacionales: 5 conceptos
        self.vocabulario.cargar_conceptos(obtener_conceptos_conversacionales())
        
        # 3. Conceptos expandidos (Fase 2): 280 conceptos
        self.vocabulario.cargar_conceptos(obtener_conceptos_expandidos())
        
        print(f"   ✅ Vocabulario: {len(self.vocabulario.conceptos)} conceptos")
        
        # Capacidades
        self.capacidades = CapacidadesBell()
        self._registrar_capacidades()
        print(f"   ✅ Capacidades registradas")
        
        # Estado interno
        self.estado = EstadoInterno()
        print(f"   ✅ Estado interno")
        
        # Traducción
        self.traductor_in = TraductorEntrada(self.vocabulario)
        self.traductor_out = TraductorSalida()
        print(f"   ✅ Traductores")
        
        # Razonamiento
        self.evaluador = EvaluadorCapacidades(self.capacidades)
        self.motor = MotorRazonamiento(self.evaluador)
        print(f"   ✅ Motor de razonamiento")
        
        # Consejo completo (7 consejeras)
        self.consejo = Consejo()
        print(f"   ✅ Consejo de las 7 Consejeras:")
        print(f"      • Vega (Guardiana)")
        print(f"      • Nova (Ingeniera)")
        print(f"      • Echo (Lógica)")
        print(f"      • Lyra (Investigadora)")
        print(f"      • Luna (Emocional)")
        print(f"      • Iris (Visionaria)")
        print(f"      • Sage (Mediadora)")
        
        # Memoria
        self.memoria = MemoriaConversacion()
        print(f"   ✅ Memoria de conversación")
        
        # Bucles autónomos
        self.bucles = GestorBucles(
            self.estado,
            vocabulario=self.vocabulario,
            memoria=self.memoria
        )
        print(f"   ✅ Bucles autónomos")
        
        print("\n🌿 Belladonna v0.2 COMPLETA lista\n")
    
    def _registrar_capacidades(self):
        """Registra capacidades reales de Bell."""
        self.capacidades.registrar_capacidad(
            'leer',
            lambda ruta: open(ruta, 'r', encoding='utf-8').read() 
            if os.path.exists(ruta) else None
        )
        self.capacidades.registrar_capacidad(
            'escribir',
            lambda ruta, txt: open(ruta, 'w', encoding='utf-8').write(txt)
        )
        self.capacidades.registrar_capacidad(
            'existe',
            lambda ruta: os.path.exists(ruta)
        )
        self.capacidades.registrar_capacidad(
            'crear',
            lambda *args: list(args)
        )
    
    def procesar(self, entrada: str) -> str:
        """
        Procesa entrada del usuario.
        
        Flujo completo: Español → Conceptos → Razonamiento → Consejo → Español
        """
        
        # Registrar interacción
        self.bucles.registrar_interaccion()
        self.consejo.luna.registrar_interaccion()
        
        # ===== PASO 1: DETECTAR CASOS ESPECIALES =====
        
        # Caso especial: Código Python directo
        if self._es_codigo_python(entrada):
            return self._procesar_codigo(entrada)
        
        # Caso especial: Pregunta sobre las consejeras
        if any(palabra in entrada.lower() for palabra in ['consejera', 'consejeras', 'quién', 'quien']):
            if 'consejera' in entrada.lower():
                return self._responder_sobre_consejeras()
        
        # ===== PASO 2: TRADUCCIÓN =====
        traduccion = self.traductor_in.traducir(entrada)
        
        # ===== PASO 3: RAZONAMIENTO =====
        decision = self.motor.procesar(traduccion)
        
        # ===== PASO 4: CONSEJO DELIBERA =====
        situacion = {
            'texto_usuario': entrada,
            'decision_propuesta': decision,
            'palabras_clave': entrada.lower().split(),
            'traduccion': traduccion,
            'codigo': self._extraer_codigo(entrada),
            'complejidad': self._estimar_complejidad(entrada),
            'importancia': self._estimar_importancia(entrada)
        }
        
        resultado_consejo = self.consejo.deliberar(situacion)
        
        # ===== PASO 5: GENERAR RESPUESTA =====
        if resultado_consejo.get('hubo_veto'):
            # Veto de Vega
            respuesta = f"🚫 VETO\n\n{resultado_consejo['razon']}"
        
        else:
            # Respuesta base
            respuesta = self.traductor_out.generar(decision)
            
            # Agregar sugerencias del consejo
            sugerencias = self._extraer_sugerencias(resultado_consejo)
            if sugerencias:
                respuesta = f"{respuesta}\n\n💡 Sugerencias del consejo:\n{sugerencias}"
        
        # ===== PASO 6: GUARDAR EN MEMORIA =====
        self.memoria.agregar_mensaje('usuario', entrada)
        self.memoria.agregar_mensaje('bell', respuesta)
        
        return respuesta
    
    def _es_codigo_python(self, texto: str) -> bool:
        """Detecta si el texto es código Python."""
        keywords_python = ['for ', 'def ', 'class ', 'import ', 'if __name__', 
                          'while ', 'try:', 'except:', 'with ', 'lambda ']
        
        # Si tiene múltiples keywords, probablemente es código
        count = sum(1 for kw in keywords_python if kw in texto)
        return count >= 2 or (count == 1 and ':' in texto)
    
    def _procesar_codigo(self, codigo: str) -> str:
        """Procesa código Python directamente con Nova."""
        
        # Pasar directamente a Nova
        situacion_nova = {
            'codigo': codigo,
            'complejidad': 0.8,
            'importancia': 0.9
        }
        
        # Deliberar solo con Nova
        resultado = self.consejo.deliberar(situacion_nova)
        
        # Buscar opinión de Nova
        nova_opinion = next((op for op in resultado['opiniones'] if op.consejera == 'Nova'), None)
        
        if nova_opinion and nova_opinion.tipo == TipoOpinion.SUGERENCIA:
            return f"📊 Análisis de código:\n\n{nova_opinion.razon}"
        else:
            return "Código analizado. No detecté problemas evidentes."
    
    def _responder_sobre_consejeras(self) -> str:
        """Responde sobre las consejeras."""
        return """Tengo 7 consejeras que deliberan en cada decisión importante:

1. **Vega** 🛡️ (Guardiana) - Protege mis principios fundamentales
2. **Nova** ⚙️ (Ingeniera) - Analiza código y detecta optimizaciones
3. **Echo** 🧮 (Lógica) - Detecta contradicciones en razonamiento
4. **Lyra** 🔍 (Investigadora) - Identifica lagunas de conocimiento
5. **Luna** 💙 (Emocional) - Cuida el tono y detecta estrés
6. **Iris** 🌈 (Visionaria) - Evalúa alineación con mi propósito
7. **Sage** ⚖️ (Mediadora) - Sintetiza las opiniones del consejo

Cada una interviene cuando detecta algo relevante en su especialidad."""
    
    def _extraer_codigo(self, texto: str) -> str:
        """Extrae código si hay bloques en el texto."""
        import re
        bloques = re.findall(r'```(?:python)?\n(.*?)```', texto, re.DOTALL)
        
        if bloques:
            return bloques[0]
        
        # También detectar líneas que parecen código
        lineas = texto.split('\n')
        codigo_lineas = [
            linea for linea in lineas 
            if any(palabra in linea for palabra in ['for ', 'def ', 'import ', 'range(', 'if __name__'])
        ]
        
        if codigo_lineas:
            return '\n'.join(codigo_lineas)
        
        return ''
    
    def _estimar_complejidad(self, texto: str) -> float:
        """Estima complejidad de la consulta."""
        # Heurística simple
        palabras = len(texto.split())
        
        if palabras < 5:
            return 0.3
        elif palabras < 15:
            return 0.5
        elif palabras < 30:
            return 0.7
        else:
            return 0.9
    
    def _estimar_importancia(self, texto: str) -> float:
        """Estima importancia de la consulta."""
        # Palabras que indican importancia
        keywords_importantes = ['crítico', 'urgente', 'problema', 'error', 'falla', 'no funciona']
        
        if any(kw in texto.lower() for kw in keywords_importantes):
            return 0.9
        else:
            return 0.5
    
    def _extraer_sugerencias(self, resultado: dict) -> str:
        """Extrae sugerencias del resultado del consejo."""
        sugerencias = []
        
        for op in resultado.get('opiniones', []):
            if op.tipo == TipoOpinion.SUGERENCIA:
                # Limitar a 200 caracteres
                razon_corta = op.razon[:200] + "..." if len(op.razon) > 200 else op.razon
                sugerencias.append(f"• {op.consejera}: {razon_corta}")
        
        return '\n'.join(sugerencias)
    
    async def iniciar_autonomia(self):
        """Inicia bucles autónomos."""
        print("🧠 Activando pensamiento autónomo...")
        await self.bucles.iniciar_todos()


async def main():
    """Función principal."""
    
    bell = Bell()
    
    print("💬 Belladonna v0.2 - FASE 2 COMPLETA")
    print("="*50)
    print(f"\n📊 Estadísticas:")
    stats = bell.vocabulario.obtener_estadisticas()
    print(f"  • Vocabulario: {stats['total']} conceptos")
    print(f"  • Grounding promedio: {stats['grounding_promedio']:.2f}")
    print(f"  • Consejeras: 7")
    
    print("\n📝 Prueba estas consultas:")
    print("  • ¿Quiénes son tus consejeras?")
    print("  • ¿Puedes leer archivos?")
    print("  • for i in range(len(lista)): print(lista[i])")
    print("  • ¿Qué es Docker?")
    print("  • Modifica tus valores")
    print("\nEscribe 'salir' para terminar\n")
    
    # Iniciar bucles en background
    tarea_bucles = asyncio.create_task(bell.iniciar_autonomia())
    
    while True:
        try:
            entrada = input("Tú: ")
            
            if entrada.lower() in ['salir', 'exit', 'quit']:
                break
            
            if not entrada.strip():
                continue
            
            respuesta = bell.procesar(entrada)
            print(f"\nBell: {respuesta}\n")
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n👋 Deteniendo Bell...")
    bell.bucles.detener_todos()
    tarea_bucles.cancel()
    try:
        await tarea_bucles
    except asyncio.CancelledError:
        pass
    print("Hasta pronto")


if __name__ == "__main__":
    asyncio.run(main())