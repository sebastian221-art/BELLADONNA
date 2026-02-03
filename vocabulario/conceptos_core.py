"""
Vocabulario core de Bell - Semana 1.
Progreso: 15 conceptos (de 30 objetivo).
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto
from core.capacidades_bell import CapacidadesBell

def obtener_conceptos_core():
    """Retorna los 15 conceptos del Día 2."""
    conceptos = []
    
    # ===== OPERACIONES SISTEMA (5 conceptos) =====
    
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
        relaciones={'requiere': {'CONCEPTO_ARCHIVO'}},
        propiedades={'retorna': 'texto', 'puede_fallar': True}
    ))
    
    # 2. CONCEPTO_ESCRIBIR
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ESCRIBIR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["escribir", "write", "guardar"],
        operaciones={'ejecutar': CapacidadesBell.escribir_archivo},
        accesible_directamente=True,
        confianza_grounding=1.0,
        relaciones={'requiere': {'CONCEPTO_ARCHIVO'}}
    ))
    
    # 3. CONCEPTO_ARCHIVO
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ARCHIVO",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["archivo", "file", "documento"],
        operaciones={
            'existe': CapacidadesBell.archivo_existe,
            'tamaño': CapacidadesBell.obtener_tamaño_archivo
        },
        accesible_directamente=True,
        confianza_grounding=1.0
    ))
    
    # 4. CONCEPTO_DIRECTORIO
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DIRECTORIO",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["directorio", "carpeta", "folder"],
        operaciones={'listar': CapacidadesBell.listar_directorio},
        accesible_directamente=True,
        confianza_grounding=1.0,
        relaciones={'contiene': {'CONCEPTO_ARCHIVO'}}
    ))
    
    # 5. CONCEPTO_EXISTE
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_EXISTE",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["existe", "hay", "está"],
        operaciones={'verificar': CapacidadesBell.archivo_existe},
        accesible_directamente=True,
        confianza_grounding=1.0
    ))
    
    # ===== PALABRAS CONVERSACIÓN (5 conceptos) =====
    
    # 6. CONCEPTO_HOLA
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_HOLA",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["hola", "hi", "hello", "hey"],
        confianza_grounding=0.9,
        propiedades={'es_saludo': True, 'requiere_respuesta': True}
    ))
    
    # 7. CONCEPTO_AYUDA
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_AYUDA",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["ayuda", "help", "ayudar", "asistir"],
        confianza_grounding=0.8,
        propiedades={'es_peticion': True}
    ))
    
    # 8. CONCEPTO_PODER
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PODER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["poder", "puedes", "puedo", "capacidad"],
        confianza_grounding=0.8,
        relaciones={'relacionado_con': {'CONCEPTO_HACER'}},
        propiedades={'es_pregunta_capacidad': True}
    ))
    
    # 9. CONCEPTO_HACER
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_HACER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["hacer", "realizar", "ejecutar"],
        confianza_grounding=0.7,
        propiedades={'es_accion': True}
    ))
    
    # 10. CONCEPTO_GRACIAS
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_GRACIAS",
        tipo=TipoConcepto.PALABRA_CONVERSACION,
        palabras_español=["gracias", "thanks", "thank you"],
        confianza_grounding=0.9,
        propiedades={'es_agradecimiento': True}
    ))
    
    # ===== CONCEPTOS COGNITIVOS (5 conceptos) =====
    
    # 11. CONCEPTO_RAZONAR
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RAZONAR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["razonar", "pensar", "analizar"],
        confianza_grounding=0.7,
        propiedades={'es_accion_interna': True}
    ))
    
    # 12. CONCEPTO_DECIDIR
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DECIDIR",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["decidir", "determinar", "elegir"],
        confianza_grounding=0.7,
        relaciones={'requiere': {'CONCEPTO_RAZONAR'}}
    ))
    
    # 13. CONCEPTO_CERTEZA
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CERTEZA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["certeza", "seguridad", "confianza"],
        confianza_grounding=0.6,
        propiedades={'es_metrica': True, 'rango': [0.0, 1.0]}
    ))
    
    # 14. CONCEPTO_ENTENDER
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ENTENDER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["entender", "comprender", "captar"],
        confianza_grounding=0.6,
        propiedades={'es_cognitivo': True}
    ))
    
    # 15. CONCEPTO_SABER
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_SABER",
        tipo=TipoConcepto.ACCION_COGNITIVA,
        palabras_español=["saber", "conocer"],
        confianza_grounding=0.7,
        propiedades={'es_estado': True}
    ))
    
    return conceptos


def obtener_concepto_por_palabra(palabra: str, conceptos: list):
    """Busca un concepto que corresponda a una palabra en español."""
    palabra_lower = palabra.lower()
    for concepto in conceptos:
        if palabra_lower in [p.lower() for p in concepto.palabras_español]:
            return concepto
    return None