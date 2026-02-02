"""
Conceptos Expandidos de Fase 2 - 280 conceptos adicionales.

Categorías:
1. Palabras interrogativas y conectores (30)
2. Verbos de acción comunes (40)
3. Conceptos Python avanzados (50)
4. Conceptos de programación general (40)
5. Conceptos de datos y estructuras (30)
6. Conceptos de optimización (30)
7. Conceptos de sistemas (30)
8. Conceptos abstractos útiles (30)
"""

from typing import Dict
from core.concepto_anclado import ConceptoAnclado, TipoConcepto


# ========================================
# CATEGORÍA 1: PALABRAS INTERROGATIVAS (30)
# ========================================

def crear_conceptos_interrogativos():
    """Palabras interrogativas y conectores básicos."""
    conceptos = []
    
    # Interrogativas básicas
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_QUE",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["que", "qué", "q"],
        operaciones={},
        relaciones={'es_un': {'PALABRA_INTERROGATIVA'}},
        propiedades={'tipo': 'interrogativa'},
        datos={'definicion': 'Palabra interrogativa - qué'},
        accesible_directamente=False,
        confianza_grounding=0.95
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_QUIEN",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["quien", "quién", "quienes", "quiénes"],
        operaciones={},
        relaciones={'es_un': {'PALABRA_INTERROGATIVA'}},
        propiedades={'tipo': 'interrogativa'},
        datos={'definicion': 'Palabra interrogativa - quién'},
        accesible_directamente=False,
        confianza_grounding=0.95
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_COMO",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["como", "cómo"],
        operaciones={},
        relaciones={'es_un': {'PALABRA_INTERROGATIVA'}},
        propiedades={'tipo': 'interrogativa'},
        datos={'definicion': 'Palabra interrogativa - cómo'},
        accesible_directamente=False,
        confianza_grounding=0.95
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CUANDO",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["cuando", "cuándo"],
        operaciones={},
        relaciones={'es_un': {'PALABRA_INTERROGATIVA'}},
        propiedades={'tipo': 'interrogativa'},
        datos={'definicion': 'Palabra interrogativa - cuándo'},
        accesible_directamente=False,
        confianza_grounding=0.95
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DONDE",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["donde", "dónde"],
        operaciones={},
        relaciones={'es_un': {'PALABRA_INTERROGATIVA'}},
        propiedades={'tipo': 'interrogativa'},
        datos={'definicion': 'Palabra interrogativa - dónde'},
        accesible_directamente=False,
        confianza_grounding=0.95
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_PORQUE",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["porque", "por qué", "porqué"],
        operaciones={},
        relaciones={'es_un': {'PALABRA_INTERROGATIVA'}},
        propiedades={'tipo': 'interrogativa'},
        datos={'definicion': 'Palabra interrogativa - por qué'},
        accesible_directamente=False,
        confianza_grounding=0.95
    ))
    
    # Conectores y artículos
    for palabra, concepto_id in [
        (["el", "la", "los", "las"], "CONCEPTO_ARTICULO"),
        (["un", "una", "unos", "unas"], "CONCEPTO_ARTICULO_INDETERMINADO"),
        (["de", "del"], "CONCEPTO_PREPOSICION_DE"),
        (["en"], "CONCEPTO_PREPOSICION_EN"),
        (["para"], "CONCEPTO_PREPOSICION_PARA"),
        (["con"], "CONCEPTO_PREPOSICION_CON"),
        (["sin"], "CONCEPTO_PREPOSICION_SIN"),
        (["y", "e"], "CONCEPTO_CONJUNCION_Y"),
        (["o", "u"], "CONCEPTO_CONJUNCION_O"),
        (["pero"], "CONCEPTO_CONJUNCION_PERO"),
        (["si"], "CONCEPTO_CONDICIONAL_SI"),
        (["no"], "CONCEPTO_NEGACION"),
        (["es", "ser", "eres", "soy"], "CONCEPTO_VERBO_SER"),
        (["está", "estar", "estás", "estoy"], "CONCEPTO_VERBO_ESTAR"),
        (["tiene", "tener", "tienes", "tengo"], "CONCEPTO_VERBO_TENER"),
        (["hace", "hacer", "haces", "hago"], "CONCEPTO_VERBO_HACER"),
        (["va", "ir", "vas", "voy"], "CONCEPTO_VERBO_IR"),
        (["puede", "poder", "puedes", "puedo"], "CONCEPTO_VERBO_PODER"),
        (["debe", "deber", "debes", "debo"], "CONCEPTO_VERBO_DEBER"),
        (["sabe", "saber", "sabes", "se"], "CONCEPTO_VERBO_SABER"),
        (["conoce", "conocer", "conoces", "conozco"], "CONCEPTO_VERBO_CONOCER"),
        (["mi", "mis", "tu", "tus", "su", "sus"], "CONCEPTO_POSESIVO"),
        (["este", "esta", "estos", "estas"], "CONCEPTO_DEMOSTRATIVO"),
        (["ese", "esa", "esos", "esas"], "CONCEPTO_DEMOSTRATIVO_ESE"),
    ]:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=palabra,
            operaciones={},
            relaciones={'es_un': {'PALABRA_FUNCIONAL'}},
            propiedades={'tipo': 'conector'},
            datos={'definicion': f'Palabra funcional: {palabra[0]}'},
            accesible_directamente=False,
            confianza_grounding=0.9
        ))
    
    return conceptos


