"""
Conceptos Cognitivos - Semana 1.

10 conceptos de acciones mentales y capacidades.
Grounding más bajo (0.6-0.8) porque son abstractos.
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_cognitivos():
    """Retorna conceptos cognitivos (10 conceptos)."""
    conceptos = []
    
    # CAPACIDADES Y ACCIONES (4)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_AYUDA",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["ayuda", "help", "ayudar", "asistir"],
        confianza_grounding=0.8,
        propiedades={'es_peticion': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PODER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["poder", "puedes", "puedo", "capacidad"],
        confianza_grounding=0.8,
        relaciones={'relacionado_con': {'CONCEPTO_HACER'}},
        propiedades={'es_pregunta_capacidad': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_HACER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["hacer", "realizar", "ejecutar"],
        confianza_grounding=0.7,
        propiedades={'es_accion': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CREAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["crear", "create", "generar"],
        confianza_grounding=0.8,
        propiedades={'es_accion_constructiva': True}
    ))
    
    # PENSAMIENTO (3)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RAZONAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["razonar", "pensar", "analizar"],
        confianza_grounding=0.7,
        propiedades={'es_accion_interna': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DECIDIR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["decidir", "determinar", "elegir"],
        confianza_grounding=0.7,
        relaciones={'requiere': {'CONCEPTO_RAZONAR'}}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ENTENDER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["entender", "comprender", "captar"],
        confianza_grounding=0.6,
        propiedades={'es_cognitivo': True}
    ))
    
    # CONOCIMIENTO (3)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_SABER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["saber", "conocer"],
        confianza_grounding=0.7,
        propiedades={'es_estado': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_EXPLICAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["explicar", "explain", "aclarar"],
        confianza_grounding=0.7,
        propiedades={'es_comunicacion': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CERTEZA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["certeza", "seguridad", "confianza"],
        confianza_grounding=0.6,
        propiedades={
            'es_metrica': True,
            'rango': [0.0, 1.0]
        }
    ))
    
    return conceptos