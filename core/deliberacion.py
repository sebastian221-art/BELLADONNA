# core/deliberacion.py

"""
Sistema de Deliberación del Consejo de Consejeras.
Gestiona la toma de decisiones colaborativa.
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum

from consejeras.consejera_base import Opinion, TipoOpinion, NivelPrioridad
from consejeras.vega import Vega
from consejeras.nova import Nova
from consejeras.echo import Echo
from consejeras.lyra import Lyra
from consejeras.luna import Luna


class EstadoDeliberacion(Enum):
    """Estados posibles de una deliberación."""
    INICIADA = "iniciada"
    EN_CURSO = "en_curso"
    CONSENSO = "consenso"
    VETO = "veto"
    FINALIZADA = "finalizada"


@dataclass
class ResultadoDeliberacion:
    """Resultado de una deliberación del consejo."""
    decision_final: str
    estado: EstadoDeliberacion
    opiniones: List[Opinion]
    razon_principal: str
    metadata: Dict[str, Any]
    hubo_veto: bool = False
    consejera_veto: Optional[str] = None


class SistemaDeliberacion:
    """
    Gestiona el proceso de deliberación del consejo.
    
    Workflow:
    1. Se presenta una situación
    2. Cada consejera opina si debe intervenir
    3. Las que intervienen analizan
    4. Vega puede vetar
    5. Se alcanza consenso o decisión
    """
    
    def __init__(self):
        # Consejeras del consejo
        self.vega = Vega()
        self.nova = Nova()
        self.echo = Echo()
        self.lyra = Lyra()
        self.luna = Luna()
        
        # Orden de consulta (Vega siempre primero)
        self.consejeras = [
            self.vega,   # Ética primero - puede vetar
            self.echo,   # Coherencia - necesita ir temprano para detectar contradicciones
            self.lyra,   # Exactitud técnica
            self.nova,   # Optimización
            self.luna    # Tono y empatía
        ]
        
        self.historial_deliberaciones = []
    
    def deliberar(self, situacion: Dict[str, Any]) -> ResultadoDeliberacion:
        """
        Ejecuta proceso completo de deliberación.
        
        Args:
            situacion: Diccionario con contexto de la situación
            
        Returns:
            ResultadoDeliberacion con la decisión del consejo
        """
        
        opiniones = []
        
        # Fase 1: Consultar a cada consejera
        for consejera in self.consejeras:
            opinion = consejera.debe_intervenir(situacion)
            opiniones.append(opinion)
            
            # Vega puede vetar inmediatamente
            if consejera.nombre == "Vega" and opinion.tipo == TipoOpinion.VETO:
                resultado = ResultadoDeliberacion(
                    decision_final="VETADO",
                    estado=EstadoDeliberacion.VETO,
                    opiniones=opiniones,
                    razon_principal=opinion.razon,
                    metadata={'veto_de': 'Vega'},
                    hubo_veto=True,
                    consejera_veto="Vega"
                )
                self.historial_deliberaciones.append(resultado)
                return resultado
        
        # Fase 2: Analizar consenso
        resultado = self._alcanzar_consenso(opiniones, situacion)
        
        # Registrar en historial
        self.historial_deliberaciones.append(resultado)
        
        # Fase 3: Actualizar estado de consejeras (IMPORTANTE para Echo)
        self._actualizar_estado_consejeras(resultado, situacion)
        
        return resultado
    
    def _actualizar_estado_consejeras(
        self, 
        resultado: ResultadoDeliberacion,
        situacion: Dict[str, Any]
    ):
        """Actualiza estado interno de consejeras después de deliberación."""
        
        # Echo necesita registrar decisiones para detectar contradicciones
        if hasattr(self.echo, 'registrar_decision'):
            # CLAVE: Registrar la decisión PROPUESTA, no la final
            # Porque Echo necesita comparar propuestas futuras con esta
            decision_propuesta = situacion.get('decision_propuesta', {})
            
            if decision_propuesta:
                # Registrar la propuesta
                decision_para_registro = {
                    'decision': decision_propuesta.get('decision', ''),
                    'contexto': decision_propuesta.get('contexto', 'general')
                }
            else:
                # Si no hay propuesta, registrar resultado final
                decision_para_registro = {
                    'decision': resultado.decision_final,
                    'contexto': situacion.get('tipo', 'general')
                }
            
            self.echo.registrar_decision(decision_para_registro)
        
        # Otras consejeras pueden necesitar actualizaciones en el futuro
        # ...
    
    def _alcanzar_consenso(
        self, 
        opiniones: List[Opinion], 
        situacion: Dict[str, Any]
    ) -> ResultadoDeliberacion:
        """Determina decisión final basada en opiniones."""
        
        # Filtrar opiniones relevantes
        opiniones_activas = [
            op for op in opiniones 
            if op.tipo != TipoOpinion.NEUTRAL
        ]
        
        if not opiniones_activas:
            # Todas neutrales → aprobar
            return ResultadoDeliberacion(
                decision_final="APROBAR",
                estado=EstadoDeliberacion.CONSENSO,
                opiniones=opiniones,
                razon_principal="Ninguna consejera detectó problemas",
                metadata={'consenso': True}
            )
        
        # Verificar advertencias de alta prioridad
        advertencias_criticas = [
            op for op in opiniones_activas
            if op.tipo == TipoOpinion.ADVERTENCIA 
            and op.prioridad == NivelPrioridad.ALTA
        ]
        
        if advertencias_criticas:
            # Advertencia crítica → requiere atención
            adv = advertencias_criticas[0]
            return ResultadoDeliberacion(
                decision_final="REQUIERE_ATENCION",
                estado=EstadoDeliberacion.FINALIZADA,
                opiniones=opiniones,
                razon_principal=adv.razon,
                metadata={
                    'advertencias_criticas': len(advertencias_criticas),
                    'consejera_principal': adv.consejera
                }
            )
        
        # Contar tipos de opiniones
        aprobaciones = sum(1 for op in opiniones_activas if op.tipo == TipoOpinion.APROBACION)
        sugerencias = sum(1 for op in opiniones_activas if op.tipo == TipoOpinion.SUGERENCIA)
        advertencias = sum(1 for op in opiniones_activas if op.tipo == TipoOpinion.ADVERTENCIA)
        
        # Lógica de decisión
        if aprobaciones > sugerencias + advertencias:
            # Mayoría aprueba
            return ResultadoDeliberacion(
                decision_final="APROBAR",
                estado=EstadoDeliberacion.CONSENSO,
                opiniones=opiniones,
                razon_principal="Consenso del consejo: aprobar",
                metadata={'aprobaciones': aprobaciones}
            )
        
        elif sugerencias > 0 and advertencias == 0:
            # Solo sugerencias → aprobar con mejoras
            return ResultadoDeliberacion(
                decision_final="APROBAR_CON_MEJORAS",
                estado=EstadoDeliberacion.CONSENSO,
                opiniones=opiniones,
                razon_principal="Aprobado con sugerencias de mejora",
                metadata={'sugerencias': sugerencias}
            )
        
        else:
            # Advertencias presentes → revisar
            return ResultadoDeliberacion(
                decision_final="REVISAR",
                estado=EstadoDeliberacion.FINALIZADA,
                opiniones=opiniones,
                razon_principal="El consejo recomienda revisión",
                metadata={'advertencias': advertencias}
            )
    
    def obtener_resumen_opiniones(self, resultado: ResultadoDeliberacion) -> str:
        """Genera resumen legible de las opiniones."""
        
        resumen = f"📊 Decisión del Consejo: {resultado.decision_final}\n\n"
        
        if resultado.hubo_veto:
            resumen += f"🚫 VETO de {resultado.consejera_veto}\n"
            resumen += f"Razón: {resultado.razon_principal}\n"
            return resumen
        
        resumen += "Opiniones:\n"
        for op in resultado.opiniones:
            emoji = self._emoji_para_tipo(op.tipo)
            resumen += f"{emoji} {op.consejera}: {op.decision}\n"
            if op.tipo != TipoOpinion.NEUTRAL:
                # Limitar razón a 100 caracteres
                razon_corta = op.razon[:100] + "..." if len(op.razon) > 100 else op.razon
                resumen += f"   {razon_corta}\n"
        
        resumen += f"\n✅ Razón principal: {resultado.razon_principal}"
        
        return resumen
    
    def _emoji_para_tipo(self, tipo: TipoOpinion) -> str:
        """Retorna emoji apropiado para tipo de opinión."""
        return {
            TipoOpinion.APROBACION: "✅",
            TipoOpinion.SUGERENCIA: "💡",
            TipoOpinion.ADVERTENCIA: "⚠️",
            TipoOpinion.VETO: "🚫",
            TipoOpinion.NEUTRAL: "➖"
        }.get(tipo, "❓")