# Diseño de Expansión Masterclass Odoo 19.0: 120 Minutos + 30 Minutos Q&A

**Fecha:** 2026-10-14  
**Autor:** Julio Serna & Equipo de Ingeniería Vauxoo Academy  
**Versión del Plan:** v8  
**Duración Total:** 150 Minutos (2 horas de exposición + 30 minutos de Q&A)

---

## 1. Objetivos del Cambio
1. Ampliar el alcance y profundidad de la Masterclass a **120 minutos de exposición + 30 minutos de sesión de preguntas en vivo**, permitiendo explicar con rigor técnico los temas clave sin prisas.
2. Incorporar los **4 elementos y modelos esenciales de auditoría** (Reporte de Existencias, Facturas por Recibir, Reporte Contable y Movimientos de Inventario).
3. Publicar la **Tabla Maestra de Movimientos Logísticos en Odoo 19.0**, clarificando qué operaciones generan apunte contable y cuáles no.
4. Desarrollar las **recomendaciones estratégicas de saneamiento en la vida real**: contrastar el uso destructivo de pólizas manuales contra el protocolo formal de "Borrón y Cuenta Nueva" (reinicio controlado de inventario y configuración limpia).

---

## 2. Nueva Estructura Temporal y Temática

| Bloque | Minutos | Nombre del Bloque | Contenido Clave |
| :--- | :---: | :--- | :--- |
| **Bloque 1** | 00:00 – 00:12 (12 min) | **El Hook & Mapa del Divorcio** | El descuadre de $482,190.00 MXN en vivo, encuesta de cadencia y las 3 causas raíz. |
| **Bloque 2** | 00:12 – 00:30 (18 min) | **La Revolución Odoo 19 & Motor Contable** | Adiós SVL e interims, Periódico vs Perpetuo, y **Tabla Maestra de Movimientos Logísticos (Cuáles sí/no generan contabilidad)**. |
| **Bloque 3** | 00:30 – 00:55 (25 min) | **La Operación Normal (AVCO MXN y USD)** | Caso 1: Teclado Ergonómico ($160 AVCO) + venta/factura ($4,800). Caso 2: Monitor 4K ($100 USD @ TC 18.50 = $37,000 MXN). |
| **Bloque 4** | 00:55 – 01:25 (30 min) | **La Clínica de Desastres (5 Casos Reales)** | 1. Mouse sin cuenta (-$8.5k). 2. Router archivado (+$2.4k). 3. Cámara en USD ($27.7k/u). 4. RAM costo manual (-$210). 5. SSD stock negativo (+$1.5k). |
| **Bloque 5** | 01:25 – 02:00 (35 min) | **Auditoría, Resolución y Saneamiento** | **1. Los 4 Elementos de Auditoría (Cuadrilátero de Control).**<br>**2. Demostración Server Action #589 & Plantilla CSV.**<br>**3. Protocolo de Saneamiento: El Parche Manual vs Borrón y Cuenta Nueva.** |
| **Bloque 6** | 02:00 – 02:30 (30 min) | **Q&A "Hot Seat" & Cierre** | Consultoría en pantalla compartida de casos de los asistentes y entrega del Kit. |

---

## 3. Especificación Detallada de los 3 Nuevos Componentes

### 3.1. Tabla Maestra de Movimientos Logísticos en Odoo 19.0 (Bloque 2)
Se integra una tabla comparativa para desmitificar qué documentos y eventos operativos disparan pólizas automáticas a la cuenta de inventario:

| Tipo de Movimiento / Documento | Modelo Odoo | ¿Genera Contabilidad a Cuenta 1150? | Justificación Técnica en Odoo 19 |
| :--- | :--- | :---: | :--- |
| **Costes en Destino (Landed Costs)** | `stock.landed.cost` | **SÍ** | Incrementa el valor del inventario imputando fletes/aranceles a las recepciones vinculadas. |
| **Facturas de Proveedor / Cliente** | `account.move` | **SÍ** | Registra el costo de adquisición o deduce el inventario reconociendo el Costo de Ventas (501). |
| **Ajustes de Inventario (Mermas / Conteos)** | `stock.move` | **SÍ** *(si configurado)* | Genera póliza si la ubicación virtual (Virtual Locations/Inventory adjustment) tiene cuenta contable. |
| **Órdenes de Producción (MO)** | `mrp.production` | **SÍ** | Acredita materias primas consumidas y debita producto terminado en almacén. |
| **Revalorización Manual de Coste** | `stock.valuation.adjustment` | **SÍ** | Cuando se ejecuta por asistente contable formal, no por simple edición en la ficha. |
| **Pedidos de Venta (SO)** | `sale.order` | **NO** | Es un compromiso comercial; no altera existencias ni saldos financieros. |
| **Pedidos de Compra (PO)** | `purchase.order` | **NO** | Es una orden de compra contractual sin flujo físico ni devengo. |
| **Traslados Internos entre Ubicaciones** | `stock.picking` (internal) | **NO** | Mover de estante A a estante B dentro de la misma compañía no cambia el valor del activo. |
| **Recepciones / Entregas en Flujo Directo** | `stock.picking` | **Ver Regla** | En v19 en flujo sin cuentas transitorias el devengo formal se amarra con la factura o el albarán valorado directo. |

