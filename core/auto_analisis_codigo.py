"""
Sistema de Auto-Análisis de Código
Belladonna puede leer y entender su propio código
"""

import ast
from pathlib import Path
import logging

class AutoAnalisisCodigo:
    """
    Permite a Belladonna analizar su propio código.
    """
    
    def __init__(self):
        self.analisis_cache = {}
    
    def analizar_archivo(self, ruta):
        """
        Analiza un archivo de código Python.
        Retorna estadísticas y problemas detectados.
        """
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                codigo = f.read()
        except Exception as e:
            return {'error': f"No se pudo leer {ruta}: {e}"}
        
        try:
            arbol = ast.parse(codigo)
        except SyntaxError as e:
            return {'error': f"Error de sintaxis en {ruta}: {e}"}
        
        analisis = {
            'archivo': ruta,
            'lineas_totales': len(codigo.split('\n')),
            'funciones': [],
            'clases': [],
            'imports': [],
            'complejidad_estimada': 0,
            'comentarios': self._contar_comentarios(codigo),
            'problemas': []
        }
        
        # Analiza estructura
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.FunctionDef):
                func = {
                    'nombre': nodo.name,
                    'parametros': [arg.arg for arg in nodo.args.args],
                    'lineas': nodo.end_lineno - nodo.lineno if nodo.end_lineno else 0,
                    'tiene_docstring': ast.get_docstring(nodo) is not None
                }
                analisis['funciones'].append(func)
                analisis['complejidad_estimada'] += func['lineas']
                
                # Detecta funciones muy largas
                if func['lineas'] > 50:
                    analisis['problemas'].append({
                        'tipo': 'funcion_larga',
                        'ubicacion': f"{ruta}:{nodo.lineno}",
                        'funcion': func['nombre'],
                        'lineas': func['lineas'],
                        'sugerencia': 'Dividir en funciones más pequeñas'
                    })
                
                # Detecta falta de docstring
                if not func['tiene_docstring']:
                    analisis['problemas'].append({
                        'tipo': 'sin_docstring',
                        'ubicacion': f"{ruta}:{nodo.lineno}",
                        'funcion': func['nombre'],
                        'sugerencia': 'Agregar docstring explicativo'
                    })
            
            elif isinstance(nodo, ast.ClassDef):
                metodos = [n.name for n in nodo.body if isinstance(n, ast.FunctionDef)]
                analisis['clases'].append({
                    'nombre': nodo.name,
                    'metodos': metodos,
                    'total_metodos': len(metodos)
                })
            
            elif isinstance(nodo, ast.Import):
                analisis['imports'].extend([alias.name for alias in nodo.names])
            
            elif isinstance(nodo, ast.ImportFrom):
                if nodo.module:
                    analisis['imports'].append(nodo.module)
        
        # Detecta falta de comentarios
        ratio_comentarios = analisis['comentarios'] / max(analisis['lineas_totales'], 1)
        if ratio_comentarios < 0.1:
            analisis['problemas'].append({
                'tipo': 'pocos_comentarios',
                'ratio': f"{ratio_comentarios*100:.1f}%",
                'sugerencia': 'Agregar más comentarios explicativos'
            })
        
        self.analisis_cache[ruta] = analisis
        
        return analisis
    
    def _contar_comentarios(self, codigo):
        """Cuenta líneas de comentarios"""
        lineas = codigo.split('\n')
        comentarios = 0
        
        for linea in lineas:
            linea_stripped = linea.strip()
            if linea_stripped.startswith('#'):
                comentarios += 1
            elif '"""' in linea or "'''" in linea:
                comentarios += 1
        
        return comentarios
    
    def analizar_sistema_completo(self):
        """
        Analiza todos los archivos de Belladonna.
        """
        archivos_core = [
            'core/sistema_autonomo.py',
            'core/razonamiento.py',
            'core/memoria.py',
            'core/estado_interno.py',
            'core/valores.py',
            'core/auto_modificacion.py'
        ]
        
        resultados = {}
        
        for archivo in archivos_core:
            if Path(archivo).exists():
                resultados[archivo] = self.analizar_archivo(archivo)
        
        # Genera resumen
        resumen = {
            'archivos_analizados': len(resultados),
            'lineas_totales': sum(r.get('lineas_totales', 0) for r in resultados.values()),
            'funciones_totales': sum(len(r.get('funciones', [])) for r in resultados.values()),
            'problemas_totales': sum(len(r.get('problemas', [])) for r in resultados.values()),
            'archivos': resultados
        }
        
        return resumen
    
    def sugerir_mejoras(self, archivo):
        """
        Genera sugerencias específicas de mejora.
        """
        if archivo not in self.analisis_cache:
            analisis = self.analizar_archivo(archivo)
        else:
            analisis = self.analisis_cache[archivo]
        
        if 'error' in analisis:
            return analisis
        
        sugerencias = []
        
        # Prioriza problemas
        problemas = analisis.get('problemas', [])
        
        for prob in problemas:
            if prob['tipo'] == 'funcion_larga':
                sugerencias.append({
                    'prioridad': 'alta',
                    'tipo': prob['tipo'],
                    'mensaje': f"Función {prob['funcion']} tiene {prob['lineas']} líneas",
                    'accion': prob['sugerencia']
                })
            elif prob['tipo'] == 'pocos_comentarios':
                sugerencias.append({
                    'prioridad': 'media',
                    'tipo': prob['tipo'],
                    'mensaje': f"Solo {prob['ratio']} del código tiene comentarios",
                    'accion': prob['sugerencia']
                })
        
        return {
            'archivo': archivo,
            'total_sugerencias': len(sugerencias),
            'sugerencias': sugerencias
        }