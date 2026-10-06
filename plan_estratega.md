# Plan Maestro: De la logística a la contabilidad: Domina la valoración de inventarios en Odoo 19.0

**Ponente:** Julio Serna, Project Manager y Experto Funcional en Vauxoo
**Duración:** 90 Minutos (1:30 hrs)
**Formato:** Virtual, en vivo
**Precio:** $100 USD

---

## 💎 Propuesta de Valor Premium (Justificación de Precio)
Este no es un tutorial de "cómo configurar" Odoo que se pueda encontrar en YouTube. Es una masterclass de **arquitectura de datos, resolución de problemas y transición estratégica a Odoo 19.0**. El valor de $100 USD se justifica porque resolver un problema de valoración mal configurado o una auditoría fallida cuesta a las empresas miles de dólares en consultoría. Aquí se entrega el conocimiento de trinchera que normalmente se reserva para implementaciones Enterprise complejas.

---

## ⏱️ Cronograma Minuto a Minuto (90 Minutos)

### 00:00 - 00:05 | El Hook y Promesa (5 min)
**Contenido:**
- Bienvenida de Julio Serna.
- **Hook:** Mostrar un Balance General descuadrado con la cuenta de inventario vs. el reporte de valoración. Preguntar en el chat: *"¿A cuántos les ha dado dolores de cabeza esto en fin de mes?"*
- Promesa de la sesión: Al salir, no solo entenderán por qué ocurre, sino cómo aprovechar la nueva arquitectura de Odoo 19.0 para que la logística hable el mismo idioma que la contabilidad.

**Justificación de Diseño:** Empezar con el "dolor" real captura la atención inmediata de financieros y logísticos. Rompe el hielo y justifica la inversión desde el minuto 1.

### 00:05 - 00:15 | 1. ¿Qué es realmente la valoración de inventario en Odoo 19.0? (10 min)
**Contenido:**
- Breve repaso conceptual: FIFO, AVCO, Standard (integrados en el nuevo framework).
- **El Gran Cambio (Odoo 19.0):** Despedida a la nomenclatura "Continental vs. Anglo-Sajona". Bienvenido "Periódico vs. Perpetuo".
- Por qué Odoo eliminó las SVL (Stock Valuation Layers) y ahora almacena la valoración directamente en los *Stock Moves*.
- **Impacto:** Menos asientos contables, base de datos más limpia, pero requiere una comprensión diferente al auditar.

**Justificación de Diseño:** Establece la base teórica pero rápidamente pivota hacia las novedades de la versión 19.0, demostrando conocimiento de vanguardia (exclusivo y actualizado).

### 00:15 - 00:35 | 2. ¿Cómo funciona bajo el capó? (20 min)
**Contenido:**
- **Flujo en Vivo:** Demostración de una compra y una venta.
- Adiós a las cuentas puente (Interim Accounts): Mostrar cómo la versión 19.0 simplifica el flujo sin cuentas de entrada/salida de stock.
- El nuevo menú de Valoración: *Accounting > Review > Inventory Valuation*.
- **Caso Real:** El impacto de transferencias con fecha retroactiva (Back-dating transfers), una función nueva y crítica, y cómo afecta los saldos.

**Justificación de Diseño:** La demostración en vivo de Odoo 19.0 aporta valor táctico. El caso de "back-dating" es un escenario avanzado que causa confusión si no se domina.

### 00:35 - 00:50 | 3. Detectando problemas: Errores comunes en implementaciones (15 min)
**Contenido:**
- **Pitfall #1:** Productos mal categorizados (categorías mixtas o cambios de método de costeo en caliente sin el ajuste correcto).
- **Pitfall #2:** Costos de aterrizaje (Landed Costs) mal aplicados a facturas no conciliadas.
- **Pitfall #3:** El abismo de la migración. Riesgos al pasar histórico a Odoo 19.0 por la falta de SVLs.

**Justificación de Diseño:** Aquí es donde el rol de "Experto de Vauxoo" brilla. Compartir "cicatrices de batalla" y errores que cuestan dinero da un valor inmenso.

