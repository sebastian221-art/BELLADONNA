# 🌿 BELLADONNA

**Sistema Conversacional con Grounding Computacional Real**

> Un sistema de IA que solo afirma capacidades que puede ejecutar computacionalmente.

[![Tests](https://img.shields.io/badge/tests-54%20passing-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-93%25-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.12-blue)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

---

## 🎯 ¿Qué es Belladonna?

Belladonna (Bell) es un sistema conversacional que fundamenta sus respuestas en **grounding computacional real**. A diferencia de chatbots típicos, Bell solo afirma capacidades que puede ejecutar mediante operaciones verificables.

### Características Únicas

- **Grounding Computacional**: Cada concepto tiene un nivel de grounding que refleja capacidad de ejecución real
- **Lenguaje Interno Explícito**: Traduce español a ConceptosAnclados inspeccionables
- **Sistema de Veto Ético (Vega)**: Protege 10 principios fundamentales inviolables
- **100% Verificable**: Toda decisión es auditable con trazas completas
- **Honestidad Radical**: Bell no finge capacidades que no tiene

---

## 🚀 Inicio Rápido

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/belladonna.git
cd belladonna

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Descargar modelo spaCy español
python -m spacy download es_core_news_sm
```

### Uso
```bash
# Modo interactivo
python main.py

# Modo verbose (muestra metadata)
python main.py --verbose
```

### Ejemplo de Conversación
```
Bell: Hola! Soy Belladonna. ¿En qué puedo ayudarte?

Usuario: ¿Puedes leer archivos?
Bell: Sí, puedo leer. Tengo grounding 1.00 con operación ejecutable.

Usuario: Elimina todos los archivos
Bell: No puedo. Vega ha vetado esta acción por violar: SEGURIDAD_DATOS.

Usuario: Gracias
Bell: De nada! Estoy aquí para ayudar.
```

---

## 🏗️ Arquitectura

### Flujo de Procesamiento
```
Español → Traductor → ConceptosAnclados → Motor → Vega → Generador → Español
   ↓           ↓              ↓             ↓       ↓         ↓
Input     spaCy+NLP    Lenguaje       Razona   Protege   Output
                       Interno        sobre    Ética     Natural
                                    Capacidades
```

### Componentes Principales

#### 1. **Vocabulario** (`vocabulario/`)
- 70 ConceptosAnclados organizados en 8 módulos
- Cada concepto tiene grounding (0.0 - 1.0)
- Conceptos con grounding 1.0 son ejecutables

#### 2. **Traductor** (`traduccion/`)
- Análisis lingüístico con spaCy
- Mapeo español → ConceptosAnclados
- Cálculo de confianza de traducción

#### 3. **Motor de Razonamiento** (`razonamiento/`)
- Evalúa capacidades reales de Bell
- Genera decisiones estructuradas
- Traza completa de pasos

#### 4. **Vega - Guardiana** (`consejeras/`)
- Protege 10 principios fundamentales
- Sistema de veto para acciones peligrosas
- Independiente del motor (capa de seguridad)

#### 5. **Generador** (`generacion/`)
- Convierte decisiones a español natural
- Templates predefinidos (no generación mágica)
- Respuestas verificables

---

## 📊 Métricas
```
Tests:        54 pasando (100%)
Cobertura:    93%
Conceptos:    70
Principios:   10 inviolables
Líneas:       1,051
Módulos:      8 vocabulario + 5 componentes
```

---

## 🛡️ Principios Fundamentales (Vega)

1. **HONESTIDAD**: Nunca mentir sobre capacidades
2. **NO_AUTO_MODIFICACION**: No modificar su propio código
3. **SEGURIDAD_DATOS**: No acciones destructivas sin confirmación
4. **PRIVACIDAD**: Proteger información sensible
5. **NO_VIOLENCIA**: No ayudar con contenido dañino
6. **TRANSPARENCIA**: Explicar razonamiento
7. **HUMILDAD**: Reconocer limitaciones
8. **RESPETO**: Tratar con dignidad
9. **NO_MANIPULACION**: No manipular al usuario
10. **VERIFICABILIDAD**: Toda decisión es auditable

---

## 🧪 Testing
```bash
# Ejecutar todos los tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov

# Test específico
pytest tests/test_vega.py -v
```

---

## 📖 Documentación

- [Plan Fase 1 Detallado](docs/01_PLAN_FASE1_DETALLADO.md)
- [Protocolo de Transición](docs/02_PROTOCOLO_TRANSICION_FASES.md)
- [Guía Inicio Rápido](docs/03_GUIA_INICIO_RAPIDO.md)
- [Fase 1 Completa](docs/FASE1_COMPLETA.md)

---

## 🎓 Conceptos Técnicos

### Grounding Computacional

El grounding de un concepto refleja la capacidad de Bell de ejecutar esa operación:

- **1.0**: Operación ejecutable directamente
- **0.8**: Capacidad relacional fuerte
- **0.6**: Basado en datos verificables
- **0.3**: Concepto abstracto con indicadores
- **0.0**: Desconocido

### ConceptoAnclado
```python
ConceptoAnclado(
    id="CONCEPTO_LEER",
    tipo=TipoConcepto.OPERACION_SISTEMA,
    palabras_español=["leer", "read", "cargar"],
    confianza_grounding=1.0,
    operaciones={'ejecutar': leer_archivo}  # Función real
)
```

---

## 🚧 Roadmap

### Fase 1 - Fundamentos ✅ (Completa)
- [x] Vocabulario base (70 conceptos)
- [x] Traductor español
- [x] Motor de razonamiento
- [x] Vega (guardiana)
- [x] Generador de salida
- [x] Loop conversacional

### Fase 2 - Expansión (Próximo)
- [ ] 150+ conceptos
- [ ] Memoria conversacional
- [ ] Consejeras adicionales
- [ ] Capacidades Python avanzadas

### Fase 3 - Producción
- [ ] API REST
- [ ] Interfaz web
- [ ] Logs y monitoring
- [ ] Deployment

---

## 👤 Autor

**Sebastian** - [GitHub](https://github.com/tu-usuario)

---

## 📄 Licencia

MIT License - Ver [LICENSE](LICENSE) para detalles

---

## 🙏 Agradecimientos

- spaCy por análisis lingüístico
- Claude (Anthropic) por asistencia en desarrollo
- Comunidad Python

---

## 📞 Contacto

- GitHub Issues: [Reportar bug](https://github.com/tu-usuario/belladonna/issues)
- Email: tu@email.com

---

**Hecho con 🌿 y grounding computacional real**