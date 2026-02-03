"""
Echo - Consejera Lógica.

Especialidad: Razonamiento puro, consistencia lógica, detección de falacias.
"""
from typing import Dict, List
from consejeras.base_consejera import Consejera
from razonamiento.tipos_decision import Decision

class Echo(Consejera):
    """
    Echo - La Lógica.
    
    Especialidad: Razonamiento puro, validación de consistencia lógica.
    
    Echo NO veta - solo señala inconsistencias y falacias.
    """
    
    def __init__(self):
        """Inicializa Echo."""
        super().__init__("Echo", "Lógica y Razonamiento")
        
        # Echo NO puede vetar
        self.puede_vetar = False
        
        # Patrones lógicos
        self.conectores_logicos = [
            'si', 'entonces', 'por lo tanto', 'porque',
            'implica', 'significa', 'consecuencia', 'causa'
        ]
        
        self.palabras_contradiccion = [
            'pero', 'sin embargo', 'aunque', 'a pesar',
            'contradice', 'opuesto', 'contrario'
        ]
    
    def revisar(self, decision: Decision, contexto: Dict) -> Dict:
        """
        Revisa desde perspectiva lógica.
        
        Echo busca:
        - Estructura lógica (si/entonces)
        - Contradicciones
        - Razonamiento inconsistente
        """
        self.revisiones_realizadas += 1
        self.opiniones_dadas += 1
        
        traduccion = contexto.get('traduccion', {})
        texto_original = traduccion.get('texto_original', '').lower()
        
        # Detectar estructura lógica
        tiene_logica = any(conector in texto_original for conector in self.conectores_logicos)
        tiene_contradiccion = any(palabra in texto_original for palabra in self.palabras_contradiccion)
        
        if tiene_logica or tiene_contradiccion:
            return self._generar_opinion_logica(texto_original, tiene_contradiccion)
        else:
            return self._generar_opinion_neutral()
    
    def _generar_opinion_logica(self, texto: str, tiene_contradiccion: bool) -> Dict:
        """Genera opinión sobre estructura lógica."""
        if tiene_contradiccion:
            opinion = "Detectada posible contradicción o estructura lógica compleja."
            sugerencias = [
                "Verificar consistencia del razonamiento",
                "Identificar si hay contradicción real",
                "Clarificar relaciones lógicas"
            ]
            confianza = 0.7
        else:
            opinion = "Detectada estructura lógica (si/entonces). Validar coherencia."
            sugerencias = [
                "Verificar premisas",
                "Validar implicaciones",
                "Asegurar conclusión lógica"
            ]
            confianza = 0.8
        
        return {
            'consejera': self.nombre,
            'aprobada': True,
            'veto': False,
            'opinion': opinion,
            'confianza': confianza,
            'razonamiento': [
                "1. Análisis: estructura lógica detectada",
                f"2. Contradicción potencial: {tiene_contradiccion}",
                "3. Recomendación: verificar consistencia"
            ],
            'sugerencias': sugerencias
        }
    
    def _generar_opinion_neutral(self) -> Dict:
        """Genera opinión neutral (no hay estructura lógica compleja)."""
        return {
            'consejera': self.nombre,
            'aprobada': True,
            'veto': False,
            'opinion': 'Sin estructura lógica compleja detectada.',
            'confianza': 0.5,
            'razonamiento': ["No hay conectores lógicos o contradicciones evidentes"],
            'sugerencias': []
        }