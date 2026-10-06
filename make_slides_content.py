#!/usr/bin/env python3
# Content for all 18 slides of the Masterclass 2026
# STRICTLY FOLLOWING masterclass-plan-final.md (Plan Definitivo v4)
# - Marco Narrativo: Las 3 Causas Raíz (Configuración, Operación, Auditoría)
# - Números reales: Cuenta 115.01.01 ($487,200.00 MXN) vs Existencias ($75,925.00 MXN) -> Descuadre $411,275.00 MXN
# - Póliza manual intrusa: MISC/2026/09/0001 por $487,000.00 MXN
# - Bloque 1 (7 min): Hook real
# - Bloque 2 (10 min): Odoo 19 AVCO + Alerta: Cambios de Configuración en Caliente ("Dos malas no hacen una buena")
# - Bloque 3 (20 min): Caso 1 WIDGET-MX ($160 MXN) + Caso 2 Compras USD & Landed Costs ($1,850 -> $2,100 MXN)
# - Bloque 4 (16 min, 4 min c/u): VALVULA-NEG, TC erróneo DOF, CABLE-MERMA (15m @ $85 MXN a gasto), TARJETA-OBS (cuenta 108.02.01)
# - Bloque 5 (14 min): Matriz de Cadencia + Caza de MISC/2026/09/0001 + 3 Reglas Blindadas
# - Bloque 6 (23 min): Q&A Hot Seat de consultoría

