# 📚 Metodología & Prompts Clave de Ingeniería: Masterclass Odoo 19.0

> **Proyecto:** *"De la logística a la contabilidad: Domina la valoración de inventarios en Odoo 19.0"*  
> **Formato:** Masterclass en vivo de 90 minutos ($100 USD por asistente) · Vauxoo Academy  
> **Autor:** Julio Serna (Project Manager & Functional Consultant, Vauxoo)  
> **Objetivo de este documento:** Preservar la genealogía exacta de las instrucciones (prompts), decisiones arquitectónicas y técnicas de IA colaborativa utilizadas para construir los 3 activos centrales:
> 1. **El Plan Estratégico** (Estructura de 90 min y pedagogía sin tecnicismos estériles)
> 2. **El Script** (Automatización Python de BD y Guion Teleprompter minuto a minuto)
> 3. **Las Slides & Portal Web** (Presentación proyectable y suite interactiva bajo marca Vauxoo Academy)

---

## 🧭 Resumen de la Metodología de Prompting

El éxito de este proyecto no radicó en un único "mega-prompt", sino en una secuencia táctica de 4 principios:
1. **Debate Dialéctico entre Agentes:** Enfrentar a dos roles de IA (Estratega Pedagógico vs. Crítico Técnico) antes de escribir una sola línea de temario.
2. **Inyección de la Voz de la Experiencia:** Introducir anécdotas reales del campo de batalla de consultoría (vicios de los clientes, pólizas manuales ciegas).
3. **Poda Despiadada de Jerga:** Prohibir términos distractores (cero NIFs teóricos, cero SAT/fiscalidad secundaria, cero mención a "kardex").
4. **Idempotencia Técnica Respaldada:** Exigir que todo lo expuesto en las diapositivas sea replicable mediante un script de base de datos automatizado.

---

## 1. 📋 Prompts Clave para Generar el PLAN (Estrategia y Temario)

### 1.1. Prompt de Génesis: Debate Dialéctico y Nivel de Calidad ($100 USD)
* **Momento:** Sesión 1 · Paso 0 (Inicio de proyecto).
* **Propósito:** Evitar explicaciones genéricas de manual de Odoo y forzar un estándar premium.

```text
Necestio que me puedas apoyar para hacer un super y bueno y de calidad y profesional yn plan para dar esta clase en odoo versión 19.0

Necesito que debatas con otro agente gemini el que consideres mejor y usando el skill de superpowers, para que me hagan un plan de como debería abordar esta masterclass, recuerda que es versión 19.0 y en odoo cambio la forma de valoración de inventario, estas es un masterclass de 1:30 es virtual y en directo, los clientes pagan por estar en esa sesión, por lo cual necesito que sea algo de calidad, que no se encuentre en cualquier video o documento que agregue valor y que represente un caso real para los clientes
```

* **Resultado generado:** Se instanciaron dos subagentes en contrapunto que produjeron la estructura en 6 bloques cronológicos, identificando que el cambio clave de Odoo 19 es la eliminación de cuentas analíticas en categorías y la nueva valoración a nivel propiedad contable.

---

### 1.2. Prompt de Refinamiento: Localización México, AVCO y Multimoneda USD
* **Momento:** Sesión 1 · Paso 71.
* **Propósito:** Aterrizar el temario al mercado objetivo real (México / USD) y podar distracciones innecesarias (multicompañía).

```text
Ahora necesito unas correciones al plan presentado, sigue usando superpowers y sigue discutiendo un otro agente de gemini
1. Vamos enfocar la masterclass con ejemplo de metodo de costo average
2. Con una configuración para mexico, plan contable y localización
3. por ahora vamos evitar el caso de uso de multicompañía
4. pero si vamos agregar el caso de uso de compras en usd, que aqui veo que pasa que usan tipos de cambio que no son, que confirman la compra pensando que es en usd, etc
5. Compañía en mxn
6. casos de compra en usd
Seguir manteniendo todo con estos cambios en la 1:30 de la mesterclass y lo que ya propusiste solo considera estos comentarios que te deje
```

* **Resultado generado:** El temario se centró en la moneda base MXN con compras internacionales en USD, evidenciando el descuadre de tipo de cambio al recibir mercancía vs facturar proveedor.

---

### 1.3. Prompt de Poda de Ruido: Blindaje del Tiempo (Cero Fiscal / Cero Pedimentos)
* **Momento:** Sesión 1 · Paso 73.
* **Propósito:** Proteger los 90 minutos de la sesión impidiendo que la IA desvíe la clase hacia temas aduanales o fiscales complejos.

