"""
TraductorSalida - Traduce conceptos anclados → español natural.
"""

from typing import Dict, List
import random


class TraductorSalida:
    """
    Traduce conceptos anclados → español natural.
    
    Genera respuestas variadas, NO usa templates fijos.
    """
    
    def __init__(self):
        # Variaciones de frases
        self.afirmaciones = [
            "Sí, puedo {accion}",
            "Claro, puedo {accion}",
            "Sí, tengo capacidad para {accion}",
            "Puedo {accion}",
        ]
        
        self.negaciones = [
            "No puedo {accion}",
            "No tengo capacidad para {accion}",
            "Ese no es algo que pueda hacer",
        ]
    
    def generar(self, decision: Dict, opiniones_consejo: List = None) -> str:
        """
        Genera respuesta en español natural.
        
        Args:
            decision: Output del MotorRazonamiento
            opiniones_consejo: Opiniones del consejo (opcional)
            
        Returns:
            Texto en español natural
        """
        tipo = decision['tipo_respuesta']
        
        # 1. Respuesta directa (social o conocimiento)
        if 'respuesta_directa' in decision:
            return decision['respuesta_directa']
        
        # 2. Pregunta de capacidad - afirmativa
        if tipo == 'afirmativa':
            return self._generar_afirmativa(decision)
        
        # 3. Pregunta de capacidad - negativa
        elif tipo == 'negativa':
            return self._generar_negativa(decision)
        
        # 4. Parcial
        elif tipo == 'parcial':
            return self._generar_parcial(decision)
        
        # 5. Comando aceptado
        elif tipo == 'comando_aceptado':
            return self._generar_comando_aceptado(decision)
        
        # 6. Comando rechazado
        elif tipo == 'comando_rechazado':
            return self._generar_comando_rechazado(decision)
        
        # 7. No entendido
        elif tipo == 'no_entendido':
            return "No entendí tu consulta. ¿Podrías reformularla?"
        
        # 8. Conocimiento sin info
        elif tipo == 'conocimiento_sin_info':
            return "No tengo información sobre eso en mi conocimiento actual."
        
        # Fallback
        else:
            return "Procesando..."
    
    def _generar_afirmativa(self, decision: Dict) -> str:
        """Genera respuesta afirmativa para pregunta de capacidad."""
        ops = decision.get('operaciones', [])
        
        if not ops:
            return "Sí, puedo hacerlo."
        
        template = random.choice(self.afirmaciones)
        
        if len(ops) == 1:
            accion_texto = ops[0].replace('_', ' ')
        else:
            accion_texto = ", ".join(ops[:-1]) + f" y {ops[-1]}"
            accion_texto = accion_texto.replace('_', ' ')
        
        respuesta = template.format(accion=accion_texto)
        
        if decision.get('certeza', 0) >= 0.9 and len(ops) <= 5:
            respuesta += f"\n\nOperaciones disponibles:"
            for op in ops:
                respuesta += f"\n• {op.replace('_', ' ')}"
        
        return respuesta
    
    def _generar_negativa(self, decision: Dict) -> str:
        """Genera respuesta negativa honesta."""
        razon = decision.get('razon', 'Capacidad no disponible')
        
        return (
            f"No puedo hacer eso.\n\n"
            f"Razón: {razon}"
        )
    
    def _generar_parcial(self, decision: Dict) -> str:
        """Genera respuesta parcial."""
        puede = decision.get('operaciones', [])
        razon = decision.get('razon', 'Capacidad limitada')
        
        if not puede:
            return self._generar_negativa(decision)
        
        ops_texto = ", ".join(puede).replace('_', ' ')
        
        return (
            f"Puedo hacer parte de esto.\n\n"
            f"Capacidades disponibles: {ops_texto}\n\n"
            f"Limitación: {razon}"
        )
    
    def _generar_comando_aceptado(self, decision: Dict) -> str:
        """Comando que se puede ejecutar."""
        return "Entendido. Puedo ejecutar eso. (En Fase 1 solo confirmo; ejecución real en Fase 2+)"
    
    def _generar_comando_rechazado(self, decision: Dict) -> str:
        """Comando que NO se puede ejecutar."""
        razon = decision.get('razon', 'No puedo ejecutar eso')
        return f"No puedo ejecutar ese comando.\n\n{razon}"