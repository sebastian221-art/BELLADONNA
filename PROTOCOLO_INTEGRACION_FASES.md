# 🔄 PROTOCOLO DE INTEGRACIÓN ENTRE FASES
**Belladonna v1.0**

## 📌 REGLA DE ORO

> **NUNCA avanzar a la siguiente fase sin integrar completamente la fase actual con todas las fases anteriores.**

---

## ✅ CHECKLIST AL COMPLETAR CADA FASE

### 1️⃣ ANTES de marcar fase como "completa"

#### A. Tests Automáticos
```bash
# Ejecutar TODOS los tests (no solo de la fase actual)
pytest tests/ -v --cov

# Debe mostrar:
# ✅ 100% tests pasando
# ✅ Cobertura > 90%
# ✅ 0 warnings críticos
```

#### B. Test de Integración Específico
```bash
# Test que verifica integración con fases previas
pytest tests/test_integracion_fase_X.py -v -s

# Debe verificar:
# ✅ Módulos de fases previas accesibles
# ✅ Datos compartidos correctamente
# ✅ No hay duplicación de funcionalidad
```

#### C. Test Manual Interactivo
```bash
python main.py

# Probar:
# ✅ Funcionalidades de TODAS las fases anteriores
# ✅ Nuevas funcionalidades de fase actual
# ✅ Integración entre funcionalidades
```

---

### 2️⃣ CHECKLIST DE INTEGRACIÓN POR FASE

## FASE 1 → FASE 2

### Archivos a ACTUALIZAR (no crear nuevos):

#### `main.py` (UNIFICAR, no duplicar)
```python
# ❌ MAL: Tener main_fase1.py y main_fase2.py
# ✅ BIEN: Un solo main.py que incluye TODO

class Bell:
    def __init__(self):
        # FASE 1: Fundamentos
        self.vocabulario = GestorVocabulario()
        self.vocabulario.cargar_conceptos(obtener_conceptos_core())  # 20 base
        
        # FASE 2: Expansión de vocabulario
        self.vocabulario.cargar_conceptos(obtener_conceptos_expandidos())  # +280
        
        # FASE 1: Vega
        self.vega = Vega()
        
        # FASE 2: Resto de consejeras
        self.consejo = Consejo()  # Incluye Vega + 6 más
```

#### `vocabulario/conceptos_core.py` (EXPANDIR)
```python
# FASE 1: 20 conceptos base
def obtener_conceptos_core():
    return [...]  # 20 conceptos

# FASE 2: +280 conceptos (AGREGAR, no reemplazar)
def obtener_conceptos_expandidos():
    """
    Conceptos adicionales de Fase 2.
    Se agregan a los conceptos core, no los reemplazan.
    """
    return [...]  # 280 conceptos más
```

#### `consejeras/consejo.py` (INCLUIR Vega)
```python
# ❌ MAL: Crear nuevas consejeras sin incluir Vega
# ✅ BIEN: Consejo incluye Vega de Fase 1

class Consejo:
    def __init__(self):
        self.consejeras = [
            Vega(),      # ← De Fase 1
            Nova(),      # Fase 2
            Echo(),      # Fase 2
            Lyra(),      # Fase 2
            Luna(),      # Fase 2
            Iris(),      # Fase 2
        ]
        self.sage = Sage()  # Fase 2
```

---

### Checklist Específico Fase 1 → 2:

- [ ] `main.py` unificado (no duplicado)
- [ ] Vocabulario tiene 300+ conceptos (20 base + 280 expandidos)
- [ ] Consejo incluye Vega de Fase 1
- [ ] Traductores usan vocabulario completo
- [ ] Motor de razonamiento accede a todas las consejeras
- [ ] Memoria persiste datos entre sesiones
- [ ] Tests de Fase 1 siguen pasando

---

## FASE 2 → FASE 3

### Archivos a ACTUALIZAR:

