# bucles/gestor_bucles.py

"""
Gestor de Bucles Autónomos - Fase 2
"""

import asyncio
from bucles.pensamiento_continuo import BuclePensamientoContinuo
from bucles.evaluacion_interna import BucleEvaluacionInterna
from datetime import datetime

# Importar aprendizaje si está disponible
try:
    from bucles.aprendizaje_pasivo import BucleAprendizajePasivo
    APRENDIZAJE_DISPONIBLE = True
except ImportError:
    APRENDIZAJE_DISPONIBLE = False


class GestorBucles:
    """Gestiona los bucles autónomos de Bell."""
    
    def __init__(self, estado_interno, vocabulario=None, memoria=None):
        """
        Inicializa gestor de bucles.
        
        Args:
            estado_interno: Estado interno de Bell
            vocabulario: Gestor de vocabulario (opcional, para Fase 2)
            memoria: Memoria de conversación (opcional, para Fase 2)
        """
        self.bucle_pensamiento = BuclePensamientoContinuo()
        self.bucle_evaluacion = BucleEvaluacionInterna(estado_interno)
        
        # Bucle de aprendizaje (Fase 2)
        if APRENDIZAJE_DISPONIBLE and vocabulario and memoria:
            self.bucle_aprendizaje = BucleAprendizajePasivo(vocabulario, memoria)
            print("   ✅ Bucle de aprendizaje disponible")
        else:
            self.bucle_aprendizaje = None
        
        self.ultima_interaccion = None
    
    def registrar_interaccion(self):
        """Registra timestamp de interacción con usuario."""
        self.ultima_interaccion = datetime.now()
        self.bucle_pensamiento.ultima_interaccion = self.ultima_interaccion
    
    async def iniciar_todos(self):
        """Inicia todos los bucles en paralelo."""
        tareas = [
            self.bucle_pensamiento.iniciar(),
            self.bucle_evaluacion.iniciar()
        ]
        
        # Agregar bucle de aprendizaje si está disponible
        if self.bucle_aprendizaje:
            tareas.append(self.bucle_aprendizaje.iniciar())
        
        await asyncio.gather(*tareas)
    
    def detener_todos(self):
        """Detiene todos los bucles."""
        self.bucle_pensamiento.detener()
        self.bucle_evaluacion.detener()
        
        if self.bucle_aprendizaje:
            self.bucle_aprendizaje.detener()