```text
tengo duda aun con los puntos CFDI de Pago, Anticipo en USD como afecta o favore para la masterclass que es de valuación de inventario, sobre todo el punto que comentas de 'Crítico para IVA acreditable', solo quiero validar si es justificable ó no es necesario, recuerda que es una masterclass de valución de inventario y meter un caso o como se va mostrar o mostaría el tema de pedimeitno ya que ahi nos podemos llevar toda la sesion
```

* **Resultado generado:** Eliminación total de CFDI de Pago y Pedimentos aduanales adyacentes, concentrando el 100% del tiempo en la balanza de comprobación vs reporte de inventario valorado.

---

### 1.4. Prompt de las "3 Causas Raíz Reales": Experiencia Viva de Consultoría
* **Momento:** Sesión 2 · Paso 577.
* **Propósito:** Inyectar los vicios reales de los usuarios observados en años de implementaciones.

```text
Lanza un agente que consideres mas intelegie de gemini par que discultan y me den conclusiones

/brainstorming como puedo agregar a la masterclass estas ideas que tengo, que en mi experiencia pasan. muchos, que son algunas de las principales casusas por las sque no se llega a tener un buen control de contabilidad vs logistica, neesito que me digas en donde agrega mas valor meterlo, si agrega valor comentarlo y en que momento de la masterclass
1. Pólizas manuales, el contador en ese momento con poco claridad o sin saber como pero el llega a un numero y decide hacer una póliza manual para cuadrar el inventario
2. El usuario, contadore, nunca audita un reporte...
3. Malas configuraciones, dos configuraciones malas no hacen una buena...
```

* **Resultado generado:** Creación del marco conceptual de la clase: *"Las 3 Causas Raíz del Divorcio entre Logística y Contabilidad"*, que se convirtió en el eje del Bloque 4.

---

### 1.5. Prompt de Delimitación Final: Los 4 Errores Permitidos y Jerga Prohibida
* **Momento:** Sesión 2 · Paso 1110.
* **Propósito:** Prohibición expresa de tecnicismos estériles y definición cerrada de los 4 desastres a simular.

```text
usando /brainstorming entonces para el bloque 4, solo quiero estos casos:
1. Un ajuste de inventario sin una cuenta de inventario configurada
2. Un recepción de compra con tipo de cambio errroneo
3. Mercancia que se entrega al cliente, sin antes recibir compra ó facturar compra ó ambas
4. Las polizas manuales de ajuste
Bloque 3, por si hay clientes que no usan importación vamos a quitar el caso de importación / aduanal, mejor agregamos el caso de venta entrega de mercancia...
General: Por favor no comentar nada de reglas NIF ya que pudeira ser que yo mismo no las conosco. No comentar que el 'kardex' por que odoo no hay un kardex. No comentar o hacer relación a cosas fiscales por que no es una masterclass de fiscal
```

* **Resultado generado:** Se consagró el **Plan Definitivo v4**, con los 4 desastres reproducibles y las reglas estrictas de vocabulario: cero NIF, cero Kardex, cero fiscal.

---

## 2. 💻 Prompts Clave para Generar el SCRIPT

La masterclass requería dos scripts de naturaleza distinta: la infraestructura de software para la base de datos y el guion verbal del presentador.

### 2.1. Script de Automatización de Base de Datos (`setup_masterclass.py`)
* **Momento:** Sesión 2 · Paso 16.
* **Propósito:** Idempotencia y repetibilidad de la demo en vivo.

```text
Ahora con relación al plan que ya esta definido, necesito que en la instancia de masterclass
1. Instales todo lo necesario
2. Hagas las configuraciones necesarias
3. Instales la data necesaria para hacer toda la masterclass
Todo lo que hagas, scripts, etc, tienen que quedar documentados por si necesito volver a crear una nueva base de datos sepas rapido como generar una nueva con todo lo necesario para la masterclass, ó que si te digo vamos de nuevo con la data de inicio pongas esa data, en caso de que haya hecho incorrecto algun ajuste o dato y las pruebas que voy a realizar
```

* **Resultado generado:** Creación del script ejecutable `setup_masterclass.py` con:
  - Carga de plan contable y localización MX.
  - Creación de categorías AVCO y 5 productos demo.
  - Generación de órdenes de compra USD y órdenes de venta MXN.
  - Creación del asiento manual del Hook (`MISC/2026/09/0001`) por $411,275 MXN de descuadre.
  - Desactivación automática del cron de cierre contable de Odoo.

---

### 2.2. Depuración del Script: Supresión del Asiento NIF
* **Momento:** Sesión 2 · Paso 910.
* **Propósito:** Alinear el script técnico con la directriz de cero tecnicismos NIF.

