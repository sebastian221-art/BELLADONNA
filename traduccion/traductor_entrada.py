"""
TraductorEntrada - Traduce español → conceptos anclados.

Este es el punto de entrada al sistema de Bell.
Convierte lenguaje natural en representación interna.
"""

from typing import Dict, List
from traduccion.analizador_gramatical import AnalizadorGramatical
from vocabulario.gestor_vocabulario import GestorVocabulario


class TraductorEntrada:
    """
    Traduce español → conceptos anclados (lenguaje interno de Bell).
    """
    
    def __init__(self, gestor_vocab: GestorVocabulario):
        self.analizador = AnalizadorGramatical()
        self.vocabulario = gestor_vocab
    
    def traducir(self, texto: str) -> Dict:
        """
        Traduce texto en español a representación interna.
        
        Args:
            texto: Entrada del usuario en español
            
        Returns:
            Dict con traducción completa
        """
        # 1. Análisis gramatical
        analisis = self.analizador.analizar(texto)
        
        # 2. Mapear lemas a conceptos
        conceptos = []
        desconocidas = []
        
        for lema in analisis['lemas']:
            concepto = self.vocabulario.obtener_concepto(lema)
            
            if concepto:
                conceptos.append({
                    'palabra': lema,
                    'concepto': concepto,
                    'grounding': concepto.confianza_grounding,
                    'operaciones': list(concepto.operaciones.keys())
                })
            else:
                # Palabra desconocida
                if lema not in desconocidas:
                    desconocidas.append(lema)
        
        # 3. Calcular confianza de traducción
        if len(analisis['lemas']) == 0:
            confianza = 0.0
        else:
            # Confianza = proporción de palabras conocidas
            palabras_conocidas = len(conceptos)
            total_palabras = len(analisis['lemas'])
            confianza = palabras_conocidas / total_palabras
        
        return {
            'texto_original': texto,
            'estructura': analisis['estructura'],
            'conceptos': conceptos,
            'palabras_desconocidas': desconocidas,
            'confianza_traduccion': confianza,
            'analisis_completo': analisis
        }
    
    def extraer_intencion(self, traduccion: Dict) -> str:
        """
        Extrae intención principal de la traducción.
        
        Args:
            traduccion: Resultado de traducir()
            
        Returns:
            Tipo de intención detectada
        """
        estructura = traduccion['estructura']
        conceptos = traduccion['conceptos']
        
        # Pregunta sobre capacidad
        if estructura == 'pregunta':
            # ¿Puedes X?
            if any(c['concepto'].id.startswith('CONCEPTO_') for c in conceptos):
                return 'pregunta_capacidad'
            return 'pregunta_general'
        
        # Comando de ejecución
        elif estructura == 'comando':
            return 'comando_ejecutar'
        
        # Afirmación
        else:
            return 'afirmacion'