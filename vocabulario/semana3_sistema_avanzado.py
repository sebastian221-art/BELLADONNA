"""
Vocabulario Sistema Avanzado - Semana 3.

30 conceptos de operaciones sistema avanzadas.
Grounding medio-alto (0.7-0.9).
"""
from core.concepto_anclado import ConceptoAnclado
from core.tipos import TipoConcepto

def obtener_conceptos_sistema_avanzado():
    """Retorna conceptos sistema avanzado (30 conceptos)."""
    conceptos = []
    
    # OPERACIONES FILESYSTEM (10)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_COPIAR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["copiar", "copy", "duplicar"],
        confianza_grounding=0.9,
        propiedades={
            'modifica_sistema': True,
            'crea_archivo': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MOVER",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["mover", "move", "renombrar"],
        confianza_grounding=0.9,
        propiedades={
            'modifica_sistema': True,
            'cambia_ubicacion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CREAR_DIRECTORIO",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["crear directorio", "mkdir", "nueva carpeta"],
        confianza_grounding=0.9,
        propiedades={
            'modifica_sistema': True,
            'crea_directorio': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PERMISOS",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["permisos", "permissions", "chmod"],
        confianza_grounding=0.8,
        propiedades={
            'es_atributo': True,
            'seguridad': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_EXTENSION",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["extensión", "extension", "tipo archivo"],
        confianza_grounding=0.9,
        propiedades={
            'identifica_tipo': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RUTA",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["ruta", "path", "ubicación"],
        confianza_grounding=0.9,
        propiedades={
            'es_string': True,
            'indica_ubicacion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ABSOLUTA",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["absoluta", "absolute", "ruta completa"],
        confianza_grounding=0.8,
        propiedades={
            'desde_raiz': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RELATIVA",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["relativa", "relative"],
        confianza_grounding=0.8,
        propiedades={
            'desde_actual': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_NOMBRE_ARCHIVO",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["nombre", "filename", "nombre archivo"],
        confianza_grounding=0.9,
        propiedades={
            'identifica_archivo': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_FECHA_MODIFICACION",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["fecha modificación", "mtime", "timestamp"],
        confianza_grounding=0.8,
        propiedades={
            'es_metadata': True,
            'es_datetime': True
        }
    ))
    
    # OPERACIONES PROCESO (10)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PROCESO",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["proceso", "process"],
        confianza_grounding=0.8,
        propiedades={
            'ejecuta_codigo': True,
            'tiene_pid': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_THREAD",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["thread", "hilo"],
        confianza_grounding=0.7,
        propiedades={
            'concurrente': True,
            'comparte_memoria': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PID",
        tipo=TipoConcepto.PROPIEDAD,
        palabras_español=["pid", "process id"],
        confianza_grounding=0.8,
        propiedades={
            'es_identificador': True,
            'es_entero': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_TERMINAR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["terminar", "kill", "detener"],
        confianza_grounding=0.8,
        propiedades={
            'finaliza_proceso': True,
            'puede_fallar': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PAUSAR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["pausar", "pause", "sleep"],
        confianza_grounding=0.9,
        propiedades={
            'detiene_ejecucion': True,
            'temporal': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_REANUDAR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["reanudar", "resume", "continuar"],
        confianza_grounding=0.8,
        propiedades={
            'continua_ejecucion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MEMORIA_RAM",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["memoria", "RAM", "memoria principal"],
        confianza_grounding=0.8,
        propiedades={
            'es_recurso': True,
            'volatil': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CPU",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["CPU", "procesador"],
        confianza_grounding=0.8,
        propiedades={
            'es_hardware': True,
            'ejecuta_instrucciones': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DISCO",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["disco", "disk", "almacenamiento"],
        confianza_grounding=0.9,
        propiedades={
            'es_hardware': True,
            'persistente': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_RED",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["red", "network"],
        confianza_grounding=0.7,
        propiedades={
            'conecta_sistemas': True
        }
    ))
    
    # OPERACIONES TEXTO (10)
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_BUSCAR_TEXTO",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["buscar", "find", "search"],
        confianza_grounding=0.9,
        propiedades={
            'retorna_posicion': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_REEMPLAZAR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["reemplazar", "replace", "sustituir"],
        confianza_grounding=0.9,
        propiedades={
            'modifica_texto': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DIVIDIR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["dividir", "split", "separar"],
        confianza_grounding=0.9,
        propiedades={
            'retorna_lista': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_UNIR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["unir", "join", "concatenar"],
        confianza_grounding=0.9,
        propiedades={
            'combina_elementos': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MAYUSCULAS",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["mayúsculas", "upper", "uppercase"],
        confianza_grounding=0.9,
        propiedades={
            'modifica_texto': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MINUSCULAS",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["minúsculas", "lower", "lowercase"],
        confianza_grounding=0.9,
        propiedades={
            'modifica_texto': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_STRIP",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["strip", "limpiar", "trim"],
        confianza_grounding=0.9,
        propiedades={
            'elimina_espacios': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_FORMATO",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["formato", "format"],
        confianza_grounding=0.9,
        propiedades={
            'inserta_valores': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ENCODING",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["encoding", "codificación", "utf-8"],
        confianza_grounding=0.8,
        propiedades={
            'representa_caracteres': True
        }
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_REGEX",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["regex", "expresión regular", "pattern"],
        confianza_grounding=0.7,
        propiedades={
            'patron_busqueda': True,
            'complejo': True
        }
    ))
    
    return conceptos