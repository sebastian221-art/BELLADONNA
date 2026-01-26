"""
Sistema de Búsqueda de Conocimiento
Búsqueda en Wikipedia (100% gratis)
"""

import requests
from bs4 import BeautifulSoup
import json

class BuscadorConocimiento:
    """
    Busca conocimiento básico en Wikipedia.
    100% gratis, sin APIs de pago.
    """
    
    def __init__(self):
        self.cache = {}  # Cache de búsquedas
        self.idioma = 'es'
    
    def buscar(self, query):
        """
        Busca información en Wikipedia.
        
        Retorna:
        - resumen: texto resumido
        - url: enlace al artículo
        - exito: si encontró algo útil
        """
        # Revisa cache primero
        if query in self.cache:
            return self.cache[query]
        
        try:
            # Busca en Wikipedia API
            resultado = self._buscar_wikipedia(query)
            
            if resultado['exito']:
                self.cache[query] = resultado
            
            return resultado
            
        except Exception as e:
            return {
                'exito': False,
                'error': str(e),
                'resumen': None,
                'url': None
            }
    
    def _buscar_wikipedia(self, query):
        """Busca en Wikipedia usando su API pública"""
        try:
            # API de Wikipedia (gratis, sin límites razonables)
            url = f"https://{self.idioma}.wikipedia.org/api/rest_v1/page/summary/{query}"
            
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                
                return {
                    'exito': True,
                    'resumen': data.get('extract', ''),
                    'url': data.get('content_urls', {}).get('desktop', {}).get('page', ''),
                    'titulo': data.get('title', query)
                }
            else:
                # Intenta búsqueda alternativa
                return self._busqueda_alternativa(query)
                
        except Exception as e:
            return {
                'exito': False,
                'error': str(e),
                'resumen': None,
                'url': None
            }
    
    def _busqueda_alternativa(self, query):
        """Búsqueda alternativa si falla la primera"""
        try:
            # Usa el buscador de Wikipedia
            search_url = f"https://{self.idioma}.wikipedia.org/w/api.php"
            params = {
                'action': 'query',
                'format': 'json',
                'list': 'search',
                'srsearch': query,
                'srlimit': 1
            }
            
            response = requests.get(search_url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                resultados = data.get('query', {}).get('search', [])
                
                if resultados:
                    primer_resultado = resultados[0]
                    titulo = primer_resultado['title']
                    
                    # Obtiene el resumen del artículo encontrado
                    return self._buscar_wikipedia(titulo.replace(' ', '_'))
            
            return {
                'exito': False,
                'error': 'No se encontraron resultados',
                'resumen': None,
                'url': None
            }
            
        except Exception as e:
            return {
                'exito': False,
                'error': str(e),
                'resumen': None,
                'url': None
            }
    
    def sintetizar(self, texto, max_palabras=100):
        """
        Sintetiza un texto largo en resumen corto.
        """
        if not texto:
            return ""
        
        # Divide en oraciones
        oraciones = texto.split('. ')
        
        # Toma las primeras oraciones hasta el límite
        resumen = []
        palabras_actuales = 0
        
        for oracion in oraciones:
            palabras = len(oracion.split())
            if palabras_actuales + palabras <= max_palabras:
                resumen.append(oracion)
                palabras_actuales += palabras
            else:
                break
        
        return '. '.join(resumen) + '.'
    
    def buscar_y_sintetizar(self, query, max_palabras=150):
        """
        Busca y retorna resumen sintetizado.
        """
        resultado = self.buscar(query)
        
        if resultado['exito']:
            resumen = self.sintetizar(resultado['resumen'], max_palabras)
            return {
                'exito': True,
                'resumen': resumen,
                'url': resultado['url'],
                'titulo': resultado.get('titulo', query)
            }
        
        return resultado