# consejeras/echo.py

"""
Echo - La Lógica
Especialidad: Detección de contradicciones y coherencia lógica
"""

from typing import Dict, Any, List
from consejeras.consejera_base import (
    ConsejeraBase, Opinion, TipoOpinion, NivelPrioridad
)
from datetime import datetime


class Echo(ConsejeraBase):
    """
    Echo - La Lógica.
    
    Detecta:
    - Contradicciones con decisiones previas
    - Incoherencias lógicas
    - Inconsistencias en razonamiento
    """
    
    def __init__(self):
        super().__init__(
            nombre="Echo",
            especialidad="Guardiana de Coherencia Lógica"
        )
        
        self.decisiones_previas = []
        self.max_historial = 20  # Mantener últimas 20 decisiones
    
    def debe_intervenir(self, situacion: Dict[str, Any]) -> Opinion:
        """Decide si Echo debe intervenir."""
        
        # Verificar contradicciones
        contradicciones = self._detectar_contradicciones(situacion)
        
        if contradicciones:
            return self.analizar(situacion)
        
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.APROBACION,
            decision="COHERENTE",
            razon="No detecté contradicciones lógicas",
            prioridad=NivelPrioridad.BAJA,
            certeza=0.9,
            metadata={}
        )
    
    def analizar(self, situacion: Dict[str, Any]) -> Opinion:
        """Analiza coherencia lógica."""
        
        contradicciones = self._detectar_contradicciones(situacion)
        
        if not contradicciones:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.APROBACION,
                decision="COHERENTE",
                razon="Lógicamente coherente",
                prioridad=NivelPrioridad.BAJA,
                certeza=0.9,
                metadata={}
            )
        
        # Hay contradicciones
        severidad = max(c['severidad'] for c in contradicciones)
        
        return Opinion(
            consejera=self.nombre,
            tipo=TipoOpinion.ADVERTENCIA,
            decision="CONTRADICCION_DETECTADA",
            razon=self._generar_razon(contradicciones),
            prioridad=NivelPrioridad.ALTA,
            certeza=severidad,
            metadata={'contradicciones': contradicciones}
        )
    
    def _detectar_contradicciones(self, situacion: Dict[str, Any]) -> List[Dict]:
        """Detecta contradicciones con decisiones previas."""
        
        contradicciones = []
        
        decision_actual = situacion.get('decision_propuesta', {})
        
        if not decision_actual:
            return []
        
        contexto_actual = decision_actual.get('contexto', '')
        decision_actual_valor = decision_actual.get('decision', '')
        
        if not contexto_actual or not decision_actual_valor:
            return []
        
        # Buscar en historial decisiones del mismo contexto
        for prev in self.decisiones_previas:
            contexto_prev = prev.get('contexto', '')
            decision_prev = prev.get('decision', '')
            
            # Mismo contexto?
            if contexto_actual == contexto_prev:
                # Decisiones contradictorias?
                if self._son_decisiones_opuestas(decision_actual_valor, decision_prev):
                    contradicciones.append({
                        'decision_previa': prev,
                        'decision_actual': decision_actual,
                        'severidad': 0.8,
                        'razon': f'Decisiones opuestas sobre {contexto_actual}'
                    })
        
        return contradicciones
    
    def _son_decisiones_opuestas(self, d1: str, d2: str) -> bool:
        """Verifica si dos decisiones son opuestas."""
        
        # Pares contradictorios conocidos
        contradictorios = [
            ('APROBAR', 'RECHAZAR'),
            ('OPTIMIZAR', 'MANTENER'),
            ('PROCEDER', 'DETENER'),
            ('ACEPTAR', 'RECHAZAR'),
            ('SÍ', 'NO'),
            ('PERMITIR', 'PROHIBIR')
        ]
        
        d1_upper = d1.upper()
        d2_upper = d2.upper()
        
        for par in contradictorios:
            if (d1_upper, d2_upper) == par or (d2_upper, d1_upper) == par:
                return True
        
        return False
    
    def _generar_razon(self, contradicciones: List[Dict]) -> str:
        """Genera explicación de contradicciones."""
        
        razon = "Detecté contradicciones lógicas:\n\n"
        
        for c in contradicciones:
            razon += f"• {c['razon']}\n"
            razon += f"  Decisión previa: {c['decision_previa'].get('decision', 'N/A')}\n"
            razon += f"  Decisión actual: {c['decision_actual'].get('decision', 'N/A')}\n\n"
        
        razon += "Se debe resolver la contradicción antes de proceder."
        
        return razon
    
    def registrar_decision(self, decision: Dict):
        """
        Registra decisión para verificación futura.
        
        IMPORTANTE: Llamar después de cada deliberación.
        """
        
        if not decision:
            return
        
        registro = {
            'contexto': decision.get('contexto', 'general'),
            'decision': decision.get('decision', ''),
            'timestamp': datetime.now().isoformat()
        }
        
        self.decisiones_previas.append(registro)
        
        # Mantener solo últimas N
        if len(self.decisiones_previas) > self.max_historial:
            self.decisiones_previas = self.decisiones_previas[-self.max_historial:]