# ========================================
# CATEGORÍA 2: VERBOS DE ACCIÓN (40)
# ========================================

def crear_conceptos_verbos():
    """Verbos de acción comunes en programación y conversación."""
    conceptos = []
    
    verbos = [
        # Verbos de programación
        (["optimizar", "optimiza"], "CONCEPTO_OPTIMIZAR", "Mejorar eficiencia"),
        (["refactorizar", "refactoriza"], "CONCEPTO_REFACTORIZAR", "Reestructurar código"),
        (["debuggear", "debug", "depurar"], "CONCEPTO_DEBUGGEAR", "Encontrar errores"),
        (["compilar", "compila"], "CONCEPTO_COMPILAR", "Convertir código"),
        (["desplegar", "deploy", "implementar"], "CONCEPTO_DESPLEGAR", "Poner en producción"),
        (["testear", "test", "probar"], "CONCEPTO_TESTEAR", "Verificar funcionamiento"),
        (["instalar", "instala"], "CONCEPTO_INSTALAR", "Agregar software"),
        (["configurar", "config"], "CONCEPTO_CONFIGURAR", "Ajustar parámetros"),
        (["importar", "import"], "CONCEPTO_IMPORTAR", "Traer módulo"),
        (["exportar", "export"], "CONCEPTO_EXPORTAR", "Enviar datos"),
        
        # Verbos de manipulación de datos
        (["filtrar", "filter"], "CONCEPTO_FILTRAR", "Seleccionar elementos"),
        (["ordenar", "sort"], "CONCEPTO_ORDENAR", "Organizar secuencia"),
        (["mapear", "map"], "CONCEPTO_MAPEAR", "Transformar elementos"),
        (["reducir", "reduce"], "CONCEPTO_REDUCIR", "Agregar elementos"),
        (["agrupar", "group"], "CONCEPTO_AGRUPAR", "Juntar similares"),
        (["unir", "join", "merge"], "CONCEPTO_UNIR", "Combinar conjuntos"),
        (["dividir", "split"], "CONCEPTO_DIVIDIR", "Separar en partes"),
        (["copiar", "copy"], "CONCEPTO_COPIAR", "Duplicar"),
        (["mover", "move"], "CONCEPTO_MOVER", "Cambiar ubicación"),
        (["renombrar", "rename"], "CONCEPTO_RENOMBRAR", "Cambiar nombre"),
        
        # Verbos de comunicación
        (["mostrar", "show", "display"], "CONCEPTO_MOSTRAR", "Presentar información"),
        (["imprimir", "print"], "CONCEPTO_IMPRIMIR", "Sacar por pantalla"),
        (["enviar", "send"], "CONCEPTO_ENVIAR", "Transmitir"),
        (["recibir", "receive"], "CONCEPTO_RECIBIR", "Obtener transmisión"),
        (["notificar", "notify"], "CONCEPTO_NOTIFICAR", "Alertar"),
        (["registrar", "log"], "CONCEPTO_REGISTRAR", "Guardar evento"),
        
        # Verbos de control
        (["iniciar", "start", "comenzar"], "CONCEPTO_INICIAR", "Empezar proceso"),
        (["detener", "stop", "parar"], "CONCEPTO_DETENER", "Finalizar proceso"),
        (["pausar", "pause"], "CONCEPTO_PAUSAR", "Suspender temporalmente"),
        (["reanudar", "resume", "continuar"], "CONCEPTO_REANUDAR", "Retomar proceso"),
        (["reiniciar", "restart"], "CONCEPTO_REINICIAR", "Volver a empezar"),
        (["cancelar", "cancel"], "CONCEPTO_CANCELAR", "Anular operación"),
        
        # Verbos de verificación
        (["verificar", "verify", "comprobar"], "CONCEPTO_VERIFICAR", "Confirmar corrección"),
        (["validar", "validate"], "CONCEPTO_VALIDAR", "Verificar cumplimiento"),
        (["buscar", "search", "encontrar"], "CONCEPTO_BUSCAR", "Localizar elemento"),
        (["detectar", "detect"], "CONCEPTO_DETECTAR", "Identificar presencia"),
        (["comparar", "compare"], "CONCEPTO_COMPARAR", "Evaluar diferencias"),
        (["medir", "measure"], "CONCEPTO_MEDIR", "Cuantificar"),
        
        # Verbos de transformación
        (["convertir", "convert"], "CONCEPTO_CONVERTIR", "Cambiar formato"),
        (["formatear", "format"], "CONCEPTO_FORMATEAR", "Dar formato"),
    ]
    
    for palabras, concepto_id, definicion in verbos:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.OPERACION_LOGICA,
            palabras_español=palabras,
            operaciones={},  # Operaciones abstractas
            relaciones={'es_un': {'VERBO_ACCION'}},
            propiedades={'accion': True},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.85
        ))
    
    return conceptos


