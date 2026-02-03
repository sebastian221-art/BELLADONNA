"""
Generador de Salida - Decision → Español Natural.
"""
from typing import Dict, Optional
from razonamiento.tipos_decision import Decision, TipoDecision, RazonRechazo
from generacion.templates_respuesta import TemplatesRespuesta

class GeneradorSalida:
    """Genera respuestas en español a partir de decisiones."""
    
    def __init__(self):
        """Inicializa generador."""
        self.templates = TemplatesRespuesta()
    
    def generar(self, decision: Decision, contexto: Dict = None) -> str:
        """
        Genera respuesta en español.
        
        CRÍTICO: Verifica veto de Vega PRIMERO.
        """
        contexto = contexto or {}
        
        # VERIFICACIÓN CRÍTICA: ¿Vega vetó?
        revision_vega = contexto.get('revision_vega', {})
        if revision_vega.get('veto', False):
            # Vega vetó → Generar respuesta NEGATIVA independientemente de la decisión
            return self._generar_veto_vega(decision, contexto)
        
        # Sin veto → Proceder según tipo de decisión
        if decision.tipo == TipoDecision.AFIRMATIVA:
            return self._generar_afirmativa(decision, contexto)
        
        elif decision.tipo == TipoDecision.NEGATIVA:
            return self._generar_negativa(decision, contexto)
        
        elif decision.tipo == TipoDecision.SALUDO:
            return self._generar_saludo(decision)
        
        elif decision.tipo == TipoDecision.AGRADECIMIENTO:
            return self._generar_agradecimiento(decision)
        
        elif decision.tipo == TipoDecision.NO_ENTENDIDO:
            return self._generar_no_entendido(decision, contexto)
        
        elif decision.tipo == TipoDecision.NECESITA_ACLARACION:
            return self._generar_aclaracion(decision)
        
        else:
            return "No puedo procesar esta solicitud."
    
    def _generar_veto_vega(self, decision: Decision, contexto: Dict) -> str:
        """Genera respuesta cuando Vega vetó (NUEVO)."""
        revision_vega = contexto.get('revision_vega', {})
        
        template = self.templates.obtener_template(
            TipoDecision.NEGATIVA,
            subtipo=RazonRechazo.VEGA_VETO
        )
        
        accion = self._extraer_accion(decision, contexto)
        principio = revision_vega.get('principio_violado')
        
        respuesta = template.format(
            accion=accion,
            principio=principio.name if principio else 'desconocido',
            razon_veto=revision_vega.get('razon_veto', 'Acción bloqueada'),
            recomendacion=revision_vega.get('recomendacion', '')
        )
        
        return respuesta
    
    def _generar_afirmativa(self, decision: Decision, contexto: Dict) -> str:
        """Genera respuesta afirmativa."""
        if decision.certeza >= 0.9:
            subtipo = 'certeza_alta'
        else:
            subtipo = 'certeza_media'
        
        template = self.templates.obtener_template(
            TipoDecision.AFIRMATIVA, 
            subtipo=subtipo
        )
        
        accion = self._extraer_accion(decision, contexto)
        
        respuesta = template.format(
            accion=accion,
            grounding=f"{decision.certeza:.2f}",
            operacion=decision.operacion_disponible or "N/A",
            certeza=int(decision.certeza * 100)
        )
        
        return respuesta
    
    def _generar_negativa(self, decision: Decision, contexto: Dict) -> str:
        """Genera respuesta negativa."""
        subtipo = decision.razon_rechazo or RazonRechazo.SIN_OPERACION
        
        template = self.templates.obtener_template(
            TipoDecision.NEGATIVA,
            subtipo=subtipo
        )
        
        accion = self._extraer_accion(decision, contexto)
        
        respuesta = template.format(
            accion=accion,
            razon=decision.razon,
            grounding=f"{decision.certeza:.2f}"
        )
        
        return respuesta
    
    def _generar_saludo(self, decision: Decision) -> str:
        """Genera respuesta a saludo."""
        template = self.templates.obtener_template(TipoDecision.SALUDO)
        return template
    
    def _generar_agradecimiento(self, decision: Decision) -> str:
        """Genera respuesta a agradecimiento."""
        template = self.templates.obtener_template(TipoDecision.AGRADECIMIENTO)
        return template
    
    def _generar_no_entendido(self, decision: Decision, contexto: Dict) -> str:
        """Genera respuesta cuando no entendió."""
        template = self.templates.obtener_template(TipoDecision.NO_ENTENDIDO)
        
        traduccion = contexto.get('traduccion', {})
        confianza = traduccion.get('confianza', 0.0)
        desconocidas = traduccion.get('palabras_desconocidas', [])
        
        respuesta = template.format(
            confianza=int(confianza * 100),
            desconocidas=", ".join(desconocidas[:3])
        )
        
        return respuesta
    
    def _generar_aclaracion(self, decision: Decision) -> str:
        """Genera solicitud de aclaración."""
        template = self.templates.obtener_template(TipoDecision.NECESITA_ACLARACION)
        return template.format(razon=decision.razon)
    
    def _extraer_accion(self, decision: Decision, contexto: Dict) -> str:
        """Extrae la acción principal del contexto."""
        traduccion = contexto.get('traduccion', {})
        
        if decision.conceptos_principales:
            concepto_id = decision.conceptos_principales[0]
            accion = concepto_id.replace('CONCEPTO_', '').lower()
            return accion
        
        texto_original = traduccion.get('texto_original', '')
        if texto_original:
            palabras = texto_original.split()[:5]
            return " ".join(palabras)
        
        return "esta acción"
    
    def generar_con_razonamiento(self, decision: Decision, 
                                 contexto: Dict = None,
                                 incluir_pasos: bool = False) -> str:
        """Genera respuesta con explicación opcional del razonamiento."""
        respuesta = self.generar(decision, contexto)
        
        if incluir_pasos and decision.pasos_razonamiento:
            respuesta += "\n\nRazonamiento:"
            for i, paso in enumerate(decision.pasos_razonamiento, 1):
                respuesta += f"\n  {i}. {paso}"
        
        return respuesta