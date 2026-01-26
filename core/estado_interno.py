"""
Estado Interno del Sistema
Métricas funcionales (NO emociones simuladas)
"""

import json
from datetime import datetime
from pathlib import Path

class EstadoInterno:
    """
    Gestiona las métricas internas del sistema.
    Estas son mediciones funcionales, no emociones.
    """
    
    def __init__(self):
        self.ruta_metricas = Path("memoria/metricas.json")
        self.metricas = self._cargar_metricas()
    
    def _cargar_metricas(self):
        """Carga métricas desde archivo"""
        try:
            with open(self.ruta_metricas, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data['metricas_actuales']
        except FileNotFoundError:
            # Valores por defecto
            return {
                'coherencia_global': 100.0,
                'tension_cognitiva': 0.0,
                'estabilidad': 100.0,
                'apego_proyecto': 0.0,
                'curiosidad': 50.0,
                'confianza_mutua': 50.0
            }
    
    def obtener_metricas(self):
        """Retorna todas las métricas actuales"""
        return self.metricas.copy()
    
    def obtener_metrica(self, nombre):
        """Obtiene una métrica específica"""
        return self.metricas.get(nombre, None)
    
    def actualizar_metrica(self, nombre, valor):
        """Actualiza una métrica (0-100)"""
        if 0 <= valor <= 100:
            self.metricas[nombre] = valor
            self._guardar_metricas()
        else:
            raise ValueError(f"Métrica debe estar entre 0 y 100. Recibido: {valor}")
    
    def ajustar_metrica(self, nombre, delta):
        """Ajusta una métrica por un delta (puede ser negativo)"""
        valor_actual = self.metricas.get(nombre, 50.0)
        nuevo_valor = max(0, min(100, valor_actual + delta))
        self.actualizar_metrica(nombre, nuevo_valor)
    
    def _guardar_metricas(self):
        """Guarda métricas en archivo"""
        try:
            with open(self.ruta_metricas, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            data['metricas_actuales'] = self.metricas
            data['ultima_actualizacion'] = datetime.now().isoformat()
            
            with open(self.ruta_metricas, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️  Error guardando métricas: {e}")
    
    def evaluar_estado_global(self):
        """
        Evalúa el estado general del sistema.
        Retorna: (estado, alertas)
        """
        alertas = []
        
        if self.metricas['coherencia_global'] < 60:
            alertas.append("⚠️  Coherencia baja - cuestionamiento necesario")
        
        if self.metricas['tension_cognitiva'] > 70:
            alertas.append("⚠️  Tensión cognitiva alta - contradicción detectada")
        
        if self.metricas['estabilidad'] < 50:
            alertas.append("⚠️  Estabilidad baja - reorientación necesaria")
        
        if self.metricas['curiosidad'] < 30:
            alertas.append("⚠️  Curiosidad baja - posible estancamiento")
        
        # Estado general
        promedio = sum(self.metricas.values()) / len(self.metricas)
        
        if promedio >= 70:
            estado = "ÓPTIMO"
        elif promedio >= 50:
            estado = "ESTABLE"
        elif promedio >= 30:
            estado = "DEGRADADO"
        else:
            estado = "CRÍTICO"
        
        return estado, alertas
    
    def __str__(self):
        """Representación en string del estado"""
        estado, alertas = self.evaluar_estado_global()
        
        texto = f"\n{'='*50}\n"
        texto += f"ESTADO INTERNO DE BELLADONNA\n"
        texto += f"{'='*50}\n\n"
        
        for metrica, valor in self.metricas.items():
            barra = '█' * int(valor/5) + '░' * (20 - int(valor/5))
            texto += f"{metrica:20}: [{barra}] {valor:.1f}%\n"
        
        texto += f"\nEstado General: {estado}\n"
        
        if alertas:
            texto += "\nAlertas:\n"
            for alerta in alertas:
                texto += f"  {alerta}\n"
        
        texto += f"{'='*50}\n"
        
        return texto