# ========================================
# CATEGORÍA 3: PYTHON AVANZADO (50)
# ========================================

def crear_conceptos_python_avanzado():
    """Conceptos de Python más avanzados."""
    conceptos = []
    
    # Funciones built-in importantes
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ENUMERATE",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["enumerate", "enumerar"],
        operaciones={
            'usar': lambda lista: list(enumerate(lista))
        },
        relaciones={
            'es_un': {'FUNCION_BUILTIN'},
            'alternativa_de': {'RANGE_LEN'},
            'mejor_que': {'FOR_INDEX'}
        },
        propiedades={
            'pythonic': True,
            'retorna': 'tuplas (indice, elemento)'
        },
        datos={
            'definicion': 'Función que retorna índice y elemento al iterar',
            'ejemplo': 'for i, item in enumerate(lista):',
            'ventaja': 'Más legible que range(len())'
        },
        accesible_directamente=True,
        confianza_grounding=1.0
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ZIP",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["zip"],
        operaciones={
            'usar': lambda *listas: list(zip(*listas))
        },
        relaciones={'es_un': {'FUNCION_BUILTIN'}},
        propiedades={'combina_iterables': True},
        datos={
            'definicion': 'Combina múltiples iterables',
            'ejemplo': 'for a, b in zip(lista1, lista2):'
        },
        accesible_directamente=True,
        confianza_grounding=1.0
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_MAP",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["map"],
        operaciones={},
        relaciones={'es_un': {'FUNCION_BUILTIN'}},
        propiedades={'funcional': True},
        datos={
            'definicion': 'Aplica función a cada elemento',
            'ejemplo': 'map(lambda x: x*2, lista)'
        },
        accesible_directamente=True,
        confianza_grounding=0.95
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_FILTER",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["filter"],
        operaciones={},
        relaciones={'es_un': {'FUNCION_BUILTIN'}},
        propiedades={'funcional': True},
        datos={
            'definicion': 'Filtra elementos según condición',
            'ejemplo': 'filter(lambda x: x > 0, lista)'
        },
        accesible_directamente=True,
        confianza_grounding=0.95
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_LAMBDA",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["lambda"],
        operaciones={},
        relaciones={'es_un': {'FUNCION_ANONIMA'}},
        propiedades={'inline': True},
        datos={
            'definicion': 'Función anónima',
            'ejemplo': 'lambda x: x * 2'
        },
        accesible_directamente=True,
        confianza_grounding=0.95
    ))
    
    # Comprehensions
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_LIST_COMPREHENSION",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["comprehension", "comprensión"],
        operaciones={},
        relaciones={'es_un': {'SINTAXIS_PYTHON'}},
        propiedades={'pythonic': True, 'conciso': True},
        datos={
            'definicion': 'Sintaxis concisa para crear listas',
            'ejemplo': '[x*2 for x in lista]'
        },
        accesible_directamente=False,
        confianza_grounding=0.9
    ))
    
    # Decoradores
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_DECORADOR",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["decorador", "decorator"],
        operaciones={},
        relaciones={'es_un': {'PATRON_PYTHON'}},
        propiedades={'modifica_funcion': True},
        datos={
            'definicion': 'Función que modifica otra función',
            'ejemplo': '@decorador\ndef funcion():'
        },
        accesible_directamente=False,
        confianza_grounding=0.85
    ))
    
    # Generators
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_GENERATOR",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["generator", "generador"],
        operaciones={},
        relaciones={'es_un': {'ITERADOR'}},
        propiedades={'lazy': True, 'eficiente_memoria': True},
        datos={
            'definicion': 'Función que genera valores bajo demanda',
            'ejemplo': 'def gen(): yield x'
        },
        accesible_directamente=False,
        confianza_grounding=0.85
    ))
    
    # Context managers
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_CONTEXT_MANAGER",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["with", "context"],
        operaciones={},
        relaciones={'es_un': {'PATRON_PYTHON'}},
        propiedades={'maneja_recursos': True},
        datos={
            'definicion': 'Gestiona recursos automáticamente',
            'ejemplo': 'with open(file) as f:'
        },
        accesible_directamente=False,
        confianza_grounding=0.9
    ))
    
    # Tipos de datos avanzados
    for tipo_dato in [
        ("set", "CONCEPTO_SET", "Conjunto sin duplicados"),
        ("tuple", "CONCEPTO_TUPLE", "Tupla inmutable"),
        ("frozenset", "CONCEPTO_FROZENSET", "Set inmutable"),
        ("bytes", "CONCEPTO_BYTES", "Secuencia de bytes"),
        ("bytearray", "CONCEPTO_BYTEARRAY", "Array de bytes mutable"),
    ]:
        palabras, concepto_id, definicion = tipo_dato
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.ENTIDAD_CODIGO,
            palabras_español=[palabras],
            operaciones={},
            relaciones={'es_un': {'TIPO_DATO_PYTHON'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=True,
            confianza_grounding=0.9
        ))
    
    # Módulos estándar importantes
    modulos = [
        ("os", "CONCEPTO_OS", "Módulo de sistema operativo"),
        ("sys", "CONCEPTO_SYS", "Módulo de sistema Python"),
        ("json", "CONCEPTO_JSON", "Módulo para JSON"),
        ("re", "CONCEPTO_RE", "Expresiones regulares"),
        ("datetime", "CONCEPTO_DATETIME", "Fechas y tiempos"),
        ("math", "CONCEPTO_MATH", "Matemáticas"),
        ("random", "CONCEPTO_RANDOM", "Números aleatorios"),
        ("collections", "CONCEPTO_COLLECTIONS", "Estructuras de datos"),
        ("itertools", "CONCEPTO_ITERTOOLS", "Herramientas de iteración"),
        ("functools", "CONCEPTO_FUNCTOOLS", "Herramientas funcionales"),
        ("pathlib", "CONCEPTO_PATHLIB", "Manejo de rutas"),
        ("asyncio", "CONCEPTO_ASYNCIO", "Programación asíncrona"),
        ("threading", "CONCEPTO_THREADING", "Hilos"),
        ("multiprocessing", "CONCEPTO_MULTIPROCESSING", "Multiprocesamiento"),
        ("pickle", "CONCEPTO_PICKLE", "Serialización"),
    ]
    
    for modulo, concepto_id, definicion in modulos:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[modulo],
            operaciones={},
            relaciones={'es_un': {'MODULO_PYTHON'}},
            propiedades={'stdlib': True},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.85
        ))
    
    # Conceptos de errores
    excepciones = [
        ("exception", "CONCEPTO_EXCEPTION", "Excepción base"),
        ("error", "CONCEPTO_ERROR", "Error genérico"),
        ("try", "CONCEPTO_TRY", "Bloque try-except"),
        ("except", "CONCEPTO_EXCEPT", "Manejo de excepción"),
        ("finally", "CONCEPTO_FINALLY", "Bloque finally"),
        ("raise", "CONCEPTO_RAISE", "Lanzar excepción"),
    ]
    
    for palabra, concepto_id, definicion in excepciones:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'MANEJO_ERRORES'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.9
        ))
    
    # Conceptos de async
    conceptos_async = [
        (["async", "asíncrono"], "CONCEPTO_ASYNC", "Programación asíncrona"),
        (["await"], "CONCEPTO_AWAIT", "Esperar tarea asíncrona"),
        (["coroutine", "corutina"], "CONCEPTO_COROUTINE", "Función asíncrona"),
    ]
    
    for palabras, concepto_id, definicion in conceptos_async:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=palabras,
            operaciones={},
            relaciones={'es_un': {'PROGRAMACION_ASINCRONA'}},
            propiedades={'async': True},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.85
        ))
    
    # Otros conceptos Python importantes
    otros = [
        (["self"], "CONCEPTO_SELF", "Referencia a instancia"),
        (["init", "__init__"], "CONCEPTO_INIT", "Constructor"),
        (["main", "__main__"], "CONCEPTO_MAIN", "Punto de entrada"),
        (["name", "__name__"], "CONCEPTO_NAME", "Nombre del módulo"),
        (["return"], "CONCEPTO_RETURN", "Retornar valor"),
        (["yield"], "CONCEPTO_YIELD", "Generar valor"),
        (["pass"], "CONCEPTO_PASS", "No hacer nada"),
        (["break"], "CONCEPTO_BREAK", "Salir de bucle"),
        (["continue"], "CONCEPTO_CONTINUE", "Siguiente iteración"),
        (["global"], "CONCEPTO_GLOBAL", "Variable global"),
        (["nonlocal"], "CONCEPTO_NONLOCAL", "Variable no local"),
        (["assert"], "CONCEPTO_ASSERT", "Afirmación"),
    ]
    
    for palabras, concepto_id, definicion in otros:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=palabras,
            operaciones={},
            relaciones={'es_un': {'KEYWORD_PYTHON'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.9
        ))
    
    return conceptos


