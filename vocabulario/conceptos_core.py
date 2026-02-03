"""
Los primeros 5 conceptos de Bell (de 150 totales en Fase 1).
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto
from core.capacidades_bell import CapacidadesBell

def obtener_conceptos_core():
    """Retorna los conceptos iniciales."""
    conceptos = []
    
    # 1. CONCEPTO_LEER
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_LEER",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["leer", "read", "cargar"],
        operaciones={
            'ejecutar': CapacidadesBell.leer_archivo,
            'verificar': CapacidadesBell.archivo_existe
        },
        accesible_directamente=True,
        confianza_grounding=1.0,
        relaciones={
            'requiere': {'CONCEPTO_ARCHIVO'}
        },
        propiedades={
            'retorna': 'texto',
            'puede_fallar': True
        }
    ))
    
    # 2. CONCEPTO_ESCRIBIR
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ESCRIBIR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["escribir", "write", "guardar"],
        operaciones={
            'ejecutar': CapacidadesBell.escribir_archivo
        },
        accesible_directamente=True,
        confianza_grounding=1.0,
        relaciones={
            'requiere': {'CONCEPTO_ARCHIVO'}
        }
    ))
    
    # 3. CONCEPTO_ARCHIVO
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ARCHIVO",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["archivo", "file"],
        operaciones={
            'existe': CapacidadesBell.archivo_existe,
            'tamaño': CapacidadesBell.obtener_tamaño_archivo
        },
        accesible_directamente=True,
        confianza_grounding=1.0
    ))
    
    # 4. CONCEPTO_HOLA
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_HOLA",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["hola", "hi", "hello"],
        confianza_grounding=0.9,
        propiedades={'es_saludo': True}
    ))
    
    # 5. CONCEPTO_AYUDA
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_AYUDA",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["ayuda", "help", "ayudar"],
        confianza_grounding=0.8,
        propiedades={'es_peticion': True}
    ))
    
    return conceptos


def obtener_concepto_por_palabra(palabra: str, conceptos: list):
    """Busca un concepto que corresponda a una palabra en español."""
    palabra_lower = palabra.lower()
    for concepto in conceptos:
        if palabra_lower in [p.lower() for p in concepto.palabras_español]:
            return concepto
    return None