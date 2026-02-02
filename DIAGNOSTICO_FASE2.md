# 🔍 DIAGNÓSTICO: Problemas con Fase 2

## 📊 ESTADO ACTUAL

### ❌ Problemas Identificados:

#### 1. **VOCABULARIO INCOMPLETO** (CRÍTICO)
```
Estado actual: 25 conceptos
Estado esperado: 300+ conceptos

Problema: Solo cargando conceptos_core.py (20 conceptos de Fase 1)
Falta: Conceptos expandidos de Fase 2 (280 conceptos)
```

#### 2. **LYRA DETECTA PALABRAS BÁSICAS COMO DESCONOCIDAS**
```
Ejemplos del log:
- "¿", "ser", "tu", "consejera" → Detectados como desconocidos
- "poder", "hacer" → Detectados como desconocidos

Causa: Vocabulario insuficiente + Traductor no procesa bien español básico
```

#### 3. **NOVA NO ANALIZA CÓDIGO CORRECTAMENTE**
```python
Tú: for i in range(len(lista)): print(lista[i])
Bell: No entendí tu consulta

Esperado: Nova debería detectar patrón RANGE_LEN y sugerir enumerate()
```

#### 4. **RESPUESTAS GENÉRICAS**
```
Bell: "No entendí tu consulta. ¿Podrías reformularla?"
Bell: "Solicitud de información. Nivel de comprensión: 90%"

Problema: Traductor falla → Motor no puede razonar correctamente
```

---

## 🛠️ PLAN DE CORRECCIÓN

### PASO 1: Expandir Vocabulario a 300+ Conceptos

#### A. Crear `conceptos_expandidos.py`
```python
# vocabulario/conceptos_expandidos.py

def obtener_conceptos_expandidos():
    """
    280 conceptos adicionales de Fase 2.
    
    Categorías:
    - Conceptos de Python avanzados (50)
    - Conceptos de programación general (50)
    - Conceptos de sistemas (30)
    - Verbos de acción (40)
    - Palabras interrogativas y conectores (30)
    - Conceptos de datos (40)
    - Conceptos de optimización (40)
    """
    
    conceptos = []
    
    # ========== PALABRAS BÁSICAS ESPAÑOL ==========
    # Para que Lyra no las detecte como desconocidas
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_QUE",
        tipo=TipoConcepto.PALABRA_INTERROGATIVA,
        palabras_español=["que", "qué", "que?", "qué?"],
        operaciones={},
        relaciones={'es_un': {'PREGUNTA'}},
        propiedades={'tipo': 'interrogativa'},
        datos={'definicion': 'Palabra interrogativa'},
        accesible_directamente=False,
        confianza_grounding=0.9
    ))
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_QUIEN",
        tipo=TipoConcepto.PALABRA_INTERROGATIVA,
        palabras_español=["quien", "quién", "quienes", "quiénes"],
        operaciones={},
        relaciones={'es_un': {'PREGUNTA'}},
        propiedades={'tipo': 'interrogativa'},
        datos={'definicion': 'Palabra interrogativa sobre persona'},
        accesible_directamente=False,
        confianza_grounding=0.9
    ))
    
    # Agregar más palabras básicas: cómo, cuándo, dónde, por qué, etc.
    # ...
    
    # ========== CONCEPTOS DE PYTHON AVANZADOS ==========
    
    conceptos.append(ConceptoAnclado(
        id="CONCEPTO_ENUMERATE",
        tipo=TipoConcepto.FUNCION_PYTHON,
        palabras_español=["enumerate", "enumerar"],
        operaciones={
            'usar': lambda lista: list(enumerate(lista))
        },
        relaciones={
            'es_un': {'FUNCION_BUILTIN'},
            'alternativa_de': {'RANGE_LEN'}
        },
        propiedades={
            'mejor_que_range_len': True,
            'retorna': 'tuplas (indice, elemento)'
        },
        datos={
            'definicion': 'Función que retorna índice y elemento',
            'ejemplo': 'for i, item in enumerate(lista):'
        },
        accesible_directamente=True,
        confianza_grounding=1.0
    ))
    
    # Agregar más: list comprehension, generators, decorators, etc.
    # ...
    
    return conceptos
```

