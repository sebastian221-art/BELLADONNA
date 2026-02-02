# tests/test_memoria.py

"""
Tests para sistema de memoria.
"""

import pytest
from memoria.memoria_conversacion import MemoriaConversacion, MensajeMemoria
from memoria.persistencia import PersistenciaMemoria
import tempfile
import os


class TestMemoriaConversacion:
    """Tests para memoria de conversación."""
    
    def test_agregar_mensaje(self):
        """Test: Agregar mensaje a memoria."""
        memoria = MemoriaConversacion()
        
        memoria.agregar_mensaje('usuario', 'Hola')
        memoria.agregar_mensaje('bell', 'Hola, ¿en qué puedo ayudar?')
        
        historial = memoria.obtener_historial()
        assert len(historial) == 2
        assert historial[0].rol == 'usuario'
        assert historial[1].rol == 'bell'
    
    def test_obtener_ultimos_n(self):
        """Test: Obtener últimos N mensajes."""
        memoria = MemoriaConversacion()
        
        for i in range(10):
            memoria.agregar_mensaje('usuario', f'Mensaje {i}')
        
        ultimos_5 = memoria.obtener_historial(ultimos_n=5)
        assert len(ultimos_5) == 5
        assert ultimos_5[0].contenido == 'Mensaje 5'
    
    def test_buscar_conceptos(self):
        """Test: Buscar mensajes por concepto."""
        memoria = MemoriaConversacion()
        
        memoria.agregar_mensaje(
            'usuario',
            'Usa Python',
            conceptos=['CONCEPTO_PYTHON']
        )
        memoria.agregar_mensaje(
            'usuario',
            'Escribe código',
            conceptos=['CONCEPTO_CODIGO']
        )
        
        con_python = memoria.buscar_conceptos('CONCEPTO_PYTHON')
        assert len(con_python) == 1
        assert 'Python' in con_python[0].contenido
    
    def test_estadisticas(self):
        """Test: Estadísticas de conversación."""
        memoria = MemoriaConversacion()
        
        memoria.agregar_mensaje('usuario', 'Hola')
        memoria.agregar_mensaje('bell', 'Hola')
        memoria.agregar_mensaje('usuario', 'Adiós')
        
        stats = memoria.estadisticas()
        
        assert stats['total_mensajes'] == 3
        assert stats['mensajes_usuario'] == 2
        assert stats['mensajes_bell'] == 1
        assert 'sesion_id' in stats


class TestPersistenciaMemoria:
    """Tests para persistencia."""
    
    def test_guardar_y_cargar_mensaje(self):
        """Test: Guardar y cargar mensajes."""
        
        # Crear DB temporal
        with tempfile.NamedTemporaryFile(delete=False) as f:
            db_path = f.name
        
        try:
            persistencia = PersistenciaMemoria(db_path)
            
            # Guardar
            persistencia.guardar_mensaje(
                'test_sesion',
                'usuario',
                'Hola Bell',
                ['CONCEPTO_SALUDO']
            )
            
            # Cargar
            mensajes = persistencia.cargar_sesion('test_sesion')
            
            assert len(mensajes) == 1
            assert mensajes[0]['rol'] == 'usuario'
            assert mensajes[0]['contenido'] == 'Hola Bell'
            assert 'CONCEPTO_SALUDO' in mensajes[0]['conceptos']
        
        finally:
            os.remove(db_path)
    
    def test_listar_sesiones(self):
        """Test: Listar sesiones guardadas."""
        
        with tempfile.NamedTemporaryFile(delete=False) as f:
            db_path = f.name
        
        try:
            persistencia = PersistenciaMemoria(db_path)
            
            # Crear varias sesiones
            persistencia.guardar_mensaje('sesion1', 'usuario', 'Mensaje 1')
            persistencia.guardar_mensaje('sesion1', 'bell', 'Respuesta 1')
            persistencia.guardar_mensaje('sesion2', 'usuario', 'Mensaje 2')
            
            sesiones = persistencia.listar_sesiones()
            
            assert len(sesiones) == 2
            
            # Verificar que sesion1 tiene 2 mensajes
            sesion1 = next(s for s in sesiones if s['sesion_id'] == 'sesion1')
            assert sesion1['mensajes'] == 2
        
        finally:
            os.remove(db_path)