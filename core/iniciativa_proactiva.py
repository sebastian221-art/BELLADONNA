"""
Iniciativa Proactiva
Belladonna INICIA conversaciones sin esperar input.
"""

from datetime import datetime, timedelta
import json
from pathlib import Path

class IniciativaProactiva:
    """
    Sistema que permite a Belladonna iniciar conversaciones.
    """
    
    def __init__(self, orquestador_aprendizaje):
        self.orquestador = orquestador_aprendizaje
        self.ultima_interaccion = datetime.now()
        self.ultima_iniciativa = None
        self.config_path = Path("data/iniciativa_config.json")
        self.config = self._cargar_config()
    
    def _cargar_config(self):
        """
        Carga configuración de iniciativa.
        """
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Config por defecto
        config = {
            'min_minutos_entre_iniciativas': 60,  # Mínimo 1 hora entre mensajes proactivos
            'umbral_palabras_aprendidas': 10,     # Reporta si aprendió 10+ palabras
            'umbral_lagunas_acumuladas': 5        # Pregunta si tiene 5+ dudas
        }
        
        self._guardar_config(config)
        return config
    
    def _guardar_config(self, config):
        """
        Guarda configuración.
        """
        self.config_path.parent.mkdir(exist_ok=True)
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
    
    def registrar_interaccion(self):
        """
        Registra que hubo interacción con el usuario.
        """
        self.ultima_interaccion = datetime.now()
    
    def debe_iniciar_conversacion(self):
        """
        Evalúa si debe iniciar una conversación.
        
        Returns:
            (bool, str, str): (debe_iniciar, tipo, mensaje)
        """
        # Verifica cooldown
        if self.ultima_iniciativa:
            minutos_desde_ultima = (datetime.now() - self.ultima_iniciativa).total_seconds() / 60
            if minutos_desde_ultima < self.config['min_minutos_entre_iniciativas']:
                return (False, None, None)
        
        # 1. ¿Tiene muchas palabras aprendidas para reportar?
        palabras_hoy = self.orquestador.obtener_palabras_aprendidas_hoy()
        
        if len(palabras_hoy) >= self.config['umbral_palabras_aprendidas']:
            mensaje = self._generar_reporte_aprendizaje(palabras_hoy)
            return (True, 'reporte_aprendizaje', mensaje)
        
        # 2. ¿Tiene dudas acumuladas?
        lagunas = self.orquestador.detector.obtener_lagunas_pendientes()
        
        if len(lagunas) >= self.config['umbral_lagunas_acumuladas']:
            mensaje = self._generar_consulta_dudas(lagunas)
            return (True, 'consulta_dudas', mensaje)
        
        return (False, None, None)
    
    def _generar_reporte_aprendizaje(self, palabras):
        """
        Genera mensaje de reporte de aprendizaje.
        """
        mensaje = f"Sebastian, quiero compartirte algo.\n\n"
        mensaje += f"Hoy aprendí {len(palabras)} palabras nuevas de nuestras conversaciones.\n\n"
        mensaje += "Las más interesantes:\n"
        
        for i, palabra in enumerate(palabras[:5], 1):
            definicion = palabra['definiciones'][0] if palabra['definiciones'] else 'Sin definición'
            mensaje += f"{i}. {palabra['palabra']}: {definicion[:100]}\n"
        
        mensaje += "\n¿Quieres que te cuente más o prefieres seguir trabajando?"
        
        return mensaje
    
    def _generar_consulta_dudas(self, lagunas):
        """
        Genera mensaje consultando dudas.
        """
        mensaje = "Sebastian, ¿tienes un momento?\n\n"
        mensaje += "Tengo algunas palabras que no pude investigar bien:\n\n"
        
        # Agrupa por palabra única
        palabras_unicas = {}
        for laguna in lagunas:
            palabra = laguna['palabra']
            if palabra not in palabras_unicas:
                palabras_unicas[palabra] = laguna['contexto']
        
        for i, (palabra, contexto) in enumerate(list(palabras_unicas.items())[:3], 1):
            mensaje += f"{i}. '{palabra}' (la usaste en: \"{contexto[:50]}...\")\n"
        
        mensaje += "\n¿Puedes explicarme qué significan?"
        
        return mensaje
    
    def marcar_iniciativa_enviada(self):
        """
        Marca que se envió una iniciativa.
        """
        self.ultima_iniciativa = datetime.now()