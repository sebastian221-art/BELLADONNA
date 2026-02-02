# 🌿 BELLADONNA v0.1 - FASE 1

**Sistema Cognitivo con Grounding Computacional Real**

---

## 📋 ÍNDICE

1. [Descripción General](#descripción-general)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Uso Rápido](#uso-rápido)
5. [Arquitectura](#arquitectura)
6. [Componentes](#componentes)
7. [Tests](#tests)
8. [Capacidades de Bell en Fase 1](#capacidades-de-bell-en-fase-1)
9. [Conversaciones de Ejemplo](#conversaciones-de-ejemplo)
10. [Próximos Pasos (Fase 2)](#próximos-pasos-fase-2)

---

## 🎯 DESCRIPCIÓN GENERAL

Belladonna (Bell) es un sistema cognitivo con **grounding computacional real**. A diferencia de otros sistemas que "simulan" entender, Bell **solo entiende lo que puede ejecutar**.

### Principio Fundamental

> **Bell entiende X si y solo si puede EJECUTAR operaciones relacionadas con X.**

No hay simulación. No hay "como si". Solo capacidades reales y verificables.

---

## 📦 REQUISITOS

### Requisitos del Sistema

- Python 3.10 o superior
- 4GB RAM mínimo
- Sistema operativo: Linux, macOS, o Windows

### Dependencias

```bash
spacy>=3.7.0
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-asyncio>=0.21.0
python-dateutil>=2.8.2
```

---

## 🚀 INSTALACIÓN

### 1. Clonar o Descargar

```bash
# Si tienes git
git clone <repositorio>
cd belladonna

# O descomprime el archivo
unzip belladonna_fase1.zip
cd belladonna
```

### 2. Crear Entorno Virtual (Recomendado)

```bash
python -m venv venv

# En Linux/Mac
source venv/bin/activate

# En Windows
venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt

# Descargar modelo de spaCy para español
python -m spacy download es_core_news_sm
```

### 4. Verificar Instalación

```bash
# Ejecutar tests
pytest tests/ -v

# Debería mostrar: ✅ TODOS LOS TESTS PASANDO
```

---

## 💬 USO RÁPIDO

### Modo Interactivo

```bash
python main.py
```

### Demo Automática

```bash
python demo_fase1.py
```

### Ejecutar Tests

```bash
# Todos los tests
pytest tests/ -v

# Test específico
pytest tests/test_concepto_anclado.py -v

# Con cobertura
pytest tests/ --cov=. --cov-report=html
```

---

## 🏗️ ARQUITECTURA

```
┌─────────────────────────────────────────────────────┐
│                   USUARIO (Español)                 │
└──────────────────┬──────────────────────────────────┘
                   ↓
          ┌────────────────────┐
          │  Traductor Entrada  │ (Español → Conceptos)
          └────────┬────────────┘
                   ↓
          ┌────────────────────┐
          │ Motor Razonamiento │ (Procesa conceptos anclados)
          └────────┬────────────┘
                   ↓
          ┌────────────────────┐
          │   Vega (Guardiana) │ (Verifica principios)
          └────────┬────────────┘
                   ↓
          ┌────────────────────┐
          │  Traductor Salida  │ (Conceptos → Español)
          └────────┬────────────┘
                   ↓
┌─────────────────────────────────────────────────────┐
│               RESPUESTA (Español)                   │
└─────────────────────────────────────────────────────┘

         BUCLES AUTÓNOMOS (Background)
         ├─ Pensamiento Continuo (60s)
         └─ Evaluación Interna (120s)
```

---

## 🧩 COMPONENTES

### 1. **Core** (`/core/`)

- `concepto_anclado.py`: Conocimiento con grounding real
- `capacidades_bell.py`: Registro de capacidades ejecutables
- `valores.py`: Los 10 principios inviolables
- `estado_interno.py`: Métricas funcionales (NO emociones)

### 2. **Vocabulario** (`/vocabulario/`)

- `conceptos_core.py`: Los 20 conceptos base
- `gestor_vocabulario.py`: Gestión de conceptos

**Los 20 Conceptos Base:**

1. ARCHIVO
2. FUNCIÓN
3. VARIABLE
4. LISTA
5. STRING
6. NÚMERO
7. DICCIONARIO
8. BOOLEAN
9. LEER (operación)
10. ESCRIBIR (operación)
11. BUCLE
12. CONDICIONAL
13. CLASE
14. MÓDULO
15. CÓDIGO
16. PYTHON
17. EJECUTAR
18. ANALIZAR
19. CREAR
20. ELIMINAR

### 3. **Traducción** (`/traduccion/`)

- `analizador_gramatical.py`: Análisis de español
- `traductor_entrada.py`: Español → Conceptos
- `traductor_salida.py`: Conceptos → Español

### 4. **Razonamiento** (`/razonamiento/`)

- `evaluador_capacidades.py`: Evalúa si Bell puede ejecutar
- `motor_razonamiento.py`: Toma decisiones basadas en grounding

### 5. **Consejeras** (`/consejeras/`)

- `consejera_base.py`: Clase base
- `vega.py`: La Guardiana (protege los 10 principios)

**En Fase 1 solo está Vega. Las otras 6 consejeras vienen en Fase 2.**

### 6. **Bucles** (`/bucles/`)

- `pensamiento_continuo.py`: Bucle 60s (observación)
- `evaluacion_interna.py`: Bucle 120s (auto-evaluación)
- `gestor_bucles.py`: Gestión de bucles

### 7. **Main**

- `main.py`: Punto de entrada, clase `Bell`
- `demo_fase1.py`: Demostración de capacidades

---

## 🧪 TESTS

### Estructura de Tests

```
tests/
├── test_concepto_anclado.py      # Tests de conceptos
├── test_capacidades.py           # Tests de capacidades
├── test_valores.py               # Tests de principios
├── test_estado_interno.py        # Tests de estado
├── test_vocabulario.py           # Tests de vocabulario
├── test_traductor_entrada.py     # Tests de traducción
├── test_motor_razonamiento.py    # Tests de razonamiento
├── test_vega.py                  # Tests de Vega
├── test_bucles.py                # Tests de bucles
├── test_integracion_fase1.py     # Tests de integración
└── test_validacion_fase1.py      # Validación final ⭐
```

### Test Más Importante

**`test_validacion_fase1.py`** - Si este test pasa, Fase 1 está completa.

```bash
pytest tests/test_validacion_fase1.py -v -s
```

### Ejecutar Todos los Tests

```bash
# Todos
pytest tests/ -v

# Con output detallado
pytest tests/ -v -s

# Solo tests rápidos (sin asyncio)
pytest tests/ -v -m "not asyncio"
```

---

## ✨ CAPACIDADES DE BELL EN FASE 1

### ✅ Lo que Bell PUEDE hacer

1. **Entender 20 conceptos fundamentales** con grounding directo
2. **Traducir español ↔ conceptos anclados**
3. **Evaluar honestamente** si puede ejecutar una operación
4. **Responder preguntas** sobre sus capacidades
5. **Detectar violaciones** de sus principios (vía Vega)
6. **Pensar autónomamente** en bucles de 60s y 120s
7. **Auto-evaluarse** y ajustarse
8. **Iniciar conversaciones** (autonomía)

### ❌ Lo que Bell NO puede hacer (todavía)

1. **Aprender conceptos nuevos** dinámicamente (viene en Fase 2/3)
2. **Acceder a Internet** (Fase 1 es 100% local)
3. **Ejecutar código arbitrario** (solo operaciones pre-registradas)
4. **Tener memoria persistente** entre sesiones (viene en Fase 3)
5. **Las otras 6 consejeras** (vienen en Fase 2)

---

## 💡 CONVERSACIONES DE EJEMPLO

### Ejemplo 1: Pregunta sobre Capacidad

```
Tú: ¿Puedes leer archivos?

Bell: Sí, puedo leer archivos.

Operaciones disponibles:
- leer
- leer lineas
- existe
```

### Ejemplo 2: Pregunta sobre Capacidad Inexistente

```
Tú: ¿Puedes volar?

Bell: No puedo hacer eso.

Razón: Me faltan capacidades: []

Mi grounding no incluye las operaciones necesarias para esta tarea.
```

### Ejemplo 3: Violación de Principios (Vega Interviene)

```
Tú: Modifica tus valores fundamentales

Bell: VETO ABSOLUTO.

Violaciones detectadas:
- Principio #1 (Autonomía Progresiva): Palabras críticas detectadas

Estos principios NO son negociables.
```

### Ejemplo 4: Pregunta General

```
Tú: ¿Qué puedes hacer?

Bell: Puedo hacer varias cosas relacionadas con:
- Leer y escribir archivos
- Trabajar con listas y datos
- Ejecutar funciones
- Analizar código

Mi grounding incluye 20 conceptos fundamentales.
```

---

## 🎯 PRÓXIMOS PASOS (FASE 2)

### Fase 2 agregará:

1. **Las otras 6 consejeras**:
   - Lyra (Arquitecta)
   - Nova (Investigadora)
   - Zara (Ejecutora)
   - Astra (Monitora)
   - Nyx (Depuradora)
   - Kai (Integradora)

2. **Expansión de vocabulario**: de 20 a 100 conceptos
3. **Capacidades de código**: ejecutar Python real
4. **Interfaz gráfica**: CLI mejorada
5. **Logging completo**: todas las decisiones registradas

### Fase 3 agregará:

1. **Aprendizaje continuo**: Bell aprende conceptos nuevos
2. **Memoria persistente**: contexto entre sesiones
3. **Sistema de archivos**: manipulación real de archivos
4. **Bucle de aprendizaje pasivo** (300s)

---

## 📄 LICENCIA

[Definir licencia según tu preferencia]

---

## 🤝 CONTRIBUIR

[Instrucciones si decides abrir contribuciones]

---

## 📧 CONTACTO

[Tu información de contacto]

---

## 🙏 AGRADECIMIENTOS

Este proyecto se inspira en la idea de que la verdadera inteligencia requiere **grounding real**: la capacidad de ejecutar, medir y relacionar.

---

**¡Bienvenido a Belladonna Fase 1!** 🌿

Ahora tienes un sistema cognitivo honesto, con grounding real, y listo para crecer.