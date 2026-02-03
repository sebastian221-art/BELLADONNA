"""
Verbos Comunes - Semana 2.

10 verbos de acción frecuentes en conversación.
Grounding medio (0.7-0.8) - conceptos de acción sin operaciones directas.
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_verbos():
    """Retorna verbos comunes (10 conceptos)."""
    conceptos = []
    
    # VERBOS DE NECESIDAD/DESEO (3)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_NECESITAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["necesitar", "necesito", "requiero", "preciso"],
        confianza_grounding=0.7,
        propiedades={
            'expresa_necesidad': True,
            'prioridad': 'alta'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_QUERER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["querer", "quiero", "desear", "deseo"],
        confianza_grounding=0.7,
        propiedades={
            'expresa_deseo': True,
            'prioridad': 'media'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_BUSCAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["buscar", "encontrar", "localizar"],
        confianza_grounding=0.8,
        propiedades={
            'es_busqueda': True,
            'retorna_resultado': True
        }
    ))
    
    # VERBOS DE COMUNICACIÓN (3)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DECIR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["decir", "mencionar", "comentar", "expresar"],
        confianza_grounding=0.7,
        propiedades={
            'es_comunicacion': True,
            'direccion': 'salida'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PREGUNTAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["preguntar", "consultar", "indagar"],
        confianza_grounding=0.7,
        propiedades={
            'es_comunicacion': True,
            'requiere_respuesta': True
        },
        relaciones={'relacionado_con': {'CONCEPTO_PREGUNTA'}}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["dar", "proporcionar", "proveer", "entregar"],
        confianza_grounding=0.7,
        propiedades={
            'es_transferencia': True,
            'direccion': 'hacia_otro'
        }
    ))
    
    # VERBOS DE PROCESO (4)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_USAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["usar", "utilizar", "emplear"],
        confianza_grounding=0.8,
        propiedades={
            'es_uso': True,
            'requiere_objeto': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_VER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["ver", "mirar", "observar", "revisar"],
        confianza_grounding=0.7,
        propiedades={
            'es_percepcion': True,
            'sentido': 'visual'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_TENER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["tener", "poseer", "contar"],
        confianza_grounding=0.7,
        propiedades={
            'es_posesion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_OBTENER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["obtener", "conseguir", "adquirir", "lograr"],
        confianza_grounding=0.7,
        propiedades={
            'es_adquisicion': True,
            'cambia_estado': True
        }
    ))
    
    return conceptos