def get_slides(doodle_oval, doodle_arrow, doodle_underline, logo_white, logo_light):
    return [
        # Slide 1: Portada Oficial
        {
            "id": 1,
            "title": "Portada Oficial",
            "bg": "gradient",
            "time": "00:00",
            "block": "Apertura",
            "notes": "Bienvenida de Julio Serna (PM y Experto Funcional en Vauxoo). Masterclass 2026 de Vauxoo Academy. Reglas de la sesión: 90 minutos estrictos enfocados en la trinchera contable y logística mexicana en Odoo 19.0 Enterprise. Enfoque exclusivo en Costo Promedio (AVCO) perpetuo.",
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
              <p class="cover-subtitle">
                Arquitectura de Costo Promedio (AVCO), Compras en USD, Landed Costs y Blindaje Contable-Fiscal ante el SAT.
              </p>
              <div class="cover-footer">
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
        # Slide 2: El Marco Narrativo - Las 3 Causas Raíz
        {
            "id": 2,
            "title": "Las 3 Causas Raíz del Divorcio",
            "bg": "white",
            "time": "00:01 - 00:03",
            "block": "Marco Narrativo",
            "notes": "Presentar el hilo conductor de toda la masterclass: las 3 causas raíz detectadas en más de una década de implementaciones en México. 1. Configuración errática; 2. Parches operativos manuales; 3. Auditoría tardía por falta de cadencia.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MARCO NARRATIVO</span>
                  <h2 class="slide-title">Las 3 Causas Raíz del Divorcio Almacén-Contabilidad</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Más de una década de auditorías de inventario en México demuestran que el descuadre nace de 3 vicios:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(3, 1fr);">
                <div class="agenda-card" style="border-top: 4px solid #1E293B;">
                  <div class="agenda-time">BLOQUE 2</div>
                  <div class="agenda-num">01</div>
                  <div class="agenda-title">CONFIGURACIÓN ERRÁTICA</div>
                  <p class="agenda-desc"><strong>"Dos malas no hacen una buena."</strong> Cambiar métodos en caliente (periódico ↔ perpetuo o standard ↔ AVCO) sin saber que Odoo 19 no genera pólizas retroactivas automáticas.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">BLOQUES 1 Y 5</div>
                  <div class="agenda-num">02</div>
                  <div class="agenda-title">PARCHES OPERATIVOS</div>
                  <p class="agenda-desc"><strong>"La aspirina manual."</strong> El contador, presionado por el cierre mensual, mete pólizas manuales ciegas a la cuenta 1150 rompiendo la paridad con el kardex físico.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #475569;">
                  <div class="agenda-time">BLOQUE 5</div>
                  <div class="agenda-num">03</div>
                  <div class="agenda-title">AUDITORÍA TARDÍA</div>
                  <p class="agenda-desc"><strong>"El costo de la infrecuencia."</strong> Esperar al cierre anual cuando hay miles de movimientos acumulados hace que encontrar la desviación sea una pesadilla de semanas.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 3: Cronograma de Batalla Rebalanceado
        {
            "id": 3,
            "title": "Cronograma de Batalla (90 min)",
            "bg": "white",
            "time": "00:03 - 00:07",
            "block": "Estructura",
            "notes": "Mostrar el cronograma rebalanceado de 90 minutos exactos: Bloque 1 (7 min), Bloque 2 (10 min con +2 min para la trampa de configuración), Bloque 3 (20 min con flujos limpios), Bloque 4 (16 min con 4 min exactos por desastre), Bloque 5 (14 min con cadencia y caza de póliza) y Bloque 6 (23 min de Hot Seat).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">AGENDA REBALANCEADA</span>
                  <h2 class="slide-title">Estructura Minuto a Minuto (90 Minutos Estrictos)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <div class="agenda-grid">
                <div class="agenda-card">
                  <div class="agenda-time">00:00 – 00:07 (7 min)</div>
                  <div class="agenda-num">01</div>
                  <div class="agenda-title">EL HOOK: El Dolor Real</div>
                  <p class="agenda-desc">Balanza 115.01.01 vs Reporte de Existencias. Descuadre en vivo de $411,275.00 MXN.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:07 – 00:17 (10 min)</div>
                  <div class="agenda-num">02</div>
                  <div class="agenda-title">EL NUEVO PARADIGMA</div>
                  <p class="agenda-desc">Odoo 19 AVCO + La alerta técnica: Cambios de método en caliente y sus vacíos.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:17 – 00:37 (20 min)</div>
                  <div class="agenda-num">03</div>
                  <div class="agenda-title">CASOS PRÁCTICOS EN VIVO</div>
                  <p class="agenda-desc">Flujo limpio en MXN ($160 MXN) y Compras en USD con Landed Costs ($1,850 → $2,100 MXN).</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:37 – 00:53 (16 min)</div>
                  <div class="agenda-num">04</div>
                  <div class="agenda-title">CLÍNICA DE DESASTRES</div>
                  <p class="agenda-desc">4 min c/u: Stock negativo, TC erróneo DOF, Mermas a gasto y Obsolescencia NIF C-4.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:53 – 01:07 (14 min)</div>
                  <div class="agenda-num">05</div>
                  <div class="agenda-title">EL MOMENTO DE LA VERDAD</div>
                  <p class="agenda-desc">Matriz de Cadencia + Caza de la póliza MISC/2026/09/0001 ($487k) + 3 Reglas de Oro.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">01:07 – 01:30 (23 min)</div>
                  <div class="agenda-num">06</div>
                  <div class="agenda-title">HOT SEAT & CONSULTORÍA</div>
                  <p class="agenda-desc">23 minutos de consultoría directa sobre casos y dudas reales de los asistentes.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 4: Bloque 1 - El Hook: "El Descuadre que Todos Conocen"
        {
            "id": 4,
            "title": "El Hook: Descuadre de $411,275 MXN",
            "bg": "white",
            "time": "00:00 - 00:07",
            "block": "Bloque 1",
            "notes": "Mostrar el split view con los números exactos del Plan Final v4: Balanza 115.01.01 ($487,200.00 MXN) vs Reporte de Existencias ($75,925.00 MXN) -> Descuadre real de $411,275.00 MXN. Lanzar la pregunta al chat.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 1 · 00:00 - 00:07</span>
                  <h2 class="slide-title">El Dolor que Todos Conocen (Caso Real en Vivo)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Cierre contable de mes. Dos reportes oficiales en la misma base de datos arrojando datos incompatibles:</p>
              
              <div class="split-audit-container">
                <div class="audit-col audit-contable">
                  <div class="audit-col-badge">Módulo de Contabilidad</div>
                  <h3 class="audit-col-title">Balanza de Comprobación SAT</h3>
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
                    <span class="diff-warn">¿Cómo se explica esto en auditoría?</span>
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

              <div class="interactive-chat-prompt">
                <span class="prompt-icon">💬</span>
                <span class="prompt-text">
                  <strong>Pregunta al chat:</strong> "¿A quién le ha tocado explicarle este descuadre de $411,275 pesos al Director General, al auditor externo o peor… al SAT? Pongan 🔥 en el chat."
                </span>
              </div>
            </div>
            '''
        },
        # Slide 5: Bloque 2 - El Nuevo Paradigma Odoo 19.0
        {
            "id": 5,
            "title": "El Nuevo Paradigma en Odoo 19.0",
            "bg": "white",
            "time": "00:07 - 00:13",
            "block": "Bloque 2",
            "notes": "Detallar el cambio de arquitectura: Adiós SVL (stock.valuation.layer) -> la valoración vive integrada en stock.move. Adiós cuentas puente interim -> asiento contable automático y directo a 115.01.01. De Anglo-Sajona a Periódico vs Perpetuo. Nuevo menú en Contabilidad > Informes > Inventario / Existencias.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 2 · 00:07 - 00:17</span>
                  <h2 class="slide-title">La Revolución Arquitectónica de Odoo 19.0</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Odoo 19 simplifica el motor contable-logístico eliminando capas intermedias:</p>
              
              <div class="paradigm-table-container">
                <table class="paradigm-table">
                  <thead>
                    <tr>
                      <th>Dimensión</th>
                      <th>Odoo ≤ 18 (Arquitectura Clásica)</th>
                      <th>Odoo 19.0 (Nuevo Paradigma)</th>
                      <th>Impacto en México</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Motor de Valoración</strong></td>
                      <td><span class="tag-old">stock.valuation.layer (SVL)</span><br><small>Tabla separada propensa a desincronizarse</small></td>
                      <td><span class="tag-new">Directo en stock.move</span><br><small>El movimiento físico ES el registro de valor</small></td>
                      <td>Menor peso en base de datos; rastreo directo 1 a 1 por póliza</td>
                    </tr>
                    <tr>
                      <td><strong>Cuentas Puente</strong></td>
                      <td><span class="tag-old">Interim Input / Output</span><br><small>Cuentas temporales con conciliaciones infinitas</small></td>
                      <td><span class="tag-new">Asiento Directo a 1150</span><br><small>Desaparecen en el flujo estándar</small></td>
                      <td>Balanza del SAT limpia; cero saldos huérfanos a fin de año</td>
                    </tr>
                    <tr>
                      <td><strong>Terminología</strong></td>
                      <td><span class="tag-old">Continental / Anglo-Sajona</span><br><small>Confuso para implementadores de LATAM</small></td>
                      <td><span class="tag-new">Periódico vs Perpetuo</span><br><small>Estándar internacional formal</small></td>
                      <td>Alineado formalmente con NIF C-4 y Art. 41 de la Ley del ISR</td>
                    </tr>
                    <tr>
                      <td><strong>Panel de Control</strong></td>
                      <td><span class="tag-old">Informes dispersos</span><br><small>Revisión manual y hojas de cálculo</small></td>
                      <td><span class="tag-new">Contabilidad > Informes > Existencias</span><br><small>Panel centralizado de valoración y cierre</small></td>
                      <td>Validación de consistencia rápida previa a estados financieros</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            '''
        },
        # Slide 6: Bloque 2 - Causa Raíz #1: La Trampa de las Configuraciones en Caliente
        {
            "id": 6,
            "title": "Causa Raíz #1: Cambios en Caliente",
            "bg": "white",
            "time": "00:13 - 00:17",
            "block": "Bloque 2",
            "notes": "ALERTA TÉCNICA CLAVE: Demostrar la lección de laboratorio en Odoo 19: 'Dos configuraciones malas no hacen una buena'. Cambiar categorías de Periódico a Perpetuo o de Standard a FIFO a AVCO cuando ya hay stock NO genera asientos retroactivos automáticos en Odoo 19. El stock anterior queda flotando sin soporte contable.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CAUSA RAÍZ #1 · CONFIGURACIÓN</span>
                  <h2 class="slide-title">La Trampa de los Cambios de Configuración en Caliente</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Historia de guerra de implementadores: <strong>"Dos configuraciones malas no hacen una buena."</strong></p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">EL ERROR DE TRINCHERA</div>
                  <h3>El "Juego" de Cambiar Métodos</h3>
                  <div class="detail-box">
                    Arrancar una empresa con valoración periódica (manual). A los 4 meses ver números extraños, cambiar la categoría a perpetua. Cambiarla luego a FIFO "para ver qué pasa", y finalmente a AVCO.
                    <br><br>
                    <strong>La creencia ingenua:</strong> Creer que Odoo 19 recalculará mágicamente el pasado y generará las pólizas contables retroactivas.
                  </div>
                </div>

                <div class="disaster-col-card" style="border: 2px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">EVIDENCIA DE LABORATORIO ODOO 19</div>
                  <h3>Odoo 19 NO Genera Asientos Retroactivos</h3>
                  <div class="detail-box">
                    Al cambiar la categoría de producto con stock existente:
                    <ul class="styled-list" style="margin-top:8px;">
                      <li><strong>Cero pólizas de ajuste:</strong> Odoo no genera asientos contables sobre las existencias anteriores.</li>
                      <li><strong>Brecha silenciosa:</strong> Las unidades físicas quedan flotando sin contrapartida en la cuenta 1150.</li>
                      <li><strong>Regla Vauxoo:</strong> La categoría de producto no es un área de juegos. Modificarla en producción exige corte formal de saldos y reclasificación planificada.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 7: Bloque 3 - Caso 1: Flujo Limpio en MXN (WIDGET-MX)
        {
            "id": 7,
            "title": "Caso 1: Flujo Limpio en MXN",
            "bg": "white",
            "time": "00:17 - 00:25",
            "block": "Bloque 3",
            "notes": "Mostrar el flujo limpio en MXN con el producto [WIDGET-MX] Widget Nacional MX (AVCO). 50u @ $150 + 50u @ $170 = 100u @ $160 MXN. Venta y entrega de 30 unidades a $160 MXN -> Asiento directo: Cargo 501.01.01 / Abono 115.01.01 por $4,800.00 MXN. Cero cuentas intermedias.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 1 (8 MIN)</span>
                  <h2 class="slide-title">Flujo Limpio en MXN: Ponderación AVCO Directa</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[WIDGET-MX] Widget Nacional MX (AVCO)</code>. Ponderación matemática en moneda base:</p>
              
              <div class="flow-steps-grid">
                <div class="flow-step-card">
                  <div class="step-badge">1. COMPRA Y PONDERACIÓN</div>
                  <h4>Entrada Física Progresiva</h4>
                  <p>Lote 1: 50 piezas @ $150.00 MXN<br>Lote 2: 50 piezas @ $170.00 MXN</p>
                  <div class="asiento-box">
                    Nuevo AVCO = (50×150 + 50×170) / 100<br>
                    <strong>Nuevo AVCO = $160.00 MXN / pieza</strong>
                  </div>
                  <div class="step-avco">Total en almacén: 100 piezas = <strong>$16,000.00 MXN</strong></div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">2. VENTA Y ENTREGA AL CLIENTE</div>
                  <h4>Salida de 30 Unidades</h4>
                  <p>Salida inmediata al AVCO vigente ponderado ($160 MXN).</p>
                  <div class="asiento-box">
                    <div class="asiento-row"><span class="cargo">CARGO</span> 501.01.01 Costo de Ventas <strong>$4,800.00 MXN</strong></div>
                    <div class="asiento-row"><span class="abono">ABONO</span> 115.01.01 Inventarios <strong>$4,800.00 MXN</strong></div>
                  </div>
                  <div class="step-avco">Cálculo exacto: 30 unidades &times; $160.00 MXN</div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">3. SALDO REMANENTE</div>
                  <h4>Transparencia en Odoo 19</h4>
                  <p>Almacén físico: 70 piezas remanentes.</p>
                  <div class="asiento-box">
                    Saldo Contable Cuenta 115.01.01: <strong>$11,200.00 MXN</strong><br>
                    Valoración Logística: 70 &times; $160 = <strong>$11,200.00 MXN</strong>
                  </div>
                  <div class="step-avco">✅ En v19 vemos la mitad de apuntes que en v18. Flujo limpio y sin intermediarios.</div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 8: Bloque 3 - Caso 2: Compras en USD y Costos en Destino
        {
            "id": 8,
            "title": "Caso 2: Compras USD y Landed Costs",
            "bg": "gradient",
            "time": "00:25 - 00:37",
            "block": "Bloque 3",
            "notes": "Mostrar el caso de compras en USD y Costos en Destino: PO en USD a $100 USD. Al recibir en almacén, Odoo toma el TC DOF de recepción ($18.50) -> $1,850.00 MXN/u. Llega la factura de fletes y maniobras por $5,000 MXN vía Costos en Destino (Landed Costs). El sistema reparte +$250 MXN a cada sensor, subiendo el AVCO de $1,850 a $2,100.00 MXN.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 2 (12 MIN)</span>
                  <h2 class="slide-title" style="color: #fff;">Compras en USD y Landed Costs (Gastos Aduanales)</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                PO internacional en USD y asignación obligatoria de gastos de importación según el Art. 39 de la Ley del ISR:
              </p>
              
              <div class="usd-timeline" style="grid-template-columns: repeat(3, 1fr);">
                <div class="timeline-step">
                  <div class="timeline-dot">1</div>
                  <div class="timeline-header">RECEPCIÓN FÍSICA EN USD</div>
                  <div class="timeline-body">
                    <p>PO en dólares a $100 USD (20 unidades).</p>
                    <div class="tc-badge" style="background:#AC0340;">TC DOF Recepción: $18.50 MXN</div>
                    <div class="timeline-val">Costo Inicial: $1,850.00 MXN / u</div>
                    <small>El costo lo fija la fecha de recepción física, NO la orden de compra.</small>
                  </div>
                </div>

                <div class="timeline-step">
                  <div class="timeline-dot">2</div>
                  <div class="timeline-header">GASTOS DE IMPORTACIÓN</div>
                  <div class="timeline-body">
                    <p>Factura de fletes aduanales por <strong>$5,000.00 MXN</strong>.</p>
                    <div class="tc-badge">Landed Cost Reparto</div>
                    <div class="timeline-val">Prorrateo: +$250.00 MXN / unidad</div>
                    <small>Asignación vinculada formalmente al albarán de entrada.</small>
                  </div>
                </div>

                <div class="timeline-step">
                  <div class="timeline-dot">3</div>
                  <div class="timeline-header">RECÁLCULO AVCO EN ODOO 19</div>
                  <div class="timeline-body">
                    <p>El sistema incrementa el valor en almacén.</p>
                    <div class="tc-badge" style="background:#16A34A;">Nuevo AVCO Oficial</div>
                    <div class="timeline-val doodle-wrap">$2,100.00 MXN / unidad {doodle_underline}</div>
                    <small>Cumplimiento estricto del Art. 39 LISR (costo capitalizado).</small>
                  </div>
                </div>
              </div>

              <div class="usd-verdict-box">
                <div class="verdict-col">
                  <h4>💡 El Error Desmentido</h4>
                  <p>Muchos contadores mandan los fletes a gastos de administración (601) para evitar configurar Landed Costs: <strong>esto subvalúa el inventario y distorsiona el margen fiscal</strong>.</p>
                </div>
                <div class="verdict-col">
                  <h4>🛡️ Blindaje Fiscal SAT</h4>
                  <p>En Odoo 19, Costos en Destino inyecta el valor monetario directamente al movimiento de almacén, preservando la trazabilidad deducible para la Declaración Anual.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 9: Bloque 4 - La Clínica de Desastres: Resumen (16 min)
        {
            "id": 9,
            "title": "La Clínica de Desastres (16 min)",
            "bg": "white",
            "time": "00:37 - 00:53",
            "block": "Bloque 4",
            "notes": "Introducción al Bloque 4: La Clínica de los Desastres (16 min totales, exactamente 4 min por desastre). Los 4 errores que destruyen la deducción fiscal del costo de ventas ante el SAT.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">BLOQUE 4 · 00:37 - 00:53 (16 MIN)</span>
                  <h2 class="slide-title">La Clínica de los Desastres: 4 Errores que Cuestan Millones</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">4 minutos exactos por cada desastre recurrente en las empresas mexicanas:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(2, 1fr); gap: 20px;">
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">DESASTRE 1 (00:37 - 00:41 | 4 MIN)</div>
                  <div class="agenda-title">Stock Negativo con AVCO</div>
                  <p class="agenda-desc">Producto <code>[VALVULA-NEG]</code>: Vender sin existencia fractura el divisor matemático del promedio ponderado y genera observaciones del SAT por kardex negativo.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">DESASTRE 2 (00:41 - 00:45 | 4 MIN)</div>
                  <div class="agenda-title">Tipo de Cambio Erróneo en Recepciones</div>
                  <p class="agenda-desc">Capturar tasas comerciales o dejar valores por omisión en lugar del DOF. Errores de centavos distorsionan decenas de miles de pesos en el costo promedio.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">DESASTRE 3 (00:45 - 00:49 | 4 MIN)</div>
                  <div class="agenda-title">Mermas y Ajustes de Conteo Físico</div>
                  <p class="agenda-desc">Producto <code>[CABLE-MERMA]</code>: Reducir cantidad manteniendo el costo unitario ($85 MXN). El faltante debe ir a gasto por merma sin destruir el costo del stock restante.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">DESASTRE 4 (00:49 - 00:53 | 4 MIN)</div>
                  <div class="agenda-title">Inventario Obsoleto y NIF C-4</div>
                  <p class="agenda-desc">Producto <code>[TARJETA-OBS]</code>: Jamás reducir el costo unitario en Odoo. La pérdida se reconoce en cuenta complementaria de activo (<code>108.02.01</code>).</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 10: Bloque 4 - Desastre 1: Stock Negativo (VALVULA-NEG)
        {
            "id": 10,
            "title": "Desastre 1: Stock Negativo (VALVULA-NEG)",
            "bg": "white",
            "time": "00:37 - 00:41",
            "block": "Bloque 4",
            "notes": "Demostración de VALVULA-NEG: Existencia en 0, venta y entrega de -10 unidades. Al recibir una compra a precio distinto, la fórmula ponderada se fractura. Recordar: Kardex negativo es observación segura y rechazo de deducciones por el SAT.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">DESASTRE 1 · 00:37 - 00:41 (4 MIN)</span>
                  <h2 class="slide-title">El Veneno Matemático: Stock Negativo con AVCO</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[VALVULA-NEG] Válvula Reguladora</code>. ¿Qué pasa cuando vendes lo que no tienes?</p>
              
              <div class="disaster-grid">
                <div class="disaster-main">
                  <h3>Secuencia de la Fractura Matemática:</h3>
                  <div class="disaster-sequence">
                    <div class="seq-step">
                      <span class="seq-num">1</span>
                      <div>Stock inicial en 0. Se confirma venta y entrega física por <strong>-10 unidades</strong>.</div>
                    </div>
                    <div class="seq-step">
                      <span class="seq-num">2</span>
                      <div>Odoo saca el producto con costo provisional ($200.00 MXN o $0.00).</div>
                    </div>
                    <div class="seq-step">
                      <span class="seq-num">3</span>
                      <div>Días después entra la compra real de 15 piezas a $350.00 MXN.</div>
                    </div>
                    <div class="seq-step" style="background: #FEE2E2; border: 1px solid #FCA5A5;">
                      <span class="seq-num" style="background:#B91C1C;">💥</span>
                      <div><strong>Colapso del divisor matemático:</strong> El sistema promedia cantidades negativas con positivas, generando costos distorsionados de <strong>$1,850 MXN o números negativos</strong>.</div>
                    </div>
                  </div>
                </div>

                <div class="disaster-sat">
                  <div class="sat-warn-card">
                    <h4>⚖️ Contingencia Fiscal SAT</h4>
                    <ul class="styled-list">
                      <li><strong>Kardex Ilegal:</strong> El SAT prohíbe inventarios negativos en la contabilidad electrónica.</li>
                      <li><strong>Rechazo de Costo de Ventas:</strong> Pérdida de deducción fiscal en la Declaración Anual.</li>
                      <li><strong>Multas por Inconsistencia:</strong> Sanciones aplicables por auditoría de comercio o inventario.</li>
                    </ul>
                    <div class="sat-rule-badge">REGLA VAUXOO: Prohibir entregas sin stock en categorías AVCO</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 11: Bloque 4 - Desastre 2: Tipo de Cambio Erróneo en Recepciones
        {
            "id": 11,
            "title": "Desastre 2: Tipo de Cambio Erróneo",
            "bg": "white",
            "time": "00:41 - 00:45",
            "block": "Bloque 4",
            "notes": "Desastre 2: Capturar tasas comerciales o dejar valores por omisión en lugar del DOF. En importaciones de alto volumen, un error de 50 centavos genera distorsiones de decenas de miles de pesos en el costo promedio.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">DESASTRE 2 · 00:41 - 00:45 (4 MIN)</span>
                  <h2 class="slide-title">Tipo de Cambio Erróneo en Recepciones de Importación</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">La tasa cambiaria oficial en la fecha de cruce físico es innegociable bajo el Art. 20 del CFF:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">EL ERROR HABITUAL</div>
                  <h3>Dejar la Tasa por Defecto en Odoo</h3>
                  <div class="detail-box">
                    Odoo tiene una tasa de cambio cargada de hace dos semanas ($18.00 MXN/USD). Al validar la recepción física de mercancía importada por $50,000 USD, se utiliza esa tasa.
                    <br><br>
                    <strong>La realidad aduanal:</strong> El pedimento aduanal y el DOF marcaron una tasa oficial de <strong>$18.65 MXN/USD</strong>.
                    <br><br>
                    <strong>La distorsión:</strong> Una diferencia de 65 centavos por dólar subvalúa el inventario en <strong>$32,500.00 MXN</strong> de entrada, corrompiendo el AVCO.
                  </div>
                </div>

                <div class="disaster-col-card">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">EL BLINDAJE VAUXOO</div>
                  <h3>Actualización Diaria DOF & Pedimento</h3>
                  <div class="detail-box">
                    En compras internacionales en México:
                    <ul class="styled-list" style="margin-top:8px;">
                      <li>Sincronización automatizada o captura de la tasa DOF del día oficial de entrada.</li>
                      <li>Validar que el albarán físico tome la tasa del pedimento aduanal.</li>
                      <li>Evita auditorías de comercio exterior y discrepancias con la balanza fiscal del SAT.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 12: Bloque 4 - Desastre 3 y 4: Mermas y Obsolescencia NIF C-4
        {
            "id": 12,
            "title": "Desastre 3 y 4: Mermas y Obsolescencia",
            "bg": "white",
            "time": "00:45 - 00:53",
            "block": "Bloque 4",
            "notes": "Desastre 3 (CABLE-MERMA): Faltan 15m @ $85 MXN. El ajuste reduce CANTIDAD, manteniendo el costo unitario ($85). El faltante va a gasto por merma. Desastre 4 (TARJETA-OBS): Jamás reducir el costo unitario del producto en Odoo. La pérdida se reconoce en cuenta complementaria 108.02.01 Estimación de obsolescencia.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">DESASTRES 3 Y 4 · 00:45 - 00:53 (8 MIN)</span>
                  <h2 class="slide-title">Mermas de Conteo Físico & Obsolescencia NIF C-4</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">DESASTRE 3: MERMAS (CABLE-MERMA)</div>
                  <h3>Conteo Físico: Faltan 15 Metros</h3>
                  <div class="detail-box">
                    <strong>La regla contable:</strong> El ajuste de inventario en Odoo 19 debe reducir <strong>CANTIDAD</strong>, manteniendo intacto el costo unitario ($85.00 MXN).
                    <br><br>
                    <strong>Destino contable:</strong> El faltante (15m &times; $85 = $1,275 MXN) se envía a una cuenta de <strong>Gasto por Merma</strong> (cuidando actas de pérdida para deducibilidad SAT), evitando que el SAT lo catalogue como venta omitida.
                  </div>
                </div>

                <div class="disaster-col-card">
                  <div class="card-pill">DESASTRE 4: OBSOLESCENCIA (TARJETA-OBS)</div>
                  <h3>Inventario de Lento Movimiento</h3>
                  <div class="detail-box">
                    <strong>El error garrafal:</strong> Reducir el costo unitario del producto en Odoo a $0.00 MXN.
                    <br><br>
                    <strong>La solución NIF C-4:</strong> Mantener el costo AVCO en Odoo y reconocer la pérdida en balance mediante una póliza manual en la cuenta complementaria de activo:
                    <div class="asiento-box" style="margin-top:6px;">
                      <span class="cargo">CARGO</span> Gasto Estimación Obsolescencia<br>
                      <span class="abono">ABONO</span> 108.02.01 Estimación de Obsolescencia
                    </div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 13: Bloque 5 - Causa Raíz #3: La Matriz de Cadencia
        {
            "id": 13,
            "title": "Causa Raíz #3: Matriz de Cadencia",
            "bg": "gradient",
            "time": "00:53 - 00:58",
            "block": "Bloque 5",
            "notes": "Parte A del Bloque 5: La Causa Raíz #3 - La Cadencia de Auditoría (5 min). Encuesta relámpago al chat: ¿Cada cuánto auditan el inventario contable contra el almacén? Presentar la Matriz de Cadencia Vauxoo (Diaria, Semanal, Mensual, Anual).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · PARTE A (00:53 - 00:58)</span>
                  <h2 class="slide-title" style="color: #fff;">Causa Raíz #3: La Cadencia de Auditoría</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                Encuesta al chat: <em>"¿Cada cuánto cruzan la cuenta 1150 contra el reporte de existencias?"</em>
              </p>
              
              <div class="sat-fiscal-table-container">
                <table class="sat-fiscal-table" style="background:rgba(255,255,255,0.06); color:#fff;">
                  <thead>
                    <tr style="background:#1E293B;">
                      <th>Frecuencia</th>
                      <th>Calificación</th>
                      <th>Esfuerzo de Revisión</th>
                      <th>Impacto en el Negocio</th>
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
                      <td>Estándar indispensable para el cierre formal y checklist contable.</td>
                    </tr>
                    <tr>
                      <td><strong>Anual</strong></td>
                      <td>❌ <span class="pill-badge" style="background:#B91C1C;">EVITARLO A TODA COSTA</span></td>
                      <td>Semanas de reconstrucción</td>
                      <td>3,000+ movimientos acumulados; laberinto indescifrable y costo destructivo.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            '''
        },
        # Slide 14: Bloque 5 - Causa Raíz #2: Caza de la Póliza Manual (MISC/2026/09/0001)
        {
            "id": 14,
            "title": "Caza de la Póliza Manual Intrusa",
            "bg": "white",
            "time": "00:58 - 01:03",
            "block": "Bloque 5",
            "notes": "Parte B del Bloque 5: Causa Raíz #2 - Caza de la Póliza Manual y Resolución del Hook (5 min). Regreso a las pantallas del Hook: diferencia de $411,275 MXN. Demostración de auditoría en vivo en 115.01.01 > Apuntes contables, filtrar Documento Origen = False. Descubrimiento de la póliza MISC/2026/09/0001 por $487,000.00 MXN.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · PARTE B (00:58 - 01:03)</span>
                  <h2 class="slide-title">Causa Raíz #2: Caza de la Póliza Manual en Vivo</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Resolviendo el misterio de los <strong>$411,275.00 MXN</strong> del Bloque 1 en menos de 5 minutos:</p>
              
              <div class="resolution-container">
                <div class="culprit-box">
                  <div class="culprit-badge">🔍 PÓLIZA MANUAL DETECTADA EN LA BD</div>
                  <h3>Póliza <code>MISC/2026/09/0001</code> por $487,000.00 MXN</h3>
                  <div class="culprit-desc">
                    El contador anterior, bajo la presión de un cierre y sin visibilidad del almacén, metió una póliza manual directa a la cuenta <strong>115.01.01</strong> contra la 501.01.02 para forzar un cuadre provisional.
                  </div>
                  <div class="culprit-flaw">
                    ❌ La "aspirina manual": Una póliza manual NUNCA crea un Stock Move físico. Infló la contabilidad artificialmente, rompiendo la paridad con el almacén.
                  </div>
                </div>

                <div class="action-result-box">
                  <div class="result-step">
                    <strong>Paso Quirúrgico en Odoo 19:</strong> Cancelación / Reclasificación de la póliza <code>MISC/2026/09/0001</code>.
                  </div>
                  <div class="balanced-state">
                    <div class="bal-item">
                      <span>Balanza de Comprobación (Cuenta 115.01.01)</span>
                      <strong>$75,925.00 MXN</strong>
                    </div>
                    <div class="bal-equal">=</div>
                    <div class="bal-item">
                      <span>Reporte de Existencias / Valoración</span>
                      <strong>$75,925.00 MXN</strong>
                    </div>
                    <div class="bal-status">
                      ✅ CUADRE PERFECTO AL CENTAVO (Diferencia: $0.00 MXN)
                    </div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 15: Bloque 5 - Las 3 Reglas de Oro Blindadas de Vauxoo
        {
            "id": 15,
            "title": "Las 3 Reglas de Oro Blindadas",
            "bg": "white",
            "time": "01:03 - 01:07",
            "block": "Bloque 5",
            "notes": "Parte C del Bloque 5: Las 3 Reglas de Oro Blindadas de Vauxoo (4 min). 1. Cero Asientos Manuales en la 1150 (bloquear por permisos); 2. Cero Stock Negativo; 3. Configuración y Cadencia Disciplinada.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MEJORES PRÁCTICAS VAUXOO</span>
                  <h2 class="slide-title">Las 3 Reglas de Oro Blindadas de Vauxoo</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Los 3 mandamientos para no volver a tener un divorcio entre contabilidad y almacén:</p>
              
              <div class="golden-rules-grid">
                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #1</div>
                  <h3>Cero Asientos Manuales en la 1150</h3>
                  <p>Restringir por permisos de seguridad que los usuarios creen pólizas manuales de diario en cuentas de inventario. Todo ajuste debe nacer exclusivamente de un movimiento logístico documentado.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #2</div>
                  <h3>Cero Stock Negativo en AVCO</h3>
                  <p>Bloquear salidas y despachos sin existencia física en todas las categorías con Costo Promedio. El stock negativo destruye la integridad matemática del kardex ante el SAT.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #3</div>
                  <h3>Configuración y Cadencia Disciplinada</h3>
                  <p>Categorías de producto inmutables una vez en producción. Y adopción de una disciplina de auditoría semanal cruzando <em>Balanza vs Existencias</em> con el checklist oficial.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 16: Bloque 6 - Q&A Hot Seat (23 min)
        {
            "id": 16,
            "title": "Bloque 6: Q&A Hot Seat (23 min)",
            "bg": "gradient",
            "time": "01:07 - 01:28",
            "block": "Bloque 6",
            "notes": "Bloque 6: Q&A Hot Seat - Consultoría en Vivo (23 minutos). Los asistentes exponen sus dudas, casuísticas de comercio exterior o descuadres reales en vivo. Julio responde en pantalla compartida sobre la base de datos de Odoo 19.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 6 · 01:07 - 01:30 (23 MIN)</span>
                  <h2 class="slide-title" style="color: #fff;">Q&A Hot Seat: Consultoría en Vivo</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              
              <div class="hotseat-container">
                <div class="hotseat-badge-col">
                  <div class="hotseat-icon">🔥</div>
                  <h3>Micrófono Abierto</h3>
                  <p>23 minutos dedicados a resolver tus peores dolores de valoración e importaciones en Odoo 19.</p>
                </div>
                <div class="hotseat-topics">
                  <h4>Casuísticas Prioritarias para la Sesión:</h4>
                  <ul class="styled-list" style="color: rgba(255,255,255,0.9);">
                    <li>¿Tienes descuadres históricos acumulados arrastrados desde v16 o v18?</li>
                    <li>¿Dudas con el reparto de Landed Costs en recepciones parciales?</li>
                    <li>¿Cómo corregir categorías mal configuradas sin corromper la balanza del SAT?</li>
                    <li>¿Tratamiento de mermas y destrucciones autorizadas ante auditorías fiscales?</li>
                  </ul>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 17: Paquete de Entregables Oficiales
        {
            "id": 17,
            "title": "Paquete de Entregables Oficiales",
            "bg": "white",
            "time": "01:28 - 01:30",
            "block": "Bloque 6",
            "notes": "Presentación de los entregables: 1. Checklist de Auditoría Logística-Contable MX con Matriz de Cadencia; 2. Tabla de Mapeo Conceptual v18 -> v19; 3. Grabación HD con capítulos; 4. Certificado de Vauxoo Academy.",
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
                  <p>Guía de validación de 4 fases para auditorías diarias, semanales y mensuales en Odoo 19 MX.</p>
                  <a href="#tab-checklist" onclick="switchTab('checklist')" class="btn btn-sm">Ver Checklist</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">📊</div>
                  <h4>Entregable #2: Tabla de Mapeo 18 → 19</h4>
                  <p>Comparativa conceptual de arquitectura: Stock Moves, cuentas puente y reglas de oro SAT.</p>
                  <a href="#tab-mapeo" onclick="switchTab('mapeo')" class="btn btn-sm">Ver Mapeo & SAT</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">🎥</div>
                  <h4>Grabación en Alta Definición</h4>
                  <p>Acceso permanente a la grabación completa indexada por bloques y capítulos para tu equipo.</p>
                  <span class="pill-badge-outline" style="color:#64748B; border-color:#CBD5E1;">Acceso permanente</span>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">🎓</div>
                  <h4>Certificado Vauxoo Academy</h4>
                  <p>Acreditación digital oficial de aprovechamiento en Valoración de Inventarios en Odoo 19.</p>
                  <span class="pill-badge-outline" style="color:#64748B; border-color:#CBD5E1;">Emisión oficial</span>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 18: Cierre y Contacto
        {
            "id": 18,
            "title": "Cierre y Agradecimientos",
            "bg": "gradient",
            "time": "01:30",
            "block": "Cierre",
            "notes": "Agradecimiento final. Invitación para proyectos de diagnóstico e implementación con Vauxoo. Cierre de la sesión.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-logo-wrap">
                {logo_white}
              </div>
              <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 12px; color: #fff;">
                Aprende. Evoluciona. Transforma.
              </h2>
              <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); max-width: 650px; margin: 0 auto 32px;">
                Gracias por acompañarnos. Tu almacén y tu contabilidad ahora operan con la misma verdad.
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

print("Plan final v4 slides module compiled successfully.")
