"""
Sistema de Auto-Modificación Segura
Permite a Belladonna modificarse a sí misma con reversibilidad total
Principio #9: Reversibilidad
"""

import ast
import shutil
import json
from datetime import datetime
from pathlib import Path
import logging
import sys
import importlib

class AutoModificador:
    """
    Permite a Belladonna modificarse a sí misma de forma segura.
    
    Flujo:
    1. Usuario propone cambio
    2. Valida sintaxis Python
    3. Crea checkpoint (backup)
    4. Aplica cambio
    5. Prueba que funciona
    6. Si falla → rollback automático
    7. Si funciona → aprende el patrón
    """
    
    def __init__(self):
        self.ruta_backups = Path("memoria/checkpoints")
        self.ruta_backups.mkdir(exist_ok=True)
        
        self.historial_cambios = Path("memoria/historial_cambios.json")
        self.cambios = self._cargar_historial()
        
        self.archivos_protegidos = [
            'memoria/proposito.json',
            'memoria/principios.json'
        ]
        
        logging.info("AutoModificador inicializado")
    
    def _cargar_historial(self):
        """Carga historial de cambios"""
        try:
            with open(self.historial_cambios, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def _guardar_historial(self):
        """Guarda historial de cambios"""
        with open(self.historial_cambios, 'w', encoding='utf-8') as f:
            json.dump(self.cambios, f, indent=2, ensure_ascii=False)
    
    def validar_codigo(self, codigo):
        """
        Valida que el código es Python válido.
        Retorna: (es_valido, error_mensaje)
        """
        try:
            ast.parse(codigo)
            return True, None
        except SyntaxError as e:
            return False, f"Error de sintaxis en línea {e.lineno}: {e.msg}"
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def crear_checkpoint(self, archivo, razon):
        """
        Crea backup del archivo antes de modificarlo.
        Retorna: ID del checkpoint
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        checkpoint_id = f"{timestamp}_{Path(archivo).stem}"
        
        # Ruta del backup
        archivo_path = Path(archivo)
        backup_path = self.ruta_backups / f"{checkpoint_id}.py"
        
        # Copia el archivo
        shutil.copy2(archivo_path, backup_path)
        
        # Registra el checkpoint
        checkpoint = {
            'id': checkpoint_id,
            'timestamp': timestamp,
            'archivo_original': str(archivo),
            'archivo_backup': str(backup_path),
            'razon': razon
        }
        
        self.cambios.append(checkpoint)
        self._guardar_historial()
        
        logging.info(f"Checkpoint creado: {checkpoint_id}")
        
        return checkpoint_id
    
    def aplicar_cambio(self, archivo, codigo_nuevo, razon):
        """
        Aplica un cambio completo a un archivo.
        
        Parámetros:
        - archivo: ruta del archivo a modificar
        - codigo_nuevo: nuevo contenido completo del archivo
        - razon: por qué se hace este cambio
        
        Retorna: (exito, mensaje, checkpoint_id)
        """
        # 1. Verificar que no sea archivo protegido
        if archivo in self.archivos_protegidos:
            return False, f"❌ Archivo protegido: {archivo}", None
        
        # 2. Validar sintaxis
        es_valido, error = self.validar_codigo(codigo_nuevo)
        if not es_valido:
            return False, f"❌ Código inválido: {error}", None
        
        # 3. Crear checkpoint
        try:
            checkpoint_id = self.crear_checkpoint(archivo, razon)
        except Exception as e:
            return False, f"❌ Error creando checkpoint: {e}", None
        
        # 4. Aplicar cambio
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write(codigo_nuevo)
            
            logging.info(f"Cambio aplicado a {archivo}")
            
            # 5. Validar que el módulo se puede importar
            exito_prueba = self._probar_importacion(archivo)
            
            if exito_prueba:
                return True, f"✅ Cambio aplicado exitosamente. Checkpoint: {checkpoint_id}", checkpoint_id
            else:
                # Rollback automático
                self.revertir(checkpoint_id)
                return False, f"❌ El cambio rompió el módulo. Rollback automático.", checkpoint_id
                
        except Exception as e:
            # Rollback en caso de error
            self.revertir(checkpoint_id)
            return False, f"❌ Error aplicando cambio: {e}. Rollback automático.", checkpoint_id
    
    def _probar_importacion(self, archivo):
        """
        Intenta reimportar el módulo para verificar que funciona.
        """
        try:
            # Convierte path a nombre de módulo
            # Ej: core/razonamiento.py → core.razonamiento
            modulo_path = Path(archivo)
            modulo_nombre = str(modulo_path.with_suffix('')).replace('/', '.').replace('\\', '.')
            
            # Remueve del cache si existe
            if modulo_nombre in sys.modules:
                del sys.modules[modulo_nombre]
            
            # Intenta importar
            importlib.import_module(modulo_nombre)
            
            return True
        except Exception as e:
            logging.error(f"Error probando importación de {archivo}: {e}")
            return False
    
    def revertir(self, checkpoint_id):
        """
        Revierte un cambio usando su checkpoint.
        """
        # Busca el checkpoint
        checkpoint = None
        for c in self.cambios:
            if c['id'] == checkpoint_id:
                checkpoint = c
                break
        
        if not checkpoint:
            return False, f"❌ Checkpoint no encontrado: {checkpoint_id}"
        
        try:
            # Restaura el backup
            shutil.copy2(checkpoint['archivo_backup'], checkpoint['archivo_original'])
            
            logging.info(f"Rollback exitoso: {checkpoint_id}")
            
            return True, f"✅ Rollback exitoso. Restaurado: {checkpoint['archivo_original']}"
            
        except Exception as e:
            return False, f"❌ Error en rollback: {e}"
    
    def modificar_funcion(self, archivo, nombre_funcion, codigo_funcion, razon):
        """
        Modifica solo una función específica dentro de un archivo.
        
        Parámetros:
        - archivo: ruta del archivo
        - nombre_funcion: nombre de la función a reemplazar
        - codigo_funcion: nuevo código de la función
        - razon: por qué se modifica
        
        Retorna: (exito, mensaje, checkpoint_id)
        """
        # 1. Lee el archivo actual
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                codigo_actual = f.read()
        except Exception as e:
            return False, f"❌ Error leyendo archivo: {e}", None
        
        # 2. Parsea el código actual
        try:
            arbol = ast.parse(codigo_actual)
        except Exception as e:
            return False, f"❌ Error parseando código actual: {e}", None
        
        # 3. Encuentra la función
        funcion_encontrada = False
        linea_inicio = None
        linea_fin = None
        
        for nodo in ast.walk(arbol):
            if isinstance(nodo, ast.FunctionDef) and nodo.name == nombre_funcion:
                funcion_encontrada = True
                linea_inicio = nodo.lineno - 1  # ast usa 1-indexed
                linea_fin = nodo.end_lineno
                break
        
        if not funcion_encontrada:
            return False, f"❌ Función '{nombre_funcion}' no encontrada en {archivo}", None
        
        # 4. Reemplaza la función
        lineas = codigo_actual.split('\n')
        codigo_nuevo = (
            '\n'.join(lineas[:linea_inicio]) + 
            '\n' + codigo_funcion + '\n' + 
            '\n'.join(lineas[linea_fin:])
        )
        
        # 5. Aplica el cambio usando el método general
        return self.aplicar_cambio(archivo, codigo_nuevo, razon)
    
    def analizar_codigo(self, codigo):
        """
        Analiza un código y extrae información útil.
        Para aprender patrones del usuario.
        """
        try:
            arbol = ast.parse(codigo)
            
            analisis = {
                'funciones': [],
                'clases': [],
                'imports': [],
                'complejidad_estimada': 0
            }
            
            for nodo in ast.walk(arbol):
                if isinstance(nodo, ast.FunctionDef):
                    analisis['funciones'].append({
                        'nombre': nodo.name,
                        'parametros': [arg.arg for arg in nodo.args.args],
                        'tiene_docstring': ast.get_docstring(nodo) is not None,
                        'lineas': len(nodo.body)
                    })
                    analisis['complejidad_estimada'] += len(nodo.body)
                    
                elif isinstance(nodo, ast.ClassDef):
                    analisis['clases'].append({
                        'nombre': nodo.name,
                        'metodos': len([n for n in nodo.body if isinstance(n, ast.FunctionDef)])
                    })
                    
                elif isinstance(nodo, ast.Import):
                    analisis['imports'].extend([alias.name for alias in nodo.names])
                    
                elif isinstance(nodo, ast.ImportFrom):
                    analisis['imports'].append(nodo.module)
            
            return analisis
            
        except Exception as e:
            return {'error': str(e)}
    
    def listar_checkpoints(self, ultimos_n=10):
        """
        Lista los últimos N checkpoints.
        """
        checkpoints_recientes = self.cambios[-ultimos_n:]
        
        resultado = []
        for c in reversed(checkpoints_recientes):
            resultado.append({
                'id': c['id'],
                'archivo': c['archivo_original'],
                'razon': c['razon'],
                'timestamp': c['timestamp']
            })
        
        return resultado
    
    def obtener_estadisticas(self):
        """
        Estadísticas del sistema de auto-modificación.
        """
        return {
            'total_cambios': len(self.cambios),
            'archivos_protegidos': len(self.archivos_protegidos),
            'checkpoints_disponibles': len(list(self.ruta_backups.glob('*.py')))
        }