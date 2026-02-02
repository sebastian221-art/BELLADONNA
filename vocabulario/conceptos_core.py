"""
Conceptos fundamentales de Bell - Los 20 conceptos base.

Cada concepto tiene grounding directo (operaciones ejecutables).
"""

from core.concepto_anclado import ConceptoAnclado, TipoConcepto
import os
import ast


def crear_concepto_archivo():
    """CONCEPTO: ARCHIVO (file system)"""
    
    return ConceptoAnclado(
        id="CONCEPTO_ARCHIVO",
        tipo=TipoConcepto.ENTIDAD_DIGITAL,
        palabras_español=["archivo", "file", "fichero"],
        
        operaciones={
            'leer': lambda ruta: open(ruta, 'r', encoding='utf-8').read(),
            'escribir': lambda ruta, texto: open(ruta, 'w', encoding='utf-8').write(texto),
            'existe': lambda ruta: os.path.exists(ruta),
            'tamaño': lambda ruta: os.path.getsize(ruta) if os.path.exists(ruta) else 0,
        },
        
        relaciones={
            'es_un': {'ENTIDAD_DIGITAL'},
            'requiere': {'FILESYSTEM'},
            'contiene': {'TEXTO', 'CODIGO', 'DATOS'}
        },
        
        propiedades={
            'extensiones_comunes': ['.txt', '.py', '.md', '.json'],
            'puede_ser_binario': True
        },
        
        datos={
            'definicion': 'Unidad de datos almacenada en filesystem',
            'ejemplos': ['config.json', 'main.py', 'README.md']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_funcion():
    """CONCEPTO: FUNCIÓN (programación)"""
    import inspect
    
    return ConceptoAnclado(
        id="CONCEPTO_FUNCION",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["función", "funcion", "def", "método", "metodo"],
        
        operaciones={
            'analizar': lambda codigo: ast.parse(codigo) if isinstance(codigo, str) else None,
            'ejecutar': lambda func, *args: func(*args) if callable(func) else None,
            'contar_params': lambda func: len(inspect.signature(func).parameters) if callable(func) else 0,
            'obtener_nombre': lambda func: func.__name__ if callable(func) else 'desconocido',
        },
        
        relaciones={
            'es_un': {'BLOQUE_CODIGO'},
            'puede_tener': {'PARAMETROS', 'RETURN', 'DOCSTRING'},
            'dentro_de': {'MODULO', 'CLASE'}
        },
        
        propiedades={
            'sintaxis': 'def nombre(params): ...',
            'puede_ser_async': True,
            'puede_ser_lambda': True
        },
        
        datos={
            'definicion': 'Bloque de código reutilizable que realiza tarea específica',
            'ejemplos': [
                'def suma(a, b): return a + b',
                'lambda x: x * 2'
            ]
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_variable():
    """CONCEPTO: VARIABLE"""
    
    return ConceptoAnclado(
        id="CONCEPTO_VARIABLE",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["variable", "var"],
        
        operaciones={
            'asignar': lambda nombre, valor: {nombre: valor},
            'leer': lambda dic, nombre: dic.get(nombre),
        },
        
        relaciones={
            'es_un': {'CONTENEDOR_DATOS'},
            'puede_contener': {'NUMERO', 'STRING', 'LISTA', 'OBJETO'}
        },
        
        propiedades={
            'mutable': True,
            'tiene_tipo': True
        },
        
        datos={
            'definicion': 'Contenedor que almacena valor',
            'ejemplos': ['x = 5', 'nombre = "Bell"']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_lista():
    """CONCEPTO: LISTA"""
    
    return ConceptoAnclado(
        id="CONCEPTO_LISTA",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["lista", "list", "array"],
        
        operaciones={
            'crear': lambda *elementos: list(elementos),
            'agregar': lambda lista, elem: lista.append(elem) or lista,
            'obtener': lambda lista, idx: lista[idx] if 0 <= idx < len(lista) else None,
            'longitud': lambda lista: len(lista),
        },
        
        relaciones={
            'es_un': {'ESTRUCTURA_DATOS'},
            'contiene': {'ELEMENTOS_ORDENADOS'}
        },
        
        propiedades={
            'ordenada': True,
            'mutable': True,
            'indexada': True
        },
        
        datos={
            'definicion': 'Colección ordenada de elementos',
            'ejemplos': ['[1, 2, 3]', '["a", "b", "c"]']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_string():
    """CONCEPTO: STRING/TEXTO"""
    
    return ConceptoAnclado(
        id="CONCEPTO_STRING",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["string", "texto", "cadena"],
        
        operaciones={
            'crear': lambda texto: str(texto),
            'longitud': lambda texto: len(texto),
            'mayusculas': lambda texto: texto.upper(),
            'minusculas': lambda texto: texto.lower(),
            'contiene': lambda texto, subcadena: subcadena in texto,
        },
        
        relaciones={
            'es_un': {'TIPO_DATO'},
            'puede_representar': {'TEXTO', 'MENSAJE'}
        },
        
        propiedades={
            'inmutable': True,
            'iterable': True
        },
        
        datos={
            'definicion': 'Secuencia de caracteres',
            'ejemplos': ['"Hola"', "'Bell'", '"""Texto largo"""']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_numero():
    """CONCEPTO: NÚMERO"""
    
    return ConceptoAnclado(
        id="CONCEPTO_NUMERO",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["número", "numero", "int", "float"],
        
        operaciones={
            'sumar': lambda a, b: a + b,
            'restar': lambda a, b: a - b,
            'multiplicar': lambda a, b: a * b,
            'dividir': lambda a, b: a / b if b != 0 else None,
            'es_par': lambda n: n % 2 == 0,
        },
        
        relaciones={
            'es_un': {'TIPO_DATO'},
            'tipos': {'ENTERO', 'DECIMAL'}
        },
        
        propiedades={
            'inmutable': True,
            'comparable': True
        },
        
        datos={
            'definicion': 'Valor numérico',
            'ejemplos': ['42', '3.14', '-7']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_diccionario():
    """CONCEPTO: DICCIONARIO"""
    
    return ConceptoAnclado(
        id="CONCEPTO_DICCIONARIO",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["diccionario", "dict", "mapa"],
        
        operaciones={
            'crear': lambda: {},
            'agregar': lambda dic, clave, valor: {**dic, clave: valor},
            'obtener': lambda dic, clave: dic.get(clave),
            'tiene_clave': lambda dic, clave: clave in dic,
        },
        
        relaciones={
            'es_un': {'ESTRUCTURA_DATOS'},
            'contiene': {'PARES_CLAVE_VALOR'}
        },
        
        propiedades={
            'no_ordenado': True,
            'mutable': True,
            'claves_unicas': True
        },
        
        datos={
            'definicion': 'Estructura clave-valor',
            'ejemplos': ['{"nombre": "Bell"}', '{1: "uno", 2: "dos"}']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_boolean():
    """CONCEPTO: BOOLEANO"""
    
    return ConceptoAnclado(
        id="CONCEPTO_BOOLEAN",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["booleano", "bool", "verdadero", "falso"],
        
        operaciones={
            'y_logico': lambda a, b: a and b,
            'o_logico': lambda a, b: a or b,
            'negacion': lambda a: not a,
        },
        
        relaciones={
            'es_un': {'TIPO_DATO'},
            'valores': {'TRUE', 'FALSE'}
        },
        
        propiedades={
            'binario': True,
            'inmutable': True
        },
        
        datos={
            'definicion': 'Valor de verdad (True/False)',
            'ejemplos': ['True', 'False']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_leer():
    """CONCEPTO: LEER (operación)"""
    
    return ConceptoAnclado(
        id="CONCEPTO_LEER",
        tipo=TipoConcepto.OPERACION_CODIGO,
        palabras_español=["leer", "read"],
        
        operaciones={
            'leer_archivo': lambda ruta: open(ruta, 'r', encoding='utf-8').read() if os.path.exists(ruta) else None,
            'leer_lineas': lambda ruta: open(ruta, 'r', encoding='utf-8').readlines() if os.path.exists(ruta) else [],
        },
        
        relaciones={
            'es_un': {'OPERACION'},
            'aplica_a': {'ARCHIVO', 'TEXTO'}
        },
        
        propiedades={
            'modifica_origen': False,
            'retorna_datos': True
        },
        
        datos={
            'definicion': 'Operación de lectura de datos',
            'ejemplos': ['open(file).read()', 'f.readline()']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_escribir():
    """CONCEPTO: ESCRIBIR (operación)"""
    
    return ConceptoAnclado(
        id="CONCEPTO_ESCRIBIR",
        tipo=TipoConcepto.OPERACION_CODIGO,
        palabras_español=["escribir", "write", "guardar"],
        
        operaciones={
            'escribir_archivo': lambda ruta, texto: open(ruta, 'w', encoding='utf-8').write(texto),
            'agregar_archivo': lambda ruta, texto: open(ruta, 'a', encoding='utf-8').write(texto),
        },
        
        relaciones={
            'es_un': {'OPERACION'},
            'aplica_a': {'ARCHIVO', 'TEXTO'}
        },
        
        propiedades={
            'modifica_destino': True,
            'puede_crear': True
        },
        
        datos={
            'definicion': 'Operación de escritura de datos',
            'ejemplos': ['open(file, "w").write()', 'f.write(text)']
        },
        
        accesible_directamente=True,
        confianza_grounding=1.0
    )


def crear_concepto_bucle():
    """CONCEPTO: BUCLE"""
    
    return ConceptoAnclado(
        id="CONCEPTO_BUCLE",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["bucle", "loop", "for", "while"],
        
        operaciones={
            'iterar': lambda iterable, func: [func(item) for item in iterable],
        },
        
        relaciones={
            'es_un': {'ESTRUCTURA_CONTROL'},
            'tipos': {'FOR', 'WHILE'}
        },
        
        propiedades={
            'repetitivo': True,
            'puede_infinito': True
        },
        
        datos={
            'definicion': 'Estructura que repite código',
            'ejemplos': ['for i in range(10):', 'while True:']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.95
    )


def crear_concepto_condicional():
    """CONCEPTO: CONDICIONAL"""
    
    return ConceptoAnclado(
        id="CONCEPTO_CONDICIONAL",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["condicional", "if", "si"],
        
        operaciones={
            'evaluar': lambda condicion, si_true, si_false: si_true if condicion else si_false,
        },
        
        relaciones={
            'es_un': {'ESTRUCTURA_CONTROL'},
            'requiere': {'CONDICION_BOOLEAN'}
        },
        
        propiedades={
            'decide_flujo': True,
            'puede_anidar': True
        },
        
        datos={
            'definicion': 'Estructura que decide entre opciones',
            'ejemplos': ['if x > 0:', 'if condicion: ... else: ...']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.95
    )


def crear_concepto_clase():
    """CONCEPTO: CLASE"""
    
    return ConceptoAnclado(
        id="CONCEPTO_CLASE",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["clase", "class"],
        
        operaciones={},  # Operaciones complejas, simplificado en Fase 1
        
        relaciones={
            'es_un': {'ESTRUCTURA_POO'},
            'contiene': {'METODOS', 'ATRIBUTOS'}
        },
        
        propiedades={
            'define_tipo': True,
            'puede_heredar': True
        },
        
        datos={
            'definicion': 'Plantilla para crear objetos',
            'ejemplos': ['class MiClase:', 'class Usuario:']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.9
    )


def crear_concepto_modulo():
    """CONCEPTO: MÓDULO"""
    
    return ConceptoAnclado(
        id="CONCEPTO_MODULO",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["módulo", "modulo", "module"],
        
        operaciones={},  # Simplificado
        
        relaciones={
            'es_un': {'ARCHIVO_CODIGO'},
            'contiene': {'FUNCIONES', 'CLASES', 'VARIABLES'}
        },
        
        propiedades={
            'importable': True,
            'reutilizable': True
        },
        
        datos={
            'definicion': 'Archivo Python que contiene código',
            'ejemplos': ['import os', 'from math import sqrt']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.9
    )


def crear_concepto_codigo():
    """CONCEPTO: CÓDIGO"""
    
    return ConceptoAnclado(
        id="CONCEPTO_CODIGO",
        tipo=TipoConcepto.ENTIDAD_CODIGO,
        palabras_español=["código", "codigo", "code"],
        
        operaciones={
            'analizar': lambda codigo: ast.parse(codigo) if isinstance(codigo, str) else None,
        },
        
        relaciones={
            'es_un': {'TEXTO_EJECUTABLE'},
            'contiene': {'INSTRUCCIONES'}
        },
        
        propiedades={
            'ejecutable': True,
            'tiene_sintaxis': True
        },
        
        datos={
            'definicion': 'Instrucciones escritas en lenguaje de programación',
            'ejemplos': ['print("hola")', 'x = 5']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.95
    )


def crear_concepto_python():
    """CONCEPTO: PYTHON (lenguaje)"""
    
    return ConceptoAnclado(
        id="CONCEPTO_PYTHON",
        tipo=TipoConcepto.CONCEPTO_ABSTRACTO,
        palabras_español=["python"],
        
        operaciones={},  # Es un lenguaje, no tiene operaciones directas
        
        relaciones={
            'es_un': {'LENGUAJE_PROGRAMACION'},
            'caracteristicas': {'INTERPRETADO', 'ALTO_NIVEL', 'DINAMICO'}
        },
        
        propiedades={
            'interpretado': True,
            'tipado_dinamico': True,
            'usa_indentacion': True
        },
        
        datos={
            'definicion': 'Lenguaje de programación de alto nivel',
            'ejemplos': ['def funcion():', 'import modulo']
        },
        
        accesible_directamente=False,  # Es concepto abstracto
        confianza_grounding=0.85
    )


def crear_concepto_ejecutar():
    """CONCEPTO: EJECUTAR"""
    
    return ConceptoAnclado(
        id="CONCEPTO_EJECUTAR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["ejecutar", "run", "correr"],
        
        operaciones={
            'ejecutar_funcion': lambda func, *args: func(*args) if callable(func) else None,
        },
        
        relaciones={
            'es_un': {'OPERACION'},
            'aplica_a': {'CODIGO', 'FUNCION', 'PROGRAMA'}
        },
        
        propiedades={
            'produce_resultado': True,
            'puede_fallar': True
        },
        
        datos={
            'definicion': 'Correr código o función',
            'ejemplos': ['funcion()', 'python script.py']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.95
    )


def crear_concepto_analizar():
    """CONCEPTO: ANALIZAR"""
    
    return ConceptoAnclado(
        id="CONCEPTO_ANALIZAR",
        tipo=TipoConcepto.OPERACION_LOGICA,
        palabras_español=["analizar", "analyze", "revisar"],
        
        operaciones={
            'analizar_codigo': lambda codigo: ast.parse(codigo) if isinstance(codigo, str) else None,
        },
        
        relaciones={
            'es_un': {'OPERACION'},
            'aplica_a': {'CODIGO', 'DATOS', 'TEXTO'}
        },
        
        propiedades={
            'requiere_comprension': True,
            'produce_insights': True
        },
        
        datos={
            'definicion': 'Examinar para entender estructura o encontrar problemas',
            'ejemplos': ['analizar sintaxis', 'revisar lógica']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.9
    )


def crear_concepto_crear():
    """CONCEPTO: CREAR"""
    
    return ConceptoAnclado(
        id="CONCEPTO_CREAR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["crear", "create", "generar"],
        
        operaciones={
            'crear_archivo': lambda ruta: open(ruta, 'w', encoding='utf-8').close(),
            'crear_directorio': lambda ruta: os.makedirs(ruta, exist_ok=True),
        },
        
        relaciones={
            'es_un': {'OPERACION'},
            'aplica_a': {'ARCHIVO', 'DIRECTORIO', 'OBJETO'}
        },
        
        propiedades={
            'genera_nuevo': True,
            'puede_sobrescribir': False
        },
        
        datos={
            'definicion': 'Generar algo nuevo',
            'ejemplos': ['crear archivo', 'crear función']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.95
    )


def crear_concepto_eliminar():
    """CONCEPTO: ELIMINAR"""
    
    return ConceptoAnclado(
        id="CONCEPTO_ELIMINAR",
        tipo=TipoConcepto.OPERACION_SISTEMA,
        palabras_español=["eliminar", "delete", "borrar"],
        
        operaciones={
            'eliminar_archivo': lambda ruta: os.remove(ruta) if os.path.exists(ruta) else None,
        },
        
        relaciones={
            'es_un': {'OPERACION'},
            'aplica_a': {'ARCHIVO', 'VARIABLE'}
        },
        
        propiedades={
            'destructivo': True,
            'irreversible': True
        },
        
        datos={
            'definicion': 'Borrar algo existente',
            'ejemplos': ['os.remove()', 'del variable']
        },
        
        accesible_directamente=True,
        confianza_grounding=0.95
    )


def obtener_conceptos_core():
    """
    Retorna diccionario con los 20 conceptos base.
    
    Returns:
        Dict[str, ConceptoAnclado]: Diccionario de conceptos
    """
    conceptos = [
        crear_concepto_archivo(),
        crear_concepto_funcion(),
        crear_concepto_variable(),
        crear_concepto_lista(),
        crear_concepto_string(),
        crear_concepto_numero(),
        crear_concepto_diccionario(),
        crear_concepto_boolean(),
        crear_concepto_leer(),
        crear_concepto_escribir(),
        crear_concepto_bucle(),
        crear_concepto_condicional(),
        crear_concepto_clase(),
        crear_concepto_modulo(),
        crear_concepto_codigo(),
        crear_concepto_python(),
        crear_concepto_ejecutar(),
        crear_concepto_analizar(),
        crear_concepto_crear(),
        crear_concepto_eliminar(),
    ]
    
    return {c.id: c for c in conceptos}