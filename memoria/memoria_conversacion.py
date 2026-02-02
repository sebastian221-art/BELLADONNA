# memoria/memoria_conversacion.py

"""
Memoria de conversación de la sesión actual.

FASE 2: Memoria en RAM (se pierde al cerrar)
FASE 3: Persistencia en SQLite
"""

from typing import List, Dict, Any
from datetime import datetime
from dataclasses import dataclass, field
import hashlib


@dataclass
class MensajeMemoria:
    """Mensaje almacenado en memoria."""
    rol: str  # 'usuario' o 'bell'
    contenido: str
    timestamp: datetime = field(default_factory=datetime.now)
    conceptos_usados: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class MemoriaConversacion:
    """
    Memoria de conversación de la sesión actual.
    
    FASE 2: Memoria en RAM (se pierde al cerrar)
    FASE 3: Persistencia en SQLite
    """
    
    def __init__(self):
        self.mensajes: List[MensajeMemoria] = []
        self.sesion_id = self._generar_sesion_id()
        self.inicio_sesion = datetime.now()
    
    def agregar_mensaje(
        self,
        rol: str,
        contenido: str,
        conceptos: List[str] = None,
        metadata: Dict = None
    ):
        """Agrega mensaje a memoria."""
        
        mensaje = MensajeMemoria(
            rol=rol,
            contenido=contenido,
            conceptos_usados=conceptos or [],
            metadata=metadata or {}
        )
        
        self.mensajes.append(mensaje)
    
    def obtener_historial(self, ultimos_n: int = None) -> List[MensajeMemoria]:
        """Obtiene historial de mensajes."""
        
        if ultimos_n is None:
            return self.mensajes.copy()
        else:
            return self.mensajes[-ultimos_n:]
    
    def obtener_contexto_reciente(self, n_mensajes: int = 5) -> str:
        """Obtiene contexto reciente como texto."""
        
        mensajes_recientes = self.obtener_historial(n_mensajes)
        
        contexto = []
        for msg in mensajes_recientes:
            prefijo = "Tú:" if msg.rol == 'usuario' else "Bell:"
            contexto.append(f"{prefijo} {msg.contenido}")
        
        return "\n".join(contexto)
    
    def buscar_conceptos(self, concepto: str) -> List[MensajeMemoria]:
        """Busca mensajes que usan concepto específico."""
        
        return [
            msg for msg in self.mensajes
            if concepto in msg.conceptos_usados
        ]
    
    def estadisticas(self) -> Dict:
        """Estadísticas de la conversación."""
        
        total = len(self.mensajes)
        usuario = sum(1 for m in self.mensajes if m.rol == 'usuario')
        bell = sum(1 for m in self.mensajes if m.rol == 'bell')
        
        # Conceptos más usados
        from collections import Counter
        conceptos = []
        for msg in self.mensajes:
            conceptos.extend(msg.conceptos_usados)
        
        top_conceptos = Counter(conceptos).most_common(10)
        
        duracion = datetime.now() - self.inicio_sesion
        
        return {
            'total_mensajes': total,
            'mensajes_usuario': usuario,
            'mensajes_bell': bell,
            'duracion_minutos': int(duracion.total_seconds() / 60),
            'top_conceptos': top_conceptos,
            'sesion_id': self.sesion_id
        }
    
    def _generar_sesion_id(self) -> str:
        """Genera ID único de sesión."""
        timestamp = str(datetime.now().timestamp())
        return hashlib.md5(timestamp.encode()).hexdigest()[:8]