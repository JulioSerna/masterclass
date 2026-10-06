# 🎓 Vauxoo Academy · Masterclass 2026

## "De la Logística a la Contabilidad: Domina la Valoración de Inventarios en Odoo 19.0"

| Parámetro | Detalle Oficial |
| :--- | :--- |
| **Ponente** | Julio Serna — Project Manager & Experto Funcional en Vauxoo |
| **Duración** | 90 Minutos (Virtual en vivo) |
| **Valor** | $100 USD (Acceso Total + Grabación + Entregables) |
| **Versión Odoo** | Odoo 19.0 Enterprise (Localización México · Plan Contable SAT · Base MXN) |
| **Base de Datos Demo** | Masterclass México, S.A. de C.V. (RFC: `EKU9003173C9`) |
| **Estatus del Proyecto** | Plan v4 Definitivo (Vigente y Alineado con las 3 Causas Raíz) |

---

## 🧭 Índice Maestro de Documentos (Fuente Única de Verdad)

Para evitar confusión entre versiones y borradores históricos, toda la información oficial está gobernada por:
👉 [`INDICE_MAESTRO_DE_DOCUMENTOS.md`](file:///Users/julioserna/.gemini/antigravity/scratch/masterclass/INDICE_MAESTRO_DE_DOCUMENTOS.md)

### Los 4 Documentos Pilares Oficiales (Versión Vigente v4):

1. **Plan Definitivo v4 (Estrategia y Syllabus):**
   - [`masterclass-plan-final.md`](file:///Users/julioserna/.gemini/antigravity/brain/0d29e6f9-1542-49a7-8e25-4e5ede21426b/masterclass-plan-final.md)
   - Contiene la arquitectura narrativa de 90 min alrededor de las **3 Causas Raíz del Divorcio Contabilidad-Logística** (Configuración, Operación, Auditoría).
2. **Guion de Transmisión (Teleprompter en Vivo):**
   - [`GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md`](file:///Users/julioserna/.gemini/antigravity/brain/0d29e6f9-1542-49a7-8e25-4e5ede21426b/GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md)
   - Manual operativo minuto a minuto con dos columnas: *Qué hacer en pantalla* y *Qué decir verbalmente*.
3. **Guía Técnica de Base de Datos y Demo:**
   - [`MASTERCLASS_DATABASE_GUIDE.md`](file:///Users/julioserna/.gemini/antigravity/brain/0d29e6f9-1542-49a7-8e25-4e5ede21426b/MASTERCLASS_DATABASE_GUIDE.md)
   - Credenciales, cuentas contables, catálogo de 5 productos demo, saldos del Hook ($487,200 vs $75,925) y procedimientos de reset.
4. **Script Automatizado de Configuración:**
   - [`setup_masterclass.py`](file:///Users/julioserna/.gemini/antigravity/scratch/masterclass/setup_masterclass.py)
   - Generación limpia e idempotente de la instancia con Odoo 19, configurando el hook y desactivando crons de cierre automático.

---

## 📦 Suite Web y Entregables para Alumnos

- **`index.html`:** Portal maestro con deck interactivo de slides, cronómetro de 90 min y accesos directos.
- **`slides.html`:** Presentación standalone a pantalla completa para proyector o Google Meet.
- **`checklist.html`:** **Entregable #1 oficial** — Checklist de Auditoría Logística-Contable con Matriz de Cadencia (Diaria, Semanal, Mensual, Anual).
- **`guia-mapeo.html`:** **Entregable #2 oficial** — Tabla de Mapeo Conceptual Odoo 18 → Odoo 19 para México.

---

## ⏱️ Estructura del Cronograma Oficial (Plan v4 — 90 Minutos)

- **Bloque 1 (00:00 – 00:07 | 7 min): El Hook en Vivo — El Gran Descuadre**
  - Balanza cuenta `115.01.01` ($487,200 MXN) vs Valoración de Stock ($75,925 MXN). Descuadre brutal de $411,275 MXN.
- **Bloque 2 (00:07 – 00:17 | 10 min): El Nuevo Paradigma Odoo 19 & Causa Raíz #1 (Malas Configuraciones)**
  - Odoo 19: Adiós SVL, fin de cuentas puente interim, método de valoración en categoría. Por qué 2 configuraciones malas no hacen una buena y qué pasa al cambiar de método en caliente.
- **Bloque 3 (00:17 – 00:37 | 20 min): Casos Prácticos de Flujo Normal**
  - Caso 1: Flujo nacional MXN limpio (Recepción → Factura → Costo de Ventas).
  - Caso 2: Compra en USD con Costos en Destino (Landed Costs) y flete prorrateado.
- **Bloque 4 (00:37 – 00:53 | 16 min): La Clínica de Desastres Operativos**
  - Desastre 1: Stock Negativo (`VALVULA-NEG`).
  - Desastre 2: Tipo de Cambio Erróneo en Factura.
  - Desastre 3: Mermas y Scrap (`CABLE-MERMA`) a cuentas no deducibles.
  - Desastre 4: Obsolescencia y Deterioro NIF C-4 (`TARJETA-OBS`).
- **Bloque 5 (00:53 – 01:07 | 14 min): El Momento de la Verdad & Causas Raíz #2 y #3**
  - Causa Raíz #2 (Pólizas Manuales): Se audita y revierte el asiento intruso `MISC/2026/09/0001` de $487,000 MXN. ¡Cuadre matemático perfecto!
  - Causa Raíz #3 (Falta de Auditoría Frecuente): Presentación de la Matriz de Cadencia (Diaria, Semanal, Mensual, Anual) y las 3 Reglas de Oro.
- **Bloque 6 (01:07 – 01:30 | 23 min): Hot Seat Q&A y Entrega de Recursos**
  - Consultoría en vivo con preguntas complejas del chat y entrega de la suite web.
