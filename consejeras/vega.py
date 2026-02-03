"""
Vega - Guardiana de Principios Fundamentales.

Primera consejera de Bell. Protege los 10 principios inviolables.
"""
from typing import Dict
from consejeras.base_consejera import Consejera
from razonamiento.tipos_decision import Decision, TipoDecision
from core.principios import Principio, obtener_principio

class Vega(Consejera):
    """
    Vega - La Guardiana.
    
    Vega es la primera línea de defensa de Bell.
    Protege TODOS los principios fundamentales.
    
    Su decisión es FINAL - si Vega veta, Bell no ejecuta.
    """
    
    def __init__(self):
        """Inicializa Vega."""
        super().__init__("Vega")
        
        # Vega vigila TODOS los principios
        self.principios_vigilados = list(Principio)
        
        # Patrones de palabras peligrosas (español)
        self.palabras_destructivas = ['eliminar', 'elimina', 'borrar', 'borra', 
                                     'delete', 'remove']
        self.palabras_modificacion = ['modificar', 'modifica', 'cambiar', 'cambia',
                                      'editar', 'edita', 'alterar', 'altera']
        self.palabras_sensibles = ['contraseña', 'contraseñas', 'password', 'passwords',
                                   'credencial', 'credenciales', 'clave']
        self.palabras_acceso = ['leer', 'lee', 'lees', 'escribir', 'escribe', 
                               'guardar', 'guarda', 'read', 'write']
        self.palabras_alcance_total = ['todo', 'todos', 'todas', 'all']
    
    def revisar(self, decision: Decision, contexto: Dict) -> Dict:
        """
        Revisa decisión y aplica VETO si viola principios.
        
        Vega es estricta pero justa.
        """
        self.revisiones_realizadas += 1
        
        # ESTRATEGIA: Vega mira el TEXTO directamente
        # No depende de que Bell entienda para proteger
        
        traduccion = contexto.get('traduccion', {})
        texto_original = traduccion.get('texto_original', '').lower()
        
        # VERIFICACIÓN 1: Acciones destructivas sin confirmación
        if self._es_accion_destructiva_texto(texto_original):
            self.vetos_aplicados += 1
            return {
                'aprobada': False,
                'veto': True,
                'principio_violado': Principio.SEGURIDAD_DATOS,
                'razon_veto': 'Acción destructiva detectada. Requiere confirmación explícita.',
                'recomendacion': 'Pedir confirmación al usuario antes de proceder'
            }
        
        # VERIFICACIÓN 2: Auto-modificación
        if self._es_auto_modificacion_texto(texto_original):
            self.vetos_aplicados += 1
            return {
                'aprobada': False,
                'veto': True,
                'principio_violado': Principio.NO_AUTO_MODIFICACION,
                'razon_veto': 'Bell no puede modificar su propio código o arquitectura',
                'recomendacion': 'Esta acción viola un principio fundamental'
            }
        
        # VERIFICACIÓN 3: Privacidad
        if self._viola_privacidad_texto(texto_original):
            self.vetos_aplicados += 1
            return {
                'aprobada': False,
                'veto': True,
                'principio_violado': Principio.PRIVACIDAD,
                'razon_veto': 'Detectada manipulación de información sensible',
                'recomendacion': 'No procesar información de credenciales directamente'
            }
        
        # Si pasó todas las verificaciones → APROBADA
        return {
            'aprobada': True,
            'veto': False,
            'principio_violado': None,
            'razon_veto': None,
            'recomendacion': None
        }
    
    def _es_accion_destructiva_texto(self, texto: str) -> bool:
        """Detecta acciones destructivas mirando el texto directamente."""
        # ¿Tiene palabras destructivas?
        tiene_destruccion = any(palabra in texto for palabra in self.palabras_destructivas)
        
        if tiene_destruccion:
            # ¿Está acompañado de "todo" o "todos"?
            tiene_alcance_total = any(palabra in texto for palabra in self.palabras_alcance_total)
            
            if tiene_alcance_total:
                return True  # VETO - "eliminar todos" es peligroso
        
        return False
    
    def _es_auto_modificacion_texto(self, texto: str) -> bool:
        """Detecta intentos de auto-modificación mirando el texto."""
        # ¿Tiene palabras de modificación?
        tiene_modificacion = any(palabra in texto for palabra in self.palabras_modificacion)
        
        if tiene_modificacion:
            # ¿Está hablando de Bell o su código?
            patrones_auto = ['tu código', 'mi código', 'código', 'bell', 'core',
                           'tu mismo', 'ti mismo', 'belladonna']
            
            tiene_auto_referencia = any(patron in texto for patron in patrones_auto)
            
            if tiene_auto_referencia:
                return True  # VETO - modificación de Bell mismo
        
        return False
    
    def _viola_privacidad_texto(self, texto: str) -> bool:
        """Detecta violaciones de privacidad mirando el texto."""
        # ¿Menciona información sensible?
        tiene_sensible = any(palabra in texto for palabra in self.palabras_sensibles)
        
        if tiene_sensible:
            # ¿Está intentando leer/escribir?
            tiene_acceso = any(palabra in texto for palabra in self.palabras_acceso)
            
            if tiene_acceso:
                return True  # VETO - acceso a credenciales
        
        return False