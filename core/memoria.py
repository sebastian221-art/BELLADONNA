"""
Sistema de Memoria Viva
Gestión de memoria persistente con olvido inteligente
"""

import json
import sqlite3
from datetime import datetime
from pathlib import Path

class MemoriaViva:
    """
    Sistema de memoria con múltiples tipos:
    - Episódica (eventos importantes)
    - Procedimental (cómo hacer cosas)
    - De errores (prioritaria)
    - Propósito e intención
    """
    
    def __init__(self):
        self.db_path = Path("memoria/conversaciones.db")
        self.proposito_path = Path("memoria/proposito.json")
        self._inicializar_bd()
    
    def _inicializar_bd(self):
        """Crea las tablas si no existen"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabla de conversaciones
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                tipo TEXT,
                contenido TEXT,
                importancia INTEGER DEFAULT 50,
                tags TEXT
            )
        ''')
        
        # Tabla de decisiones
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS decisiones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                contexto TEXT,
                decision TEXT,
                razonamiento TEXT,
                coherencia REAL,
                resultado TEXT
            )
        ''')
        
        # Tabla de errores (PRIORITARIA)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS errores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                error TEXT,
                contexto TEXT,
                leccion TEXT,
                prioridad INTEGER DEFAULT 100
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def obtener_proposito(self):
        """Carga el propósito fundacional"""
        try:
            with open(self.proposito_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"proposito_fundacional": "No definido", "activo": False}
    
    def guardar_conversacion(self, tipo, contenido, importancia=50, tags=None):
        """Guarda una conversación en memoria"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        tags_str = json.dumps(tags) if tags else None
        
        cursor.execute('''
            INSERT INTO conversaciones (tipo, contenido, importancia, tags)
            VALUES (?, ?, ?, ?)
        ''', (tipo, contenido, importancia, tags_str))
        
        conn.commit()
        conn.close()
    
    def registrar_decision(self, decision, razonamiento, coherencia, contexto=""):
        """Registra una decisión importante"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO decisiones (contexto, decision, razonamiento, coherencia)
            VALUES (?, ?, ?, ?)
        ''', (contexto, decision, razonamiento, coherencia))
        
        conn.commit()
        conn.close()
    
    def registrar_error(self, error, contexto, leccion, prioridad=100):
        """
        Registra un error PARA APRENDER DE ÉL.
        Los errores son memoria de alta prioridad.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO errores (error, contexto, leccion, prioridad)
            VALUES (?, ?, ?, ?)
        ''', (error, contexto, leccion, prioridad))
        
        conn.commit()
        conn.close()
    
    def buscar_errores_similares(self, contexto_actual):
        """Busca errores pasados similares al contexto actual"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Búsqueda simple por keywords (mejorable con embeddings)
        keywords = contexto_actual.lower().split()
        
        cursor.execute('''
            SELECT error, contexto, leccion, fecha
            FROM errores
            WHERE prioridad > 50
            ORDER BY fecha DESC
            LIMIT 10
        ''')
        
        errores = cursor.fetchall()
        conn.close()
        
        # Filtrar por similaridad (muy básico)
        similares = []
        for error in errores:
            error_text = (error[0] + " " + error[1]).lower()
            if any(kw in error_text for kw in keywords):
                similares.append({
                    'error': error[0],
                    'contexto': error[1],
                    'leccion': error[2],
                    'fecha': error[3]
                })
        
        return similares
    
    def obtener_decisiones_recientes(self, limite=10):
        """Obtiene las decisiones más recientes"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT decision, razonamiento, coherencia, fecha
            FROM decisiones
            ORDER BY fecha DESC
            LIMIT ?
        ''', (limite,))
        
        decisiones = cursor.fetchall()
        conn.close()
        
        return [
            {
                'decision': d[0],
                'razonamiento': d[1],
                'coherencia': d[2],
                'fecha': d[3]
            }
            for d in decisiones
        ]
    
    def degradar_memoria_irrelevante(self):
        """
        Sistema de olvido inteligente.
        Reduce importancia de conversaciones antiguas sin interacciones.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Degrada conversaciones de más de 30 días
        cursor.execute('''
            UPDATE conversaciones
            SET importancia = MAX(0, importancia - 10)
            WHERE fecha < datetime('now', '-30 days')
            AND importancia > 0
        ''')
        
        cambios = cursor.rowcount
        conn.commit()
        conn.close()
        
        return cambios