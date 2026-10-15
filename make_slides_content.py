#!/usr/bin/env python3
# Content for all slides of the Masterclass 2026
# Aligned strictly with masterclass-plan-final.md v7
# Catálogo: Hardware & Cómputo (100% Unidades Enteras · Cero NIF · Cero Landed Costs)


def get_slides(doodle_oval, doodle_arrow, doodle_underline, logo_white, logo_light):
    return [
        # Slide 1: Portada Oficial
        {
            "id": 1,
            "title": "Portada Oficial",
            "bg": "gradient",
            "time": "00:00",
            "block": "Apertura",
            "notes": "Bienvenida de Julio Serna (PM y Experto Funcional en Vauxoo). Masterclass 2026 de Vauxoo Academy. Reglas de la sesión: 90 minutos enfocados en la sincronía contable y logística en Odoo 19.0 Enterprise.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-logo-wrap">
                {logo_white}
              </div>
              <div class="cover-badge-row">
                <span class="pill-badge">MASTERCLASS 2026</span>
                <span class="pill-badge-outline">ODOO 19.0 ENTERPRISE · MÉXICO</span>
                <span class="pill-badge-outline">90 MINUTOS ESTRICTOS</span>
              </div>
              <h1 class="cover-title">
                De la Logística a la Contabilidad:
                <span class="doodle-wrap">
                  Domina la Valoración de Inventarios
                  {doodle_underline}
                </span>
                en Odoo 19.0
              </h1>
              <div class="cover-footer" style="margin-top: 40px;">
                <div class="speaker-card">
                  <div class="speaker-avatar">JS</div>
                  <div class="speaker-info">
                    <span class="speaker-name">Julio Serna</span>
                    <span class="speaker-role">Project Manager & Experto Funcional en Vauxoo</span>
                  </div>
                </div>
                <div class="cover-price-tag">
                  <span class="price-val">$100 USD</span>
                  <span class="price-label">Acceso Total · Grabación HD · Entregables</span>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 2: El Hook - Descuadre de $482,190 MXN
        {
            "id": 2,
            "title": "El Hook: Descuadre de $482,190 MXN",
            "bg": "white",
            "time": "00:01 - 00:04",
            "block": "Bloque 1",
            "notes": "Mostrar el split view en vivo en Odoo 19: Balanza 115.01.01 ($821,100.00 MXN) vs Reporte de Existencias ($338,910.00 MXN) -> Descuadre real de $482,190.00 MXN ($487k de póliza manual + $4,810 de descuadres operativos). Plantear el dolor de todo cierre contable.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 1 · 00:00 - 00:09</span>
                  <h2 class="slide-title">El Dolor que Todos Conocen (Caso Real en Vivo)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Cierre contable de mes. Dos reportes oficiales en la misma base de datos arrojando datos incompatibles:</p>
              
              <div class="split-audit-container">
                <div class="audit-col audit-contable">
                  <div class="audit-col-badge">Módulo de Contabilidad</div>
                  <h3 class="audit-col-title">Balanza de Comprobación</h3>
                  <div class="audit-code">Cuenta 115.01.01 · Mercancías en Almacén</div>
                  <div class="audit-amount">$821,100.00 MXN</div>
                  <div class="audit-detail">Saldo deudor contable al corte mensual</div>
                  <div class="audit-status audit-err">⚠️ Generado por libro mayor contable</div>
                </div>

                <div class="audit-vs">
                  <div class="audit-diff-card">
                    <span class="diff-label">DESCUADRE REAL</span>
                    <span class="diff-amount doodle-wrap">
                      $482,190.00 MXN
                      {doodle_oval}
                    </span>
                    <span class="diff-warn">¿Cómo conciliar esta brecha en el cierre?</span>
                  </div>
                </div>

                <div class="audit-col audit-logistica">
                  <div class="audit-col-badge">Módulo de Inventario</div>
                  <h3 class="audit-col-title">Reporte de Existencias / Valoración</h3>
                  <div class="audit-code">Valoración de Stock (Valuation)</div>
                  <div class="audit-amount">$338,910.00 MXN</div>
                  <div class="audit-detail">Valoración real de los productos en almacén</div>
                  <div class="audit-status audit-ok">📦 Generado por Stock Moves físicos</div>
                </div>
              </div>

              <div class="interactive-chat-prompt" style="background:#F1F5F9; border:1px solid #CBD5E1;">
                <span class="prompt-icon">💡</span>
                <span class="prompt-text" style="color:#1E293B;">
                  <strong>El objetivo de la sesión:</strong> Identificar el origen exacto de esta diferencia de $482,190 MXN ($487,000 de parche manual + $4,810 de fallas de operación) y resolverla en vivo durante la clase.
                </span>
              </div>
            </div>
            '''
        },

        # Slide 3: Las 3 Causas Recurrentes del Divorcio
        {
            "id": 3,
            "title": "Las 3 Causas Recurrentes del Divorcio",
            "bg": "white",
            "time": "00:04 - 00:07",
            "block": "Bloque 1",
            "notes": "Explicar por qué ocurre este divorcio contable a partir de los 3 frentes reales: 1. Configuración errática (Fase 0); 2. Parches operativos manuales; 3. Ceguera de auditoría por falta de cadencia.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 1 · 00:00 - 00:09</span>
                  <h2 class="slide-title">Las 3 Causas Recurrentes del Divorcio Almacén-Contabilidad</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">La experiencia en implementaciones demuestra que el descuadre nace de 3 fuentes principales:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(3, 1fr);">
                <div class="agenda-card" style="border-top: 4px solid #1E293B;">
                  <div class="agenda-time">FASE 0 · CONFIGURACIÓN</div>
                  <div class="agenda-num">01</div>
                  <div class="agenda-title">CONFIGURACIÓN ERRÁTICA</div>
                  <p class="agenda-desc"><strong>"Dos malas no hacen una buena."</strong> Cambiar métodos en caliente, compras en divisa sin tasa oficial o saldos iniciales huérfanos.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">OPERACIÓN</div>
                  <div class="agenda-num">02</div>
                  <div class="agenda-title">PARCHES OPERATIVOS</div>
                  <p class="agenda-desc"><strong>"La aspirina manual."</strong> Pólizas manuales para 'cuadrar', alterar costos a mano en la ficha o forzar despachos en stock negativo.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #475569;">
                  <div class="agenda-time">CONTROL</div>
                  <div class="agenda-num">03</div>
                  <div class="agenda-title">CEGUERA DE AUDITORÍA</div>
                  <p class="agenda-desc"><strong>"El costo de la infrecuencia."</strong> Esperar al cierre anual cuando hay miles de movimientos acumulados hace que conciliar sea una pesadilla de semanas.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 4: Matriz de Cadencia de Auditoría & Encuesta al Chat
        {
            "id": 4,
            "title": "Matriz de Cadencia de Auditoría",
            "bg": "gradient",
            "time": "00:06 - 00:09",
            "block": "Bloque 1",
            "notes": "Lanzar la encuesta al chat: ¿Cada cuánto auditan el inventario contable contra el almacén? Mostrar la Matriz de Cadencia Vauxoo (Diario, Semanal, Mensual, Anual).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">ENCUESTA AL CHAT · CADENCIA DE CONTROL</span>
                  <h2 class="slide-title" style="color: #fff;">¿Cada Cuánto Auditan Contabilidad vs Almacén?</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                La frecuencia con la que se concilia el inventario determina el tiempo, esfuerzo y costo de resolver las diferencias:
              </p>
              
              <div class="cadencia-table-container">
                <table class="cadencia-table" style="background:rgba(255,255,255,0.06); color:#fff;">
                  <thead>
                    <tr style="background:#1E293B;">
                      <th>Frecuencia</th>
                      <th>Calificación</th>
                      <th>Esfuerzo de Revisión</th>
                      <th>Impacto Operativo en el Negocio</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Diaria</strong></td>
                      <td>⭐⭐⭐⭐⭐ <span class="pill-badge" style="background:#16A34A;">EXCELENTE</span></td>
                      <td>2 a 5 minutos</td>
                      <td>Detección inmediata al vuelo; 1-2 movimientos; cero sorpresas a fin de mes.</td>
                    </tr>
                    <tr>
                      <td><strong>Semanal</strong></td>
                      <td>⭐⭐⭐⭐ <span class="pill-badge" style="background:#0D9488;">RECOMENDADO</span></td>
                      <td>15 minutos</td>
                      <td>Fricción mínima; máximo 10 movimientos sospechosos por revisar.</td>
                    </tr>
                    <tr>
                      <td><strong>Mensual</strong></td>
                      <td>⭐⭐⭐ <span class="pill-badge" style="background:#3B82F6;">BUENO</span></td>
                      <td>1 a 2 horas</td>
                      <td>Estándar indispensable para el cierre formal y reporte contable gerencial.</td>
                    </tr>
                    <tr>
                      <td><strong>Anual</strong></td>
                      <td>❌ <span class="pill-badge" style="background:#B91C1C;">EVITARLO A TODA COSTA</span></td>
                      <td>Semanas de reconstrucción</td>
                      <td>Miles de movimientos acumulados; rastreo prácticamente imposible y desgaste severo.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            '''
        },

        # Slide 5: Bloque 2 - ¿Por qué Odoo 19.0?
        {
            "id": 5,
            "title": "¿Por qué Odoo 19.0 para esta Masterclass?",
            "bg": "white",
            "time": "00:09 - 00:13",
            "block": "Bloque 2",
            "notes": "Explicar las 4 grandes razones arquitectónicas de Odoo 19: sin SVL (en stock.move), sin cuentas interim en flujos directos, terminología Formal Periódico/Perpetuo, auditoría visual inmediata en Informes > Inventario.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 2 · 00:09 - 00:17</span>
                  <h2 class="slide-title">Odoo 19.0: La Gran Simplificación de la Auditoría</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Por qué elegimos la versión 19.0 para esta masterclass: auditoría 10 veces más fácil, visual y limpia:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(2, 1fr); gap: 20px;">
                <div class="agenda-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">ARQUITECTURA</div>
                  <div class="agenda-title">Adiós Capas SVL Paralelas</div>
                  <p class="agenda-desc">En versiones previas, una tabla separada (SVL) se desincronizaba. En Odoo 19 la valoración vive <strong>directamente en cada movimiento de stock (<code>stock.move</code>)</strong>.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #1E293B;">
                  <div class="agenda-time">CONTABILIDAD</div>
                  <div class="agenda-title">Adiós Cuentas Puente Interim</div>
                  <p class="agenda-desc">En flujos directos desaparecen las cuentas intermedias de tránsito. El apunte contable va limpio y directo a la cuenta 1150 de Inventario.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #0D9488;">
                  <div class="agenda-time">ESTÁNDAR</div>
                  <div class="agenda-title">Terminología Periódico vs Perpetuo</div>
                  <p class="agenda-desc">Se elimina la ambigüedad anglosajona/continental. Odoo adopta la formalidad contable estándar para inventario permanente.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #3B82F6;">
                  <div class="agenda-time">AUDITORÍA VISUAL</div>
                  <div class="agenda-title">Trazabilidad en 1 Clic</div>
                  <p class="agenda-desc">El nuevo menú en <em>Contabilidad > Informes > Inventario</em> conecta cada póliza contable con su albarán físico correspondiente de forma bidireccional.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 6: Bloque 2 - Tranquilidad para v16, v17 y v18
        {
            "id": 6,
            "title": "¿Y si mi empresa está en Odoo 16, 17 o 18?",
            "bg": "white",
            "time": "00:13 - 00:17",
            "block": "Bloque 2",
            "notes": "Mensaje de tranquilidad: la lógica de Costo Promedio (AVCO), la valoración perpetua y el cuadre balanza vs existencias son idénticos. La diferencia es que en v19 es más visual y directo.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#1E293B;">BLOQUE 2 · TRANQUILIDAD</span>
                  <h2 class="slide-title">¿Y si Mi Empresa Está en Odoo 16, 17 o 18?</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead"><strong>Respiren tranquilos: esta masterclass es 100% aplicable para ustedes.</strong></p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card" style="border-left: 4px solid #16A34A;">
                  <div class="card-pill" style="color:#16A34A;">LÓGICA CONTABLE UNIVERSAL</div>
                  <h3>Las Matemáticas No Cambian</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li><strong>Fórmula de Costo Promedio (AVCO):</strong> Idéntica en todas las versiones de Odoo.</li>
                      <li><strong>Inventario Perpetuo:</strong> El reconocimiento de salida contable por cada entrega sigue la misma lógica de negocio.</li>
                      <li><strong>Principio de Cuadre:</strong> Saldo deudor en Balanza (1150) = Valor total en reporte de existencias.</li>
                    </ul>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">LA DIFERENCIA TÉCNICA</div>
                  <h3>Odoo 19 'Limpió la Casa'</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li><strong>En v16–v18:</strong> La valoración estaba detrás de capas intermedias y cuentas puente que hacían el rastreo más laborioso.</li>
                      <li><strong>En v19:</strong> Todo está integrado y expuesto de forma transparente para el auditor.</li>
                      <li><strong>Beneficio hoy:</strong> Lo aprendido les permite sanear su Odoo actual y los prepara para una migración limpia.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 7: Bloque 3 - Operación Normal Paso 1 (Compra Limpia MXN)
        {
            "id": 7,
            "title": "Operación Normal: Compra Progresiva en MXN",
            "bg": "white",
            "time": "00:17 - 00:25",
            "block": "Bloque 3",
            "notes": "Mostrar la compra progresiva y el cálculo ponderado en Odoo 19 con [TECL-INAL-USB]. 50 u @ $150 + 50 u @ $170 = 100 u @ $160 MXN. Cuenta 1150 suma $16,000 MXN.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 1</span>
                  <h2 class="slide-title">Operación Normal: Compra Progresiva y Ponderación AVCO</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[TECL-INAL-USB] Teclado Ergonómico Inalámbrico</code>. Ponderación limpia en tiempo real:</p>
              
              <div class="flow-steps-grid" style="grid-template-columns: repeat(3, 1fr);">
                <div class="flow-step-card">
                  <div class="step-badge">RECEPCIÓN 1 (PO 1)</div>
                  <h4>Primera Compra</h4>
                  <p>50 unidades @ $150.00 MXN</p>
                  <div class="asiento-box">
                    Subtotal: <strong>$7,500.00 MXN</strong><br>
                    AVCO Inicial: <strong>$150.00 MXN</strong>
                  </div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">RECEPCIÓN 2 (PO 2)</div>
                  <h4>Segunda Compra (Precio Mayor)</h4>
                  <p>50 unidades @ $170.00 MXN</p>
                  <div class="asiento-box">
                    Subtotal: <strong>$8,500.00 MXN</strong><br>
                    Valor añadido en entrada física
                  </div>
                </div>

                <div class="flow-step-card" style="border: 2px solid var(--rojo-vauxoo);">
                  <div class="step-badge" style="background:var(--rojo-vauxoo); color:#fff;">PONDERACIÓN ODOO 19</div>
                  <h4>Nuevo Costo Promedio</h4>
                  <div class="asiento-box">
                    (50&times;150 + 50&times;170) / 100 =<br>
                    <strong style="color:var(--rojo-vauxoo); font-size:1.15rem;">$160.00 MXN / pieza</strong>
                  </div>
                  <div class="step-avco">Total Activo en Almacén: 100 u = <strong>$16,000.00 MXN</strong></div>
                </div>
              </div>

              <div class="interactive-chat-prompt" style="background:#F8FAFC; border:1px solid #E2E8F0; margin-top:24px;">
                <span class="prompt-icon">📊</span>
                <span class="prompt-text">
                  <strong>Asiento contable limpio:</strong> Cargo directo a la cuenta <code>115.01.01 Inventario</code> por <strong>$16,000.00 MXN</strong> sin cuentas puente intermedias.
                </span>
              </div>
            </div>
            '''
        },

        # Slide 8: Bloque 3 - Operación Normal Paso 2 (Venta y Costo de Ventas)
        {
            "id": 8,
            "title": "Operación Normal: Venta y Costo de Ventas",
            "bg": "white",
            "time": "00:25 - 00:30",
            "block": "Bloque 3",
            "notes": "Mostrar el pedido de venta S00001, entrega física de 30 piezas y factura con Costo de Ventas ($4,800 MXN). Cuadre perfecto: 70 u en existencias = $11,200 MXN en la 1150.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 1 (PARTE 2)</span>
                  <h2 class="slide-title">Venta, Entrega Física y Registro del Costo de Ventas</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Completando el ciclo comercial en moneda nacional: despacho físico y asiento automático de costo:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">OPERACIÓN COMERCIAL (S00001)</div>
                  <h3>Venta y Entrega de 30 Unidades</h3>
                  <div class="detail-box">
                    <p>Almacén valida la salida. Odoo descarga 30 piezas al costo promedio vigente ($160.00 MXN).</p>
                    <div class="asiento-box" style="margin-top:12px;">
                      <div class="asiento-row"><span class="cargo">CARGO</span> 501.01.01 Costo de Ventas: <strong>$4,800.00 MXN</strong></div>
                      <div class="asiento-row"><span class="abono">ABONO</span> 115.01.01 Inventario: <strong>$4,800.00 MXN</strong></div>
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card" style="border: 2px solid #16A34A;">
                  <div class="card-pill" style="color:#16A34A;">SINCRONIZACIÓN PERFECTA</div>
                  <h3>Cuadre de Cierre Inmediato</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li><strong>En Almacén Físico:</strong> Quedan 70 piezas @ $160 = <strong>$11,200.00 MXN</strong>.</li>
                      <li><strong>En el Libro Mayor (115.01.01):</strong> Saldo deudor de <strong>$11,200.00 MXN</strong>.</li>
                      <li><strong>Diferencia:</strong> $0.00 MXN. Sincronía contable y logística total.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 9: Bloque 3 - Operación Normal en USD (Monitor 4K)
        {
            "id": 9,
            "title": "Operación Normal: Compra de Importación en USD",
            "bg": "white",
            "time": "00:30 - 00:37",
            "block": "Bloque 3",
            "notes": "Mostrar la compra en USD con [MON-27-4K]. 20 u @ 100 USD. Odoo fija el costo contable con el TC del día de recepción física ($18.50 = $1,850 MXN). Total $37,000 MXN.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 2</span>
                  <h2 class="slide-title">Compra de Importación en USD: La Fecha de Recepción Manda</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[MON-27-4K] Monitor Profesional 27" 4K</code>. Impacto del Tipo de Cambio:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">ORDEN DE COMPRA & FACTURA</div>
                  <h3>Orden en $100.00 USD</h3>
                  <div class="detail-box">
                    <p>La orden se pacta con el proveedor internacional en $100 USD por monitor. El mito común cree que la fecha de la OC o de la factura fija el costo.</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      20 monitores &times; $100 USD = <strong>$2,000.00 USD</strong>
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card" style="border: 2px solid #345D90;">
                  <div class="card-pill" style="color:#345D90;">RECEPCIÓN FÍSICA EN ALMACÉN</div>
                  <h3>El Tipo de Cambio del Día Fija el Costo</h3>
                  <div class="detail-box">
                    <p>Al recibir en bodega, Odoo toma automáticamente el Tipo de Cambio oficial del DOF ($18.50 MXN/USD):</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      $100.00 USD &times; $18.50 = <strong>$1,850.00 MXN / pieza</strong><br>
                      Total Activo en Almacén: <strong>$37,000.00 MXN</strong>
                    </div>
                    <div class="vauxoo-rule-badge" style="margin-top:10px;">REGLA VAUXOO: El costo contable lo define la recepción física, no la OC ni la factura.</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 10: Bloque 4 - La Clínica de Desastres (5 Casos)
        {
            "id": 10,
            "title": "La Clínica de Desastres: 5 Errores Reales",
            "bg": "white",
            "time": "00:37 - 00:40",
            "block": "Bloque 4",
            "notes": "Introducir la clínica de 5 desastres reales probados en laboratorio: 1. Ajuste sin cuenta; 2. Producto archivado; 3. Error de divisa (MXN en USD); 4. Costo manual en ficha; 5. Stock negativo.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">BLOQUE 4 · 00:37 - 00:53</span>
                  <h2 class="slide-title">La Clínica de Desastres: 5 Errores que Cuestan Millones</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Los 5 desvíos operativos y de configuración más comunes en empresas mexicanas:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(3, 1fr); gap: 16px;">
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">ERROR #1 · CONFIGURACIÓN</div>
                  <div class="agenda-title">Ajuste sin Póliza Contable</div>
                  <p class="agenda-desc"><strong>Mouse Óptico:</strong> Conteo inicial en categoría periódica; las piezas entran a bodega pero la cuenta 1150 queda vacía ($8,500).</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">ERROR #2 · CATÁLOGO</div>
                  <div class="agenda-title">Archivado con Existencias</div>
                  <p class="agenda-desc"><strong>Router Legacy:</strong> Archivar para "limpiar catálogo" mientras tiene saldo; borrado en almacén pero vivo en Balanza ($2,400).</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">ERROR #3 · OPERACIÓN</div>
                  <div class="agenda-title">Error de Moneda en Compra</div>
                  <p class="agenda-desc"><strong>Cámara Web:</strong> Costo de $1,500 MXN capturado como $1,500 USD en la OC; al recibir a TC 18.50 se infla a $27,750 MXN ($277.5k).</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">ERROR #4 · PARCHE</div>
                  <div class="agenda-title">Costo Manual en Ficha</div>
                  <p class="agenda-desc"><strong>Memoria RAM:</strong> Editar a mano el costo en el formulario ($100 a $121); el almacén sube a $1,210 pero contabilidad queda en $1,000 ($210).</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">ERROR #5 · DESPACHO</div>
                  <div class="agenda-title">Stock Negativo Forzado</div>
                  <p class="agenda-desc"><strong>Disco SSD:</strong> Salida urgente en 0 a costo viejo ($200) y compra posterior a $350; costo deducible perdido y balance inflado ($1,500).</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #1E293B; background:#F8FAFC;">
                  <div class="agenda-time">EL PARCHE DE CIERRE</div>
                  <div class="agenda-title">La Póliza Manual del Hook</div>
                  <p class="agenda-desc"><strong>El Parche:</strong> El contador inyecta una póliza de $487,000 MXN directa a la 1150 sin SKU para forzar el balance general.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 11: Desastres 1 y 2 (Mouse y Router)
        {
            "id": 11,
            "title": "Desastres 1 y 2: Ajuste Huérfano y Producto Archivado",
            "bg": "white",
            "time": "00:40 - 00:44",
            "block": "Bloque 4",
            "notes": "Detalle del Desastre 1 (Mouse Óptico) y Desastre 2 (Router Wi-Fi 4 Legacy). Explicar por qué ocurren y cómo se evidencian en el sistema.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA · CASOS 1 Y 2</span>
                  <h2 class="slide-title">Ajustes Huérfanos y Productos Archivados con Saldo</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">CASO 1 · MOUSE ÓPTICO (MOUS-OPT-USB)</div>
                  <h3>Ajuste Físico sin Respaldo Contable</h3>
                  <div class="detail-box">
                    <p>Se realiza un ajuste inicial de 100 piezas físicas cuando la categoría operaba en valoración periódica o sin cuenta de ajuste asignada.</p>
                    <ul class="styled-list">
                      <li><strong>En Almacén:</strong> 100 mouses @ $85 = <strong>$8,500.00 MXN</strong>.</li>
                      <li><strong>En Contabilidad:</strong> <strong>$0.00 MXN</strong> (cero pólizas generadas).</li>
                      <li><strong>Diagnóstico:</strong> Valor no reconocido que genera una brecha silenciosa.</li>
                    </ul>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid #B91C1C;">
                  <div class="card-pill" style="color:#B91C1C;">CASO 2 · ROUTER LEGACY (ROUT-WIFI4-LEG)</div>
                  <h3>El Peligro de Archivar con Existencias</h3>
                  <div class="detail-box">
                    <p>Se compra y factura un lote de routers por $2,400 MXN. Para "limpiar" el catálogo, el usuario hace clic en <strong>Archivar</strong>.</p>
                    <ul class="styled-list">
                      <li><strong>En Reporte de Almacén:</strong> <strong>$0.00 MXN</strong> (el filtro oculta inactivos).</li>
                      <li><strong>En Balanza de Comprobación:</strong> <strong>$2,400.00 MXN</strong> vivos.</li>
                      <li><strong>Diagnóstico:</strong> Saldo contable fantasma imposible de cuadrar a simple vista.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 12: Desastres 3 y 4 (Cámara Web y Memoria RAM)
        {
            "id": 12,
            "title": "Desastres 3 y 4: Error de Moneda y Costo Manual en Ficha",
            "bg": "white",
            "time": "00:44 - 00:48",
            "block": "Bloque 4",
            "notes": "Detalle del Desastre 3 (Cámara Web con error de moneda USD) y Desastre 4 (Memoria RAM con costo cambiado a mano).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA · CASOS 3 Y 4</span>
                  <h2 class="slide-title">Error de Moneda y Costo Alterado a Mano en Ficha</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">CASO 3 · CÁMARA WEB (CAM-WEB-4K)</div>
                  <h3>La Trampa de la Divisa en la OC</h3>
                  <div class="detail-box">
                    <p>Un producto de $1,500.00 MXN es comprado por error en una orden en <strong>USD</strong> capturando 1,500 USD por pieza:</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      10 unidades &times; 1,500 USD @ TC $18.50 =<br>
                      <strong>Costo unitario Odoo: $27,750.00 MXN</strong><br>
                      Total Activo Inflado: <strong>$277,500.00 MXN</strong> ($262.5k de sobrecosto).
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid #B91C1C;">
                  <div class="card-pill" style="color:#B91C1C;">CASO 4 · MEMORIA RAM (MEM-RAM-16GB)</div>
                  <h3>Cambio Manual de Coste en Formulario</h3>
                  <div class="detail-box">
                    <p>Compra real de 10 u @ $100 MXN ($1,000 MXN en la 1150). El usuario edita el campo <em>Coste</em> en la ficha a mano de $100 a $121 MXN.</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      Almacén recalcula: 10 &times; $121 = <strong>$1,210.00 MXN</strong><br>
                      Contabilidad 1150: Se queda en <strong>$1,000.00 MXN</strong><br>
                      <strong style="color:#B91C1C;">Descuadre silencioso: -$210.00 MXN sin póliza.</strong>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 13: Desastre 5 (Disco SSD - Stock Negativo)
        {
            "id": 13,
            "title": "Desastre 5: Stock Negativo con Compra Posterior",
            "bg": "white",
            "time": "00:48 - 00:53",
            "block": "Bloque 4",
            "notes": "Detalle del Desastre 5 (Disco SSD 1TB). Explicar por qué vender en negativo fractura el AVCO y cómo deja $1,500 flotando en el balance.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA · CASO 5</span>
                  <h2 class="slide-title">Stock Negativo: La Fractura del Costo de Ventas</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[DISC-SSD-1TB] Disco Sólido SSD NVMe 1TB</code>. Despachar antes de recibir compra:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">DESPACHO URGENTE EN EXISTENCIA 0</div>
                  <h3>Salida a Costo Desfasado</h3>
                  <div class="detail-box">
                    <p>Se entregan 10 discos cuando había 0 existencias. Odoo descarga a costo provisional ($200 MXN = $2,000 MXN costo ventas).</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      Días después: Se valida la compra de 20 discos a <strong>$350.00 MXN</strong> ($7,000 MXN en factura).
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">EL LIMBO CONTABLE</div>
                  <h3>Autopsia de la Brecha</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li>Los 10 discos consumidos costaron en realidad $3,500 pero en libros solo se dedujeron $2,000.</li>
                      <li><strong>En Almacén Físico:</strong> Quedan 10 discos @ $350 = <strong>$3,500.00 MXN</strong>.</li>
                      <li><strong>En Balanza (1150):</strong> Saldo deudor de <strong>$5,000.00 MXN</strong> ($7,000 compra - $2,000 costo).</li>
                      <li><strong style="color:var(--rojo-vauxoo);">Brecha: +$1,500.00 MXN en el limbo</strong> (balance inflado y deducción perdida).</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 14: Bloque 5 - Metodología de Auditoría SKU por SKU
        {
            "id": 14,
            "title": "Metodología de Auditoría SKU por SKU",
            "bg": "white",
            "time": "00:53 - 01:00",
            "block": "Bloque 5",
            "notes": "Intro de Julio Serna en Bloque 5. Regla de oro: NUNCA auditar solo totales consolidados. Los errores se compensan (+/-). La conciliación SOLO es real si cada SKU tiene diferencia cero. Presentar la fórmula y la Acción de Servidor.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · 00:53 - 01:07</span>
                  <h2 class="slide-title">Metodología de Auditoría Forense: SKU por SKU</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div style="display:grid; grid-template-columns: 1.15fr 0.95fr; gap: 14px; margin-bottom: 16px;">
                <div class="interactive-chat-prompt" style="background:#FFFBEB; border:1px solid #FCD34D; margin-bottom:0;">
                  <span class="prompt-icon">📐</span>
                  <span class="prompt-text" style="color:#92400E; font-size:0.86rem; line-height:1.4;">
                    <strong>Fórmula de Cuadre en Odoo 19:</strong><br>
                    <code>Diferencia = Valor Existencias - (Valor por Facturar + Contabilidad 1150 + No Reconocido)</code>
                  </span>
                </div>
                <div class="interactive-chat-prompt" style="background:#FEF2F2; border:1px solid #FCA5A5; margin-bottom:0;">
                  <span class="prompt-icon">⚠️</span>
                  <span class="prompt-text" style="color:#991B1B; font-size:0.86rem; line-height:1.4;">
                    <strong>La Trampa de la Compensación Global:</strong><br>
                    ¡Prohibido auditar solo por totales! Mouse (+$8.5k), Router (-$2.4k), RAM (+$210) y SSD (-$1.5k) se compensan. <strong>La conciliación sólo vale si cada SKU = $0.00.</strong>
                  </span>
                </div>
              </div>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(2, 1fr); gap: 16px;">
                <div class="agenda-card" style="border-top: 4px solid #1E293B;">
                  <div class="agenda-time">PASO 1 · AISLAR EL PARCHE MANUAL</div>
                  <div class="agenda-title">Caza de Pólizas en la 1150</div>
                  <p class="agenda-desc">Filtrar en cuenta 115.01.01 movimientos sin documento logístico y cancelar la póliza manual intrusa de $487,000 MXN.</p>
                </div>
                
                <div class="agenda-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">PASO 2 · ACCIÓN DE SERVIDOR EN 1 CLIC</div>
                  <div class="agenda-title">Reporte CSV Forense por Producto</div>
                  <p class="agenda-desc">Ejecutar la Acción de Servidor en Odoo 19 que exporta el reporte completo con productos activos y archivados con saldo.</p>
                </div>

                <div class="agenda-card" style="border-top: 4px solid #0D9488;">
                  <div class="agenda-time">PASO 3 · REGULARIZACIÓN LIMPIA</div>
                  <div class="agenda-title">Plantilla CSV con product_id</div>
                  <p class="agenda-desc">Importar la póliza balanceada asignando obligatoriamente el producto en la 1150 para sanear Mouse, Router, RAM y SSD.</p>
                </div>

                <div class="agenda-card" style="border-top: 4px solid #475569;">
                  <div class="agenda-time">PASO 4 · CANDADOS PREVENTIVOS</div>
                  <div class="agenda-title">Bloqueo de Modificaciones y Negativos</div>
                  <p class="agenda-desc">Prohibir asientos manuales, congelar categorías en caliente y activar bloqueo de stock negativo.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 15: Bloque 5 - Cuadre Perfecto al Centavo
        {
            "id": 15,
            "title": "Cuadre Perfecto al Centavo ($338,910 = $338,910)",
            "bg": "gradient",
            "time": "01:00 - 01:04",
            "block": "Bloque 5",
            "notes": "Celebrar el cuadre perfecto al centavo. Balanza ($338,910.00) = Existencias ($338,910.00). Diferencia $0.00 MXN en todos los productos.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">EL MOMENTO DE LA VERDAD</span>
                  <h2 class="slide-title" style="color: #fff;">Cuadre Perfecto al Centavo: $0.00 de Diferencia</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                Al remover el parche manual y aplicar la plantilla de regularización por SKU, el sistema recupera su coherencia matemática:
              </p>
              
              <div class="split-audit-container" style="margin-top:30px;">
                <div class="audit-col" style="background: rgba(255,255,255,0.1); border: 2px solid #16A34A; color:#fff;">
                  <div class="audit-col-badge" style="background:#16A34A; color:#fff;">Libro Mayor Saneado</div>
                  <h3 class="audit-col-title" style="color:#fff;">Balanza de Comprobación</h3>
                  <div class="audit-code" style="color:rgba(255,255,255,0.8);">Cuenta 115.01.01 · Inventario</div>
                  <div class="audit-amount" style="color:#fff;">$338,910.00 MXN</div>
                  <div class="audit-status audit-ok" style="background:rgba(22,163,74,0.2); color:#4ADE80;">✅ Saldo Real Verificado</div>
                </div>

                <div class="audit-vs">
                  <div class="audit-diff-card" style="background:#fff; color:#1E293B;">
                    <span class="diff-label" style="color:#16A34A;">DIFERENCIA CONCILIADA</span>
                    <span class="diff-amount" style="color:#16A34A; font-size:2.5rem;">
                      $0.00 MXN
                    </span>
                    <span class="diff-warn" style="color:#16A34A; font-weight:600;">¡Sincronización Total!</span>
                  </div>
                </div>

                <div class="audit-col" style="background: rgba(255,255,255,0.1); border: 2px solid #16A34A; color:#fff;">
                  <div class="audit-col-badge" style="background:#16A34A; color:#fff;">Almacén Físico</div>
                  <h3 class="audit-col-title" style="color:#fff;">Reporte de Existencias</h3>
                  <div class="audit-code" style="color:rgba(255,255,255,0.8);">Valoración de Stock (Odoo 19)</div>
                  <div class="audit-amount" style="color:#fff;">$338,910.00 MXN</div>
                  <div class="audit-status audit-ok" style="background:rgba(22,163,74,0.2); color:#4ADE80;">📦 Stock Moves Físicos</div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 16: Bloque 5 - Las 5 Reglas de Oro Blindadas de Vauxoo
        {
            "id": 16,
            "title": "Las 5 Reglas de Oro Blindadas de Vauxoo",
            "bg": "white",
            "time": "01:04 - 01:07",
            "block": "Bloque 5",
            "notes": "Parte C del Bloque 5: Las 5 Reglas de Oro Blindadas de Vauxoo. 1. Cero Asientos Manuales en la 1150; 2. Cero Salidas sin Recepción Registrada; 3. Configuración Congelada y Auditoría Disciplinada; 4. Cero Cambios Manuales de Coste; 5. Auditoría SKU por SKU y trazabilidad contable con product_id.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MEJORES PRÁCTICAS VAUXOO</span>
                  <h2 class="slide-title">Las 5 Reglas de Oro Blindadas de Vauxoo</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Cinco lineamientos operativos para garantizar que el divorcio contable nunca vuelva a ocurrir:</p>
              
              <div class="golden-rules-grid" style="grid-template-columns: repeat(3, 1fr); gap: 14px;">
                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #1</div>
                  <h3>Cero Asientos Manuales en 1150</h3>
                  <p>Prohibir por permisos que usuarios creen pólizas manuales de diario en cuentas de inventario. Todo apunte debe nacer de un movimiento de almacén.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #2</div>
                  <h3>Cero Salidas sin Recepción</h3>
                  <p>Asegurar que toda entrega al cliente cuente con su recepción validada previamente en Odoo para no fracturar la fórmula matemática del costo promedio.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #3</div>
                  <h3>Configuración & Cadencia</h3>
                  <p>Categorías inmutables en caliente sin protocolo de corte, y adoptar la disciplina semanal o mensual de conciliar Balanza vs Existencias con el checklist.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #4</div>
                  <h3>Cero Cambios Manuales de Coste</h3>
                  <p>En AVCO el costo promedio unitario nunca se tipea a mano en la ficha del producto; se recalcula exclusivamente por compras validadas.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #5</div>
                  <h3>Auditoría SKU & <code>product_id</code></h3>
                  <p>Auditar siempre producto por producto para evitar compensaciones engañosas (+/-). Si se autoriza un ajuste contable en la 1150, es mandatorio asignar el campo <strong>Producto</strong>.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 17: Bloque 6 - Q&A Hot Seat
        {
            "id": 17,
            "title": "Bloque 6: Q&A Hot Seat (Consultoría en Vivo)",
            "bg": "gradient",
            "time": "01:07 - 01:28",
            "block": "Bloque 6",
            "notes": "Bloque 6: Q&A Hot Seat - Consultoría en Vivo (23 minutos). Los asistentes exponen sus dudas operativas, configuraciones o descuadres reales en vivo. Julio responde en pantalla sobre Odoo 19.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 6 · 01:07 - 01:30</span>
                  <h2 class="slide-title" style="color: #fff;">Q&A Hot Seat: Consultoría en Vivo</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              
              <div class="hotseat-container">
                <div class="hotseat-badge-col">
                  <div class="hotseat-icon">🔥</div>
                  <h3>Micrófono Abierto</h3>
                  <p>Espacio abierto para analizar casuísticas reales de valoración y operativa en Odoo 19.</p>
                </div>
                <div class="hotseat-topics">
                  <h4>Temas Abiertos para Consulta:</h4>
                  <ul class="styled-list" style="color: rgba(255,255,255,0.9);">
                    <li>¿Tienes descuadres acumulados en versiones previas de Odoo?</li>
                    <li>¿Cómo corregir categorías de producto sin generar vacíos de saldos?</li>
                    <li>¿Qué hacer con ubicaciones de ajuste físico que no generan póliza?</li>
                    <li>¿Mejores prácticas para compras en USD y cortes de inventario?</li>
                  </ul>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 18: Suite de Entregables Oficiales
        {
            "id": 18,
            "title": "Paquete de Entregables Oficiales",
            "bg": "white",
            "time": "01:28 - 01:30",
            "block": "Bloque 6",
            "notes": "Presentación de los entregables: 1. Checklist de Auditoría Logística-Contable con Matriz de Cadencia; 2. Tabla de Mapeo Conceptual v18 -> v19; 3. Kit Técnico de Regularización y Acción de Servidor; 4. Grabación HD y Certificado.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MATERIALES DE LA MASTERCLASS</span>
                  <h2 class="slide-title">Suite Oficial de Entregables</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="deliverables-grid">
                <div class="deliv-card">
                  <div class="deliv-icon">📋</div>
                  <h4>Entregable #1: Checklist con Matriz de Cadencia</h4>
                  <p>Guía de validación operativa para auditorías diarias, semanales y mensuales en Odoo 19.</p>
                  <a href="#tab-checklist" onclick="switchTab('checklist')" class="btn btn-sm">Ver Checklist</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">📊</div>
                  <h4>Entregable #2: Tabla de Mapeo 18 → 19</h4>
                  <p>Comparativa conceptual de arquitectura: Stock Moves, cuentas directas y control de cierre.</p>
                  <a href="#tab-mapeo" onclick="switchTab('mapeo')" class="btn btn-sm">Ver Mapeo</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">🛠️</div>
                  <h4>Entregable #4: Kit Técnico de Auditoría</h4>
                  <p>Plantilla CSV de regularización con product_id y código de la Acción de Servidor Odoo 19.</p>
                  <a href="#tab-kit" onclick="switchTab('kit')" class="btn btn-sm">Ver Kit Técnico</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">🎓</div>
                  <h4>Certificado Vauxoo Academy</h4>
                  <p>Constancia oficial digital de participación en la Masterclass Odoo 19.</p>
                  <span class="pill-badge-outline" style="color:#64748B; border-color:#CBD5E1;">Emisión oficial</span>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 19: Cierre y Agradecimientos
        {
            "id": 19,
            "title": "Cierre y Agradecimientos",
            "bg": "gradient",
            "time": "01:30",
            "block": "Cierre",
            "notes": "Agradecimiento final de Julio Serna. Contacto y cierre de la masterclass.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-logo-wrap">
                {logo_white}
              </div>
              <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 12px; color: #fff;">
                Construyamos algo genial.
              </h2>
              <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); max-width: 650px; margin: 0 auto 32px;">
                Gracias por acompañarnos en esta sesión técnica de Vauxoo Academy.
              </p>
              
              <div class="closing-contact-card">
                <div>
                  <strong>Julio Serna</strong> · Project Manager & Functional Specialist<br>
                  <span style="color: rgba(255,255,255,0.8);">Vauxoo — Odoo Gold Partner</span>
                </div>
                <div style="display:flex; gap:12px; justify-content:center; margin-top:16px;">
                  <span class="pill-badge">vauxoo.com/vauxoo-academy</span>
                  <span class="pill-badge-outline">#VauxooAcademy2026</span>
                </div>
              </div>
            </div>
            '''
        }
    ]

print("make_slides_content.py updated successfully (19 slides).")