# ========================================
# CATEGORÍA 4: PROGRAMACIÓN GENERAL (40)
# ========================================

def crear_conceptos_programacion_general():
    """Conceptos generales de programación."""
    conceptos = []
    
    # Paradigmas
    paradigmas = [
        ("poo", "CONCEPTO_POO", "Programación Orientada a Objetos"),
        ("funcional", "CONCEPTO_FUNCIONAL", "Programación Funcional"),
        ("procedural", "CONCEPTO_PROCEDURAL", "Programación Procedural"),
        ("declarativo", "CONCEPTO_DECLARATIVO", "Programación Declarativa"),
        ("imperativo", "CONCEPTO_IMPERATIVO", "Programación Imperativa"),
    ]
    
    for palabra, concepto_id, definicion in paradigmas:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'PARADIGMA_PROGRAMACION'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    # Estructuras de control
    estructuras = [
        (["recursion", "recursión"], "CONCEPTO_RECURSION", "Función que se llama a sí misma"),
        (["iteración"], "CONCEPTO_ITERACION", "Repetición de proceso"),
        (["switch", "match"], "CONCEPTO_SWITCH", "Selección múltiple"),
    ]
    
    for palabras, concepto_id, definicion in estructuras:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=palabras,
            operaciones={},
            relaciones={'es_un': {'ESTRUCTURA_CONTROL'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.85
        ))
    
    # Conceptos de complejidad
    complejidad = [
        ("complejidad", "CONCEPTO_COMPLEJIDAD", "Medida de eficiencia"),
        ("algoritmo", "CONCEPTO_ALGORITMO", "Secuencia de pasos"),
        ("eficiencia", "CONCEPTO_EFICIENCIA", "Uso óptimo de recursos"),
        ("performance", "CONCEPTO_PERFORMANCE", "Rendimiento"),
        ("latencia", "CONCEPTO_LATENCIA", "Tiempo de respuesta"),
        ("throughput", "CONCEPTO_THROUGHPUT", "Cantidad procesada"),
    ]
    
    for palabra, concepto_id, definicion in complejidad:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'METRICA_RENDIMIENTO'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    # Patrones de diseño
    patrones = [
        ("singleton", "CONCEPTO_SINGLETON", "Una sola instancia"),
        ("factory", "CONCEPTO_FACTORY", "Creación de objetos"),
        ("observer", "CONCEPTO_OBSERVER", "Patrón de observador"),
        ("strategy", "CONCEPTO_STRATEGY", "Estrategia intercambiable"),
        ("adapter", "CONCEPTO_ADAPTER", "Adaptador de interfaces"),
    ]
    
    for palabra, concepto_id, definicion in patrones:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'PATRON_DISEÑO'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.75
        ))
    
    # Conceptos de testing
    testing = [
        ("unittest", "CONCEPTO_UNITTEST", "Prueba unitaria"),
        ("pytest", "CONCEPTO_PYTEST", "Framework de testing"),
        ("mock", "CONCEPTO_MOCK", "Simulación"),
        ("assert", "CONCEPTO_ASSERT_TEST", "Afirmación en test"),
        ("coverage", "CONCEPTO_COVERAGE", "Cobertura de tests"),
    ]
    
    for palabra, concepto_id, definicion in testing:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'TESTING'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    # Conceptos de versionado y control
    versionado = [
        ("git", "CONCEPTO_GIT", "Control de versiones"),
        ("commit", "CONCEPTO_COMMIT", "Guardar cambios"),
        ("branch", "CONCEPTO_BRANCH", "Rama de desarrollo"),
        ("merge", "CONCEPTO_MERGE", "Fusionar ramas"),
        ("pull", "CONCEPTO_PULL", "Obtener cambios"),
        ("push", "CONCEPTO_PUSH", "Enviar cambios"),
    ]
    
    for palabra, concepto_id, definicion in versionado:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'CONTROL_VERSIONES'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    # Conceptos de documentación
    documentacion = [
        ("docstring", "CONCEPTO_DOCSTRING", "Documentación de función"),
        ("comentario", "CONCEPTO_COMENTARIO", "Nota explicativa"),
        ("readme", "CONCEPTO_README", "Documentación principal"),
        ("api", "CONCEPTO_API", "Interfaz de programación"),
        ("endpoint", "CONCEPTO_ENDPOINT", "Punto de acceso"),
    ]
    
    for palabra, concepto_id, definicion in documentacion:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'DOCUMENTACION'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.85
        ))
    
    return conceptos


