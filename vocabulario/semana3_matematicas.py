"""
Conceptos Matemáticos - Semana 3.

20 conceptos de operaciones y términos matemáticos.
Grounding medio-alto (0.75-0.85).
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_matematicas():
    """Retorna conceptos matemáticos (20 conceptos)."""
    conceptos = []
    
    # OPERACIONES BÁSICAS (4) - RENOMBRADOS para evitar duplicados
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_SUMA",  # ← RENOMBRADO de CONCEPTO_SUMAR
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["suma", "adición", "más"],
        confianza_grounding=0.85,
        propiedades={
            'es_operacion': True,
            'simbolo': '+',
            'conmutativa': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RESTA",  # ← RENOMBRADO de CONCEPTO_RESTAR
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["resta", "sustracción", "menos"],
        confianza_grounding=0.85,
        propiedades={
            'es_operacion': True,
            'simbolo': '-',
            'conmutativa': False
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MULTIPLICACION",  # ← RENOMBRADO de CONCEPTO_MULTIPLICAR
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["multiplicación", "producto", "por"],
        confianza_grounding=0.85,
        propiedades={
            'es_operacion': True,
            'simbolo': '*',
            'conmutativa': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DIVISION",  # ← RENOMBRADO de CONCEPTO_DIVIDIR
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["división", "dividir", "entre"],
        confianza_grounding=0.85,
        propiedades={
            'es_operacion': True,
            'simbolo': '/',
            'conmutativa': False,
            'puede_error': True
        }
    ))
    
    # TÉRMINOS NUMÉRICOS (4)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ENTERO",  # ← Más específico que CONCEPTO_NUMERO
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["entero", "integer", "número entero"],
        confianza_grounding=0.80,
        propiedades={
            'es_tipo_numerico': True,
            'tiene_decimales': False
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DECIMAL",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["decimal", "flotante", "float"],
        confianza_grounding=0.80,
        propiedades={
            'es_tipo_numerico': True,
            'tiene_decimales': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_POSITIVO",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["positivo", "mayor que cero"],
        confianza_grounding=0.75,
        propiedades={
            'es_signo': True,
            'valor': '> 0'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_NEGATIVO",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["negativo", "menor que cero"],
        confianza_grounding=0.75,
        propiedades={
            'es_signo': True,
            'valor': '< 0'
        }
    ))
    
    # OPERACIONES AVANZADAS (6)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_POTENCIA",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["potencia", "exponente", "elevado"],
        confianza_grounding=0.80,
        propiedades={
            'es_operacion': True,
            'simbolo': '**'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RAIZ",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["raíz", "raíz cuadrada", "sqrt"],
        confianza_grounding=0.80,
        propiedades={
            'es_operacion': True,
            'inversa_de': 'potencia'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MODULO",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["módulo", "resto", "mod"],
        confianza_grounding=0.80,
        propiedades={
            'es_operacion': True,
            'simbolo': '%',
            'retorna': 'resto'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ABS",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["absoluto", "abs", "valor absoluto"],
        confianza_grounding=0.80,
        propiedades={
            'es_funcion': True,
            'retorna': 'positivo'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_REDONDEO",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["redondear", "round", "aproximar"],
        confianza_grounding=0.75,
        propiedades={
            'es_funcion': True,
            'modifica_precision': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MAXIMO",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["máximo", "max", "mayor"],
        confianza_grounding=0.80,
        propiedades={
            'es_comparacion': True,
            'retorna': 'mayor_valor'
        }
    ))
    
    # CONCEPTOS ESTADÍSTICOS (6)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PROMEDIO",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["promedio", "media", "average"],
        confianza_grounding=0.75,
        propiedades={
            'es_estadistica': True,
            'requiere': 'lista_numeros'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MINIMO",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["mínimo", "min", "menor"],
        confianza_grounding=0.80,
        propiedades={
            'es_comparacion': True,
            'retorna': 'menor_valor'
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RANGO",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["rango", "range", "intervalo"],
        confianza_grounding=0.75,
        propiedades={
            'tiene_inicio': True,
            'tiene_fin': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PORCENTAJE",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["porcentaje", "por ciento", "percent"],
        confianza_grounding=0.75,
        propiedades={
            'simbolo': '%',
            'base': 100
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_FRACCION",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["fracción", "quebrado", "racional"],
        confianza_grounding=0.70,
        propiedades={
            'tiene_numerador': True,
            'tiene_denominador': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ECUACION",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["ecuación", "igualdad", "fórmula"],
        confianza_grounding=0.70,
        propiedades={
            'tiene_variables': True,
            'tiene_igualdad': True
        }
    ))
    
    return conceptos