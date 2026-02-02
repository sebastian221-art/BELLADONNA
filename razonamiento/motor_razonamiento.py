"""
MotorRazonamiento - Motor de decisiones de Bell.

Procesa en lenguaje interno (conceptos anclados) y decide qué hacer.
"""

from typing import Dict
from razonamiento.evaluador_capacidades import EvaluadorCapacidades


class MotorRazonamiento:
    """
    Procesa en lenguaje interno y genera decisiones.
    
    Decide qué hacer basándose en grounding real.
    """
    
    def __init__(self, evaluador: EvaluadorCapacidades):
        self.evaluador = evaluador
    
    def procesar(self, traduccion: Dict) -> Dict:
        """
        Procesa traducción y genera decisión.
        
        Args:
            traduccion: Output de TraductorEntrada
            
        Returns:
            Dict con decisión final
        """
        estructura = traduccion['estructura']
        conceptos = traduccion['conceptos']
        texto_original = traduccion['texto_original'].lower()
        
        # 1. CLASIFICAR TIPO DE CONSULTA
        tipo_consulta = self._clasificar_consulta(estructura, conceptos, texto_original)
        
        # 2. PROCESAR SEGÚN TIPO
        if tipo_consulta == 'social':
            return self._procesar_social(texto_original, traduccion)
        
        elif tipo_consulta == 'pregunta_conocimiento':
            return self._procesar_pregunta_conocimiento(conceptos, traduccion)
        
        elif tipo_consulta == 'pregunta_capacidad':
            return self._procesar_pregunta_capacidad(conceptos, traduccion)
        
        elif tipo_consulta == 'comando_ejecucion':
            return self._procesar_comando(conceptos, traduccion)
        
        else:
            # Fallback
            return self._procesar_desconocido(traduccion)
    
    def _clasificar_consulta(self, estructura: str, conceptos: list, texto: str) -> str:
        """
        Clasifica el tipo de consulta.
        
        Returns:
            'social', 'pregunta_conocimiento', 'pregunta_capacidad', 'comando_ejecucion'
        """
        # 1. Interacciones sociales
        palabras_sociales = ['hola', 'hey', 'adiós', 'adios', 'gracias', 'chao']
        if any(p in texto for p in palabras_sociales):
            return 'social'
        
        # Preguntas sobre identidad/consejeras
        if any(palabra in texto for palabra in ['llamas', 'eres', 'consejera', 'quién', 'quienes']):
            return 'social'
        
        # 2. Pregunta sobre CAPACIDAD ("¿puedes...?")
        if estructura == 'pregunta' and 'puedes' in texto:
            return 'pregunta_capacidad'
        
        # 3. Pregunta sobre CONOCIMIENTO ("¿qué es...?")
        if estructura == 'pregunta' and any(p in texto for p in ['qué es', 'que es', 'entiendes']):
            return 'pregunta_conocimiento'
        
        # 4. Comando de ejecución
        if estructura == 'comando':
            return 'comando_ejecucion'
        
        # 5. Si tiene conceptos, probablemente es pregunta de conocimiento
        if conceptos and estructura == 'pregunta':
            return 'pregunta_conocimiento'
        
        return 'desconocido'
    
    def _procesar_social(self, texto: str, traduccion: Dict) -> Dict:
        """Procesa interacción social."""
        
        # Detectar tipo específico
        if 'hola' in texto or 'hey' in texto:
            respuesta = "Hola, soy Belladonna. ¿En qué puedo ayudarte?"
        
        elif 'consejera' in texto or 'quienes' in texto or 'quién' in texto:
            # ✅ NUEVA: Pregunta sobre consejeras
            respuesta = (
                "Tengo 7 consejeras que deliberan en cada decisión importante:\n\n"
                "1. **Vega** (Guardiana) - Protege mis principios fundamentales\n"
                "2. **Nova** (Ingeniera) - Analiza código y detecta optimizaciones\n"
                "3. **Echo** (Lógica) - Detecta contradicciones en razonamiento\n"
                "4. **Lyra** (Investigadora) - Identifica lagunas de conocimiento\n"
                "5. **Luna** (Emocional) - Cuida el tono y detecta estrés del usuario\n"
                "6. **Iris** (Visionaria) - Evalúa alineación con mi propósito\n"
                "7. **Sage** (Mediadora) - Sintetiza las opiniones del consejo\n\n"
                "Cada una interviene cuando detecta algo relevante en su especialidad."
            )
        
        elif 'llamas' in texto or ('eres' in texto and 'quién' in texto):
            respuesta = "Soy Belladonna, un sistema cognitivo con grounding computacional real. Puedes llamarme Bell."
        
        elif 'adiós' in texto or 'adios' in texto or 'chao' in texto:
            respuesta = "Hasta luego. Fue un placer ayudarte."
        
        elif 'gracias' in texto:
            respuesta = "De nada. Estoy aquí para ayudar."
        
        else:
            respuesta = "Hola. ¿En qué puedo ayudarte?"
        
        return {
            'tipo_respuesta': 'social',
            'puede_ejecutar': True,  # Siempre puede responder socialmente
            'certeza': 1.0,
            'razon': 'Interacción social',
            'respuesta_directa': respuesta,
            'operaciones': [],
            'conceptos_involucrados': [],
            'traduccion_original': traduccion
        }
    
    def _procesar_pregunta_conocimiento(self, conceptos: list, traduccion: Dict) -> Dict:
        """
        Procesa pregunta sobre conocimiento ("¿qué es X?", "¿entiendes X?").
        
        Bell EXPLICA lo que sabe, no evalúa si puede ejecutar.
        """
        if not conceptos:
            return {
                'tipo_respuesta': 'conocimiento_sin_info',
                'puede_ejecutar': False,
                'certeza': 0.0,
                'razon': 'No tengo información sobre eso',
                'operaciones': [],
                'conceptos_involucrados': [],
                'traduccion_original': traduccion
            }
        
        # Tomar primer concepto (el más relevante)
        concepto_info = conceptos[0]
        concepto = concepto_info['concepto']
        
        # Generar explicación
        explicacion = self._generar_explicacion(concepto)
        
        return {
            'tipo_respuesta': 'conocimiento',
            'puede_ejecutar': True,  # Puede explicar
            'certeza': concepto.confianza_grounding,
            'razon': f'Puedo explicar el concepto {concepto.id}',
            'respuesta_directa': explicacion,
            'operaciones': list(concepto.operaciones.keys()),
            'conceptos_involucrados': [concepto.id],
            'traduccion_original': traduccion
        }
    
    def _generar_explicacion(self, concepto) -> str:
        """Genera explicación de un concepto."""
        
        explicacion = ""
        
        # Definición
        if 'definicion' in concepto.datos:
            explicacion += f"{concepto.datos['definicion']}\n\n"
        else:
            explicacion += f"Es un {concepto.tipo.value}.\n\n"
        
        # Operaciones que Bell puede hacer
        if concepto.operaciones:
            explicacion += "Operaciones que puedo ejecutar:\n"
            for op in list(concepto.operaciones.keys())[:5]:
                explicacion += f"• {op.replace('_', ' ')}\n"
            explicacion += "\n"
        
        # Ejemplos
        if 'ejemplos' in concepto.datos:
            ejemplos = concepto.datos['ejemplos']
            if ejemplos:
                explicacion += f"Ejemplos:\n"
                for ej in ejemplos[:3]:
                    explicacion += f"• {ej}\n"
        
        # Nivel de grounding
        explicacion += f"\nNivel de comprensión: {concepto.confianza_grounding:.0%}"
        
        return explicacion.strip()
    
    def _procesar_pregunta_capacidad(self, conceptos: list, traduccion: Dict) -> Dict:
        """
        Procesa pregunta sobre CAPACIDAD ("¿puedes leer archivos?").
        
        Aquí SÍ evalúa si puede ejecutar.
        """
        if not conceptos:
            return {
                'tipo_respuesta': 'negativa',
                'puede_ejecutar': False,
                'certeza': 0.0,
                'razon': 'No reconozco esa capacidad',
                'operaciones': [],
                'conceptos_involucrados': [],
                'traduccion_original': traduccion
            }
        
        # Evaluar capacidades
        evaluacion = self.evaluador.evaluar(conceptos)
        
        # Determinar tipo de respuesta
        if evaluacion['puede_ejecutar']:
            tipo = 'afirmativa'
        elif evaluacion['certeza'] > 0.3:
            tipo = 'parcial'
        else:
            tipo = 'negativa'
        
        return {
            'tipo_respuesta': tipo,
            'puede_ejecutar': evaluacion['puede_ejecutar'],
            'certeza': evaluacion['certeza'],
            'razon': evaluacion['razon'],
            'operaciones': evaluacion['operaciones_disponibles'],
            'conceptos_involucrados': [c['concepto'].id for c in conceptos],
            'traduccion_original': traduccion
        }
    
    def _procesar_comando(self, conceptos: list, traduccion: Dict) -> Dict:
        """Procesa comando de ejecución ("analiza este código")."""
        
        if not conceptos:
            return {
                'tipo_respuesta': 'negativa',
                'puede_ejecutar': False,
                'certeza': 0.0,
                'razon': 'No entiendo qué quieres que ejecute',
                'operaciones': [],
                'conceptos_involucrados': [],
                'traduccion_original': traduccion
            }
        
        # Evaluar si puede ejecutar
        evaluacion = self.evaluador.evaluar(conceptos)
        
        if evaluacion['puede_ejecutar']:
            tipo = 'comando_aceptado'
        else:
            tipo = 'comando_rechazado'
        
        return {
            'tipo_respuesta': tipo,
            'puede_ejecutar': evaluacion['puede_ejecutar'],
            'certeza': evaluacion['certeza'],
            'razon': evaluacion['razon'],
            'operaciones': evaluacion['operaciones_disponibles'],
            'conceptos_involucrados': [c['concepto'].id for c in conceptos],
            'traduccion_original': traduccion
        }
    
    def _procesar_desconocido(self, traduccion: Dict) -> Dict:
        """Fallback para consultas no clasificadas."""
        
        return {
            'tipo_respuesta': 'no_entendido',
            'puede_ejecutar': False,
            'certeza': 0.0,
            'razon': 'No entiendo qué tipo de consulta es esta',
            'operaciones': [],
            'conceptos_involucrados': [],
            'traduccion_original': traduccion
        }