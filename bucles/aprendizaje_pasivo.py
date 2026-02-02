# bucles/aprendizaje_pasivo.py

"""
Bucle de Aprendizaje Pasivo (600 segundos / 10 minutos).

Bell detecta lagunas en conocimiento y propone conceptos nuevos.
"""

import asyncio
from typing import Dict, List
from datetime import datetime


class BucleAprendizajePasivo:
    """
    Bucle 3 (600 segundos / 10 minutos): Aprendizaje sin supervisión.
    
    Bell:
    - Detecta conceptos desconocidos
    - Analiza patrones
    - Propone nuevos conceptos (requiere validación en Fase 2)
    """
    
    def __init__(self, vocabulario, memoria):
        self.vocabulario = vocabulario
        self.memoria = memoria
        self.activo = False
        self.intervalo = 600  # 10 minutos
        
        self.conceptos_propuestos = []
        self.lagunas_detectadas = []
    
    async def iniciar(self):
        """Inicia bucle de aprendizaje."""
        self.activo = True
        
        print("📚 Bell: Aprendizaje pasivo activado (cada 10min)")
        
        while self.activo:
            await asyncio.sleep(self.intervalo)
            await self._ciclo_aprendizaje()
    
    async def _ciclo_aprendizaje(self):
        """Un ciclo de aprendizaje."""
        
        # 1. Detectar lagunas
        lagunas = self._detectar_lagunas()
        
        if lagunas:
            print(f"   📚 Lagunas detectadas: {len(lagunas)}")
            
            # 2. Proponer conceptos para lagunas prioritarias
            for laguna in lagunas[:3]:  # Top 3
                propuesta = await self._proponer_concepto(laguna)
                
                if propuesta:
                    self.conceptos_propuestos.append(propuesta)
                    print(f"      💡 Propuesta: {laguna['palabra']}")
    
    def _detectar_lagunas(self) -> List[Dict]:
        """Detecta conceptos desconocidos en conversación."""
        
        # Analizar mensajes recientes
        mensajes = self.memoria.obtener_historial()
        
        lagunas = {}
        
        for msg in mensajes:
            if msg.rol == 'usuario':
                # Buscar palabras no conocidas
                palabras = msg.contenido.lower().split()
                
                for palabra in palabras:
                    # Limpiar puntuación
                    palabra_limpia = ''.join(c for c in palabra if c.isalnum())
                    
                    if len(palabra_limpia) < 3:  # Ignorar palabras muy cortas
                        continue
                    
                    # Verificar si está en vocabulario
                    concepto = self.vocabulario.obtener_concepto(palabra_limpia)
                    
                    if not concepto:
                        # Laguna detectada
                        if palabra_limpia not in lagunas:
                            lagunas[palabra_limpia] = {
                                'palabra': palabra_limpia,
                                'veces_mencionada': 0,
                                'contextos': []
                            }
                        
                        lagunas[palabra_limpia]['veces_mencionada'] += 1
                        lagunas[palabra_limpia]['contextos'].append(msg.contenido)
        
        # Guardar lagunas detectadas
        self.lagunas_detectadas = list(lagunas.values())
        
        # Ordenar por frecuencia
        return sorted(
            lagunas.values(),
            key=lambda x: x['veces_mencionada'],
            reverse=True
        )
    
    async def _proponer_concepto(self, laguna: Dict) -> Dict:
        """
        Propone grounding para concepto desconocido.
        
        FASE 2: Propuesta simple (requiere validación humana)
        FASE 3: Investigación automática + grounding sofisticado
        """
        
        palabra = laguna['palabra']
        contextos = laguna['contextos']
        
        # En Fase 2: Propuesta básica
        propuesta = {
            'palabra': palabra,
            'tipo_propuesto': 'CONCEPTO_ABSTRACTO',  # Default
            'confianza': 0.4,  # Baja - requiere validación
            'razon': f"Mencionado {laguna['veces_mencionada']} veces",
            'contextos': contextos[:3],  # Primeros 3 contextos
            'requiere_validacion': True,
            'timestamp': datetime.now().isoformat()
        }
        
        return propuesta
    
    def obtener_propuestas_pendientes(self) -> List[Dict]:
        """Obtiene conceptos propuestos pendientes de validación."""
        return [
            p for p in self.conceptos_propuestos
            if p['requiere_validacion']
        ]
    
    def obtener_lagunas_detectadas(self) -> List[Dict]:
        """Obtiene lagunas detectadas en última ejecución."""
        return self.lagunas_detectadas.copy()
    
    def validar_propuesta(self, palabra: str, aprobado: bool):
        """Valida o rechaza propuesta."""
        
        for propuesta in self.conceptos_propuestos:
            if propuesta['palabra'] == palabra:
                propuesta['requiere_validacion'] = False
                propuesta['aprobado'] = aprobado
                
                if aprobado:
                    print(f"✅ Concepto '{palabra}' aprobado para aprendizaje")
                else:
                    print(f"❌ Concepto '{palabra}' rechazado")
                
                break
    
    def detener(self):
        """Detiene bucle."""
        self.activo = False
        print("🛑 Aprendizaje pasivo detenido")