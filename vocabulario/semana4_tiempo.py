"""
Conceptos de Tiempo y Temporalidad - Semana 4.

10 conceptos relacionados con tiempo, fechas, duraciones.
Grounding medio (0.70-0.80).

NOTA: Se eliminaron 5 duplicados que ya existían en Semana 3:
- CONCEPTO_AHORA (ya en semana3_conversacion_expandida)
- CONCEPTO_ANTES (ya en semana3_conversacion_expandida)
- CONCEPTO_DESPUES (ya en semana3_conversacion_expandida)
- CONCEPTO_SIEMPRE (ya en semana3_conversacion_expandida)
- CONCEPTO_NUNCA (ya en semana3_conversacion_expandida)
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_tiempo():
    """Retorna conceptos de tiempo (10 conceptos - sin duplicados)."""
    conceptos = []
    
    # MOMENTOS TEMPORALES (3) - Eliminados: AHORA, ANTES, DESPUES (ya en Semana 3)
    
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
    
    # VELOCIDAD/FRECUENCIA TEMPORAL (2) - Eliminados: SIEMPRE, NUNCA (ya en Semana 3)
    
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
    
    return conceptos