# ========================================
# CATEGORÍA 5: DATOS Y ESTRUCTURAS (30)
# ========================================

def crear_conceptos_datos():
    """Conceptos de datos y estructuras."""
    conceptos = []
    
    # Estructuras de datos
    estructuras = [
        ("stack", "CONCEPTO_STACK", "Pila LIFO"),
        ("queue", "CONCEPTO_QUEUE", "Cola FIFO"),
        ("tree", "CONCEPTO_TREE", "Árbol"),
        ("graph", "CONCEPTO_GRAPH", "Grafo"),
        ("hash", "CONCEPTO_HASH", "Tabla hash"),
        ("linked list", "CONCEPTO_LINKED_LIST", "Lista enlazada"),
    ]
    
    for palabra, concepto_id, definicion in estructuras:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'ESTRUCTURA_DATOS'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    # Formatos de datos
    formatos = [
        ("csv", "CONCEPTO_CSV", "Valores separados por comas"),
        ("xml", "CONCEPTO_XML", "Lenguaje de marcado"),
        ("yaml", "CONCEPTO_YAML", "YAML Ain't Markup Language"),
        ("toml", "CONCEPTO_TOML", "Tom's Obvious Minimal Language"),
        ("ini", "CONCEPTO_INI", "Archivo de configuración"),
    ]
    
    for palabra, concepto_id, definicion in formatos:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'FORMATO_DATOS'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.85
        ))
    
    # Bases de datos
    bd = [
        ("database", "CONCEPTO_DATABASE", "Base de datos"),
        ("sql", "CONCEPTO_SQL", "Structured Query Language"),
        ("nosql", "CONCEPTO_NOSQL", "Base de datos no relacional"),
        ("query", "CONCEPTO_QUERY", "Consulta"),
        ("table", "CONCEPTO_TABLE", "Tabla"),
        ("index", "CONCEPTO_INDEX", "Índice"),
    ]
    
    for palabra, concepto_id, definicion in bd:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'BASE_DATOS'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    # Operaciones de datos
    operaciones_datos = [
        ("serialize", "CONCEPTO_SERIALIZE", "Convertir a formato almacenable"),
        ("deserialize", "CONCEPTO_DESERIALIZE", "Restaurar desde formato"),
        ("encode", "CONCEPTO_ENCODE", "Codificar"),
        ("decode", "CONCEPTO_DECODE", "Decodificar"),
        ("compress", "CONCEPTO_COMPRESS", "Comprimir"),
        ("decompress", "CONCEPTO_DECOMPRESS", "Descomprimir"),
    ]
    
    for palabra, concepto_id, definicion in operaciones_datos:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'OPERACION_DATOS'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    return conceptos