### 00:50 - 01:05 | 4. Auditoría Logística-Contable y el Checklist (15 min)
**Contenido:**
- Presentación de la nueva interfaz guiada de cierre de periodo en Odoo 19.0.
- Cómo usar el menú de revisión de valoración para cruzar con contabilidad.
- **Interactivo:** Lanzamiento de una encuesta (Poll) sobre el mayor reto de auditoría de la audiencia.
- Revelación guiada del **Checklist Entregable** (Ver estructura abajo).

**Justificación de Diseño:** Convertir la auditoría de una tarea aburrida a un proceso sistemático mediante el checklist, otorgando una herramienta accionable al día siguiente.

### 01:05 - 01:15 | 5. Correcciones y Revaloración en la Trinchera (10 min)
**Contenido:**
- ¿Qué hacer cuando el costo promedio se corrompe por un error humano?
- Cómo usar la herramienta de ajuste de inventario y revaloración en Odoo 19.0.
- Efectos contables de un ajuste de inventario.

**Justificación de Diseño:** Respuestas a la pregunta de pánico: "Ya me equivoqué, ¿cómo lo arreglo?".

### 01:15 - 01:20 | 6. Buenas Prácticas (5 min)
**Contenido:**
- Permisos estrictos para cambios de fecha (Back-dating).
- Definición clara del "Cut-off" a fin de mes.
- Uso del entorno de Staging (Pruebas) para migraciones de saldos.

**Justificación de Diseño:** Cierre magistral con reglas de oro, posicionando a Julio como líder de pensamiento.

### 01:20 - 01:30 | Q&A y Cierre (10 min)
**Contenido:**
- Resolución de dudas complejas en vivo.
- Agradecimiento y mención sobre cómo acceder a la grabación y certificado.

**Justificación de Diseño:** El Q&A en vivo es clave para justificar eventos sincrónicos de alto ticket.

---

## 📋 Estructura del Entregable: Checklist de Auditoría Logística-Contable (Odoo 19.0)

Este PDF interactivo de 1-2 páginas se diseña para que el equipo financiero y de almacén lo ejecuten cada fin de mes.

**SECCIÓN 1: Validaciones Previas al Cierre**
- [ ] ¿Están todos los *Stock Moves* de entrada y salida procesados en estado 'Done'?
- [ ] ¿Hay albaranes atrasados (Backlog)? (Revisión de Back-dating controls).
- [ ] ¿Se han registrado todos los Costos en Destino (Landed Costs) del periodo?

**SECCIÓN 2: Conciliación Odoo 19.0**
- [ ] Revisión del menú *Accounting > Review > Inventory Valuation*.
- [ ] Cruce del total de Valoración de Inventario contra el saldo de la cuenta de Activo de Inventario en el Balance de Prueba. (Nota Odoo 19.0: Ya no se revisan cuentas Interim).
- [ ] Validación de la nueva interfaz guiada de cierre: ¿Hay advertencias de movimientos pendientes?

**SECCIÓN 3: Detección de Anomalías**
- [ ] Buscar productos con costo unitario = $0.00 o negativo (si se permite).
- [ ] Revisión de asientos manuales no generados por el sistema en las cuentas de inventario.
- [ ] Validación de Categorías de Producto (Confirmar que Método de Costeo y Valoración de Inventario (Periódico/Perpetuo) no fueron alterados sin procedimiento de ajuste).

**SECCIÓN 4: Migración y Datos Históricos (Para clientes en transición a 19.0)**
- [ ] Mapeo de balances migrados (Stock Moves vs. viejos SVLs).

---

## 🎯 Elementos PREMIUM para la audiencia
1. **Material Exclusivo:** El análisis del cambio de arquitectura (Adiós SVL y Cuentas Interim) de Odoo 19.0 no está documentado profundamente en foros públicos aún.
2. **Autoridad de Vauxoo:** Casos reales (Back-dating impact y Migraciones) que solo consultores Gold Partners ven.
3. **El Checklist:** Una herramienta de consultoría "empaquetada" que ahorra horas de auditoría a los asistentes, con valor residual enorme.
