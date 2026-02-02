"""
Conceptos Conversacionales - Palabras comunes de conversación.
"""

from typing import Dict
from core.concepto_anclado import ConceptoAnclado, TipoConcepto


def crear_concepto_saludo() -> ConceptoAnclado:
    """CONCEPTO: SALUDO"""
    return ConceptoAnclado(
        id="CONCEPTO_SALUDO",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["hola", "hey", "hi", "buenos", "buenas", "saludos"],
        operaciones={},
        relaciones={'es_un': {'EXPRESION_CONVERSACIONAL'}},
        propiedades={'intención': 'iniciar_conversación'},
        datos={'definicion': 'Expresión para iniciar conversación'},
        accesible_directamente=False,
        confianza_grounding=0.9
    )


def crear_concepto_despedida() -> ConceptoAnclado:
    """CONCEPTO: DESPEDIDA"""
    return ConceptoAnclado(
        id="CONCEPTO_DESPEDIDA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["adiós", "adios", "chao", "hasta", "luego", "vemos", "bye", "salir"],
        operaciones={},
        relaciones={'es_un': {'EXPRESION_CONVERSACIONAL'}},
        propiedades={'intención': 'finalizar_conversación'},
        datos={'definicion': 'Expresión para finalizar conversación'},
        accesible_directamente=False,
        confianza_grounding=0.9
    )


def crear_concepto_pregunta() -> ConceptoAnclado:
    """CONCEPTO: PREGUNTA"""
    return ConceptoAnclado(
        id="CONCEPTO_PREGUNTA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["qué", "quién", "cuándo", "dónde", "por", "cómo", "cuál", "puedes"],
        operaciones={},
        relaciones={'es_un': {'EXPRESION_CONVERSACIONAL'}},
        propiedades={'intención': 'solicitar_información'},
        datos={'definicion': 'Solicitud de información'},
        accesible_directamente=False,
        confianza_grounding=0.9
    )


def crear_concepto_afirmacion() -> ConceptoAnclado:
    """CONCEPTO: AFIRMACION"""
    return ConceptoAnclado(
        id="CONCEPTO_AFIRMACION",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["sí", "si", "claro", "ok", "vale", "perfecto"],
        operaciones={},
        relaciones={'es_un': {'EXPRESION_CONVERSACIONAL'}},
        propiedades={'intención': 'confirmar'},
        datos={'definicion': 'Confirmación o acuerdo'},
        accesible_directamente=False,
        confianza_grounding=0.9
    )


def crear_concepto_nombre() -> ConceptoAnclado:
    """CONCEPTO: NOMBRE"""
    return ConceptoAnclado(
        id="CONCEPTO_NOMBRE",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["llamo", "nombre", "soy"],
        operaciones={},
        relaciones={'es_un': {'EXPRESION_CONVERSACIONAL'}},
        propiedades={'intención': 'identificar'},
        datos={'definicion': 'Identificación de persona'},
        accesible_directamente=False,
        confianza_grounding=0.8
    )


def obtener_conceptos_conversacionales() -> Dict[str, ConceptoAnclado]:
    """Retorna los 5 conceptos conversacionales."""
    conceptos = [
        crear_concepto_saludo(),
        crear_concepto_despedida(),
        crear_concepto_pregunta(),
        crear_concepto_afirmacion(),
        crear_concepto_nombre()
    ]
    return {c.id: c for c in conceptos}