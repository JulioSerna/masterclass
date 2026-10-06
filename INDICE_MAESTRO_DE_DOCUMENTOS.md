# 📚 Índice Maestro y Fuente de Verdad: Masterclass Odoo 19.0

> **Proyecto:** Masterclass "De la logística a la contabilidad: Domina la valoración de inventarios en Odoo 19.0"  
> **Ponente:** Julio Serna (Project Manager y Experto Funcional, Vauxoo)  
> **Fecha de Actualización:** 6 de Octubre, 2026  
> **Estado:** Vigente y Alineado (Plan v4)

Este documento es la **Fuente Única de Verdad** para el ponente y para todos los agentes de IA que colaboren en el proyecto. Define la estructura de archivos, el historial de versiones y cuáles documentos son oficiales y cuáles son históricos.

---

## 🧭 Los 4 Documentos Pilares Oficiales (Versión Vigente v4)

Cualquier duda sobre qué decir, qué hacer en pantalla, qué configurar o cómo funciona la sesión debe consultarse exclusivamente en estos cuatro documentos:

| # | Documento Oficial | Ubicación en el Proyecto | ¿Qué hace? y ¿Para qué sirve? |
|:---:|:---|:---|:---|
| **1** | **Plan Definitivo v4 (Estrategia y Estructura)** | [`masterclass-plan-final.md`](file:///Users/julioserna/.gemini/antigravity/brain/0d29e6f9-1542-49a7-8e25-4e5ede21426b/masterclass-plan-final.md) | **El marco conceptual y temario de la sesión.**<br>• Define los 6 bloques cronológicos a 90 minutos exactos.<br>• Establece el marco narrativo: *Las 3 Causas Raíz del Divorcio Contabilidad-Logística*.<br>• Contiene las especificaciones de los dos entregables (Checklist con Matriz de Cadencia y Tabla de Mapeo v18→v19). |
| **2** | **Guion de Transmisión (Teleprompter)** | [`GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md`](file:///Users/julioserna/.gemini/antigravity/brain/0d29e6f9-1542-49a7-8e25-4e5ede21426b/GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md) | **El manual operativo en vivo minuto a minuto para Julio Serna.**<br>• Columna izquierda: **Qué hacer en pantalla** (pestañas exactas, clics, filtros, campos a resaltar).<br>• Columna derecha: **Qué decir verbalmente** (diálogos, anécdotas, advertencias y preguntas al chat).<br>• Tiempos rebalanceados: Hook (7m), Paradigma (10m), Casos Prácticos (20m), Desastres (16m), Momento de la Verdad (14m), Q&A Hot Seat (23m). |
| **3** | **Guía Técnica de Base de Datos y Demo** | [`MASTERCLASS_DATABASE_GUIDE.md`](file:///Users/julioserna/.gemini/antigravity/brain/0d29e6f9-1542-49a7-8e25-4e5ede21426b/MASTERCLASS_DATABASE_GUIDE.md) | **Coordenadas y estado de la instancia de Odoo 19.**<br>• URL, credenciales de acceso, idioma Español (MX), menús contables.<br>• Catálogo de los 5 productos demo y órdenes de compra/venta precargadas.<br>• Verificación de saldos: Balanza $487,200 vs Almacén $75,925 (Descuadre Hook = $411,275).<br>• Instrucciones para reiniciar la base de datos a su estado virgen en cualquier momento. |
| **4** | **Script Automatizado de Configuración** | [`setup_masterclass.py`](file:///Users/julioserna/.gemini/antigravity/scratch/masterclass/setup_masterclass.py) | **El script Python reproducible.**<br>• Si la base de datos se rompe o se necesita una instancia nueva, ejecuta la creación completa de categorías AVCO, productos, órdenes, tipos de cambio USD y el asiento manual del Hook (`MISC/2026/09/0001`).<br>• Desactiva el cron de cierre automático para evitar que Odoo genere asientos no deseados. |

---

## 🌐 Suite Web Interactiva y Entregables para Alumnos

Generados bajo la identidad corporativa oficial **Vauxoo Academy** (paleta Azul Academy / Blanco / Rojo Vauxoo, sin dependencias externas):

* **`index.html`:** Portal maestro con el deck de diapositivas interactivo, cronómetro de 90 min y accesos a entregables.
* **`slides.html`:** Presentación a pantalla completa lista para proyectar en Zoom o Google Meet.
* **`checklist.html`:** **Entregable #1 oficial** (Checklist de Auditoría Logística-Contable con Matriz de Cadencia: Diaria, Semanal, Mensual, Anual).
* **`guia-mapeo.html`:** **Entregable #2 oficial** (Tabla de Mapeo Conceptual Odoo 18 → Odoo 19 para México).

---

## 🗄️ Historial de Archivos y Borradores (Para Referencia Histórica)

Estos archivos se generaron en fases previas de debate técnico y diseño. **Ya no deben modificarse** y solo se conservan como bitácora:

| Archivo | Fase en que se creó | Estado actual |
|:---|:---|:---:|
| `plan_estratega.md` & `plan_critico.md` | Debate inicial v1 (cuando se evaluaban anticipos y CFDI de pago). | ❌ Obsoleto (Superado por v3 y v4) |
| `plan_v2_estratega.md` & `plan_v2_critico.md` | Debate v2 (cuando se acotó el tema de importaciones y se quitó el CFDI). | ❌ Obsoleto (Superado por v3 y v4) |
| `PLAN_PRUEBA_CAMBIOS_CONFIGURACION_ODOO19.md` | Plan del experimento técnico para validar qué hacía Odoo 19 al cambiar categorías en caliente. | ✅ Ejecutado |
| `resultados_prueba_config_odoo19.md` | Resultado del laboratorio técnico: confirmó que Odoo 19 NO genera asientos retroactivos. | ✅ Concluido (Sustentó el Bloque 2 del Plan v4) |

---

## 📌 Regla de Oro para Agentes

Cualquier nuevo agente o sesión que trabaje en esta masterclass **debe tomar como base única**:
1. El **Plan v4** (`masterclass-plan-final.md`).
2. El **Guion v4** (`GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md`).
3. La **Guía de BD** (`MASTERCLASS_DATABASE_GUIDE.md`) y el script `setup_masterclass.py`.
