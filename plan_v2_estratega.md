# 🎯 Plan Estratégico v2: Masterclass 2026 (Enfoque AVCO y México)

## "De la logística a la contabilidad: Domina la valoración de inventarios en Odoo 19.0"

| Dato | Detalle |
|------|---------|
| **Ponente** | Julio Serna — PM y Experto Funcional en Vauxoo |
| **Duración** | 90 minutos (1h 30min) |
| **Formato** | Virtual, en vivo |
| **Precio** | $100 USD |
| **Versión** | Odoo 19.0 |
| **Localización** | México (Moneda Base: MXN, Plan Contable Mexicano, CFDI) |
| **Entregables** | Certificado · Grabación · Checklist de Auditoría · Tabla de Mapeo 18→19 |

---

## 💎 ¿Por qué vale $100 USD?

> [!IMPORTANT]
> Este **no** es un tutorial genérico. Es una masterclass de **arquitectura de datos, resolución de desastres reales en importaciones y transición estratégica a Odoo 19.0** — conocimiento de trinchera que cuesta miles de dólares en consultoría.

**Lo que NO encuentras gratis en YouTube:**
1. Análisis profundo del cambio arquitectónico de Odoo 19.0 (eliminación de SVL y cuentas interim).
2. El uso exclusivo del **Costo Promedio (AVCO)** en Odoo 19, que es el método por excelencia en México.
3. **El caso crítico:** Cómo manejar compras en USD para una compañía en MXN, resolviendo los desastres generados por fluctuaciones del tipo de cambio (recepción vs. facturación).
4. El impacto de manufactura (MRP) en la valoración y en la cuenta de inventarios (1150).
5. Demostración del "momento de la verdad": rastrear y resolver un descuadre en vivo, alineado con el SAT y la contabilidad mexicana.

---

## ⏱️ Cronograma Minuto a Minuto

### Bloque 1: EL HOOK — "El Dolor que Todos Conocen"
**⏰ 00:00 – 00:07 (7 min)**

| Elemento | Detalle |
|----------|---------|
| **Apertura** | Bienvenida de Julio. Contexto de Vauxoo. |
| **Hook Visual** | Pantalla dividida: Balance General (Cuenta 1150 Inventarios) vs. Reporte de Valoración de Inventario a la derecha. **Diferencia visible de miles de pesos (MXN)**. |
| **Pregunta al chat** | *"¿A quién le ha tocado explicarle este descuadre al Director Financiero o al Auditor del SAT? Pongan 🔥 en el chat"* |
| **La Promesa** | "En los próximos 90 minutos dominarán la valoración AVCO en Odoo 19.0. Y entenderán cómo las variaciones cambiarias no tienen por qué ser un dolor de cabeza." |

---

### Bloque 2: EL NUEVO PARADIGMA — "Odoo 19.0 y el dominio del Costo Promedio"
**⏰ 00:07 – 00:15 (8 min)**

**Contenido:**
- **Foco absoluto en Costo Promedio (AVCO):** Por qué en esta masterclass ignoramos FIFO y Estándar. AVCO es el estándar de facto para el cumplimiento en México.
- **El Gran Cambio Arquitectónico** (6 min):
  - 🚫 **Adiós SVL** (Stock Valuation Layers) → La valoración ahora vive en los **Stock Moves**.
  - 🚫 **Adiós cuentas puente** (Stock Input/Output) → Menos asientos, contabilidad más limpia para el catálogo del SAT.
  - 🔄 **Adiós "Continental vs. Anglo-Sajona"** → Bienvenido **"Periódico vs. Perpetuo"**.
  - ✅ **Nuevo**: Interfaz guiada de cierre de periodo y menú *Accounting > Review > Inventory Valuation*.

---

### Bloque 3: BAJO EL CAPÓ — "Casos Prácticos en Vivo (AVCO + MXN)"
**⏰ 00:15 – 00:35 (20 min)**

> [!WARNING]
> **Preparación:** Flujos pre-configurados. El foco es la **vista de valoración y el asiento contable resultante** en MXN, usando cuentas mexicanas (1150, 5100).

**Caso 1: Distribución Pura (5 min)**
- Flujo de compra → recepción → venta → entrega (todo en MXN).
- Mostrar la afectación directa a la cuenta 1150 (Inventarios) y 5100 (Costo de Ventas).
- Comparar v18 vs 19.0: Menos asientos de diario, misma exactitud.

**Caso 2: Manufactura (MRP) (7 min)**
- Orden de producción completada con componentes en AVCO.
- Cómo fluye el valor hacia la cuenta WIP (Producción en Proceso) y la liquidación al terminar.
- *"El 80% de las empresas industriales en México pierden el control de su AVCO aquí."*

**Caso 3: EL CASO CRÍTICO - Importaciones (Compras en USD para Cía en MXN) (8 min)**
- Compañía con moneda base MXN.
- Compra a proveedor extranjero en USD.
- **La magia y el terror:** 
  1) PO confirmada con Tipo de Cambio (TC) del día 1.
  2) Recepción de mercancía con TC del día 15.
  3) Factura de proveedor recibida días después con TC del día 20 (y su respectivo CFDI / Pedimento).
- Cómo esto afecta o recalcula el **Costo Promedio (AVCO)** y qué asientos genera (diferencias cambiarias).

---

### Bloque 4: LA CLÍNICA DE LOS DESASTRES — "Los Errores que Cuestan Millones"
**⏰ 00:35 – 00:55 (20 min)**

> [!CAUTION]
> Bloque estrella. "Cicatrices de batalla" reales de implementaciones mexicanas.