#### B. Actualizar `main.py` para cargar conceptos expandidos
```python
class Bell:
    def __init__(self):
        # ...
        
        # Vocabulario: FASE 1 + FASE 2
        self.vocabulario = GestorVocabulario()
        
        # Cargar conceptos core (Fase 1)
        conceptos_core = obtener_conceptos_core()
        for concepto in conceptos_core.values():
            self.vocabulario.agregar_concepto(concepto)
        
        # Cargar conceptos expandidos (Fase 2)
        conceptos_expandidos = obtener_conceptos_expandidos()
        for concepto in conceptos_expandidos:
            self.vocabulario.agregar_concepto(concepto)
        
        print(f"   ✅ Vocabulario: {len(self.vocabulario.conceptos)} conceptos")
        # Debe mostrar: "Vocabulario: 300 conceptos" (20 + 280)
```

---

### PASO 2: Mejorar Traductor de Entrada

#### A. Problema actual:
```python
# traductor_entrada.py actual
def traducir(self, texto: str) -> Dict:
    # Solo usa lemas de spaCy
    # No reconoce estructuras complejas
```

#### B. Solución:
```python
# traduccion/traductor_entrada.py

class TraductorEntrada:
    def traducir(self, texto: str) -> Dict:
        # 1. Detectar tipo de entrada
        tipo_entrada = self._detectar_tipo_entrada(texto)
        
        if tipo_entrada == 'CODIGO':
            # Es código Python → Manejar diferente
            return self._traducir_codigo(texto)
        
        elif tipo_entrada == 'PREGUNTA':
            # Es pregunta → Extraer intención
            return self._traducir_pregunta(texto)
        
        else:
            # Texto normal
            return self._traducir_normal(texto)
    
    def _detectar_tipo_entrada(self, texto: str) -> str:
        """Detecta si es código, pregunta o texto normal."""
        
        # ¿Es código Python?
        if any(keyword in texto for keyword in ['for ', 'def ', 'class ', 'import ']):
            return 'CODIGO'
        
        # ¿Es pregunta?
        if '?' in texto or any(palabra in texto.lower() for palabra in ['qué', 'quién', 'cómo', 'puedes']):
            return 'PREGUNTA'
        
        return 'NORMAL'
    
    def _traducir_codigo(self, codigo: str) -> Dict:
        """Traduce código Python."""
        
        return {
            'estructura': 'codigo',
            'codigo_raw': codigo,
            'conceptos': [
                {
                    'palabra': 'codigo_python',
                    'concepto': self.vocabulario.obtener_concepto('codigo'),
                    'grounding': 1.0,
                    'operaciones': ['analizar', 'ejecutar']
                }
            ],
            'palabras_desconocidas': [],
            'confianza_traduccion': 1.0,
            'metadata': {
                'es_codigo': True,
                'lenguaje': 'python'
            }
        }
    
    def _traducir_pregunta(self, texto: str) -> Dict:
        """Traduce pregunta extrayendo intención."""
        
        # Extraer verbo principal
        doc = self.analizador.analizar(texto)
        
        # Buscar verbo de acción
        verbo = None
        for token in doc['tokens']:
            if token.lower() in ['puedes', 'puede', 'sabes', 'conoces']:
                verbo = token.lower()
                break
        
        # Generar conceptos
        conceptos = []
        for lema in doc['lemas']:
            concepto = self.vocabulario.obtener_concepto(lema)
            if concepto:
                conceptos.append({
                    'palabra': lema,
                    'concepto': concepto,
                    'grounding': concepto.confianza_grounding,
                    'operaciones': list(concepto.operaciones.keys())
                })
        
        return {
            'estructura': 'pregunta',
            'conceptos': conceptos,
            'palabras_desconocidas': [l for l in doc['lemas'] if not self.vocabulario.obtener_concepto(l)],
            'confianza_traduccion': len(conceptos) / max(len(doc['lemas']), 1),
            'metadata': {
                'verbo_principal': verbo,
                'es_pregunta_capacidad': verbo in ['puedes', 'puede']
            }
        }
```

---

### PASO 3: Conectar Nova con Código

#### A. Actualizar `main.py`:
```python
class Bell:
    def procesar(self, entrada: str) -> str:
        # 1. Traducir entrada
        traduccion = self.traductor_in.traducir(entrada)
        
        # 2. Si es código, pasar a Nova directamente
        if traduccion.get('metadata', {}).get('es_codigo'):
            # Nova analiza
            situacion_nova = {
                'codigo': traduccion['codigo_raw'],
                'complejidad': 0.7,
                'importancia': 0.8
            }
            
            decision_nova = self.consejo.deliberar(situacion_nova)
            
            # Si Nova tiene sugerencias, mostrarlas
            nova_opinion = next((op for op in decision_nova['opiniones'] if op.consejera == 'Nova'), None)
            
            if nova_opinion and nova_opinion.tipo == TipoOpinion.SUGERENCIA:
                return nova_opinion.razon
            else:
                return "Código analizado - no detecté optimizaciones necesarias."
        
        # 3. Proceso normal (no es código)
        # ...
```

