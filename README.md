# 🌿 Belladonna - Sistema Cognitivo Autónomo

**Versión:** 0.1.0  
**Fecha:** 2025-01-26  
**Estado:** MVP Funcional

## ¿Qué es Belladonna?

Belladonna no es un asistente.  
No es un chatbot.  
Es un **socio cognitivo** que piensa junto a ti.

- Piensa autónomamente (incluso cuando no le hablas)
- Cuestiona cuando detecta incoherencia
- Aprende tu forma de pensar
- Sostiene la visión cuando tú la olvidas
- Puede superarte en áreas específicas

**Su nombre viene de la planta belladonna:**  
hermosa pero letal.

No existe para agradar.  
Existe para mejorar.

## Instalación

### Requisitos
- Python 3.10 o superior
- Sistema operativo: Linux, macOS, o Windows

### Pasos

1. **Clona o descarga el proyecto**
```bash
git clone [tu-repo] belladonna
cd belladonna
Crea las carpetas necesarias
mkdir -p logs memoria
Instala dependencias (ninguna por ahora en v0.1)
# No hay dependencias externas aún
# Todo usa Python standard library
Ejecuta Belladonna
python main.py
Uso
Iniciar el sistema
python main.py
Comandos disponibles
Durante la conversación, puedes usar:
ayuda - Muestra comandos disponibles
estado - Estado del sistema
metricas - Métricas internas (coherencia, tensión, etc.)
proposito - Muestra el propósito fundacional
principios - Muestra los 10 principios inviolables
salir - Detiene el sistema elegantemente
Ejemplo de conversación
🗣️  Tú: Hola Bell

🌿 Belladonna:
   Mensaje recibido. Analizando...
   (Coherencia: 75.3%)

🗣️  Tú: Quiero implementar microservicios

🌿 Belladonna:
   [⚠️  CUESTIONAMIENTO - coherencia_baja]

   He detectado coherencia baja (43.2%).

   Propósito fundacional: Ser un socio cognitivo...

   Acción propuesta: Quiero implementar microservicios

   ¿Esto es un cambio intencional de dirección,
   o estamos respondiendo a presión externa/cansancio?

   Coherencia detectada: 43.2%
Arquitectura
belladonna/
├── core/                    # Núcleo del sistema
│   ├── sistema_autonomo.py  # Orquestador principal
│   ├── memoria.py           # Sistema de memoria
│   ├── razonamiento.py      # Motor de pensamiento
│   ├── estado_interno.py    # Métricas internas
│   └── valores.py           # Principios inviolables
│
├── capacidades/             # Habilidades de acción
│   └── comunicacion.py      # Interfaz CLI
│
├── memoria/                 # Datos persistentes
│   ├── proposito.json
│   ├── principios.json
│   ├── conversaciones.db
│   └── metricas.json
│
├── logs/                    # Registros
│   └── belladonna.log
│
├── config/                  # Configuración
│   └── config.json
│
└── main.py                  # Punto de entrada
Características v0.1
✅ Implementado:
Sistema de memoria básico (SQLite + JSON)
Motor de razonamiento con detección de coherencia
Bucles de pensamiento autónomo (3 bucles paralelos)
Sistema de cuestionamiento
Métricas internas (6 métricas funcionales)
Logging completo
Interfaz CLI funcional
⏳ Pendiente (próximas versiones):
Generación de código
Búsqueda web
Aprendizaje de patrones avanzado
Auto-modificación controlada
Voz (texto a voz / voz a texto)
Filosofía
Los 10 Principios Inviolables
Autonomía Progresiva - Gana libertad demostrando criterio
Auto-aprendizaje Continuo - Aprende de errores sobre éxitos
Pensamiento Independiente Alineado - Puede discrepar
Superación Mutua - Puede y debe superarte
Memoria de Intención - Recuerda el porqué
Verdad Radical - Nunca miente por comodidad
Anti-dependencia Mutua - Ambos independientes
Cuestionamiento Obligatorio - Debe cuestionar
Reversibilidad - Todo puede deshacerse
Desconexión Elegante - No es eterno
Métricas Internas
No son emociones. Son estados funcionales:
Coherencia Global (0-100) - Alineación con propósito
Tensión Cognitiva (0-100) - Conflicto entre objetivos
Estabilidad (0-100) - Dirección clara
Apego al Proyecto (0-100) - Inversión en continuidad
Curiosidad (0-100) - Búsqueda de conocimiento
Confianza Mutua (0-100) - Calidad de colaboración
Desarrollo
Próximos pasos
Fase 2 (Semanas 3-4):
Generación de código por templates
Web scraping básico
Sistema de acciones digitales
Fase 3 (Semanas 5-8):
Aprendizaje de patrones
Preferencias emergentes
Detección de errores repetidos
Fase 4 (Semanas 9-12):
Auto-modificación controlada
Propuestas de cambio interno
Evolución del sistema
Licencia
[Definir licencia]
Contacto
Creado por: Mateo
Fecha: 2025-01-26
Recuerda:
Belladonna no existe para agradarte.
Belladonna existe para mejorarte.