**🔥 Desastre #1: Stock Negativo con AVCO (5 min)**
- Qué pasa cuando permites vender sin stock: el Costo Promedio se **corrompe de forma irreparable**.
- Demo: Producto con AVCO que se vende en negativo → costo unitario distorsionado.
- *"Si el SAT te audita un kardex con inventario negativo, es multa segura. En Odoo 19.0 esto se bloquea o audita diferente."*

**🔥 Desastre #2: El Desfase Cambiario en Recepciones vs Facturas (7 min)**
- El error común de registrar la factura del proveedor con un tipo de cambio radicalmente diferente al de la recepción de mercancía extranjera.
- El inventario se queda valorado con un costo que no corresponde a la realidad financiera.
- Diferencias Cambiarias (Ganancia/Pérdida) y su tratamiento.

**🔥 Desastre #3: Landed Costs (Gastos Aduanales y Fletes) (4 min)**
- Cómo prorratear correctamente los gastos de importación (pedimentos, agentes aduanales) al AVCO del producto.
- El error de aplicar un costo en destino a una factura no conciliada.

**🔥 Desastre #4: Implicaciones Fiscales ante el SAT (4 min)**
- Ajustes masivos de inventario a fin de año (o cambios de método de costeo erróneos) que generan **Ingresos Ficticios** o alteran el Costo de lo Vendido deducible.
- *"Un ajuste de revaloración no es solo contable — tiene un efecto directo en la declaración anual."*

---

### Bloque 5: EL "MOMENTO DE LA VERDAD" — Auditoría y Corrección
**⏰ 00:55 – 01:10 (15 min)**

**Auditoría en Vivo (8 min)**
- Uso del menú *Accounting > Review > Inventory Valuation*.
- Cruzar total de valoración contra la cuenta 1150 en la Balanza de Comprobación.
- Revisar la nueva interfaz guiada de cierre de periodo en 19.0.

**Resolución del Descuadre Inicial (4 min)**
- Resolver el hook del inicio: Encontrar un asiento contable manual indebido en la cuenta 1150 (Inventarios).
- Rastrearlo y corregirlo con los clics exactos.

**Reglas de Oro en México (3 min)**
- 🥇 Jamás permitir stock negativo en AVCO.
- 🥇 El "Cut-off" a fin de mes es innegociable antes del cierre contable (emisión de CFDI).
- 🥇 Cuidados estrictos con el Tipo de Cambio al momento de validar recepciones.

---

### Bloque 6: Q&A "HOT SEAT" — Consultoría en Vivo
**⏰ 01:10 – 01:30 (20 min)**

- Los asistentes exponen sus peores problemas de valoración (AVCO, importaciones, diferencias cambiarias).
- Julio responde aplicando la lógica de Odoo 19.0 (con demo rápida si aplica).
- Cierre: Links de los entregables y agradecimiento.

---

## 📋 Entregable #1: Checklist de Auditoría Logística-Contable (Odoo 19.0 MX)

*Documento en PDF (2 páginas) para ejecutarse en el cierre de mes.*

**1. Validaciones de Inventario (AVCO)**
- [ ] No existen productos con Stock Negativo (crítico para la exactitud del Costo Promedio).
- [ ] No hay productos con costo unitario = $0.00 (salvo muestras gratuitas documentadas).
- [ ] Todas las categorías de producto operan con "AVCO" y "Valoración Perpetua".

**2. Operaciones y Cierre (Localización MX)**
- [ ] Todos los Stock Moves de entrada/salida están en estado 'Done'.
- [ ] Las Órdenes de Producción cerraron correctamente sin saldos extraños en WIP.
- [ ] Todos los Costos en Destino (Gastos Aduanales / Pedimentos) fueron asignados al AVCO.
- [ ] Verificación de Tipo de Cambio: Los movimientos de entrada por compras en USD cuadran con los tipos de cambio de las facturas (o se registraron correctamente las diferencias cambiarias).

**3. Conciliación Contable en Odoo 19.0**
- [ ] Uso de *Inventory Valuation* para auditar diferencias.
- [ ] Saldo del Reporte de Valoración = Saldo de la cuenta 1150 (Balanza de Comprobación).
- [ ] Búsqueda de asientos manuales (pólizas directas) en la cuenta 1150.
- [ ] No existen saldos arrastrados de cuentas Interim/Puente (v18 o anterior).

---

## 📋 Entregable #2: Tabla de Mapeo Conceptual v18 → v19 (México)

| Concepto | Odoo ≤ 18 | Odoo 19.0 | Impacto Fiscal/Contable (MX) |
|----------|-----------|-----------|------------------------------|
| **Capa de Valoración** | Stock Valuation Layers | Directo en Stock Moves | Más fácil rastrear el origen del AVCO por póliza |
| **Cuentas Contables** | Interim (Input/Output) | Directo (1150 / Proveedores) | Balanza de comprobación más limpia |
| **Cierre de Periodo** | Manual/Scripts | Interfaz Guiada | Bloquea movimientos logísticos fuera de tiempo |
| **Reportes** | Dispersos | Centralizados | Menos tiempo en la auditoría mensual del SAT |

---

## 🎬 Preparación Pre-Masterclass (Checklist del Ponente)

- [ ] **Instancia:** Odoo 19.0 con Localización Mexicana (MXN base).
- [ ] **Plan Contable:** Cuentas 1150, 5100, diferencias cambiarias.
- [ ] **Demos Pre-cargadas (Críticas):**
  - Orden de Compra en USD → Recepción (TC1) → Factura Proveedor (TC2) para mostrar impacto en AVCO.
  - Orden de Producción terminada con componentes AVCO.
  - Asiento manual intruso en cuenta 1150 para la demo del "Momento de la verdad".
  - Producto corrompido intencionalmente por stock negativo.
