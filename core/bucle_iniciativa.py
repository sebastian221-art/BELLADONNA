"""
Bucle de Iniciativa
Evalúa periódicamente si Belladonna debe iniciar conversación.
"""

import threading
import time
import logging

class BucleIniciativa:
    """
    Bucle que se ejecuta en background evaluando si debe iniciar conversación.
    """
    
    def __init__(self, sistema_belladonna, callback_enviar_mensaje):
        self.sistema = sistema_belladonna
        self.callback = callback_enviar_mensaje
        self.activo = False
        self.thread = None
        self.frecuencia_segundos = 300  # Evalúa cada 5 minutos
    
    def iniciar(self):
        """
        Inicia el bucle de iniciativa.
        """
        if self.activo:
            return
        
        self.activo = True
        self.thread = threading.Thread(
            target=self._ejecutar_bucle,
            daemon=True,
            name="BucleIniciativa"
        )
        self.thread.start()
        logging.info("Bucle de Iniciativa iniciado")
    
    def detener(self):
        """
        Detiene el bucle.
        """
        self.activo = False
        if self.thread:
            self.thread.join(timeout=2)
    
    def _ejecutar_bucle(self):
        """
        Bucle principal.
        """
        while self.activo:
            try:
                # Evalúa si debe hablar
                debe_hablar, tipo, mensaje = self.sistema.iniciativa.debe_iniciar_conversacion()
                
                if debe_hablar:
                    # Marca que se envió
                    self.sistema.iniciativa.marcar_iniciativa_enviada()
                    
                    # Envía mensaje
                    self.callback(mensaje, tipo)
                    
                    logging.info(f"Iniciativa enviada: {tipo}")
                
            except Exception as e:
                logging.error(f"Error en bucle de iniciativa: {e}")
            
            # Espera
            time.sleep(self.frecuencia_segundos)