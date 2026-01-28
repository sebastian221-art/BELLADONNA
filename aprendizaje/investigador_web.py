"""
Investigador Web
Busca conocimiento en internet de forma autónoma.
"""

import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
from datetime import datetime
import time

class InvestigadorWeb:
    """
    Investiga palabras/conceptos en internet.
    """
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.cache_path = Path("data/cache_investigaciones.json")
        self.cache = self._cargar_cache()
    
    def _cargar_cache(self):
        """
        Carga cache de investigaciones previas.
        """
        if self.cache_path.exists():
            with open(self.cache_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def _guardar_cache(self):
        """
        Guarda cache.
        """
        self.cache_path.parent.mkdir(exist_ok=True)
        with open(self.cache_path, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)
    
    def investigar_palabra(self, palabra):
        """
        Investiga una palabra en internet.
        
        Args:
            palabra: Palabra a investigar
            
        Returns:
            {
                'palabra': str,
                'definiciones': [...],
                'ejemplos': [...],
                'tipo': str,
                'confianza': int,
                'fuentes': [...],
                'timestamp': str
            }
        """
        # Verifica cache
        if palabra.lower() in self.cache:
            print(f"[Cache] '{palabra}' encontrada en cache")
            return self.cache[palabra.lower()]
        
        print(f"[Web] Investigando '{palabra}'...")
        
        # Busca en múltiples fuentes
        resultado = {
            'palabra': palabra,
            'definiciones': [],
            'ejemplos': [],
            'tipo': 'desconocido',
            'confianza': 0,
            'fuentes': [],
            'timestamp': datetime.now().isoformat()
        }
        
        # 1. Intenta RAE (Diccionario)
        rae_result = self._buscar_en_rae(palabra)
        if rae_result:
            resultado['definiciones'].extend(rae_result.get('definiciones', []))
            resultado['tipo'] = rae_result.get('tipo', 'desconocido')
            resultado['fuentes'].append('RAE')
            resultado['confianza'] += 30
        
        # 2. Intenta WordReference
        wr_result = self._buscar_en_wordreference(palabra)
        if wr_result:
            resultado['definiciones'].extend(wr_result.get('definiciones', []))
            resultado['ejemplos'].extend(wr_result.get('ejemplos', []))
            resultado['fuentes'].append('WordReference')
            resultado['confianza'] += 20
        
        # 3. Google simple (contexto)
        google_result = self._buscar_en_google(palabra)
        if google_result:
            if not resultado['definiciones']:  # Solo si no tiene aún
                resultado['definiciones'].append(google_result.get('definicion', ''))
            resultado['ejemplos'].extend(google_result.get('ejemplos', []))
            resultado['fuentes'].append('Google')
            resultado['confianza'] += 10
        
        # Normaliza confianza
        resultado['confianza'] = min(resultado['confianza'], 100)
        
        # Guarda en cache
        self.cache[palabra.lower()] = resultado
        self._guardar_cache()
        
        return resultado
    
    def _buscar_en_rae(self, palabra):
        """
        Busca en RAE (Real Academia Española).
        """
        try:
            url = f"https://dle.rae.es/{palabra}"
            response = requests.get(url, headers=self.headers, timeout=5)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Extrae definiciones
                definiciones = []
                acepciones = soup.find_all('p', class_='j')
                
                for acepcion in acepciones[:3]:  # Primeras 3
                    texto = acepcion.get_text(strip=True)
                    if texto:
                        definiciones.append(texto)
                
                if definiciones:
                    return {
                        'definiciones': definiciones,
                        'tipo': 'formal'
                    }
        except Exception as e:
            print(f"[RAE] Error: {e}")
        
        return None
    
    def _buscar_en_wordreference(self, palabra):
        """
        Busca en WordReference.
        """
        try:
            url = f"https://www.wordreference.com/definicion/{palabra}"
            response = requests.get(url, headers=self.headers, timeout=5)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                definiciones = []
                ejemplos = []
                
                # Extrae definiciones
                entries = soup.find_all('li', class_='even')
                entries.extend(soup.find_all('li', class_='odd'))
                
                for entry in entries[:3]:
                    texto = entry.get_text(strip=True)
                    if texto and len(texto) < 200:
                        definiciones.append(texto)
                
                if definiciones:
                    return {
                        'definiciones': definiciones,
                        'ejemplos': ejemplos
                    }
        except Exception as e:
            print(f"[WordReference] Error: {e}")
        
        return None
    
    def _buscar_en_google(self, palabra):
        """
        Busca definición simple en Google.
        """
        try:
            query = f"significado de {palabra}"
            url = f"https://www.google.com/search?q={query}"
            
            response = requests.get(url, headers=self.headers, timeout=5)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Busca featured snippet
                snippet = soup.find('div', {'data-attrid': 'definition'})
                if not snippet:
                    snippet = soup.find('div', class_='BNeawe')
                
                if snippet:
                    texto = snippet.get_text(strip=True)
                    return {
                        'definicion': texto[:300],  # Max 300 chars
                        'ejemplos': []
                    }
        except Exception as e:
            print(f"[Google] Error: {e}")
        
        return None