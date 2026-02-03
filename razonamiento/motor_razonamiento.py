"""
Motor de Razonamiento - El cerebro de Bell.

Recibe traducción → Genera decisión.
"""
from typing import Dict
from razonamiento.tipos_decision import Decision
from razonamiento.generador_decisiones import GeneradorDecisiones

class MotorRazonamiento:
    """
    El cerebro de Bell.
    
    Proceso:
    1. Recibe traducción (conceptos + intención)
    2. Evalúa qué puede hacer
    3. Genera decisión estructurada
    
    Bell NO piensa como humano. Bell evalúa grounding.
    """
    
    def __init__(self):
        """Inicializa motor."""
        self.generador = GeneradorDecisiones()
    
    def razonar(self, traduccion: Dict) -> Decision:
        """
        Razona sobre una traducción y genera una decisión.
        
        Args:
            traduccion: Dict retornado por TraductorEntrada
            
        Returns:
            Decision object
        """
        conceptos = traduccion['conceptos']
        intencion = traduccion['intencion']
        confianza = traduccion['confianza']
        
        # Si confianza muy baja → NO_ENTENDIDO
        if confianza < 0.3:
            return self.generador.generar_decision_no_entendido(confianza)
        
        # Procesar según intención
        if intencion == 'SALUDO':
            return self.generador.generar_decision_saludo(conceptos)
        
        elif intencion == 'AGRADECIMIENTO':
            return self.generador.generar_decision_agradecimiento(conceptos)
        
        elif intencion == 'PREGUNTA_CAPACIDAD':
            return self.generador.generar_decision_capacidad(conceptos, intencion)
        
        elif intencion == 'PETICION_ACCION':
            # Evaluar si puede hacer la acción
            return self.generador.generar_decision_capacidad(conceptos, intencion)
        
        elif intencion == 'PREGUNTA_INFO':
            # Por ahora, mismo tratamiento que capacidad
            # En Fase 2 esto será diferente
            return self.generador.generar_decision_capacidad(conceptos, intencion)
        
        else:
            # CONVERSACION genérica
            # Por ahora, evaluar capacidad general
            return self.generador.generar_decision_capacidad(conceptos, intencion)
    
    def explicar_decision(self, decision: Decision) -> str:
        """
        Genera explicación legible de una decisión.
        
        Útil para debugging.
        """
        explicacion = f"""
Decisión: {decision.tipo.name}
Certeza: {decision.certeza:.0%}
Puede ejecutar: {decision.puede_ejecutar}

Razonamiento:
{chr(10).join(decision.pasos_razonamiento)}

Conclusión: {decision.razon}
        """.strip()
        
        return explicacion