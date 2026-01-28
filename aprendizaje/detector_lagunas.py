"""
Detector de Lagunas Lingüísticas
Detecta TODO lo que Belladonna no conoce.
"""

import re
import json
from pathlib import Path
from datetime import datetime

class DetectorLagunas:
    """
    Analiza mensajes y detecta palabras/expresiones desconocidas.
    """
    
    def __init__(self):
        self.vocabulario_conocido = self._cargar_vocabulario()
        self.lagunas_detectadas = []
        
    def _cargar_vocabulario(self):
        """
        Carga vocabulario conocido desde archivo.
        """
        vocab_path = Path("data/vocabulario_conocido.json")
        
        if vocab_path.exists():
            with open(vocab_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return set(data['palabras'])
        else:
            # Vocabulario base inicial (español básico)
            return self._crear_vocabulario_base()
    
    def _crear_vocabulario_base(self):
        """
        Crea vocabulario base con palabras comunes del español.
        """
        # Palabras más comunes del español
        base = {
            # Artículos
            'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
            
            # Pronombres
            'yo', 'tu', 'tú', 'él', 'ella', 'nosotros', 'ustedes', 'ellos',
            'me', 'te', 'se', 'nos', 'les', 'lo', 'le',
            'este', 'esta', 'ese', 'esa', 'aquel', 'aquella',
            'mio', 'mío', 'tuyo', 'suyo',
            
            # Verbos comunes
            'ser', 'estar', 'haber', 'tener', 'hacer', 'poder', 'decir',
            'ir', 'ver', 'dar', 'saber', 'querer', 'llegar', 'pasar',
            'deber', 'poner', 'parecer', 'quedar', 'creer', 'hablar',
            'llevar', 'dejar', 'seguir', 'encontrar', 'llamar', 'venir',
            'pensar', 'salir', 'volver', 'tomar', 'conocer', 'vivir',
            'sentir', 'tratar', 'mirar', 'contar', 'empezar', 'esperar',
            'buscar', 'existir', 'entrar', 'trabajar', 'escribir',
            'perder', 'producir', 'ocurrir', 'entender', 'pedir',
            'recibir', 'recordar', 'terminar', 'permitir', 'aparecer',
            'conseguir', 'comenzar', 'servir', 'sacar', 'necesitar',
            'mantener', 'resultar', 'leer', 'caer', 'cambiar',
            'presentar', 'crear', 'abrir', 'considerar', 'oír', 'acabar',
            
            # Adjetivos comunes
            'bueno', 'grande', 'pequeño', 'nuevo', 'viejo', 'mismo',
            'otro', 'todo', 'mucho', 'poco', 'primero', 'último',
            'mejor', 'peor', 'mayor', 'menor', 'propio', 'cierto',
            'largo', 'corto', 'alto', 'bajo', 'fuerte', 'débil',
            'claro', 'oscuro', 'fácil', 'difícil', 'simple', 'complejo',
            
            # Adverbios
            'muy', 'más', 'menos', 'poco', 'mucho', 'bien', 'mal',
            'aquí', 'ahí', 'allí', 'ahora', 'luego', 'después', 'antes',
            'siempre', 'nunca', 'casi', 'solo', 'sólo', 'también',
            'tampoco', 'además', 'entonces', 'así', 'tan', 'como',
            'cuando', 'donde', 'dónde',
            
            # Preposiciones
            'a', 'ante', 'bajo', 'con', 'contra', 'de', 'desde',
            'durante', 'en', 'entre', 'hacia', 'hasta', 'para',
            'por', 'según', 'sin', 'sobre', 'tras',
            
            # Conjunciones
            'y', 'e', 'o', 'u', 'pero', 'sino', 'aunque', 'porque',
            'que', 'qué', 'si', 'sí',
            
            # Interrogativos
            'quién', 'quien', 'cuál', 'cual', 'cómo', 'cuándo', 'cuando',
            'cuánto', 'cuanto',
            
            # Números
            'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete',
            'ocho', 'nueve', 'diez', 'cien', 'mil',
            
            # Palabras técnicas básicas
            'código', 'programa', 'sistema', 'función', 'archivo', 'dato',
            'error', 'problema', 'solución', 'proyecto', 'versión',
            'belladonna', 'bell',
            
            # Palabras conversacionales
            'hola', 'adiós', 'gracias', 'por favor', 'perdón', 'disculpa',
            'ok', 'vale', 'claro', 'entiendo', 'perfecto',
        }
        
        # Guarda vocabulario base
        self._guardar_vocabulario(base)
        
        return base
    
    def _guardar_vocabulario(self, vocabulario):
        """
        Guarda vocabulario en archivo.
        """
        vocab_path = Path("data/vocabulario_conocido.json")
        vocab_path.parent.mkdir(exist_ok=True)
        
        with open(vocab_path, 'w', encoding='utf-8') as f:
            json.dump({
                'palabras': list(vocabulario),
                'total': len(vocabulario),
                'ultima_actualizacion': datetime.now().isoformat()
            }, f, ensure_ascii=False, indent=2)
    
    def analizar_mensaje(self, texto):
        """
        Analiza mensaje y detecta lagunas.
        
        Args:
            texto: Mensaje del usuario
            
        Returns:
            {
                'palabras_desconocidas': [...],
                'total_palabras': int,
                'total_desconocidas': int,
                'porcentaje_desconocido': float
            }
        """
        # Tokeniza
        palabras = self._tokenizar(texto)
        
        # Detecta desconocidas
        desconocidas = []
        for palabra in palabras:
            if not self.conoce_palabra(palabra):
                desconocidas.append({
                    'palabra': palabra,
                    'contexto': texto,
                    'timestamp': datetime.now().isoformat()
                })
        
        # Registra lagunas
        self.lagunas_detectadas.extend(desconocidas)
        
        return {
            'palabras_desconocidas': desconocidas,
            'total_palabras': len(palabras),
            'total_desconocidas': len(desconocidas),
            'porcentaje_desconocido': (len(desconocidas) / len(palabras) * 100) if palabras else 0
        }
    
    def conoce_palabra(self, palabra):
        """
        Verifica si conoce una palabra.
        """
        return palabra.lower() in self.vocabulario_conocido
    
    def _tokenizar(self, texto):
        """
        Separa texto en palabras.
        """
        # Limpia puntuación
        texto_limpio = re.sub(r'[¿?¡!.,;:()"\']', ' ', texto)
        
        # Separa en palabras
        palabras = texto_limpio.split()
        
        # Filtra palabras muy cortas y normaliza
        palabras_filtradas = []
        for palabra in palabras:
            # Ignora palabras de 1-2 letras (excepto algunas)
            if len(palabra) <= 2 and palabra.lower() not in {'yo', 'tú', 'tu', 'él', 'me', 'te', 'se', 'la', 'el', 'un', 'si', 'sí', 'no', 'ya'}:
                continue
            
            palabras_filtradas.append(palabra)
        
        return palabras_filtradas
    
    def agregar_palabra_conocida(self, palabra):
        """
        Añade palabra al vocabulario conocido.
        """
        self.vocabulario_conocido.add(palabra.lower())
        self._guardar_vocabulario(self.vocabulario_conocido)
    
    def obtener_lagunas_pendientes(self):
        """
        Obtiene lagunas que aún no se han resuelto.
        """
        return self.lagunas_detectadas
    
    def marcar_laguna_resuelta(self, palabra):
        """
        Marca una laguna como resuelta.
        """
        self.lagunas_detectadas = [
            l for l in self.lagunas_detectadas 
            if l['palabra'].lower() != palabra.lower()
        ]