"""
Conceptos de Tiempo y Temporalidad - Semana 4.

15 conceptos relacionados con tiempo, fechas, duraciones.
Grounding medio (0.70-0.80).
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_tiempo():
    """Retorna conceptos de tiempo (15 conceptos)."""
    conceptos = []
    
    # MOMENTOS TEMPORALES (5)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_HOY",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["hoy", "today"],
        confianza_grounding=0.80,
        propiedades={
            'es_temporal': True,
            'relativo': True,
            'precision': 'dia'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_AYER",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["ayer", "yesterday"],
        confianza_grounding=0.80,
        propiedades={
            'es_temporal': True,
            'relativo': True,
            'direccion': 'pasado'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MAÑANA",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["mañana", "tomorrow"],
        confianza_grounding=0.80,
        propiedades={
            'es_temporal': True,
            'relativo': True,
            'direccion': 'futuro'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ANTES",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["antes", "previo", "anterior"],
        confianza_grounding=0.75,
        propiedades={
            'es_temporal': True,
            'es_comparativo': True,
            'direccion': 'pasado'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DESPUES",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["después", "luego", "posterior"],
        confianza_grounding=0.75,
        propiedades={
            'es_temporal': True,
            'es_comparativo': True,
            'direccion': 'futuro'
        }
    ))
    
    # DURACIONES (5)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_SEGUNDO",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["segundo", "segundos"],
        confianza_grounding=0.75,
        propiedades={
            'es_unidad_tiempo': True,
            'duracion_segundos': 1
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MINUTO",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["minuto", "minutos"],
        confianza_grounding=0.75,
        propiedades={
            'es_unidad_tiempo': True,
            'duracion_segundos': 60
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_HORA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["hora", "horas"],
        confianza_grounding=0.75,
        propiedades={
            'es_unidad_tiempo': True,
            'duracion_segundos': 3600
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DIA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["día", "dias"],
        confianza_grounding=0.75,
        propiedades={
            'es_unidad_tiempo': True,
            'duracion_segundos': 86400
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_SEMANA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["semana", "semanas"],
        confianza_grounding=0.75,
        propiedades={
            'es_unidad_tiempo': True,
            'duracion_segundos': 604800
        }
    ))
    
    # VELOCIDAD/FRECUENCIA TEMPORAL (5)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RAPIDO_TIEMPO",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["pronto", "rápido"],
        confianza_grounding=0.70,
        propiedades={
            'es_velocidad_temporal': True,
            'valor': 'alto'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_LENTO_TIEMPO",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["tarde", "despacio"],
        confianza_grounding=0.70,
        propiedades={
            'es_velocidad_temporal': True,
            'valor': 'bajo'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_AHORA",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["ahora", "ya", "inmediatamente"],
        confianza_grounding=0.80,
        propiedades={
            'es_temporal': True,
            'momento': 'presente',
            'urgencia': 'alta'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_SIEMPRE",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["siempre", "constantemente"],
        confianza_grounding=0.75,
        propiedades={
            'es_frecuencia': True,
            'valor': 'continuo'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_NUNCA",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["nunca", "jamás"],
        confianza_grounding=0.75,
        propiedades={
            'es_frecuencia': True,
            'valor': 'ninguno',
            'es_negacion': True
        }
    ))
    
    return conceptos