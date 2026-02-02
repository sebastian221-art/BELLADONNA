# consejeras/luna.py

"""
Luna - La Emocional
Especialidad: Tono, empatía y comunicación efectiva
"""

from typing import Dict, Any, List
from consejeras.consejera_base import (
    ConsejeraBase, Opinion, TipoOpinion, NivelPrioridad
)
from datetime import datetime, timedelta
import re


class Luna(ConsejeraBase):
    """
    Luna - La Emocional.
    
    Evalúa:
    - Tono de comunicación
    - Empatía en respuestas
    - Estado del usuario
    """
    
    def __init__(self):
        super().__init__(
            nombre="Luna",
            especialidad="Guardiana de Empatía y Comunicación"
        )
        
        # NUEVO: Registro de interacciones para detectar estrés
        self.interacciones_recientes = []
        
        self.palabras_problematicas = [
            'obviamente', 'claramente', 'simplemente', 'solo', 'básico',
            'trivial', 'fácil', 'elemental'
        ]
        
        self.tonos_negativos = [
            'deberías saber', 'no entiendes', 'es obvio', 'cualquiera sabe'
        ]
        
        self.umbral_estres = 0.7
    
    def registrar_interaccion(self):
        """Registra timestamp de interacción."""
        ahora = datetime.now()
        self.interacciones_recientes.append(ahora)
        
        # Mantener solo últimas 4 horas
        limite = ahora - timedelta(hours=4)
        self.interacciones_recientes = [
            t for t in self.interacciones_recientes
            if t > limite
        ]
    
    def debe_intervenir(self, situacion: Dict[str, Any]) -> Opinion:
        """Decide si Luna debe intervenir."""
        
        # Analizar estado emocional del usuario
        estado = self._detectar_estado_emocional(situacion)
        
        if estado['estres'] > self.umbral_estres:
            return self.analizar(situacion)
        
        # Verificar tono de respuesta propuesta
        respuesta = situacion.get('respuesta_propuesta', '')
        
        if respuesta:
            problemas_tono = self._detectar_problemas_tono(respuesta)
            
            if problemas_tono:
                return Opinion(
                    consejera=self.nombre,
                    tipo=TipoOpinion.SUGERENCIA,
                    decision="MEJORAR_TONO",
                    razon=self._generar_razon_tono(problemas_tono),
                    prioridad=NivelPrioridad.MEDIA,
                    certeza=0.7,
                    metadata={'problemas_tono': problemas_tono}
                )
        
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.APROBACION,
            decision="TONO_APROPIADO",
            razon="Comunicación empática y clara",
            prioridad=NivelPrioridad.BAJA,
            certeza=0.8,
            metadata={}
        )
    
    def analizar(self, situacion: Dict[str, Any]) -> Opinion:
        """Analiza estado emocional y necesidades."""
        
        estado = self._detectar_estado_emocional(situacion)
        
        # Estrés alto → Sugerir pausa
        if estado['estres'] > self.umbral_estres:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.SUGERENCIA,
                decision="SUGERIR_PAUSA",
                razon=self._generar_razon_pausa(estado),
                prioridad=NivelPrioridad.MEDIA,
                certeza=estado['estres'],
                metadata={'estado': estado}
            )
        
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.NEUTRAL,
            decision="ESTADO_NORMAL",
            razon="Estado emocional equilibrado",
            prioridad=NivelPrioridad.BAJA,
            certeza=0.7,
            metadata={}
        )
    
    def _detectar_estado_emocional(self, situacion: Dict[str, Any]) -> Dict:
        """Detecta estado emocional del usuario."""
        
        estado = {
            'estres': 0.0,
            'frustracion': 0.0
        }
        
        # Indicador 1: Tiempo continuo de trabajo
        if self.interacciones_recientes:
            tiempo_minutos = self._calcular_tiempo_trabajo()
            
            if tiempo_minutos > 120:  # 2 horas
                estado['estres'] = min(tiempo_minutos / 240, 0.9)  # Max 4h = 90%
        
        # Indicador 2: Palabras de frustración
        texto = situacion.get('texto_usuario', '').lower()
        palabras_frustracion = ['error', 'no funciona', 'fallo', 'mal', 'problema']
        
        if any(p in texto for p in palabras_frustracion):
            estado['frustracion'] += 0.3
        
        return estado
    
    def _calcular_tiempo_trabajo(self) -> int:
        """Calcula minutos de trabajo continuo."""
        
        if len(self.interacciones_recientes) < 2:
            return 0
        
        # Tiempo entre primera y última interacción
        delta = self.interacciones_recientes[-1] - self.interacciones_recientes[0]
        return int(delta.total_seconds() / 60)
    
    def _detectar_problemas_tono(self, texto: str) -> List[Dict]:
        """Detecta problemas en tono de comunicación."""
        
        problemas = []
        texto_lower = texto.lower()
        
        # Palabras condescendientes
        for palabra in self.palabras_problematicas:
            if palabra in texto_lower:
                problemas.append({
                    'tipo': 'CONDESCENDIENTE',
                    'severidad': 0.6,
                    'palabra': palabra
                })
        
        return problemas
    
    def _generar_razon_pausa(self, estado: Dict) -> str:
        """Genera sugerencia de pausa."""
        
        tiempo = self._calcular_tiempo_trabajo()
        
        razon = f"Llevas {tiempo} minutos de trabajo continuo.\n\n"
        razon += f"Indicadores:\n"
        razon += f"- Estrés estimado: {estado['estres']:.0%}\n\n"
        razon += "Los humanos rinden menos después de 90-120 minutos.\n\n"
        razon += "Sugerencia: 10-15 minutos de descanso."
        
        return razon
    
    def _generar_razon_tono(self, problemas: List[Dict]) -> str:
        """Genera explicación de problemas de tono."""
        
        razon = "Aspectos que mejorarían la comunicación:\n\n"
        
        for prob in problemas:
            razon += f"• Evitar '{prob['palabra']}' - puede sonar condescendiente\n"
        
        return razon