#### `vocabulario/gestor_vocabulario.py` (CONECTAR con Grafo)
```python
class GestorVocabulario:
    def __init__(self):
        self.conceptos = {}
        self.grafo = None  # ← AGREGAR en Fase 3
    
    def conectar_grafo(self, grafo):
        """FASE 3: Conecta vocabulario con grafo."""
        self.grafo = grafo
        
        # Migrar conceptos existentes al grafo
        for concepto in self.conceptos.values():
            self.grafo.agregar_concepto(concepto)
```

#### `aprendizaje/aprendizaje_conceptos.py` (USAR vocabulario existente)
```python
class AprendizajeConceptos:
    def __init__(self, vocabulario, investigador):
        # ✅ Usar vocabulario de Fases 1 y 2
        self.vocabulario = vocabulario  # Ya tiene 300+ conceptos
        self.investigador = investigador
```

### Checklist Específico Fase 2 → 3:

- [ ] Grafo inicializado con 300+ conceptos de Fase 2
- [ ] Aprendizaje usa vocabulario existente
- [ ] Consejeras acceden al grafo
- [ ] Memoria integrada con grafo
- [ ] Tests de Fases 1 y 2 siguen pasando

---

## FASE 3 → FASE 4

### Archivos a ACTUALIZAR:

#### `aprendizaje/meta_aprendizaje.py` (REGISTRAR desde Fase 3)
```python
class MetaAprendizaje:
    def __init__(self):
        # Cargar histórico de aprendizajes de Fase 3
        self.cargar()
```

#### `core/registro_emergente.py` (OBSERVAR desde inicio)
```python
class RegistroEmergente:
    def __init__(self):
        # Comenzar a registrar desde Fase 3
        self.cargar()
```

### Checklist Específico Fase 3 → 4:

- [ ] Meta-aprendizaje tiene datos de Fase 3
- [ ] Registro emergente observa desde Fase 3
- [ ] Creador de conceptos usa grafo de Fase 3
- [ ] Tests de Fases 1, 2 y 3 siguen pasando

---

## 🧪 TESTS MANUALES OBLIGATORIOS

### Al Completar Cada Fase:

#### Test 1: Funcionalidades Básicas
```bash
python main.py

# Probar:
Tú: ¿Puedes leer archivos?
Bell: [Debe responder con capacidades de Fase 1]

Tú: ¿Quiénes son tus consejeras?
Bell: [Debe listar las 7 de Fase 2]

Tú: ¿Cuántos conceptos conoces?
Bell: [Debe reportar 300+ en Fase 2, 800+ en Fase 3]
```

#### Test 2: Integración entre Fases
```bash
# Fase 2: Verificar que Fase 1 sigue funcionando
Tú: Modifica tus valores
Bell: [Vega debe vetar - Fase 1]

Tú: for i in range(len(lista)): pass
Bell: [Nova debe detectar - Fase 2]
```

#### Test 3: Nuevas Capacidades
```bash
# Fase 2:
Tú: ¿Qué conceptos no conoces?
Bell: [Lyra debe responder honestamente]

# Fase 3:
Tú: Investiga qué es Docker
Bell: [Debe investigar autónomamente]

# Fase 4:
Tú: ¿Cómo has mejorado tu aprendizaje?
Bell: [Meta-aprendizaje debe reportar]
```

---

## 📊 CHECKLIST DE VALIDACIÓN COMPLETA

### Antes de Marcar Fase como "100% Completa":

#### ✅ Tests Automáticos
- [ ] `pytest tests/ -v` → 100% pasando
- [ ] `pytest tests/test_integracion_fase_X.py -v -s` → Pasando
- [ ] Cobertura > 90%

#### ✅ Tests Manuales
- [ ] Todas las funcionalidades de fases previas funcionan
- [ ] Nuevas funcionalidades de fase actual funcionan
- [ ] Integración entre fases funciona

#### ✅ Documentación
- [ ] `docs/FASEX_COMPLETO.md` creado
- [ ] Estadísticas actualizadas
- [ ] Decisiones técnicas documentadas

