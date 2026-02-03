"""
Conceptos de Conversación - Semana 1.

10 conceptos de palabras básicas de conversación.
Incluye saludos, interrogativos, afirmación/negación.
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_conversacion():
    """Retorna conceptos de conversación (10 conceptos)."""
    conceptos = []
    
    # SALUDOS Y CORTESÍA (2)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_HOLA",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["hola", "hi", "hello", "hey"],
        confianza_grounding=0.9,
        propiedades={
            'es_saludo': True,
            'requiere_respuesta': True
        },
        datos={
            'respuestas_apropiadas': [
                "Hola, ¿en qué puedo ayudarte?",
                "¡Hola! ¿Qué necesitas?"
            ]
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_GRACIAS",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["gracias", "thanks", "thank you"],
        confianza_grounding=0.9,
        propiedades={
            'es_agradecimiento': True
        }
    ))
    
    # AFIRMACIÓN/NEGACIÓN (2)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_SI",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["sí", "si", "yes", "afirmativo"],
        confianza_grounding=0.9,
        propiedades={'es_afirmacion': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_NO",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["no", "nope", "negativo"],
        confianza_grounding=0.9,
        propiedades={'es_negacion': True}
    ))
    
    # INTERROGATIVOS (6)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_QUE",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["qué", "que", "what"],
        confianza_grounding=0.8,
        propiedades={'es_interrogativo': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_COMO",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["cómo", "como", "how"],
        confianza_grounding=0.8,
        propiedades={'es_interrogativo': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_QUIEN",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["quién", "quien", "who"],
        confianza_grounding=0.8,
        propiedades={'es_interrogativo': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DONDE",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["dónde", "donde", "where"],
        confianza_grounding=0.8,
        propiedades={'es_interrogativo': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CUANDO",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["cuándo", "cuando", "when"],
        confianza_grounding=0.8,
        propiedades={'es_interrogativo': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_POR_QUE",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["por qué", "porque", "why"],
        confianza_grounding=0.8,
        propiedades={
            'es_interrogativo': True,
            'pide_razon': True
        }
    ))
    
    return conceptos