"""
Cliente SQLite para manejo de bases de datos.
FASE 3 - Semana 8 (VERSIÓN DEFINITIVA CON TRANSACCIONES)
"""

import sqlite3
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ResultadoQuery:
    """Resultado de una query SQL."""
    exitoso: bool
    filas: List[Tuple]
    filas_afectadas: int
    columnas: List[str]
    error: Optional[str] = None


class ClienteSQLite:
    """
    Cliente SQLite simple usando sqlite3 (stdlib).
    
    Capacidades:
    - Crear y conectar bases de datos
    - Crear tablas
    - INSERT, SELECT, UPDATE, DELETE
    - Queries con filtros
    - Transacciones
    - Manejo de errores
    """
    
    def __init__(self, db_path: str = ":memory:"):
        """
        Inicializa el cliente SQLite.
        
        Args:
            db_path: Ruta a la base de datos. ":memory:" para BD en memoria
        """
        self.db_path = db_path
        self.conexion: Optional[sqlite3.Connection] = None
        self.cursor: Optional[sqlite3.Cursor] = None
        self.auto_commit_enabled = True  # Control de auto-commit
    
    def conectar(self) -> bool:
        """
        Conecta a la base de datos.
        
        Returns:
            True si conexión exitosa
        """
        try:
            self.conexion = sqlite3.connect(self.db_path)
            # NO usar row_factory para que las filas sean tuplas accesibles por índice
            self.cursor = self.conexion.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Error conectando: {e}")
            return False
    
    def desconectar(self):
        """Cierra la conexión a la base de datos."""
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
        self.conexion = None
        self.cursor = None
    
    def ejecutar_sql(
        self,
        sql: str,
        parametros: Optional[Tuple] = None
    ) -> ResultadoQuery:
        """
        Ejecuta una query SQL.
        
        Args:
            sql: Query SQL
            parametros: Parámetros para la query
            
        Returns:
            ResultadoQuery
        """
        if not self.conexion:
            return ResultadoQuery(
                exitoso=False,
                filas=[],
                filas_afectadas=0,
                columnas=[],
                error="No hay conexión a la base de datos"
            )
        
        try:
            if parametros:
                self.cursor.execute(sql, parametros)
            else:
                self.cursor.execute(sql)
            
            # Intentar obtener resultados (para SELECT)
            try:
                filas = self.cursor.fetchall()
                columnas = [desc[0] for desc in self.cursor.description] if self.cursor.description else []
            except:
                filas = []
                columnas = []
            
            filas_afectadas = self.cursor.rowcount
            
            # Auto-commit SOLO si está habilitado y es operación de escritura
            if self.auto_commit_enabled:
                if sql.strip().upper().startswith(('INSERT', 'UPDATE', 'DELETE', 'CREATE', 'DROP', 'ALTER')):
                    self.conexion.commit()
            
            return ResultadoQuery(
                exitoso=True,
                filas=filas,
                filas_afectadas=filas_afectadas,
                columnas=columnas
            )
            
        except sqlite3.Error as e:
            return ResultadoQuery(
                exitoso=False,
                filas=[],
                filas_afectadas=0,
                columnas=[],
                error=str(e)
            )
    
    def crear_tabla(
        self,
        nombre: str,
        columnas: Dict[str, str],
        primary_key: Optional[str] = None
    ) -> bool:
        """
        Crea una tabla.
        
        Args:
            nombre: Nombre de la tabla
            columnas: Dict {nombre_columna: tipo}
            primary_key: Nombre de la columna primary key
            
        Returns:
            True si creación exitosa
        """
        # Construir definición de columnas
        columnas_def = []
        for col, tipo in columnas.items():
            definicion = f"{col} {tipo}"
            if primary_key and col == primary_key:
                definicion += " PRIMARY KEY"
            columnas_def.append(definicion)
        
        sql = f"CREATE TABLE IF NOT EXISTS {nombre} ({', '.join(columnas_def)})"
        
        resultado = self.ejecutar_sql(sql)
        return resultado.exitoso
    
    def insertar(
        self,
        tabla: str,
        datos: Dict[str, Any]
    ) -> ResultadoQuery:
        """
        Inserta un registro.
        
        Args:
            tabla: Nombre de la tabla
            datos: Dict {columna: valor}
            
        Returns:
            ResultadoQuery
        """
        columnas = list(datos.keys())
        valores = list(datos.values())
        placeholders = ', '.join(['?' for _ in valores])
        
        sql = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({placeholders})"
        
        return self.ejecutar_sql(sql, tuple(valores))
    
    def seleccionar(
        self,
        tabla: str,
        columnas: Optional[List[str]] = None,
        where: Optional[str] = None,
        order_by: Optional[str] = None,
        limit: Optional[int] = None
    ) -> ResultadoQuery:
        """
        Selecciona registros.
        
        Args:
            tabla: Nombre de la tabla
            columnas: Columnas a seleccionar (None = todas)
            where: Condición WHERE (puede contener valores directos)
            order_by: Columna para ordenar
            limit: Límite de resultados
            
        Returns:
            ResultadoQuery
        """
        cols = ', '.join(columnas) if columnas else '*'
        sql = f"SELECT {cols} FROM {tabla}"
        
        if where:
            sql += f" WHERE {where}"
        
        if order_by:
            sql += f" ORDER BY {order_by}"
        
        if limit:
            sql += f" LIMIT {limit}"
        
        return self.ejecutar_sql(sql)
    
    def actualizar(
        self,
        tabla: str,
        datos: Dict[str, Any],
        where: str
    ) -> ResultadoQuery:
        """
        Actualiza registros.
        
        Args:
            tabla: Nombre de la tabla
            datos: Dict {columna: nuevo_valor}
            where: Condición WHERE (valores directos)
            
        Returns:
            ResultadoQuery
        """
        set_clause = ', '.join([f"{col} = ?" for col in datos.keys()])
        sql = f"UPDATE {tabla} SET {set_clause} WHERE {where}"
        
        valores = tuple(datos.values())
        
        return self.ejecutar_sql(sql, valores)
    
    def eliminar(
        self,
        tabla: str,
        where: str
    ) -> ResultadoQuery:
        """
        Elimina registros.
        
        Args:
            tabla: Nombre de la tabla
            where: Condición WHERE (valores directos)
            
        Returns:
            ResultadoQuery
        """
        sql = f"DELETE FROM {tabla} WHERE {where}"
        
        return self.ejecutar_sql(sql)
    
    def contar(
        self,
        tabla: str,
        where: Optional[str] = None
    ) -> int:
        """
        Cuenta registros.
        
        Args:
            tabla: Nombre de la tabla
            where: Condición WHERE opcional (valores directos)
            
        Returns:
            Número de registros
        """
        sql = f"SELECT COUNT(*) FROM {tabla}"
        
        if where:
            sql += f" WHERE {where}"
        
        resultado = self.ejecutar_sql(sql)
        
        if resultado.exitoso and resultado.filas:
            return resultado.filas[0][0]
        
        return 0
    
    def listar_tablas(self) -> List[str]:
        """
        Lista todas las tablas de la base de datos.
        
        Returns:
            Lista de nombres de tablas
        """
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        resultado = self.ejecutar_sql(sql)
        
        if resultado.exitoso:
            return [fila[0] for fila in resultado.filas]
        
        return []
    
    def obtener_esquema(self, tabla: str) -> List[Dict[str, Any]]:
        """
        Obtiene el esquema de una tabla.
        
        Args:
            tabla: Nombre de la tabla
            
        Returns:
            Lista de dicts con info de columnas
        """
        sql = f"PRAGMA table_info({tabla})"
        resultado = self.ejecutar_sql(sql)
        
        if resultado.exitoso:
            columnas = []
            for fila in resultado.filas:
                columnas.append({
                    'cid': fila[0],
                    'nombre': fila[1],
                    'tipo': fila[2],
                    'notnull': fila[3],
                    'default': fila[4],
                    'pk': fila[5]
                })
            return columnas
        
        return []
    
    def existe_tabla(self, tabla: str) -> bool:
        """
        Verifica si una tabla existe.
        
        Args:
            tabla: Nombre de la tabla
            
        Returns:
            True si existe
        """
        return tabla in self.listar_tablas()
    
    def eliminar_tabla(self, tabla: str) -> bool:
        """
        Elimina una tabla.
        
        Args:
            tabla: Nombre de la tabla
            
        Returns:
            True si eliminación exitosa
        """
        sql = f"DROP TABLE IF EXISTS {tabla}"
        resultado = self.ejecutar_sql(sql)
        return resultado.exitoso
    
    def vaciar_tabla(self, tabla: str) -> bool:
        """
        Vacía una tabla (elimina todos los registros).
        
        Args:
            tabla: Nombre de la tabla
            
        Returns:
            True si operación exitosa
        """
        sql = f"DELETE FROM {tabla}"
        resultado = self.ejecutar_sql(sql)
        return resultado.exitoso


