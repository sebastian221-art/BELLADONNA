# memoria/persistencia.py

"""
Persistencia de memoria en SQLite.

FASE 2: Implementación básica
FASE 3: Expandir con grafo de conocimiento
"""

import sqlite3
import json
from typing import List, Dict
from datetime import datetime
from pathlib import Path


class PersistenciaMemoria:
    """
    Persistencia de memoria en SQLite.
    
    FASE 2: Implementación básica
    FASE 3: Expandir con grafo de conocimiento
    """
    
    def __init__(self, db_path: str = "data/conversaciones.db"):
        self.db_path = db_path
        
        # Crear directorio si no existe
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Inicializar base de datos
        self._inicializar_db()
    
    def _inicializar_db(self):
        """Crea tablas si no existen."""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sesion_id TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                rol TEXT NOT NULL,
                contenido TEXT NOT NULL,
                conceptos TEXT,
                metadata TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def guardar_mensaje(
        self,
        sesion_id: str,
        rol: str,
        contenido: str,
        conceptos: List[str] = None,
        metadata: Dict = None
    ):
        """Guarda mensaje en base de datos."""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO conversaciones 
            (sesion_id, timestamp, rol, contenido, conceptos, metadata)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            sesion_id,
            datetime.now().isoformat(),
            rol,
            contenido,
            json.dumps(conceptos or []),
            json.dumps(metadata or {})
        ))
        
        conn.commit()
        conn.close()
    
    def cargar_sesion(self, sesion_id: str) -> List[Dict]:
        """Carga conversación completa de una sesión."""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT timestamp, rol, contenido, conceptos, metadata
            FROM conversaciones
            WHERE sesion_id = ?
            ORDER BY timestamp
        """, (sesion_id,))
        
        mensajes = []
        for row in cursor.fetchall():
            mensajes.append({
                'timestamp': row[0],
                'rol': row[1],
                'contenido': row[2],
                'conceptos': json.loads(row[3]),
                'metadata': json.loads(row[4])
            })
        
        conn.close()
        return mensajes
    
    def listar_sesiones(self) -> List[Dict]:
        """Lista todas las sesiones guardadas."""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT sesion_id, MIN(timestamp) as inicio, COUNT(*) as mensajes
            FROM conversaciones
            GROUP BY sesion_id
            ORDER BY inicio DESC
        """)
        
        sesiones = []
        for row in cursor.fetchall():
            sesiones.append({
                'sesion_id': row[0],
                'inicio': row[1],
                'mensajes': row[2]
            })
        
        conn.close()
        return sesiones