# ========================================
# CATEGORÍA 6: OPTIMIZACIÓN (30)
# ========================================

def crear_conceptos_optimizacion():
    """Conceptos relacionados con optimización."""
    conceptos = []
    
    # Técnicas de optimización
    tecnicas = [
        ("cache", "CONCEPTO_CACHE", "Almacenamiento temporal"),
        ("memoization", "CONCEPTO_MEMOIZATION", "Cache de resultados de función"),
        ("lazy loading", "CONCEPTO_LAZY_LOADING", "Carga diferida"),
        ("eager loading", "CONCEPTO_EAGER_LOADING", "Carga anticipada"),
        ("pooling", "CONCEPTO_POOLING", "Agrupación de recursos"),
        ("indexing", "CONCEPTO_INDEXING", "Indexación"),
    ]
    
    for palabra, concepto_id, definicion in tecnicas:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'TECNICA_OPTIMIZACION'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.75
        ))
    
    # Métricas
    metricas = [
        ("tiempo", "CONCEPTO_TIEMPO", "Duración de ejecución"),
        ("memoria", "CONCEPTO_MEMORIA", "Uso de RAM"),
        ("cpu", "CONCEPTO_CPU", "Uso de procesador"),
        ("disco", "CONCEPTO_DISCO", "Almacenamiento"),
        ("red", "CONCEPTO_RED", "Uso de red"),
        ("bandwidth", "CONCEPTO_BANDWIDTH", "Ancho de banda"),
    ]
    
    for palabra, concepto_id, definicion in metricas:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'METRICA_RECURSO'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.85
        ))
    
    # Patrones de rendimiento
    patrones_rendimiento = [
        ("batch", "CONCEPTO_BATCH", "Procesamiento por lotes"),
        ("stream", "CONCEPTO_STREAM", "Procesamiento en flujo"),
        ("pipeline", "CONCEPTO_PIPELINE", "Tubería de procesamiento"),
        ("parallel", "CONCEPTO_PARALLEL", "Procesamiento paralelo"),
        ("concurrent", "CONCEPTO_CONCURRENT", "Procesamiento concurrente"),
        ("asynchronous", "CONCEPTO_ASYNCHRONOUS", "Procesamiento asíncrono"),
    ]
    
    for palabra, concepto_id, definicion in patrones_rendimiento:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'PATRON_RENDIMIENTO'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    # Big O
    notaciones = [
        ("O(1)", "CONCEPTO_O1", "Complejidad constante"),
        ("O(n)", "CONCEPTO_ON", "Complejidad lineal"),
        ("O(log n)", "CONCEPTO_OLOGN", "Complejidad logarítmica"),
        ("O(n²)", "CONCEPTO_ON2", "Complejidad cuadrática"),
        ("O(2ⁿ)", "CONCEPTO_O2N", "Complejidad exponencial"),
    ]
    
    for notacion, concepto_id, definicion in notaciones:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[notacion],
            operaciones={},
            relaciones={'es_un': {'BIG_O_NOTATION'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    return conceptos


# ========================================
# CATEGORÍA 7: SISTEMAS (30)
# ========================================

def crear_conceptos_sistemas():
    """Conceptos de sistemas y arquitectura."""
    conceptos = []
    
    # Arquitectura
    arquitectura = [
        ("microservices", "CONCEPTO_MICROSERVICES", "Arquitectura de microservicios"),
        ("monolith", "CONCEPTO_MONOLITH", "Aplicación monolítica"),
        ("client-server", "CONCEPTO_CLIENT_SERVER", "Cliente-servidor"),
        ("rest", "CONCEPTO_REST", "API RESTful"),
        ("graphql", "CONCEPTO_GRAPHQL", "GraphQL"),
        ("websocket", "CONCEPTO_WEBSOCKET", "WebSocket"),
    ]
    
    for palabra, concepto_id, definicion in arquitectura:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'ARQUITECTURA'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.75
        ))
    
    # Contenedores y orquestación
    contenedores = [
        ("docker", "CONCEPTO_DOCKER", "Plataforma de contenedores"),
        ("container", "CONCEPTO_CONTAINER", "Contenedor"),
        ("image", "CONCEPTO_IMAGE", "Imagen"),
        ("kubernetes", "CONCEPTO_KUBERNETES", "Orquestación de contenedores"),
        ("pod", "CONCEPTO_POD", "Pod de Kubernetes"),
    ]
    
    for palabra, concepto_id, definicion in contenedores:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'CONTENEDORES'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.75
        ))
    
    # Cloud
    cloud = [
        ("cloud", "CONCEPTO_CLOUD", "Computación en la nube"),
        ("aws", "CONCEPTO_AWS", "Amazon Web Services"),
        ("azure", "CONCEPTO_AZURE", "Microsoft Azure"),
        ("gcp", "CONCEPTO_GCP", "Google Cloud Platform"),
    ]
    
    for palabra, concepto_id, definicion in cloud:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'CLOUD'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.7
        ))
    
    # DevOps
    devops = [
        ("ci/cd", "CONCEPTO_CICD", "Integración/Despliegue continuo"),
        ("jenkins", "CONCEPTO_JENKINS", "Servidor de CI/CD"),
        ("github actions", "CONCEPTO_GITHUB_ACTIONS", "Automatización GitHub"),
        ("terraform", "CONCEPTO_TERRAFORM", "Infraestructura como código"),
        ("ansible", "CONCEPTO_ANSIBLE", "Automatización de configuración"),
    ]
    
    for palabra, concepto_id, definicion in devops:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'DEVOPS'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.7
        ))
    
    # Seguridad
    seguridad = [
        ("authentication", "CONCEPTO_AUTHENTICATION", "Autenticación"),
        ("authorization", "CONCEPTO_AUTHORIZATION", "Autorización"),
        ("encryption", "CONCEPTO_ENCRYPTION", "Encriptación"),
        ("https", "CONCEPTO_HTTPS", "HTTP Seguro"),
        ("token", "CONCEPTO_TOKEN", "Token de acceso"),
        ("jwt", "CONCEPTO_JWT", "JSON Web Token"),
    ]
    
    for palabra, concepto_id, definicion in seguridad:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=[palabra],
            operaciones={},
            relaciones={'es_un': {'SEGURIDAD'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.8
        ))
    
    return conceptos