```text
Por favor omite esta póliza manual MISC/2026/09/0002 en el script que tenemos de generar la instancia por favor no agreagr este paso y no considerar almenos esta póliza de nif, solo dejemos el caso de la póliza manual MISC/2026/09/0001
```

* **Resultado generado:** Modificación del script para dejar únicamente el caso del descuadre clásico por ajuste contable sin soporte de almacén.

---

### 2.3. Guion de Transmisión en Vivo (`GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md`)
* **Momento:** Sesión 2 · Paso 569 y refinamientos de teleprompter.
* **Propósito:** Tener un manual segundo a segundo para no improvisar frente al público.

```text
habias preparado un script de que decir y hacer no lo veo donde esta o por que ya no lo muestras?

Estructura el guion segundo a segundo para la transmisión en directo con dos columnas claras:
- Minuto y Qué proyectar en pantalla en Odoo (pestañas, clics, filtros exactos)
- Speech textual de lo que debo decir frente al micrófono (anécdotas, preguntas al chat y alertas)
Asegura que el Bloque 1 arranque con el Hook del balance descuadrado y que el Bloque 5 explique la auditoría en 4 pasos.
```

* **Resultado generado:** El archivo `GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md`, que actúa como teleprompter sincronizado con cada pantalla de Odoo 19.

---

## 3. 🖥️ Prompts Clave para Generar las SLIDES y el Portal Web

### 3.1. Arquitectura de Diapositivas: Apertura con el HOOK y Metodología en 4 Pasos
* **Momento:** Sesión 2 · Pasos de diseño y ajuste de slides.
* **Propósito:** Construir un portal interactivo para dictar la clase en vivo y como entregable para los asistentes.

```text
Ahora necesitamos las diapositivas de la masterclass. Debe ser una presentación interactiva web en HTML/JS lista para proyectar en pantalla completa, aplicando la marca y colores oficiales de Vauxoo.
Quiero que la Slide 2 sea inmediatamente el HOOK: poner la captura del balance con el descuadre de -$17,760 MXN para captar la atención de inmediato antes de entrar en la teoría de Odoo 19.
En la Slide del Bloque 5, no resuelvas la auditoría diciendo 'haz clic aquí'; explica la metodología paso a paso de los 4 pasos para conciliar contabilidad vs inventario valorado.
```

* **Resultado generado:**
  - `slides.html`: Presentación a pantalla completa con navegación por teclado (`←`, `→`, `F` fullscreen, `N` notas).
  - Slide 2 configurada como el Hook visual inmediato.
  - Slide 14 detallando la Metodología Forense de 4 Pasos (Aislar fecha → Conciliar cuenta de tránsito 115.01 → Auditar ajustes → Rastrear pólizas manuales).

---

### 3.2. Congelación de Versión Definitiva (Baseline v5.0)
* **Momento:** Sesión 2 · Paso 1339.
* **Propósito:** Congelar el estado final del repositorio para evitar regresiones antes del evento en vivo.

```text
por ahora guarda esto como la ultima versión, para cuando te pida cambios no tengas que hacer de nuevo todo y solo se actualice sobre la ultima version
```

* **Resultado generado:**
  - Creación del tag Git `v5.0-baseline` en el repositorio `JulioSerna/masterclass`.
  - Compilación y publicación del portal unificado en GitHub Pages:
    - 🌐 **Portal Maestro:** `https://julioserna.github.io/masterclass/`
    - 📽️ **Deck de Diapositivas:** `https://julioserna.github.io/masterclass/slides.html`
    - 📋 **Checklist Interactivo:** `https://julioserna.github.io/masterclass/checklist.html`
    - 📊 **Guía de Mapeo Odoo 18 → 19:** `https://julioserna.github.io/masterclass/guia-mapeo.html`

---

## 🚀 Lecciones Aprendidas de Prompt Engineering (Para Replicar)

1. **No aceptar el primer borrador:** Utilizar `/brainstorming` y exigir debate entre subagentes para exponer debilidades metodológicas antes de aprobar el plan.
2. **Definir explícitamente las "Palabras Prohibidas":** Indicar qué conceptos NO deben aparecer (por ejemplo: NIF, SAT, Kardex) ahorra horas de corrección.
3. **Diseñar el contenido desde el "Dolor del Alumno":** Comenzar con un balance descuadrado en el minuto 2 conecta mucho más que empezar con 15 minutos de diapositivas conceptuales.
4. **Respaldar el discurso con código reproducible:** Crear siempre un script (`setup_masterclass.py`) que pueda restaurar el estado inicial en menos de 60 segundos ante cualquier error en vivo.

