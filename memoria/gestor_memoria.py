"""
Gestor de Memoria - Interfaz principal para memoria persistente.

Proporciona métodos de alto nivel para guardar y recuperar
información entre sesiones.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime
import uuid

from memoria.almacen import AlmacenJSON
from memoria.tipos_memoria import (
    TipoMemoria,
    RegistroConcepto,
    RegistroDecision,
    RegistroPatron,
    RegistroInsight,
    RegistroAjuste,
    RegistroSesion
)

class GestorMemoria:
    """
    Gestor central de memoria persistente.
    
    Proporciona métodos para:
    - Guardar conceptos, decisiones, patrones, insights
    - Recuperar información histórica
    - Generar estadísticas de uso
    - Gestionar sesiones
    """
    
    def __init__(self, directorio: str = "memoria_bell"):
        """
        Inicializa gestor de memoria.
        
        Args:
            directorio: Directorio donde guardar datos
        """
        self.almacen = AlmacenJSON(directorio)
        self.sesion_actual: Optional[str] = None
        self.sesion_inicio: Optional[str] = None
    
    # ===== SESIONES =====
    
    def iniciar_sesion(self) -> str:
        """
        Inicia una nueva sesión.
        
        Returns:
            ID de la sesión
        """
        self.sesion_actual = str(uuid.uuid4())
        self.sesion_inicio = datetime.now().isoformat()
        
        sesion: RegistroSesion = {
            'id_sesion': self.sesion_actual,
            'inicio': self.sesion_inicio,
            'fin': None,
            'mensajes_procesados': 0,
            'decisiones_tomadas': 0,
            'conceptos_usados': 0,
            'patrones_detectados': 0
        }
        
        self.almacen.guardar('sesiones', sesion)
        return self.sesion_actual
    
    def finalizar_sesion(self):
        """Finaliza la sesión actual."""
        if not self.sesion_actual:
            return
        
        # Cargar sesión
        sesiones = self.almacen.cargar('sesiones')
        for sesion in sesiones:
            if sesion['id_sesion'] == self.sesion_actual:
                sesion['fin'] = datetime.now().isoformat()
                break
        
        # Guardar actualización
        self.almacen.limpiar('sesiones')
        for sesion in sesiones:
            self.almacen.guardar('sesiones', sesion)
        
        self.sesion_actual = None
        self.sesion_inicio = None
    
    def _actualizar_contador_sesion(self, campo: str):
        """Actualiza contador en la sesión actual."""
        if not self.sesion_actual:
            return
        
        sesiones = self.almacen.cargar('sesiones')
        for sesion in sesiones:
            if sesion['id_sesion'] == self.sesion_actual:
                sesion[campo] = sesion.get(campo, 0) + 1
                break
        
        self.almacen.limpiar('sesiones')
        for sesion in sesiones:
            self.almacen.guardar('sesiones', sesion)
    
    # ===== CONCEPTOS =====
    
    def guardar_concepto_usado(self, concepto_id: str, certeza: float = 0.0):
        """
        Guarda uso de un concepto.
        
        Args:
            concepto_id: ID del concepto
            certeza: Certeza con que se usó
        """
        registro: RegistroConcepto = {
            'concepto_id': concepto_id,
            'timestamp': datetime.now().isoformat(),
            'veces_usado': 1,
            'ultima_certeza': certeza
        }
        
        self.almacen.guardar('conceptos', registro)
        self._actualizar_contador_sesion('conceptos_usados')
    
    def obtener_conceptos_mas_usados(self, n: int = 10) -> List[Dict[str, Any]]:
        """
        Obtiene los N conceptos más usados.
        
        Args:
            n: Número de conceptos a retornar
        
        Returns:
            Lista de conceptos con estadísticas
        """
        conceptos = self.almacen.cargar('conceptos')
        
        # Agrupar por concepto_id
        conteo: Dict[str, Dict[str, Any]] = {}
        for registro in conceptos:
            cid = registro['concepto_id']
            if cid not in conteo:
                conteo[cid] = {
                    'concepto_id': cid,
                    'usos': 0,
                    'certeza_promedio': 0.0,
                    'ultimo_uso': registro['timestamp']
                }
            conteo[cid]['usos'] += registro['veces_usado']
            conteo[cid]['ultimo_uso'] = max(conteo[cid]['ultimo_uso'], registro['timestamp'])
        
        # Ordenar por usos
        ranking = sorted(conteo.values(), key=lambda x: x['usos'], reverse=True)
        return ranking[:n]
    
    # ===== DECISIONES =====
    
    def guardar_decision(self, decision_info: Dict[str, Any]):
        """
        Guarda una decisión tomada.
        
        Args:
            decision_info: Información de la decisión
        """
        registro: RegistroDecision = {
            'timestamp': datetime.now().isoformat(),
            'tipo': decision_info.get('tipo', 'DESCONOCIDO'),
            'puede_ejecutar': decision_info.get('puede_ejecutar', False),
            'certeza': decision_info.get('certeza', 0.0),
            'conceptos_principales': decision_info.get('conceptos_principales', []),
            'grounding_promedio': decision_info.get('grounding_promedio', 0.0)
        }
        
        self.almacen.guardar('decisiones', registro)
        self._actualizar_contador_sesion('decisiones_tomadas')
    
    def obtener_decisiones_recientes(self, n: int = 20) -> List[RegistroDecision]:
        """
        Obtiene las N decisiones más recientes.
        
        Args:
            n: Número de decisiones
        
        Returns:
            Lista de decisiones
        """
        decisiones = self.almacen.cargar('decisiones')
        return decisiones[-n:]
    
    def obtener_estadisticas_decisiones(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas de decisiones.
        
        Returns:
            Dict con estadísticas
        """
        decisiones = self.almacen.cargar('decisiones')
        
        if not decisiones:
            return {
                'total': 0,
                'tasa_ejecucion': 0.0,
                'certeza_promedio': 0.0,
                'tipos': {}
            }
        
        ejecutables = sum(1 for d in decisiones if d['puede_ejecutar'])
        certezas = [d['certeza'] for d in decisiones]
        
        tipos: Dict[str, int] = {}
        for d in decisiones:
            tipo = d['tipo']
            tipos[tipo] = tipos.get(tipo, 0) + 1
        
        return {
            'total': len(decisiones),
            'tasa_ejecucion': (ejecutables / len(decisiones)) * 100,
            'certeza_promedio': sum(certezas) / len(certezas),
            'tipos': tipos
        }
    
    # ===== PATRONES =====
    
    def guardar_patron(self, patron_info: Dict[str, Any]):
        """
        Guarda un patrón detectado.
        
        Args:
            patron_info: Información del patrón
        """
        registro: RegistroPatron = {
            'timestamp': datetime.now().isoformat(),
            'tipo_patron': patron_info.get('tipo', 'DESCONOCIDO'),
            'descripcion': patron_info.get('descripcion', ''),
            'frecuencia': patron_info.get('frecuencia', 0),
            'confianza': patron_info.get('confianza', 0.0)
        }
        
        self.almacen.guardar('patrones', registro)
        self._actualizar_contador_sesion('patrones_detectados')
    
    def obtener_patrones_recientes(self, n: int = 10) -> List[RegistroPatron]:
        """
        Obtiene los N patrones más recientes.
        
        Args:
            n: Número de patrones
        
        Returns:
            Lista de patrones
        """
        patrones = self.almacen.cargar('patrones')
        return patrones[-n:]
    
    # ===== INSIGHTS =====
    
    def guardar_insight(self, insight_info: Dict[str, Any]):
        """
        Guarda un insight generado.
        
        Args:
            insight_info: Información del insight
        """
        registro: RegistroInsight = {
            'timestamp': datetime.now().isoformat(),
            'tipo_insight': insight_info.get('tipo', 'DESCONOCIDO'),
            'descripcion': insight_info.get('descripcion', ''),
            'relevancia': insight_info.get('relevancia', 'BAJA'),
            'datos': insight_info.get('datos', {})
        }
        
        self.almacen.guardar('insights', registro)
    
    def obtener_insights_recientes(
        self,
        n: int = 10,
        relevancia: Optional[str] = None
    ) -> List[RegistroInsight]:
        """
        Obtiene insights recientes.
        
        Args:
            n: Número de insights
            relevancia: Filtrar por relevancia ('ALTA', 'MEDIA', 'BAJA')
        
        Returns:
            Lista de insights
        """
        insights = self.almacen.cargar('insights')
        
        if relevancia:
            insights = [i for i in insights if i['relevancia'] == relevancia]
        
        return insights[-n:]
    
    # ===== AJUSTES DE GROUNDING =====
    
    def guardar_ajuste_grounding(
        self,
        concepto_id: str,
        grounding_anterior: float,
        grounding_nuevo: float,
        razon: str,
        aplicado: bool = True
    ):
        """
        Guarda un ajuste de grounding.
        
        Args:
            concepto_id: ID del concepto
            grounding_anterior: Valor anterior
            grounding_nuevo: Nuevo valor
            razon: Razón del ajuste
            aplicado: Si se aplicó o no
        """
        registro: RegistroAjuste = {
            'timestamp': datetime.now().isoformat(),
            'concepto_id': concepto_id,
            'grounding_anterior': grounding_anterior,
            'grounding_nuevo': grounding_nuevo,
            'razon': razon,
            'aplicado': aplicado
        }
        
        self.almacen.guardar('ajustes', registro)
    
    def obtener_ajustes_concepto(self, concepto_id: str) -> List[RegistroAjuste]:
        """
        Obtiene historial de ajustes de un concepto.
        
        Args:
            concepto_id: ID del concepto
        
        Returns:
            Lista de ajustes
        """
        ajustes = self.almacen.cargar('ajustes')
        return [a for a in ajustes if a['concepto_id'] == concepto_id]
    
    # ===== UTILIDADES =====
    
    def obtener_resumen_sesion(self, id_sesion: Optional[str] = None) -> Optional[RegistroSesion]:
        """
        Obtiene resumen de una sesión.
        
        Args:
            id_sesion: ID de sesión (None = sesión actual)
        
        Returns:
            Resumen de sesión o None
        """
        id_buscar = id_sesion or self.sesion_actual
        if not id_buscar:
            return None
        
        sesiones = self.almacen.cargar('sesiones')
        for sesion in sesiones:
            if sesion['id_sesion'] == id_buscar:
                return sesion
        
        return None
    
    def obtener_estadisticas_globales(self) -> Dict[str, Any]:
        """
        Obtiene estadísticas globales del sistema.
        
        Returns:
            Dict con estadísticas completas
        """
        return {
            'total_sesiones': self.almacen.contar('sesiones'),
            'total_conceptos_usados': self.almacen.contar('conceptos'),
            'total_decisiones': self.almacen.contar('decisiones'),
            'total_patrones': self.almacen.contar('patrones'),
            'total_insights': self.almacen.contar('insights'),
            'total_ajustes': self.almacen.contar('ajustes'),
            'conceptos_mas_usados': self.obtener_conceptos_mas_usados(5),
            'estadisticas_decisiones': self.obtener_estadisticas_decisiones(),
            'almacen': self.almacen.obtener_estadisticas()
        }
    
    def limpiar_memoria(self, tipo: Optional[str] = None):
        """
        Limpia memoria.
        
        Args:
            tipo: Tipo específico a limpiar (None = todo)
        """
        if tipo:
            self.almacen.limpiar(tipo)
        else:
            self.almacen.limpiar_todo()
    
    def exportar_memoria(self, archivo: str) -> bool:
        """
        Exporta toda la memoria a un archivo.
        
        Args:
            archivo: Ruta del archivo
        
        Returns:
            True si se exportó correctamente
        """
        return self.almacen.exportar(archivo)
    
    def importar_memoria(self, archivo: str) -> bool:
        """
        Importa memoria desde un archivo.
        
        Args:
            archivo: Ruta del archivo
        
        Returns:
            True si se importó correctamente
        """
        return self.almacen.importar(archivo)