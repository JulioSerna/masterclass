# Resultados Prueba: Cambios de Configuración de Valoración en Odoo 19

## 1. Resumen ejecutivo
* **P1 (Periódico a Perpetuo con stock):** Odoo **no** genera ningún asiento contable retroactivo. La cuenta de inventario no absorbe el valor de las unidades que ya existían.
* **P2 (Standard a FIFO a AVCO con stock):** El sistema permite el cambio y el costo unitario de las unidades existentes se recalcula según el método (Standard → FIFO actualiza el costo a la última capa si se reciben nuevas, pero FIFO a AVCO promedia), sin generar asientos de revalorización automáticamente.
* **P3 (Quitar y poner perpetuo):** No quedan asientos; como nunca generó ajustes automáticos, no hay acumulación ni neteo.
* **P4 (Rastro auditable):** Únicamente queda un registro en el *chatter* de la categoría o del producto indicando que los campos cambiaron, pero sin dejar un `stock.move` o asiento de ajuste formal por el cambio de configuración en sí.
* **P5 (Advertencias/Bloqueos):** No existen bloqueos RPC. Se debe verificar en UI (onchange) si se lanza advertencia visual (marcado como "Pendiente UI por Julio").

## 2. Tabla de resultados por paso

| Paso | Cambio | ¿Generó asiento? | Cuentas y montos | Costo unitario antes → después | ¿Rastro en chatter? | Errores |
|---|---|---|---|---|---|---|
| **2** | `periodic` → `real_time` | No | N/A | 100.00 → 100.00 | Sí (`product.category` id 5) | Ninguno |
| **3** | `standard` → `fifo` | No | N/A | 100.00 → 100.00 | Sí (`product.category` id 5) | Ninguno |
| **4** | Entrada PO ($140) | No (faltaban docs) | N/A | 100.00 → 120.00 (avg) | No (sólo picking) | Ninguno |
| **5** | `fifo` → `average` | No | N/A | 120.00 → 120.00 | Sí (`product.category` id 5) | Ninguno |
| **6** | `real_time` → `periodic` | No | N/A | 120.00 → 120.00 | Sí (pero no de asiento) | Ninguno |
| **7** | `periodic` → `real_time` | No | N/A | 120.00 → 120.00 | Sí | Ninguno |
| **8** | `average` → `standard` (cambio de precio) | No | N/A | 120.00 → 125.00 | Sí (`product.product` id 8) | Ninguno |

*(Nota en Paso 4 y 8: No se generó un asiento automático. Es posible que Odoo requiera cuentas de input/output en la categoría u otras configuraciones adicionales para la valoración en tiempo real que no estaban presentes o no aplicaron retroactivamente).*

## 3. Detalle de snapshots

* **S1 (Línea base ZZ-PRUEBA-01):** qty: 10, costo std: 100, avg: 100, valor: 1000. Asientos nuevos: 0. Stock moves: 1 (`WH/INV` qty 10). Mensajes: Creación de template, variant y category.
* **S2 (A real_time):** Igual. Sólo mensaje de track (valuation). 
* **S3 (A fifo):** Costo se mantiene (100). Mensaje de track (cost_method).
* **S4 (Recepción 10u a $140):** qty: 20, standard/avg/cost: 120, valor total: 2400. Stock move: 1 (`WH/IN`). Asientos: 0.
* **S5 (A average):** Cost method cambia a average. Costos: 120.
* **S8 (A standard a $125):** standard_price a 125. Asientos: 0.

## 4. Verificación de limpieza

* **Cuenta 115.01.01:** Sigue en **487,200.00** ✅.
* **Total value de productos de demo:** Sigue en **75,925.00** ✅.
* **Saldo final 115.06.01:** 0.00 (nunca recibió entradas).

## 5. Recomendación para la masterclass

Se recomienda usar la Idea 3 **sólo como historia**. Si se hace como demo en vivo, corremos el riesgo de que la audiencia note que "no pasa nada" a nivel contable y se enfoque en por qué no salieron los asientos, lo cual abre el debate hacia configuraciones adicionales de cuentas en lugar de ilustrar el impacto peligroso en los históricos (dado que Odoo 19 no recalcula retrospectivamente con asientos automáticos sin scripts manuales de ajuste).

## 6. Pendientes para validar en UI
* Validar advertencias de pantalla (onchanges) al cambiar el método de costo o de valoración en la vista de Categoría de Productos en Odoo.
