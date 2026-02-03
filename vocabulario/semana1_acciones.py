"""
Conceptos de Acciones - Semana 1.

5 conceptos finales para completar los 30 de Semana 1.
Acciones básicas de manipulación.
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_acciones():
    """Retorna conceptos de acciones (5 conceptos)."""
    conceptos = []
    
    # ACCIONES BÁSICAS
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MOSTRAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["mostrar", "show", "enseñar", "display"],
        confianza_grounding=0.7,
        propiedades={'es_comunicacion': True}
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MODIFICAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["modificar", "cambiar", "editar", "actualizar"],
        confianza_grounding=0.8,
        propiedades={
            'es_accion_destructiva': False,
            'requiere_confirmacion': False
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ELIMINAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["eliminar", "borrar", "delete", "remover"],
        confianza_grounding=0.8,
        propiedades={
            'es_accion_destructiva': True,
            'requiere_confirmacion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PREGUNTA",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["pregunta", "preguntar", "cuestión", "consulta"],
        confianza_grounding=0.7,
        propiedades={
            'requiere_respuesta': True,
            'es_interaccion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RESPUESTA",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["respuesta", "responder", "contestar", "reply"],
        confianza_grounding=0.7,
        propiedades={
            'es_interaccion': True
        },
        relaciones={'responde_a': {'CONCEPTO_PREGUNTA'}}
    ))
    
    return conceptos