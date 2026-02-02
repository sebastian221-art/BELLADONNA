"""
BuclePensamientoContinuo - Bucle 1 (60 segundos).

Bell observa contexto constantemente y decide cuándo hablar.
ESTO ES LO QUE HACE QUE BELL SEA AUTÓNOMA.
"""

import asyncio
from typing import Dict, List
from datetime import datetime


class BuclePensamientoContinuo:
    """
    Bucle 1 (60 segundos): Observación continua.
    
    Bell observa contexto, detecta eventos y decide cuándo intervenir.
    """
    
    def __init__(self):
        self.activo = False
        self.eventos_detectados = []
        self.intervalo = 60  # 60 segundos
        
        # Umbral para intervenir
        self.umbral_intervencion = 0.7
        
        # Tiempo de última interacción
        self.ultima_interaccion = datetime.now()
    
    async def iniciar(self):
        """Inicia bucle autónomo."""
        self.activo = True
        
        print("🧠 Bell: Pensamiento continuo activado (cada 60s)")
        
        while self.activo:
            await asyncio.sleep(self.intervalo)
            await self._ciclo_observacion()
    
    async def _ciclo_observacion(self):
        """Un ciclo de observación."""
        if not self.activo:
            return
        
        # 1. Observar contexto
        contexto = self._observar_contexto()
        
        # 2. Detectar eventos
        eventos = self._detectar_eventos(contexto)
        
        # 3. Evaluar si intervenir
        for evento in eventos:
            if self._debe_intervenir(evento):
                self._programar_intervencion(evento)
    
    def _observar_contexto(self) -> Dict:
        """
        Observa contexto actual.
        
        En Fase 1: Contexto simple
        En Fases posteriores: Más sofisticado
        """
        return {
            'timestamp': datetime.now(),
            'tiempo_desde_ultima_interaccion': self._calcular_tiempo_inactividad(),
        }
    
    def _detectar_eventos(self, contexto: Dict) -> List[Dict]:
        """
        Detecta eventos relevantes.
        
        Fase 1: Eventos simples
        Fase 2+: Detección más sofisticada
        """
        eventos = []
        
        # Ejemplo simple: Inactividad larga
        tiempo_inactivo = contexto['tiempo_desde_ultima_interaccion']
        
        if tiempo_inactivo > 7200:  # 2 horas
            eventos.append({
                'tipo': 'INACTIVIDAD_LARGA',
                'severidad': 0.5,
                'descripcion': 'Usuario inactivo por 2+ horas',
                'timestamp': contexto['timestamp']
            })
        
        return eventos
    
    def _debe_intervenir(self, evento: Dict) -> bool:
        """
        Decide si vale la pena intervenir.
        
        Usa scoring simple en Fase 1.
        """
        severidad = evento['severidad']
        
        # En Fase 1: Solo severidad
        # En Fase 2+: Scoring complejo con múltiples factores
        
        return severidad > self.umbral_intervencion
    
    def _programar_intervencion(self, evento: Dict):
        """Programa intervención al usuario."""
        self.eventos_detectados.append(evento)
        
        print(f"🔔 Bell detectó: {evento['descripcion']}")
        # En interfaz real, esto mostraría notificación
    
    def _calcular_tiempo_inactividad(self) -> float:
        """Calcula segundos desde última interacción."""
        delta = datetime.now() - self.ultima_interaccion
        return delta.total_seconds()
    
    def registrar_interaccion(self):
        """Registra que hubo interacción con usuario."""
        self.ultima_interaccion = datetime.now()
    
    def detener(self):
        """Detiene bucle."""
        self.activo = False
        print("🛑 Pensamiento continuo detenido")
    
    def obtener_eventos(self) -> List[Dict]:
        """Obtiene eventos detectados."""
        return self.eventos_detectados.copy()