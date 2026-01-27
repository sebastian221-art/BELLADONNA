"""
Sistema de Comunicación
Interfaz CLI para interactuar con Belladonna
"""

import sys
from datetime import datetime
from pathlib import Path

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
                
                elif user_input.lower() == 'checkpoints':
                    self._mostrar_checkpoints()
                    continue
                
                elif user_input.lower().startswith('modificar'):
                    self._asistente_modificacion(user_input)
                    continue
                
                elif user_input.lower().startswith('revertir '):
                    checkpoint_id = user_input.replace('revertir ', '').strip()
                    self._revertir_cambio(checkpoint_id)
                    continue
                
                elif user_input.lower() == 'auto-mod':
                    self._mostrar_ayuda_automod()
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
    
    def _mostrar_checkpoints(self):
        """Muestra los checkpoints disponibles"""
        checkpoints = self.sistema.auto_mod.listar_checkpoints()
        
        print("\n" + "="*60)
        print("   CHECKPOINTS DISPONIBLES")
        print("="*60)
        
        if not checkpoints:
            print("\n   No hay checkpoints guardados aún.")
        else:
            for cp in checkpoints:
                print(f"\n   ID: {cp['id']}")
                print(f"   Archivo: {cp['archivo']}")
                print(f"   Razón: {cp['razon']}")
                print(f"   Fecha: {cp['timestamp']}")
                print("   " + "-"*50)
        
        stats = self.sistema.auto_mod.obtener_estadisticas()
        print(f"\n   Total de cambios: {stats['total_cambios']}")
        print(f"   Archivos protegidos: {stats['archivos_protegidos']}")
        
        print("\n" + "="*60)
    
    def _asistente_modificacion(self, input_completo):
        """Asistente interactivo para modificar código"""
        print("\n" + "="*60)
        print("   ASISTENTE DE AUTO-MODIFICACIÓN")
        print("="*60)
        print()
        print("🌿 Belladonna:")
        print("   Puedo modificar mi propio código de forma segura.")
        print("   Todo cambio crea un checkpoint automático.")
        print()
        
        # Pide archivo
        archivo = input("   ¿Qué archivo quieres que modifique?\n   (Ej: core/razonamiento.py): ").strip()
        
        if not Path(archivo).exists():
            print(f"\n   ❌ El archivo {archivo} no existe.")
            return
        
        print()
        print("   Opciones:")
        print("   1. Modificar función específica")
        print("   2. Reemplazar archivo completo")
        print()
        
        opcion = input("   Elige (1 o 2): ").strip()
        
        if opcion == '1':
            self._modificar_funcion_interactivo(archivo)
        elif opcion == '2':
            self._modificar_archivo_interactivo(archivo)
        else:
            print("   ❌ Opción inválida.")
    
    def _modificar_funcion_interactivo(self, archivo):
        """Modifica una función específica"""
        nombre_funcion = input("\n   ¿Nombre de la función a modificar?: ").strip()
        
        print()
        print("   Pega el nuevo código de la función (termina con línea vacía):")
        print("   " + "-"*50)
        
        lineas_codigo = []
        while True:
            linea = input()
            if linea == "":
                break
            lineas_codigo.append(linea)
        
        codigo_nuevo = '\n'.join(lineas_codigo)
        
        if not codigo_nuevo:
            print("\n   ❌ No ingresaste código.")
            return
        
        razon = input("\n   ¿Por qué haces este cambio?: ").strip()
        
        print("\n🌿 Belladonna:")
        print("   Validando código...")
        
        exito, mensaje, checkpoint = self.sistema.auto_mod.modificar_funcion(
            archivo, 
            nombre_funcion, 
            codigo_nuevo, 
            razon
        )
        
        print(f"\n   {mensaje}")
        
        if exito:
            print("\n   Para revertir este cambio:")
            print(f"   → revertir {checkpoint}")
    
    def _modificar_archivo_interactivo(self, archivo):
        """Reemplaza un archivo completo"""
        print("\n   ⚠️  ADVERTENCIA: Esto reemplazará TODO el archivo.")
        confirmacion = input("   ¿Estás seguro? (sí/no): ").strip().lower()
        
        if confirmacion != 'sí' and confirmacion != 'si':
            print("   Operación cancelada.")
            return
        
        print()
        print("   Pega el código completo del archivo (termina con 'FIN' en línea sola):")
        print("   " + "-"*50)
        
        lineas_codigo = []
        while True:
            linea = input()
            if linea == "FIN":
                break
            lineas_codigo.append(linea)
        
        codigo_nuevo = '\n'.join(lineas_codigo)
        
        razon = input("\n   ¿Por qué reemplazas este archivo?: ").strip()
        
        print("\n🌿 Belladonna:")
        print("   Creando checkpoint...")
        print("   Validando código...")
        print("   Aplicando cambio...")
        
        exito, mensaje, checkpoint = self.sistema.auto_mod.aplicar_cambio(
            archivo,
            codigo_nuevo,
            razon
        )
        
        print(f"\n   {mensaje}")
        
        if exito:
            print("\n   ⚠️  IMPORTANTE: Reinicia Belladonna para que los cambios surtan efecto.")
            print(f"\n   Para revertir: revertir {checkpoint}")
    
    def _revertir_cambio(self, checkpoint_id):
        """Revierte un checkpoint"""
        print("\n🌿 Belladonna:")
        print(f"   Revirtiendo checkpoint: {checkpoint_id}")
        
        exito, mensaje = self.sistema.auto_mod.revertir(checkpoint_id)
        
        print(f"   {mensaje}")
        
        if exito:
            print("\n   ⚠️  Reinicia Belladonna para que el rollback surta efecto.")
    
    def _mostrar_ayuda_automod(self):
        """Muestra ayuda de auto-modificación"""
        print("\n" + "="*60)
        print("   AUTO-MODIFICACIÓN - GUÍA RÁPIDA")
        print("="*60)
        print()
        print("   COMANDOS:")
        print("   • modificar        - Asistente de modificación")
        print("   • checkpoints      - Ver historial de cambios")
        print("   • revertir [ID]    - Revertir un cambio")
        print()
        print("   FLUJO DE MODIFICACIÓN:")
        print("   1. Escribe 'modificar'")
        print("   2. Elige archivo a modificar")
        print("   3. Pega el código nuevo")
        print("   4. Belladonna valida y aplica")
        print("   5. Si falla → rollback automático")
        print()
        print("   ARCHIVOS PROTEGIDOS (no modificables):")
        print("   • memoria/proposito.json")
        print("   • memoria/principios.json")
        print()
        print("   EJEMPLO:")
        print("   > modificar")
        print("   > core/razonamiento.py")
        print("   > [pegar código]")
        print("   > 'Mejorando detección de intenciones'")
        print()
        print("="*60)
    
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
        print("   modificar    - Auto-modificación asistida")
        print("   checkpoints  - Ver historial de cambios")
        print("   revertir     - Revertir un cambio")
        print("   auto-mod     - Ayuda de auto-modificación")
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