# ========================================
# CATEGORÍA 8: ABSTRACTOS ÚTILES (30)
# ========================================

def crear_conceptos_abstractos():
    """Conceptos abstractos útiles para conversación."""
    conceptos = []
    
    # Adjetivos de calidad
    adjetivos = [
        (["bueno", "buena", "buenos", "buenas"], "CONCEPTO_BUENO", "De calidad"),
        (["malo", "mala", "malos", "malas"], "CONCEPTO_MALO", "De baja calidad"),
        (["mejor"], "CONCEPTO_MEJOR", "Superior"),
        (["peor"], "CONCEPTO_PEOR", "Inferior"),
        (["rápido", "rápida"], "CONCEPTO_RAPIDO", "Veloz"),
        (["lento", "lenta"], "CONCEPTO_LENTO", "Pausado"),
        (["simple", "simples"], "CONCEPTO_SIMPLE", "Sencillo"),
        (["complejo", "compleja"], "CONCEPTO_COMPLEJO", "Complicado"),
        (["fácil", "facil"], "CONCEPTO_FACIL", "Sin dificultad"),
        (["difícil", "dificil"], "CONCEPTO_DIFICIL", "Con dificultad"),
    ]
    
    for palabras, concepto_id, definicion in adjetivos:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=palabras,
            operaciones={},
            relaciones={'es_un': {'ADJETIVO'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.9
        ))
    
    # Sustantivos útiles
    sustantivos = [
        (["problema"], "CONCEPTO_PROBLEMA", "Situación a resolver"),
        (["solución", "solucion"], "CONCEPTO_SOLUCION", "Respuesta a problema"),
        (["proyecto"], "CONCEPTO_PROYECTO", "Esfuerzo organizado"),
        (["trabajo"], "CONCEPTO_TRABAJO", "Actividad laboral"),
        (["tarea"], "CONCEPTO_TAREA", "Trabajo específico"),
        (["meta", "objetivo"], "CONCEPTO_META", "Objetivo a alcanzar"),
        (["resultado"], "CONCEPTO_RESULTADO", "Consecuencia"),
        (["proceso"], "CONCEPTO_PROCESO", "Secuencia de pasos"),
        (["método", "metodo"], "CONCEPTO_METODO", "Forma de hacer"),
        (["forma", "manera"], "CONCEPTO_FORMA", "Modo"),
    ]
    
    for palabras, concepto_id, definicion in sustantivos:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=palabras,
            operaciones={},
            relaciones={'es_un': {'SUSTANTIVO'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.85
        ))
    
    # Conceptos temporales
    temporales = [
        (["hoy"], "CONCEPTO_HOY", "Día actual"),
        (["ayer"], "CONCEPTO_AYER", "Día anterior"),
        (["mañana"], "CONCEPTO_MAÑANA", "Día siguiente"),
        (["ahora"], "CONCEPTO_AHORA", "Momento actual"),
        (["antes"], "CONCEPTO_ANTES", "Tiempo previo"),
        (["después", "despues"], "CONCEPTO_DESPUES", "Tiempo posterior"),
        (["siempre"], "CONCEPTO_SIEMPRE", "Todo el tiempo"),
        (["nunca"], "CONCEPTO_NUNCA", "Ningún momento"),
    ]
    
    for palabras, concepto_id, definicion in temporales:
        conceptos.append(ConceptoAnclado(
            id=concepto_id,
            tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
            palabras_español=palabras,
            operaciones={},
            relaciones={'es_un': {'TEMPORAL'}},
            propiedades={},
            datos={'definicion': definicion},
            accesible_directamente=False,
            confianza_grounding=0.9
        ))
    
    return conceptos


