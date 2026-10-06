#!/usr/bin/env python3
# Content for all slides of the Masterclass 2026
# Aligned strictly with masterclass-plan-final.md v5 and GUION_DE_TRANSMISION_QUE_DECIR_Y_QUE_HACER.md


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

        # Slide 2: El Hook - Descuadre de $411,275 MXN
        {
            "id": 2,
            "title": "El Hook: Descuadre de $411,275 MXN",
            "bg": "white",
            "time": "00:01 - 00:04",
            "block": "Bloque 1",
            "notes": "Mostrar el split view en vivo en Odoo 19: Balanza 115.01.01 ($487,200.00 MXN) vs Reporte de Existencias ($75,925.00 MXN) -> Descuadre real de $411,275.00 MXN. Plantear el dolor de todo cierre contable.",
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
                  <div class="audit-amount">$487,200.00 MXN</div>
                  <div class="audit-detail">Saldo deudor contable al corte mensual</div>
                  <div class="audit-status audit-err">⚠️ Generado por libro mayor contable</div>
                </div>

                <div class="audit-vs">
                  <div class="audit-diff-card">
                    <span class="diff-label">DESCUADRE REAL</span>
                    <span class="diff-amount doodle-wrap">
                      $411,275.00 MXN
                      {doodle_oval}
                    </span>
                    <span class="diff-warn">¿Cómo conciliar esta brecha en el cierre?</span>
                  </div>
                </div>

                <div class="audit-col audit-logistica">
                  <div class="audit-col-badge">Módulo de Inventario</div>
                  <h3 class="audit-col-title">Reporte de Existencias / Valoración</h3>
                  <div class="audit-code">Valoración de Stock (Valuation)</div>
                  <div class="audit-amount">$75,925.00 MXN</div>
                  <div class="audit-detail">Valoración real de los productos en almacén</div>
                  <div class="audit-status audit-ok">📦 Generado por Stock Moves físicos</div>
                </div>
              </div>

              <div class="interactive-chat-prompt" style="background:#F1F5F9; border:1px solid #CBD5E1;">
                <span class="prompt-icon">💡</span>
                <span class="prompt-text" style="color:#1E293B;">
                  <strong>El objetivo de la sesión:</strong> Identificar el origen exacto de esta diferencia de $411,275 MXN y resolverla en vivo durante la clase.
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
                  <p class="agenda-desc"><strong>"Dos malas no hacen una buena."</strong> Cambiar métodos en caliente, factores UoM invertidos, ubicaciones de ajuste sin cuenta contable o saldos iniciales duplicados.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">OPERACIÓN</div>
                  <div class="agenda-num">02</div>
                  <div class="agenda-title">PARCHES OPERATIVOS</div>
                  <p class="agenda-desc"><strong>"La aspirina manual."</strong> Pólizas manuales para 'cuadrar', recepciones con tipo de cambio erróneo o despachos a clientes sin compra recibida/facturada.</p>
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

        # Slide 7: Bloque 3 - Happy Path Paso 1 (Compra Progresiva AVCO)
        {
            "id": 7,
            "title": "Happy Path: Compra Progresiva AVCO",
            "bg": "white",
            "time": "00:17 - 00:25",
            "block": "Bloque 3",
            "notes": "Mostrar la compra progresiva y el cálculo ponderado en Odoo 19 con [WIDGET-MX]. 50 u @ $150 + 50 u @ $170 = 100 u @ $160 MXN. Cuenta 1150 suma $16,000 MXN.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · PASO 1</span>
                  <h2 class="slide-title">El Happy Path: Compra Progresiva y Ponderación AVCO</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[WIDGET-MX] Widget Nacional MX (AVCO)</code>. Ponderación limpia en tiempo real:</p>
              
              <div class="flow-steps-grid" style="grid-template-columns: repeat(3, 1fr);">
                <div class="flow-step-card">
                  <div class="step-badge">RECEPCIÓN 1 (WH/IN/00001)</div>
                  <h4>Primera Compra</h4>
                  <p>50 unidades @ $150.00 MXN</p>
                  <div class="asiento-box">
                    Subtotal: <strong>$7,500.00 MXN</strong><br>
                    AVCO Inicial: <strong>$150.00 MXN</strong>
                  </div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">RECEPCIÓN 2 (WH/IN/00002)</div>
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
                  <strong>Asiento contable limpio:</strong> Cargo directo a la cuenta <code>115.01.01 Inventario</code> por <strong>$16,000.00 MXN</strong> sin pasos intermedios.
                </span>
              </div>
            </div>
            '''
        },

        # Slide 8: Bloque 3 - Happy Path Paso 2 (Venta, Entrega y Facturación)
        {
            "id": 8,
            "title": "Happy Path: Venta, Entrega y Costo de Ventas",
            "bg": "white",
            "time": "00:25 - 00:35",
            "block": "Bloque 3",
            "notes": "Mostrar el pedido de venta S00001, entrega física WH/OUT/00001 (30 piezas) y factura INV/2026/00001 con Costo de Ventas ($4,800 MXN). Cuadre perfecto: 70 u en existencias = $11,200 MXN en la 1150.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · PASO 2</span>
                  <h2 class="slide-title">Venta, Entrega Física y Registro del Costo de Ventas</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Completando el ciclo comercial: despacho físico y asiento automático de costo:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">OPERACIÓN COMERCIAL (S00001)</div>
                  <h3>Venta y Entrega de 30 Unidades</h3>
                  <div class="detail-box">
                    <p>Almacén valida la salida <code>WH/OUT/00001</code>. Odoo descarga 30 piezas al costo promedio vigente ($160.00 MXN).</p>
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

        # Slide 9: Bloque 4 - La Clínica de Problemas Operativos
        {
            "id": 9,
            "title": "La Clínica de Problemas Operativos (4 Casos)",
            "bg": "white",
            "time": "00:35 - 00:37",
            "block": "Bloque 4",
            "notes": "Introducir la clínica de 4 casos operativos: 1. Ajuste sin cuenta; 2. TC erróneo; 3. Entrega sin compra recibida/facturada; 4. Pólizas manuales.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">BLOQUE 4 · 00:35 - 00:55</span>
                  <h2 class="slide-title">La Clínica de Problemas Operativos</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Los 4 desvíos operativos más comunes en el día a día que destruyen la sincronía:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(2, 1fr); gap: 20px;">
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">CASO OPERATIVO #1</div>
                  <div class="agenda-title">Ajuste de Inventario sin Cuenta Contable</div>
                  <p class="agenda-desc">La existencia física cambia en almacén, pero contabilidad no genera asiento por falta de cuenta contrapartida en la ubicación o categoría.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">CASO OPERATIVO #2</div>
                  <div class="agenda-title">Recepción de Compra con Tipo de Cambio Erróneo</div>
                  <p class="agenda-desc">Capturar una tasa equivocada al recibir compras en divisa envenena el costo unitario ponderado en pesos y contamina las ventas futuras.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">CASO OPERATIVO #3</div>
                  <div class="agenda-title">Entrega sin Compra Recibida o sin Facturar</div>
                  <p class="agenda-desc">Despachar al cliente antes de registrar la recepción del proveedor o su factura altera la temporalidad del costo y provoca revaloraciones bruscas.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">CASO OPERATIVO #4</div>
                  <div class="agenda-title">Las Pólizas Manuales de Ajuste</div>
                  <p class="agenda-desc">Inyectar pólizas manuales de diario directo a la cuenta 1150 para forzar cuadres contables sin documento logístico asociado.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 10: Bloque 4 · Caso 1: Ajuste sin Cuenta Contable
        {
            "id": 10,
            "title": "Caso 1: Ajuste sin Cuenta Contable Configurada",
            "bg": "white",
            "time": "00:37 - 00:41",
            "block": "Bloque 4",
            "notes": "Caso 1: Ajuste de inventario sin cuenta contable. Ubicación virtual de pérdida o conteo físico sin cuenta asignada. El stock cambia, contabilidad queda intacta.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA · CASO 1</span>
                  <h2 class="slide-title">Ajuste de Inventario sin Cuenta Contable Configurada</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">El almacenista registra un conteo físico o merma, pero la configuración tiene vacíos contables:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">EL MECANISMO DE LA FALLA</div>
                  <h3>Ubicación Virtual sin Contrapartida</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li>La ubicación <code>Virtual Locations/Inventory adjustment</code> no tiene cuenta contable configurada.</li>
                      <li>Al validar el ajuste físico, el reporte de almacén descuenta o suma piezas inmediatamente.</li>
                      <li><strong>En Contabilidad:</strong> Odoo no puede generar la póliza o arroja un error silencioso de validación.</li>
                    </ul>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">IMPACTO Y SOLUCIÓN</div>
                  <h3>Descuadre Inmediato Almacén vs Balanza</h3>
                  <div class="detail-box">
                    <p>Las existencias físicas bajaron de valor, pero la cuenta <code>115.01.01</code> sigue con el saldo anterior.</p>
                    <div class="vauxoo-rule-badge" style="margin-top:12px;">REGLA VAUXOO: Auditar que cada ubicación de ajuste y categoría tenga cuenta contrapartida asignada antes de operar.</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 11: Bloque 4 · Caso 2: Recepción con Tipo de Cambio Erróneo
        {
            "id": 11,
            "title": "Caso 2: Recepción con Tipo de Cambio Erróneo",
            "bg": "white",
            "time": "00:41 - 00:45",
            "block": "Bloque 4",
            "notes": "Caso 2: Recepción con TC erróneo. Captura equivocada en moneda extranjera. El costo en moneda base entra adulterado y afecta el AVCO de los próximos meses.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA · CASO 2</span>
                  <h2 class="slide-title">Recepción de Compra con Tipo de Cambio Erróneo</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">En compras en moneda extranjera, la tasa del día de recepción física fija el costo contable en pesos:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">EL ERROR HABITUAL</div>
                  <h3>Tasa Equivocada o Desactualizada</h3>
                  <div class="detail-box">
                    <p>El operador confirma la recepción con una tasa por defecto o comete un error tipográfico (ej. capturar $1.85 en vez de $18.50 MXN/USD).</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      Compra de $20,000 USD con error de captura:<br>
                      <strong>Distorsión directa de cientos de miles de pesos en la 1150.</strong>
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">EL EFECTO CONTAMINANTE</div>
                  <h3>Costo Promedio Envenenado</h3>
                  <div class="detail-box">
                    <p>Al mezclarse con las existencias anteriores, la fórmula ponderada adopta un costo falso. Cada factura emitida en las próximas semanas descargará un costo de ventas distorsionado.</p>
                    <div class="vauxoo-rule-badge" style="margin-top:12px;">REGLA VAUXOO: Sincronización oficial del tipo de cambio a la fecha estricta de recepción física.</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 12: Bloque 4 · Caso 3: Entrega sin Compra Recibida o Facturada
        {
            "id": 12,
            "title": "Caso 3: Entrega sin Compra Recibida o sin Facturar",
            "bg": "white",
            "time": "00:45 - 00:50",
            "block": "Bloque 4",
            "notes": "Caso 3: Mercancía que se entrega al cliente sin antes recibir compra o facturar compra. La prisa comercial invierte el orden lógico y genera revaloraciones abruptas.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA · CASO 3</span>
                  <h2 class="slide-title">Mercancía Entregada sin Recibir o sin Facturar Compra</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">La prisa comercial de despachar invierte el orden natural del ciclo operativo:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">EL DESFASE TEMPORAL</div>
                  <h3>Entrega Física sin Entrada en Sistema</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li>El camión del proveedor llegó a patio, pero el auxiliar no ha validado la recepción en Odoo.</li>
                      <li>Ventas y despacho entregan la mercancía al cliente apresuradamente.</li>
                      <li>La salida se procesa con stock en cero o costo provisional desfasado.</li>
                    </ul>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">CONSECUENCIA EN ODOO 19</div>
                  <h3>Revaloraciones Forzadas</h3>
                  <div class="detail-box">
                    <p>Cuando la compra o factura del proveedor entra días después, el sistema debe reajustar movimientos pasados, provocando saltos anómalos en el costo de ventas.</p>
                    <div class="vauxoo-rule-badge" style="margin-top:12px;">REGLA VAUXOO: Respetar la secuencia estricta: Orden de Compra &rarr; Recepción en Sistema &rarr; Entrega al Cliente.</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 13: Bloque 4 · Caso 4: Las Pólizas Manuales de Ajuste
        {
            "id": 13,
            "title": "Caso 4: Las Pólizas Manuales de Ajuste",
            "bg": "white",
            "time": "00:50 - 00:55",
            "block": "Bloque 4",
            "notes": "Caso 4: Pólizas manuales de ajuste. El contador bajo presión mete un asiento manual en la cuenta 1150 para 'cuadrar' el balance. La aspirina manual que rompe el enlace con almacén.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA · CASO 4</span>
                  <h2 class="slide-title">Las Pólizas Manuales de Ajuste: "La Aspirina Manual"</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">El parche por excelencia que condena la trazabilidad contable a largo plazo:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">CÓMO OCURRE</div>
                  <h3>Presión en el Cierre Mensual</h3>
                  <div class="detail-box">
                    <p>El contador ve que la cuenta 1150 no coincide con el balance esperado. Faltan horas para emitir estados financieros, calcula la diferencia en su hoja de cálculo y registra un asiento manual en diario de operaciones varias (<code>MISC</code>).</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      Cargo o Abono directo a la <strong>115.01.01</strong>:<br>
                      <em>"Ajuste manual para cuadrar inventario"</em>
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">POR QUÉ ENVENENA EL SISTEMA</div>
                  <h3>Fractura Permanente con Almacén</h3>
                  <div class="detail-box">
                    <p>Una póliza contable manual <strong>NUNCA crea un movimiento de stock</strong>. Modifica el saldo contable, pero deja intacto el reporte de existencias físicas. A partir de ese segundo, contabilidad y logística quedan divorciados para siempre.</p>
                    <div class="vauxoo-rule-badge" style="margin-top:12px;">REGLA VAUXOO: Prohibir permisos de asientos manuales directos en la cuenta 1150.</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 14: Bloque 5 - Metodología de Auditoría para Encontrar las Diferencias
        {
            "id": 14,
            "title": "Metodología de Auditoría para Encontrar las Diferencias",
            "bg": "white",
            "time": "00:55 - 01:03",
            "block": "Bloque 5",
            "notes": "Intro de Julio Serna en Bloque 5: 'Bueno, ya vimos en el Bloque 1 las principales causas que hay que evitar para no tener un divorcio contable y logístico. En los bloques anteriores entendimos cómo es la valoración con el Happy Path y qué pasa con los problemas comunes. Pero muchos de los que están aquí ya tienen Odoo en producción, ya iniciaron operaciones y YA TIENEN el issue encima. Vamos a ver entonces cómo lo auditamos y sobre todo cómo lo corregimos.' Explicar la metodología de auditoría integral y los 4 frentes críticos de validación.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · 00:55 - 01:07</span>
                  <h2 class="slide-title">Metodología de Auditoría para Encontrar las Diferencias</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Protocolo integral de diagnóstico para rastrear y sanear cualquier brecha entre contabilidad y almacén:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(2, 1fr); gap: 20px;">
                <div class="agenda-card" style="border-top: 4px solid #1E293B;">
                  <div class="agenda-time">PASO 1 · INTEGRIDAD ESTRUCTURAL</div>
                  <div class="agenda-title">Cuentas en Categorías de Producto</div>
                  <p class="agenda-desc">Validar que todas las categorías de productos almacenables apunten a la <strong>cuenta correcta de inventario (1150)</strong> y cuenten con cuentas de contrapartida de valoración y merma válidas.</p>
                </div>
                
                <div class="agenda-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">PASO 2 · TRÁNSITO PROVEEDORES</div>
                  <div class="agenda-title">Pendiente por Facturar (Proveedor)</div>
                  <p class="agenda-desc">Auditar recepciones físicas de compra que no cuentan con factura de proveedor vinculada o compras facturadas sin recepción (desfase entre costo en inventario y pasivo).</p>
                </div>

                <div class="agenda-card" style="border-top: 4px solid #0D9488;">
                  <div class="agenda-time">PASO 3 · TRÁNSITO CLIENTES</div>
                  <div class="agenda-title">Pendiente por Facturar (Cliente)</div>
                  <p class="agenda-desc">Auditar entregas de mercancía al cliente con salida física de almacén pendientes de facturación, o facturas emitidas sin registrar la entrega de stock correspondiente.</p>
                </div>

                <div class="agenda-card" style="border-top: 4px solid #475569;">
                  <div class="agenda-time">PASO 4 · ANÁLISIS DE LA CUENTA 1150</div>
                  <div class="agenda-title">Cruce Balanza vs Existencias & Filtros</div>
                  <p class="agenda-desc">Analizar los apuntes contables de la cuenta 1150 para <strong>aislar pólizas manuales</strong> (<code>Documento Origen = Vacío</code>), movimientos huérfanos y conciliar la cifra al centavo.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 15: Bloque 5 - Cuadre Perfecto al Centavo
        {
            "id": 15,
            "title": "Cuadre Perfecto al Centavo ($75,925 = $75,925)",
            "bg": "gradient",
            "time": "01:01 - 01:04",
            "block": "Bloque 5",
            "notes": "Celebrar el cuadre perfecto al centavo. Balanza ($75,925.00) = Existencias ($75,925.00). Diferencia $0.00 MXN.",
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
                Al remover el parche manual, el sistema recupera su coherencia matemática y contable original:
              </p>
              
              <div class="split-audit-container" style="margin-top:30px;">
                <div class="audit-col" style="background: rgba(255,255,255,0.1); border: 2px solid #16A34A; color:#fff;">
                  <div class="audit-col-badge" style="background:#16A34A; color:#fff;">Libro Mayor Saneado</div>
                  <h3 class="audit-col-title" style="color:#fff;">Balanza de Comprobación</h3>
                  <div class="audit-code" style="color:rgba(255,255,255,0.8);">Cuenta 115.01.01 · Inventario</div>
                  <div class="audit-amount" style="color:#fff;">$75,925.00 MXN</div>
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
                  <div class="audit-amount" style="color:#fff;">$75,925.00 MXN</div>
                  <div class="audit-status audit-ok" style="background:rgba(22,163,74,0.2); color:#4ADE80;">📦 Stock Moves Físicos</div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 16: Bloque 5 - Las 3 Reglas de Oro Blindadas de Vauxoo
        {
            "id": 16,
            "title": "Las 3 Reglas de Oro Blindadas de Vauxoo",
            "bg": "white",
            "time": "01:04 - 01:07",
            "block": "Bloque 5",
            "notes": "Parte C del Bloque 5: Las 3 Reglas de Oro Blindadas de Vauxoo. 1. Cero Asientos Manuales en la 1150; 2. Cero Salidas sin Recepción Registrada; 3. Configuración Congelada y Auditoría Disciplinada.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MEJORES PRÁCTICAS VAUXOO</span>
                  <h2 class="slide-title">Las 3 Reglas de Oro Blindadas de Vauxoo</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Tres lineamientos operativos para garantizar que el divorcio contable nunca vuelva a ocurrir:</p>
              
              <div class="golden-rules-grid">
                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #1</div>
                  <h3>Cero Asientos Manuales en la 1150</h3>
                  <p>Restringir por permisos de seguridad que usuarios o contadores creen pólizas manuales de diario en cuentas de inventario. Todo apunte debe nacer de un movimiento de almacén.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #2</div>
                  <h3>Cero Salidas sin Recepción Registrada</h3>
                  <p>Asegurar que toda entrega a cliente cuente con su recepción y compra procesadas en el sistema para mantener la coherencia matemática del costo de ventas.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #3</div>
                  <h3>Configuración y Cadencia Disciplinada</h3>
                  <p>Categorías inmutables en caliente sin protocolo de corte, y adoptar la disciplina semanal o mensual de conciliar Balanza vs Existencias con el checklist oficial.</p>
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
                    <li>¿Mejores prácticas para cortes logísticos de fin de mes en almacén?</li>
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
            "notes": "Presentación de los entregables: 1. Checklist de Auditoría Logística-Contable con Matriz de Cadencia; 2. Tabla de Mapeo Conceptual v18 -> v19; 3. Grabación HD con capítulos; 4. Certificado de Vauxoo Academy.",
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
                  <div class="deliv-icon">🎥</div>
                  <h4>Grabación en Alta Definición</h4>
                  <p>Acceso permanente a la grabación completa indexada por bloques temáticos.</p>
                  <span class="pill-badge-outline" style="color:#64748B; border-color:#CBD5E1;">Acceso permanente</span>
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
