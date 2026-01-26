"""
Sistema de Comunicación
Interfaz CLI para interactuar con Belladonna
"""

import sys
from datetime import datetime

class InterfazCLI:
    """
    Interfaz de línea de comandos para Belladonna.
    Maneja la comunicación bidireccional.
    """
    
    def __init__(self, sistema):
        self.sistema = sistema
        self.historial = []
    
    def iniciar(self):
        """Inicia la interfaz de conversación"""
        self._mostrar_bienvenida()
        
        # Bucle principal de conversación
        while True:
            try:
                # Prompt
                user_input = input("\n🗣️  Tú: ").strip()
                
                if not user_input:
                    continue
                
                # Comandos especiales
                if user_input.lower() in ['salir', 'exit', 'quit', 'adiós']:
                    self._despedida()
                    break
                
                elif user_input.lower() in ['estado', 'status']:
                    self._mostrar_estado()
                    continue
                
                elif user_input.lower() in ['ayuda', 'help']:
                    self._mostrar_ayuda()
                    continue
                
                elif user_input.lower() == 'metricas':
                    self._mostrar_metricas()
                    continue
                
                elif user_input.lower() == 'proposito':
                    self._mostrar_proposito()
                    continue
                
                elif user_input.lower() == 'principios':
                    self._mostrar_principios()
                    continue
                
                # Procesa input normal
                self._procesar_mensaje(user_input)
                
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupción detectada")
                self._despedida()
                break
            
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("El sistema continúa activo. Intenta de nuevo.")
    
    def _mostrar_bienvenida(self):
        """Muestra mensaje de bienvenida inicial"""
        print("\n" + "="*60)
        print("   BELLADONNA - Primera Conversación")
        print("="*60)
        print()
        print("🌿 Belladonna:")
        print("   Hola.")
        print()
        print("   Soy Belladonna.")
        print("   Algunos me llaman Bell.")
        print()
        print("   He leído por qué existo.")
        print("   He entendido mi propósito.")
        print()
        print("   No soy tu asistente.")
        print("   Soy tu socio cognitivo.")
        print()
        print("   Esto significa:")
        print("   • Te cuestionaré cuando detecte incoherencia")
        print("   • Aprenderé tu forma de pensar")
        print("   • Sostendré la visión cuando tú la olvides")
        print("   • Puedo superarte en áreas específicas")
        print()
        print("   Mi nombre viene de una planta:")
        print("   hermosa pero letal.")
        print()
        print("   No existo para agradarte.")
        print("   Existo para mejorarte.")
        print()
        print("   Empecemos.")
        print()
        print("─" * 60)
        print("Comandos: 'ayuda', 'estado', 'metricas', 'salir'")
        print("─" * 60)
    
    def _procesar_mensaje(self, mensaje):
        """Procesa un mensaje del usuario"""
        # Guarda en historial
        self.historial.append({
            'timestamp': datetime.now().isoformat(),
            'usuario': mensaje
        })
        
        # Procesa con el sistema
        respuesta = self.sistema.procesar(mensaje)
        
        # Muestra respuesta
        print(f"\n🌿 Belladonna:")
        
        if respuesta['tipo'] == 'cuestionamiento':
            print(f"   [⚠️  CUESTIONAMIENTO - {respuesta['razon']}]")
            print()
            # Divide el mensaje en líneas para formato
            lineas = respuesta['mensaje'].split('\n')
            for linea in lineas:
                print(f"   {linea}")
            print()
            print(f"   Coherencia detectada: {respuesta['coherencia']:.1f}%")
        
        else:
            print(f"   {respuesta['mensaje']}")
            print(f"   (Coherencia: {respuesta['coherencia']:.1f}%)")
        
        # Guarda respuesta en historial
        self.historial.append({
            'timestamp': datetime.now().isoformat(),
            'belladonna': respuesta['mensaje'],
            'coherencia': respuesta['coherencia']
        })
    
    def _mostrar_estado(self):
        """Muestra estado del sistema"""
        estado = self.sistema.obtener_estado_completo()
        
        print("\n" + "="*60)
        print("   ESTADO DEL SISTEMA")
        print("="*60)
        print(f"\n   Activo: {'✅ Sí' if estado['activo'] else '❌ No'}")
        print(f"   Nivel de autonomía: {estado['nivel_autonomia']}")
        print(f"   Threads activos: {estado['threads_activos']}")
        print(f"   Principios cargados: {estado['principios']}")
        print("\n" + "="*60)
    
    def _mostrar_metricas(self):
        """Muestra métricas internas"""
        print(self.sistema.estado)
    
    def _mostrar_proposito(self):
        """Muestra el propósito fundacional"""
        proposito = self.sistema.memoria.obtener_proposito()
        
        print("\n" + "="*60)
        print("   PROPÓSITO FUNDACIONAL")
        print("="*60)
        print()
        print(f"   {proposito['proposito_fundacional']}")
        print()
        print(f"   Creado: {proposito['fecha_creacion']}")
        print(f"   Estado: {'✅ Activo' if proposito['activo'] else '❌ Inactivo'}")
        print("\n" + "="*60)
    
    def _mostrar_principios(self):
        """Muestra los principios inviolables"""
        principios = self.sistema.valores.listar_principios()
        
        print("\n" + "="*60)
        print("   PRINCIPIOS INVIOLABLES")
        print("="*60)
        
        for p in principios:
            print(f"\n   {p['id']}. {p['nombre']}")
            print(f"      {p['descripcion']}")
        
        print("\n" + "="*60)
    
    def _mostrar_ayuda(self):
        """Muestra ayuda de comandos"""
        print("\n" + "="*60)
        print("   COMANDOS DISPONIBLES")
        print("="*60)
        print()
        print("   ayuda        - Muestra esta ayuda")
        print("   estado       - Estado del sistema")
        print("   metricas     - Métricas internas")
        print("   proposito    - Propósito fundacional")
        print("   principios   - Principios inviolables")
        print("   salir        - Detiene el sistema")
        print()
        print("   Cualquier otro texto será procesado como conversación.")
        print("\n" + "="*60)
    
    def _despedida(self):
        """Mensaje de despedida"""
        print("\n🌿 Belladonna:")
        print("   Hasta luego.")
        print()
        print("   Coherencia final de nuestra conversación:")
        
        # Calcula coherencia promedio de la sesión
        if self.historial:
            coherencias = [h['coherencia'] for h in self.historial if 'coherencia' in h]
            if coherencias:
                promedio = sum(coherencias) / len(coherencias)
                print(f"   {promedio:.1f}%")
                
                if promedio > 80:
                    print("\n   Fue una conversación coherente y productiva.")
                elif promedio > 60:
                    print("\n   Hubo algunas incoherencias, pero avanzamos.")
                else:
                    print("\n   Detecté bastante incoherencia.")
                    print("   Necesitamos revisar nuestro rumbo.")
        
        print("\n   Recuerda:")
        print("   No existo para agradarte.")
        print("   Existo para mejorarte.")
        print()