# ========================================
# FUNCIÓN PRINCIPAL
# ========================================

def obtener_conceptos_expandidos() -> Dict[str, ConceptoAnclado]:
    """
    Retorna TODOS los 280 conceptos expandidos de Fase 2.
    
    Returns:
        Dict[str, ConceptoAnclado]: Diccionario de conceptos
    """
    todos_conceptos = []
    
    # Categoría 1: Interrogativos (30)
    todos_conceptos.extend(crear_conceptos_interrogativos())
    
    # Categoría 2: Verbos (40)
    todos_conceptos.extend(crear_conceptos_verbos())
    
    # Categoría 3: Python avanzado (50)
    todos_conceptos.extend(crear_conceptos_python_avanzado())
    
    # Categoría 4: Programación general (40)
    todos_conceptos.extend(crear_conceptos_programacion_general())
    
    # Categoría 5: Datos (30)
    todos_conceptos.extend(crear_conceptos_datos())
    
    # Categoría 6: Optimización (30)
    todos_conceptos.extend(crear_conceptos_optimizacion())
    
    # Categoría 7: Sistemas (30)
    todos_conceptos.extend(crear_conceptos_sistemas())
    
    # Categoría 8: Abstractos (30)
    todos_conceptos.extend(crear_conceptos_abstractos())
    
    # Convertir a diccionario
    return {c.id: c for c in todos_conceptos}