"""
Sistema de Aprendizaje Acelerado
Permite a Belladonna aprender RÁPIDO de sus interacciones
"""

import json
from datetime import datetime
from pathlib import Path

class AprendizajeAcelerado:
    """
    Sistema que acelera el aprendizaje de Belladonna.
    
    Estrategias:
    1. Auto-identificación de lagunas de conocimiento
    2. Práctica simulada de respuestas
    3. Evaluación continua de mejora
    4. Priorización de aprendizaje
    """
    
    def __init__(self, sistema):
        self.sistema = sistema
        self.ruta_conocimiento = Path("memoria/conocimiento_adquirido.json")
        self.ruta_lagunas = Path("memoria/lagunas_conocimiento.json")
        self.conocimiento = self._cargar_conocimiento()
        self.lagunas = self._cargar_lagunas()
        self.estadisticas = {
            'total_aprendido': 0,
            'lagunas_identificadas': 0,
            'lagunas_resueltas': 0,
            'mejoras_detectadas': 0
        }
    
    def _cargar_conocimiento(self):
        """Carga conocimiento adquirido"""
        try:
            with open(self.ruta_conocimiento, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def _cargar_lagunas(self):
        """Carga lagunas de conocimiento detectadas"""
        try:
            with open(self.ruta_lagunas, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def identificar_laguna(self, pregunta, contexto):
        """
        Identifica una laguna en el conocimiento.
        Cuando Belladonna no sabe responder algo.
        """
        laguna = {
            'pregunta': pregunta,
            'contexto': contexto,
            'timestamp': datetime.now().isoformat(),
            'prioridad': self._calcular_prioridad(pregunta, contexto),
            'resuelta': False
        }
        
        self.lagunas.append(laguna)
        self.estadisticas['lagunas_identificadas'] += 1
        self._guardar_lagunas()
        
        return laguna
    
    def _calcular_prioridad(self, pregunta, contexto):
        """
        Calcula prioridad de aprender algo.
        Más prioridad = más importante aprender.
        """
        prioridad = 50  # Base
        
        # Aumenta si es pregunta sobre sí misma
        palabras_auto = ['tu', 'tú', 'eres', 'tienes', 'puedes', 'sabes']
        if any(p in pregunta.lower() for p in palabras_auto):
            prioridad += 30
        
        # Aumenta si es pregunta frecuente
        preguntas_similares = [l for l in self.lagunas if self._similar(l['pregunta'], pregunta)]
        prioridad += len(preguntas_similares) * 10
        
        # Aumenta si la coherencia fue baja
        if contexto.get('coherencia', 100) < 50:
            prioridad += 20
        
        return min(100, prioridad)
    
    def _similar(self, texto1, texto2):
        """Detecta si dos textos son similares"""
        palabras1 = set(texto1.lower().split())
        palabras2 = set(texto2.lower().split())
        overlap = len(palabras1 & palabras2)
        return overlap >= 2
    
    def aprender_de_interaccion(self, pregunta, respuesta, coherencia, fue_exitosa):
        """
        Aprende de una interacción completa.
        
        fue_exitosa: True si la respuesta fue buena, False si no
        """
        conocimiento_nuevo = {
            'pregunta': pregunta,
            'respuesta': respuesta,
            'coherencia': coherencia,
            'exitosa': fue_exitosa,
            'timestamp': datetime.now().isoformat()
        }
        
        # Genera clave única para la pregunta
        clave = self._generar_clave(pregunta)
        
        if clave not in self.conocimiento:
            self.conocimiento[clave] = []
        
        self.conocimiento[clave].append(conocimiento_nuevo)
        self.estadisticas['total_aprendido'] += 1
        
        # Si fue exitosa, marca laguna como resuelta
        if fue_exitosa:
            self._marcar_laguna_resuelta(pregunta)
        
        self._guardar_conocimiento()
    
    def _generar_clave(self, pregunta):
        """Genera clave única para categorizar pregunta"""
        # Extrae palabras clave importantes
        stopwords = {'el', 'la', 'de', 'que', 'y', 'a', 'en', 'un', 'es', 'por', 'como', 'para'}
        palabras = [p.lower() for p in pregunta.split() if p.lower() not in stopwords]
        return "_".join(sorted(palabras[:3]))
    
    def _marcar_laguna_resuelta(self, pregunta):
        """Marca una laguna como resuelta"""
        for laguna in self.lagunas:
            if self._similar(laguna['pregunta'], pregunta) and not laguna['resuelta']:
                laguna['resuelta'] = True
                laguna['fecha_resolucion'] = datetime.now().isoformat()
                self.estadisticas['lagunas_resueltas'] += 1
        
        self._guardar_lagunas()
    
    def obtener_lagunas_prioritarias(self, n=5):
        """
        Retorna las N lagunas más prioritarias para aprender.
        """
        lagunas_no_resueltas = [l for l in self.lagunas if not l['resuelta']]
        lagunas_ordenadas = sorted(lagunas_no_resueltas, key=lambda x: x['prioridad'], reverse=True)
        return lagunas_ordenadas[:n]
    
    def buscar_conocimiento_previo(self, pregunta):
        """
        Busca si ya aprendió algo similar antes.
        """
        clave = self._generar_clave(pregunta)
        
        if clave in self.conocimiento:
            # Retorna el conocimiento más exitoso
            exitosos = [c for c in self.conocimiento[clave] if c['exitosa']]
            if exitosos:
                return exitosos[-1]  # Más reciente exitoso
        
        return None
    
    def evaluar_mejora(self):
        """
        Evalúa si Belladonna está mejorando.
        """
        if self.estadisticas['lagunas_identificadas'] == 0:
            return {
                'mejorando': None,
                'razon': 'Aún no hay suficientes datos'
            }
        
        tasa_resolucion = self.estadisticas['lagunas_resueltas'] / self.estadisticas['lagunas_identificadas']
        
        if tasa_resolucion > 0.7:
            return {
                'mejorando': True,
                'razon': f'Resolviendo {tasa_resolucion*100:.1f}% de lagunas',
                'estadisticas': self.estadisticas
            }
        elif tasa_resolucion > 0.4:
            return {
                'mejorando': 'parcialmente',
                'razon': f'Resolviendo {tasa_resolucion*100:.1f}% de lagunas',
                'estadisticas': self.estadisticas
            }
        else:
            return {
                'mejorando': False,
                'razon': f'Solo resolviendo {tasa_resolucion*100:.1f}% de lagunas',
                'estadisticas': self.estadisticas
            }
    
    def obtener_estadisticas(self):
        """Retorna estadísticas de aprendizaje"""
        return self.estadisticas
    
    def _guardar_conocimiento(self):
        """Guarda conocimiento adquirido"""
        self.ruta_conocimiento.parent.mkdir(exist_ok=True)
        with open(self.ruta_conocimiento, 'w', encoding='utf-8') as f:
            json.dump(self.conocimiento, f, indent=2, ensure_ascii=False)
    
    def _guardar_lagunas(self):
        """Guarda lagunas detectadas"""
        self.ruta_lagunas.parent.mkdir(exist_ok=True)
        with open(self.ruta_lagunas, 'w', encoding='utf-8') as f:
            json.dump(self.lagunas, f, indent=2, ensure_ascii=False)