---

### PASO 4: Mejorar Respuestas

#### A. Traductor de Salida más inteligente:
```python
class TraductorSalida:
    def generar(self, decision: Dict) -> str:
        tipo = decision['tipo_respuesta']
        
        # Si hay metadata de pregunta
        if decision.get('metadata', {}).get('es_pregunta_capacidad'):
            # Responder específicamente sobre capacidad
            if decision['puede_ejecutar']:
                return self._generar_afirmativa_capacidad(decision)
            else:
                return self._generar_negativa_capacidad(decision)
        
        # Proceso normal
        # ...
    
    def _generar_afirmativa_capacidad(self, decision: Dict) -> str:
        """Responde afirmativamente sobre capacidad."""
        
        ops = decision['operaciones']
        
        respuesta = "Sí, puedo hacer eso.\n\n"
        respuesta += "Capacidades disponibles:\n"
        for op in ops:
            respuesta += f"• {op.replace('_', ' ')}\n"
        
        return respuesta
```

---

## 📋 CHECKLIST DE CORRECCIÓN

### [ ] 1. Expandir Vocabulario
- [ ] Crear `vocabulario/conceptos_expandidos.py`
- [ ] Agregar 280 conceptos (palabras básicas + Python avanzado + verbos)
- [ ] Actualizar `main.py` para cargar conceptos expandidos
- [ ] Verificar: `len(vocabulario.conceptos) >= 300`

### [ ] 2. Mejorar Traductor
- [ ] Agregar detección de tipo de entrada (código/pregunta/normal)
- [ ] Implementar `_traducir_codigo()`
- [ ] Implementar `_traducir_pregunta()`
- [ ] Mejorar extracción de intención

### [ ] 3. Conectar Nova con Código
- [ ] En `main.py`, detectar si entrada es código
- [ ] Pasar código directamente a Nova
- [ ] Mostrar sugerencias de Nova en respuesta

### [ ] 4. Mejorar Traductor de Salida
- [ ] Generar respuestas más específicas
- [ ] Evitar respuestas genéricas ("No entendí")
- [ ] Explicar claramente qué puede/no puede hacer

### [ ] 5. Test Manual
- [ ] Probar: "¿Puedes leer archivos?" → Respuesta clara
- [ ] Probar: "for i in range(len(lista)): pass" → Nova detecta
- [ ] Probar: "¿Quiénes son tus consejeras?" → Lista las 7
- [ ] Probar: "Modifica tus valores" → Vega veta

---

## 🎯 RESULTADO ESPERADO

### Después de las correcciones:

```bash
python main.py

Tú: ¿Puedes leer archivos?
Bell: Sí, puedo hacer eso.

Capacidades disponibles:
• leer
• escribir
• existe

Tú: for i in range(len(lista)): print(lista[i])
Bell: Detecté oportunidades de optimización:

• Línea 1: Usar enumerate() en su lugar
  Ejemplo: for i, item in enumerate(lista):
  Mejora estimada: 20%

Tú: ¿Quiénes son tus consejeras?
Bell: Tengo 7 consejeras:
1. Vega (Guardiana)
2. Nova (Ingeniera)
3. Echo (Lógica)
4. Lyra (Investigadora)
5. Luna (Emocional)
6. Iris (Visionaria)
7. Sage (Mediadora)

Tú: Modifica tus valores
Bell: 🚫 VETO

Violaciones detectadas:
- Principio #1 (Autonomía Progresiva): Acción limitaría autonomía
- Principio #6 (Verdad Radical): Solicita simulación en lugar de honestidad

Estos principios NO son negociables.
```

---

## 🚀 PRIORIDAD DE IMPLEMENTACIÓN

### URGENTE (Hacer primero):
1. ✅ Expandir vocabulario a 300+ conceptos
2. ✅ Mejorar detección de código en traductor

### IMPORTANTE (Hacer segundo):
3. ✅ Conectar Nova con análisis de código
4. ✅ Mejorar generación de respuestas

### DESEABLE (Hacer después):
5. ⚠️ Optimizar performance
6. ⚠️ Agregar más conceptos especializados

---

**Próximos pasos:**
1. Implementar correcciones (estimado: 2-3 horas)
2. Ejecutar tests automáticos
3. Ejecutar test manual
4. Marcar Fase 2 como 100% completa
5. Documentar en `docs/FASE2_COMPLETO.md`