---

### 3.2. Los 4 Modelos / Reportes Esenciales de Auditoría (Bloque 5)
Para auditar inventarios, se enseña el modelo mental del **"Cuadrilátero de Control"**:

1. **Reporte de Existencias (Almacén - `stock.quant` / `stock.valuation`):**
   - Muestra las unidades físicas en mano multiplicadas por el costo unitario de la ficha (`standard_price`).
   - Revela: cantidades físicas y valor total estimado en bodega.
2. **Reporte de Mercancía por Facturar / Facturas por Recibir:**
   - Cruce entre líneas de compra recibidas (`qty_received`) vs facturadas (`qty_invoiced`).
   - Revela: provisiones pendientes y compras en tránsito contable.
3. **Reporte Contable (Mayor de la Cuenta `115.01.01`):**
   - Saldo deudor de la Balanza de Comprobación y detalle de apuntes contables (`account.move.line`).
   - Revela: apuntes huérfanos sin producto, pólizas manuales de diario y fechas efectivas.
4. **Movimientos de Inventario (`stock.move`):**
   - Historial granular de cada entrada, salida y ajuste con fecha, origen, destino y valor monetario.
   - Revela: la causa raíz física de cualquier alteración en el costeo promedio.

---

### 3.3. Recomendaciones Estratégicas para Saneamiento en Producción (Bloque 5)
Se presenta la comparativa práctica entre dos enfoques:

#### Vía A: El Parche Manual ("La Aspirina Destructiva")
* Qué hace el contador: Mete una póliza manual tipo `MISC` cargando o abonando a la `115.01.01` contra resultados para que la balanza coincida con su reporte de almacén.
* Por qué es un error crítico:
  - No genera ningún movimiento en el almacén.
  - El almacén sigue teniendo cantidades o costos erróneos.
  - Al vender en el futuro, el sistema volverá a descargar con costos desfasados, recreando el descuadre una y otra vez.

#### Vía B: Protocolo "Borrón y Cuenta Nueva" (La Solución Blindada Vauxoo)
Procedimiento paso a paso para empresas con inventario gravemente contaminado:
1. **Corte Operativo:** Congelar transacciones de almacén durante la ventana de auditoría.
2. **Descarga Total a Cero:** Ajuste de inventario llevando todas las cantidades físicas de las ubicaciones internas a `0.00` (utilizando una ubicación virtual transitoria de saneamiento).
3. **Ajuste Contable del Saldo Residual:** Llevar la cuenta `115.01.01` a `$0.00` mediante un asiento contable contra Pérdidas por Inventario / Resultados de Ejercicios Anteriores.
4. **Blindaje de la Fase 0:** Verificar categorías con AVCO, Valoración Perpetua, cuentas contables asignadas y permisos bloqueados para edición manual de costes.
5. **Carga del Conteo Físico Real:** Subir plantilla con conteo real verificado y costo unitario real auditado, con contrapartida a cuenta de apertura/transitoria.
6. **Resultado:** Almacén y Contabilidad inician alineados al 100% al centavo, con trazabilidad limpia hacia adelante.

---

## 4. Archivos Impactados
1. `masterclass-plan-final.md`: Actualización integral a **v8** con la nueva duración de 150 min (120+30) y los 3 temas desarrollados.
2. `make_slides_content.py`: Inclusión de 3 nuevas diapositivas visuales (pasando de 19 a 22 diapositivas).
3. `make_cronograma_content.py`: Actualización del desglose minuto a minuto para reflejar los 120 minutos + 30 minutos de Q&A.
4. `make_mapeo_content.py`: Incorporación de la Tabla Maestra de Movimientos Logísticos y el Cuadrilátero de Auditoría.
5. `compile_all.py` / `assemble_hub.py`: Recompilación de `index.html`, `slides.html`, `checklist.html`, `guia-mapeo.html`.
