"""
Conceptos Python Básico - Semana 2.

15 conceptos de programación Python.
Grounding medio-alto (Bell puede trabajar con código Python).
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_python():
    """Retorna conceptos de Python (15 conceptos)."""
    conceptos = []
    
    # ESTRUCTURAS BÁSICAS (5)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_VARIABLE",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["variable", "var"],
        confianza_grounding=0.8,
        propiedades={
            'es_contenedor': True,
            'mutable': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_FUNCION",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["función", "function", "def"],
        confianza_grounding=0.8,
        propiedades={
            'es_bloque_codigo': True,
            'puede_retornar': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CLASE",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["clase", "class"],
        confianza_grounding=0.7,
        propiedades={
            'es_plantilla': True,
            'tiene_metodos': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_LISTA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["lista", "list", "array"],
        confianza_grounding=0.8,
        propiedades={
            'es_coleccion': True,
            'ordenada': True,
            'mutable': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DICCIONARIO",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["diccionario", "dict", "map"],
        confianza_grounding=0.8,
        propiedades={
            'es_coleccion': True,
            'clave_valor': True
        }
    ))
    
    # CONTROL DE FLUJO (5)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_IF",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["if", "si", "condicional"],
        confianza_grounding=0.8,
        propiedades={
            'es_control_flujo': True,
            'evalua_condicion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_FOR",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["for", "bucle", "loop"],
        confianza_grounding=0.8,
        propiedades={
            'es_iteracion': True,
            'controlado': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_WHILE",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["while", "mientras"],
        confianza_grounding=0.8,
        propiedades={
            'es_iteracion': True,
            'condicional': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RETURN",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["return", "retornar", "devolver"],
        confianza_grounding=0.8,
        propiedades={
            'termina_funcion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_IMPORT",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["import", "importar"],
        confianza_grounding=0.8,
        propiedades={
            'carga_modulo': True
        }
    ))
    
    # OPERACIONES (5)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PRINT",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["print", "imprimir", "mostrar"],
        confianza_grounding=0.9,
        propiedades={
            'es_salida': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_INPUT",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["input", "entrada", "leer"],
        confianza_grounding=0.9,
        propiedades={
            'es_entrada': True,
            'espera_usuario': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_LEN",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["len", "longitud", "tamaño"],
        confianza_grounding=0.9,
        propiedades={
            'retorna_entero': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_TYPE",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["type", "tipo"],
        confianza_grounding=0.9,
        propiedades={
            'retorna_tipo': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_STR",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["str", "string", "texto", "cadena"],
        confianza_grounding=0.8,
        propiedades={
            'es_tipo_dato': True,
            'inmutable': True
        }
    ))
    
    return conceptos