#### ✅ Archivos Actualizados
- [ ] `main.py` incluye nueva fase
- [ ] Módulos de fases previas actualizados (no duplicados)
- [ ] Tests de integración creados

---

## 🚨 SEÑALES DE ALERTA (Fase NO lista)

### ❌ NO avanzar si:

1. **Tests fallan**
   ```bash
   pytest tests/
   # Si hay ALGÚN fallo → NO avanzar
   ```

2. **Funcionalidad de fase previa rota**
   ```python
   # Si algo que funcionaba en Fase 1 ya no funciona en Fase 2
   # → Hay regresión, arreglar antes de avanzar
   ```

3. **Duplicación de código**
   ```python
   # ❌ Si hay main_fase1.py Y main_fase2.py
   # ❌ Si hay consejo_fase1.py Y consejo_fase2.py
   # → Consolidar en archivos únicos
   ```

4. **Vocabulario no integrado**
   ```python
   # Si vocabulario de Fase 2 NO incluye conceptos de Fase 1
   # → Integrar vocabularios
   ```

5. **Test manual falla**
   ```bash
   python main.py
   Tú: [Pregunta de fase previa]
   Bell: [No funciona]
   # → Arreglar integración
   ```

---

## 📝 PLANTILLA DE REPORTE POST-FASE

```markdown
# ✅ FASE X COMPLETADA

## Fecha de Finalización: [Fecha]

### Tests Automáticos
- Total tests: X
- Tests pasando: 100%
- Cobertura: X%

### Tests Manuales
- [ ] Funcionalidades Fase 1: ✅
- [ ] Funcionalidades Fase 2: ✅
- [ ] ... (según fase actual)
- [ ] Integración: ✅

### Archivos Actualizados
- [ ] `main.py`
- [ ] `vocabulario/`
- [ ] `consejeras/`
- [ ] ... (según fase)

### Estadísticas Finales
- Vocabulario: X conceptos
- Consejeras: X
- Bucles: X
- etc.

### Problemas Encontrados y Resueltos
1. [Problema 1] → [Solución]
2. [Problema 2] → [Solución]

### Próximos Pasos
- Fase X+1: [Objetivo principal]
- Archivos a actualizar: [Lista]
```

---

## 🎯 RESUMEN EJECUTIVO

### Reglas Simples:

1. **Una sola fuente de verdad**
   - Un solo `main.py` (no main_fase1.py, main_fase2.py)
   - Un solo `GestorVocabulario` (acumula conceptos)
   - Un solo `Consejo` (incluye todas las consejeras)

2. **Siempre integrar, nunca reemplazar**
   - Fase 2 SUMA a Fase 1, no reemplaza
   - Fase 3 SUMA a Fases 1+2, no reemplaza

3. **Tests son obligatorios**
   - Automáticos: `pytest tests/`
   - Manuales: `python main.py` + interacción

4. **Documentar decisiones**
   - Por qué se hizo X
   - Qué se actualizó
   - Qué problemas hubo

---

## 🔧 HERRAMIENTAS DE VALIDACIÓN

### Script de Validación Rápida
```bash
# validar_fase.sh
#!/bin/bash

echo "🔍 Validando integración de fases..."

# 1. Tests automáticos
pytest tests/ -v --tb=short
if [ $? -ne 0 ]; then
    echo "❌ Tests fallan - NO avanzar"
    exit 1
fi

# 2. Verificar archivos únicos
if [ -f "main_fase1.py" ] || [ -f "main_fase2.py" ]; then
    echo "❌ Archivos duplicados detectados"
    exit 1
fi

# 3. Test de vocabulario
python -c "
from vocabulario.gestor_vocabulario import GestorVocabulario
g = GestorVocabulario()
# Cargar todos los conceptos
assert len(g.conceptos) >= 300, 'Vocabulario incompleto'
print(f'✅ Vocabulario: {len(g.conceptos)} conceptos')
"

echo "✅ Validación exitosa - Fase lista para marcar como completa"
```

---

**FIN DEL PROTOCOLO**

> Este documento debe consultarse SIEMPRE al completar cada fase.