# Ejemplo de uso
if __name__ == '__main__':
    # Crear cliente con BD en memoria
    cliente = ClienteSQLite(":memory:")
    
    # Conectar
    if cliente.conectar():
        print("✅ Conectado a la base de datos")
        
        # Crear tabla
        exitoso = cliente.crear_tabla(
            "usuarios",
            {"id": "INTEGER", "nombre": "TEXT", "edad": "INTEGER"},
            primary_key="id"
        )
        print(f"✅ Tabla 'usuarios' creada: {exitoso}")
        
        # Insertar datos
        cliente.insertar("usuarios", {"id": 1, "nombre": "Bell", "edad": 1})
        cliente.insertar("usuarios", {"id": 2, "nombre": "Lyra", "edad": 25})
        print("✅ Datos insertados")
        
        # Seleccionar
        resultado = cliente.seleccionar("usuarios")
        print(f"\n📊 Usuarios ({len(resultado.filas)}):")
        for fila in resultado.filas:
            print(f"   ID: {fila[0]}, Nombre: {fila[1]}, Edad: {fila[2]}")
        
        # Actualizar
        cliente.actualizar("usuarios", {"edad": 2}, "nombre = 'Bell'")
        print("\n✅ Usuario actualizado")
        
        # Contar
        total = cliente.contar("usuarios")
        print(f"📊 Total usuarios: {total}")
        
        # Desconectar
        cliente.desconectar()
        print("\n✅ Desconectado")