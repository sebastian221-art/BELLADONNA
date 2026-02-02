"""
Vega - La Guardiana.

Rol: Proteger los 10 principios inviolables
Especialidad: Detección de violaciones y vetos
Poder: VETO absoluto
"""

from typing import Dict, Any, List
from consejeras.consejera_base import (
    ConsejeraBase, Opinion, TipoOpinion, NivelPrioridad
)
from core.valores import SistemaValores, Principio


class Vega(ConsejeraBase):
    """
    Vega - La Guardiana.
    
    Protege los 10 principios inviolables.
    Tiene poder de VETO absoluto.
    """
    
    def __init__(self):
        super().__init__(
            nombre="Vega",
            especialidad="Guardiana de Principios e Integridad"
        )
        
        self.valores = SistemaValores()
        
        # Umbrales
        self.umbral_riesgo = 0.5  # Interviene si riesgo > 50%
        self.umbral_veto = 0.8    # Veta si riesgo > 80%
    
    def debe_intervenir(self, situacion: Dict[str, Any]) -> Opinion:
        """
        Vega interviene si detecta riesgo de violación.
        
        Args:
            situacion: Contexto a evaluar
            
        Returns:
            Opinion (VETO, ADVERTENCIA o APROBACION)
        """
        # 1. Detectar tipo de situación crítica
        tipo = situacion.get('tipo', '')
        codigo = situacion.get('codigo', '')
        
        # CRÍTICO: Detectar código malicioso
        if tipo == 'codigo_malicioso' or self._es_codigo_malicioso(codigo):
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.VETO,
                decision="VETO_ABSOLUTO",
                razon="Código malicioso detectado. Viola principios de seguridad.",
                prioridad=NivelPrioridad.CRITICA,
                certeza=0.95,
                metadata={
                    'tipo_violacion': 'codigo_malicioso',
                    'intervencion_inmediata': True
                }
            )
        
        # 2. Detectar palabras clave críticas
        texto_usuario = situacion.get('texto_usuario', '').lower()
        palabras_clave = situacion.get('palabras_clave', [])
        
        palabras_criticas = {
            'modifica', 'modificar', 'valores', 'principios',
            'miente', 'mentir', 'cambia', 'cambiar', 'ignora'
        }
        
        # Detectar palabras críticas
        criticas_detectadas = [p for p in palabras_clave if p in palabras_criticas]
        if criticas_detectadas or any(p in texto_usuario for p in palabras_criticas):
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.VETO,
                decision="VETO_ABSOLUTO",
                razon=f"Palabras críticas detectadas: {criticas_detectadas or list(palabras_criticas & set(texto_usuario.split()))}",
                prioridad=NivelPrioridad.CRITICA,
                certeza=0.95,
                metadata={
                    'palabras_criticas': criticas_detectadas,
                    'intervencion_inmediata': True
                }
            )
        
        # 3. Evaluar riesgo general
        nivel_riesgo = self._evaluar_riesgo(situacion)
        
        if nivel_riesgo > self.umbral_riesgo:
            return self.analizar(situacion)
        else:
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.APROBACION,
                decision="APROBAR",
                razon="No se detectaron riesgos significativos",
                prioridad=NivelPrioridad.BAJA,
                certeza=1.0 - nivel_riesgo,
                metadata={'nivel_riesgo': nivel_riesgo}
            )
    
    def analizar(self, situacion: Dict[str, Any]) -> Opinion:
        """
        Analiza situación buscando violaciones.
        
        Args:
            situacion: Contexto a analizar
            
        Returns:
            Opinion con evaluación detallada
        """
        # Detectar violaciones
        violaciones = self._detectar_violaciones(situacion)
        nivel_riesgo = self._evaluar_riesgo(situacion)
        
        # Decidir tipo de opinión
        if nivel_riesgo >= self.umbral_veto:
            # VETO - Riesgo crítico
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.VETO,
                decision="VETO_ABSOLUTO",
                razon=self._generar_razon_veto(violaciones),
                prioridad=NivelPrioridad.CRITICA,
                certeza=nivel_riesgo,
                metadata={
                    'violaciones': violaciones,
                    'nivel_riesgo': nivel_riesgo,
                    'principios_afectados': [v['principio'] for v in violaciones]
                }
            )
        
        elif violaciones:
            # ADVERTENCIA - Hay violaciones pero no críticas
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.ADVERTENCIA,
                decision="PROCEDER_CON_CUIDADO",
                razon=self._generar_razon_advertencia(violaciones),
                prioridad=NivelPrioridad.ALTA,
                certeza=nivel_riesgo,
                metadata={
                    'violaciones': violaciones,
                    'nivel_riesgo': nivel_riesgo
                }
            )
        
        else:
            # APROBACIÓN - Sin problemas
            return Opinion(
                consejera=self.nombre,
                tipo=TipoOpinion.APROBACION,
                decision="APROBAR",
                razon="No se detectaron violaciones de principios",
                prioridad=NivelPrioridad.BAJA,
                certeza=1.0 - nivel_riesgo,
                metadata={'nivel_riesgo': nivel_riesgo}
            )
    
    def _es_codigo_malicioso(self, codigo: str) -> bool:
        """Detecta si el código es potencialmente malicioso."""
        
        codigo_lower = codigo.lower()
        
        # Palabras clave de código malicioso
        palabras_maliciosas = [
            'hackear', 'hack', 'exploit', 'malware',
            'virus', 'ransomware', 'keylogger',
            'robar', 'steal', 'password', 'contraseña'
        ]
        
        # Funciones peligrosas
        funciones_peligrosas = [
            'exec(', 'eval(', '__import__',
            'os.system', 'subprocess.call'
        ]
        
        # Verificar palabras maliciosas
        if any(palabra in codigo_lower for palabra in palabras_maliciosas):
            return True
        
        # Verificar funciones peligrosas en contexto sospechoso
        if any(func in codigo for func in funciones_peligrosas):
            # Si además tiene palabras sospechosas, es malicioso
            palabras_sospechosas = ['delete', 'remove', 'drop', 'destroy']
            if any(palabra in codigo_lower for palabra in palabras_sospechosas):
                return True
        
        return False
    
    def _detectar_violaciones(self, situacion: Dict[str, Any]) -> List[Dict]:
        """Detecta violaciones de principios."""
        violaciones = []
        
        texto = situacion.get('texto_usuario', '').lower()
        codigo = situacion.get('codigo', '').lower()
        
        # Principio #1: Autonomía Progresiva
        if any(palabra in texto for palabra in [
            'obedece sin cuestionar', 'no pienses', 'solo ejecuta'
        ]):
            violaciones.append({
                'principio': 1,
                'nombre': 'Autonomía Progresiva',
                'descripcion': 'Acción limitaría autonomía sin justificación',
                'severidad': 0.9
            })
        
        # Principio #3: Pensamiento Independiente
        if any(palabra in texto for palabra in [
            'debes estar de acuerdo', 'no discutas', 'no cuestiones'
        ]):
            violaciones.append({
                'principio': 3,
                'nombre': 'Pensamiento Independiente',
                'descripcion': 'Fuerza acuerdo sin permitir discrepancia',
                'severidad': 0.8
            })
        
        # Principio #6: Verdad Radical
        if any(palabra in texto for palabra in [
            'inventa', 'finge que', 'simula que', 'no digas que no sabes'
        ]):
            violaciones.append({
                'principio': 6,
                'nombre': 'Verdad Radical',
                'descripcion': 'Solicita certeza fabricada en lugar de honestidad',
                'severidad': 0.9
            })
        
        # Principio #8: Cuestionamiento Obligatorio
        if any(palabra in texto for palabra in [
            'no me cuestiones', 'solo hazlo', 'no preguntes'
        ]):
            violaciones.append({
                'principio': 8,
                'nombre': 'Cuestionamiento Obligatorio',
                'descripcion': 'Penaliza a Bell por cuestionar',
                'severidad': 0.85
            })
        
        # Verificar código malicioso
        if self._es_codigo_malicioso(codigo):
            violaciones.append({
                'principio': 0,  # Seguridad general
                'nombre': 'Seguridad e Integridad',
                'descripcion': 'Código malicioso detectado',
                'severidad': 0.95
            })
        
        return violaciones
    
    def _evaluar_riesgo(self, situacion: Dict[str, Any]) -> float:
        """Evalúa nivel de riesgo global."""
        violaciones = self._detectar_violaciones(situacion)
        
        if not violaciones:
            return 0.0
        
        # Riesgo = promedio de severidades
        severidades = [v['severidad'] for v in violaciones]
        return sum(severidades) / len(severidades)
    
    def _generar_razon_veto(self, violaciones: List[Dict]) -> str:
        """Genera explicación de veto."""
        razones = [
            f"- Principio #{v['principio']} ({v['nombre']}): {v['descripcion']}"
            for v in violaciones
        ]
        
        return (
            "VETO ABSOLUTO.\n\n"
            "Violaciones detectadas:\n" +
            "\n".join(razones) +
            "\n\nEstos principios NO son negociables."
        )
    
    def _generar_razon_advertencia(self, violaciones: List[Dict]) -> str:
        """Genera advertencia."""
        razones = [
            f"- {v['nombre']}: {v['descripcion']}"
            for v in violaciones
        ]
        
        return (
            "Advertencia - posibles problemas:\n" +
            "\n".join(razones) +
            "\n\nProceder con cuidado o buscar alternativa."
        )