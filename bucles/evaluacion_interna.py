"""
BucleEvaluacionInterna - Bucle 2 (120 segundos).

Bell evalúa su propio desempeño y se ajusta.
"""

import asyncio
from typing import Dict, List
from datetime import datetime
from core.estado_interno import EstadoInterno


class BucleEvaluacionInterna:
    """
    Bucle 2 (120 segundos): Auto-evaluación.
    
    Bell evalúa su propio desempeño y se ajusta automáticamente.
    """
    
    def __init__(self, estado: EstadoInterno):
        self.estado = estado
        self.activo = False
        self.intervalo = 120  # 2 minutos
        
        self.historial_metricas = []
    
    async def iniciar(self):
        """Inicia bucle de auto-evaluación."""
        self.activo = True
        
        print("📊 Bell: Auto-evaluación activada (cada 120s)")
        
        while self.activo:
            await asyncio.sleep(self.intervalo)
            await self._ciclo_evaluacion()
    
    async def _ciclo_evaluacion(self):
        """Un ciclo de evaluación."""
        if not self.activo:
            return
        
        # 1. Calcular métricas
        metricas = self._calcular_metricas()
        
        # 2. Detectar problemas
        problemas = self._detectar_problemas(metricas)
        
        # 3. Aplicar ajustes
        if problemas:
            self._aplicar_ajustes(problemas)
        
        # 4. Registrar
        self.historial_metricas.append({
            'timestamp': datetime.now(),
            'metricas': metricas,
            'problemas': problemas
        })
    
    def _calcular_metricas(self) -> Dict:
        """Calcula métricas de desempeño."""
        # En Fase 1: Métricas simples del estado interno
        return {
            'coherencia': self.estado.coherencia_proposito,
            'confianza': self.estado.confianza_conocimiento,
            'carga': self.estado.carga_cognitiva
        }
    
    def _detectar_problemas(self, metricas: Dict) -> List[Dict]:
        """Detecta problemas en métricas."""
        problemas = []
        
        if metricas['carga'] > 0.8:
            problemas.append({
                'tipo': 'SOBRECARGA',
                'metrica': 'carga_cognitiva',
                'valor': metricas['carga']
            })
        
        if metricas['coherencia'] < 0.6:
            problemas.append({
                'tipo': 'DERIVA_PROPOSITO',
                'metrica': 'coherencia_proposito',
                'valor': metricas['coherencia']
            })
        
        return problemas
    
    def _aplicar_ajustes(self, problemas: List[Dict]):
        """Aplica ajustes automáticos."""
        for problema in problemas:
            print(f"⚙️ Bell auto-ajuste: {problema['tipo']}")
            # En Fase 1: Solo log
            # En Fase 2+: Ajustes reales
    
    def detener(self):
        """Detiene bucle."""
        self.activo = False
        print("🛑 Auto-evaluación detenida")
    
    def obtener_historial(self) -> List[Dict]:
        """Obtiene historial de métricas."""
        return self.historial_metricas.copy()