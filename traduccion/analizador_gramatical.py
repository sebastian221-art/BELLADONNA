"""
AnalizadorGramatical - Análisis de estructura gramatical del español.

Usa spaCy cuando está disponible, fallback a análisis básico si no.
"""

import warnings
from typing import List, Dict

# Intentar cargar spaCy
try:
    import spacy  # type: ignore
    nlp = spacy.load("es_core_news_sm")
    SPACY_DISPONIBLE = True
except (ImportError, OSError):
    SPACY_DISPONIBLE = False
    nlp = None
    warnings.warn("spaCy no disponible - usando análisis básico")


class AnalizadorGramatical:
    """
    Analiza estructura gramatical del español.
    
    Extrae:
    - Tokens (palabras)
    - Lemas (forma base de palabras)
    - POS tags (tipos gramaticales)
    - Estructura (pregunta/afirmación/comando)
    - Entidades nombradas
    """
    
    def __init__(self):
        self.spacy_disponible = SPACY_DISPONIBLE
    
    def analizar(self, texto: str) -> Dict:
        """
        Analiza texto y extrae información lingüística.
        
        Args:
            texto: Texto en español a analizar
            
        Returns:
            Dict con análisis completo
        """
        if self.spacy_disponible and nlp is not None:
            return self._analizar_spacy(texto)
        else:
            return self._analizar_basico(texto)
    
    def _analizar_spacy(self, texto: str) -> Dict:
        """Análisis con spaCy (completo)."""
        if nlp is None:
            return self._analizar_basico(texto)
            
        doc = nlp(texto)
        
        return {
            'tokens': [token.text for token in doc],
            'lemas': [token.lemma_ for token in doc],
            'pos_tags': [token.pos_ for token in doc],
            'estructura': self._detectar_estructura_spacy(texto, doc),
            'entidades': [
                {'texto': ent.text, 'tipo': ent.label_}
                for ent in doc.ents
            ]
        }
    
    def _analizar_basico(self, texto: str) -> Dict:
        """Análisis básico sin spaCy (fallback)."""
        # Tokenización simple
        tokens = texto.split()
        
        return {
            'tokens': tokens,
            'lemas': self._lematizar_basico(tokens),
            'pos_tags': ['UNKNOWN'] * len(tokens),
            'estructura': self._detectar_estructura_basico(texto),
            'entidades': []
        }
    
    def _lematizar_basico(self, tokens: List[str]) -> List[str]:
        """
        Lematización básica (simplificada).
        
        Elimina plurales simples y algunas conjugaciones comunes.
        """
        lemas = []
        
        for token in tokens:
            token_lower = token.lower()
            
            # Reglas básicas de lematización
            if token_lower.endswith('s') and len(token_lower) > 3:
                # Posible plural
                lema = token_lower[:-1]
            elif token_lower.endswith('ar') or token_lower.endswith('er') or token_lower.endswith('ir'):
                # Posible infinitivo
                lema = token_lower
            else:
                lema = token_lower
            
            lemas.append(lema)
        
        return lemas
    
    def _detectar_estructura_spacy(self, texto: str, doc) -> str:
        """Detecta estructura con spaCy."""
        # Signos de interrogación
        if '?' in texto or '¿' in texto:
            return 'pregunta'
        
        # Palabras interrogativas
        interrogativas = ['qué', 'quién', 'cómo', 'cuándo', 'dónde', 'por qué', 'cuál']
        if any(palabra in texto.lower() for palabra in interrogativas):
            return 'pregunta'
        
        # Verbos imperativos (primera palabra es verbo)
        if doc and len(doc) > 0:
            primer_token = doc[0]
            if primer_token.pos_ == 'VERB' and primer_token.morph.get('Mood') == ['Imp']:
                return 'comando'
        
        # Verbos imperativos comunes
        imperativos = ['analiza', 'crea', 'lee', 'escribe', 'ejecuta', 'muestra', 
                      'dame', 'haz', 'genera', 'busca']
        primera_palabra = texto.split()[0].lower() if texto.split() else ''
        if primera_palabra in imperativos:
            return 'comando'
        
        return 'afirmacion'
    
    def _detectar_estructura_basico(self, texto: str) -> str:
        """Detecta estructura sin spaCy."""
        # Signos de interrogación
        if '?' in texto or '¿' in texto:
            return 'pregunta'
        
        # Palabras interrogativas
        interrogativas = ['qué', 'quién', 'cómo', 'cuándo', 'dónde', 'por qué', 'cuál', 'puedes']
        if any(palabra in texto.lower() for palabra in interrogativas):
            return 'pregunta'
        
        # Verbos imperativos comunes
        imperativos = ['analiza', 'crea', 'lee', 'escribe', 'ejecuta', 'muestra',
                      'dame', 'haz', 'genera', 'busca', 'abre', 'cierra']
        primera_palabra = texto.split()[0].lower() if texto.split() else ''
        if primera_palabra in imperativos:
            return 'comando'
        
        return 'afirmacion'