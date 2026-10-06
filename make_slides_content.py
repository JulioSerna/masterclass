#!/usr/bin/env python3
# Content for all slides of the Masterclass 2026
# ADJUSTED PER USER REQUIREMENTS:
# - Slide 1: Remove "Arquitectura de Costo Promedio (AVCO), Compras en USD, Landed Costs y Blindaje Contable-Fiscal ante el SAT."
# - Slide 3 (former 4): Remove "Pregunta al chat: '¿A quién le ha tocado explicarle este descuadre...'"
# - Former Slide 5: Removed (demasiado técnica)
# - Former Slide 9: Removed mention of NIF C-4
# - Former Slide 10: Removed "Contingencia Fiscal SAT" section
# - Former Slide 11: Removed entirely
# - Former Slide 12: Removed entirely

def get_slides(doodle_oval, doodle_arrow, doodle_underline, logo_white, logo_light):
    return [
        # Slide 1: Portada Oficial (Subtitle cleaned)
        {
            "id": 1,
            "title": "Portada Oficial",
            "bg": "gradient",
            "time": "00:00",
            "block": "Apertura",
            "notes": "Bienvenida de Julio Serna (PM y Experto Funcional en Vauxoo). Masterclass 2026 de Vauxoo Academy. Reglas de la sesión: 90 minutos enfocados en la trinchera contable y logística mexicana en Odoo 19.0 Enterprise.",
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
        # Slide 2: El Marco Narrativo - Las 3 Causas Raíz
        {
            "id": 2,
            "title": "Las 3 Causas Raíz del Divorcio",
            "bg": "white",
            "time": "00:01 - 00:04",
            "block": "Marco Narrativo",
            "notes": "Presentar el hilo conductor de toda la masterclass: las 3 causas raíz detectadas en implementaciones en México. 1. Configuración errática; 2. Parches operativos manuales; 3. Auditoría tardía por falta de cadencia.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MARCO NARRATIVO</span>
                  <h2 class="slide-title">Las 3 Causas Raíz del Divorcio Almacén-Contabilidad</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">La experiencia en implementaciones demuestra que el descuadre nace de 3 vicios principales:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(3, 1fr);">
                <div class="agenda-card" style="border-top: 4px solid #1E293B;">
                  <div class="agenda-time">CONFIGURACIÓN</div>
                  <div class="agenda-num">01</div>
                  <div class="agenda-title">CONFIGURACIÓN ERRÁTICA</div>
                  <p class="agenda-desc"><strong>"Dos malas no hacen una buena."</strong> Cambiar métodos en caliente (periódico ↔ perpetuo o standard ↔ AVCO) sin considerar que Odoo 19 no genera pólizas retroactivas automáticas.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">OPERACIÓN</div>
                  <div class="agenda-num">02</div>
                  <div class="agenda-title">PARCHES OPERATIVOS</div>
                  <p class="agenda-desc"><strong>"La aspirina manual."</strong> El contador, presionado por el cierre mensual, mete pólizas manuales directas a la cuenta 1150 rompiendo la paridad con el kardex físico.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #475569;">
                  <div class="agenda-time">CONTROL</div>
                  <div class="agenda-num">03</div>
                  <div class="agenda-title">AUDITORÍA TARDÍA</div>
                  <p class="agenda-desc"><strong>"El costo de la infrecuencia."</strong> Esperar al cierre anual cuando hay miles de movimientos acumulados hace que encontrar la desviación sea una pesadilla de semanas.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 3: El Hook - El Descuadre que Todos Conocen (Sin pregunta al chat de SAT/Director)
        {
            "id": 3,
            "title": "El Hook: Descuadre de $411,275 MXN",
            "bg": "white",
            "time": "00:04 - 00:09",
            "block": "Bloque 1",
            "notes": "Mostrar el split view con los números exactos: Balanza 115.01.01 ($487,200.00 MXN) vs Reporte de Existencias ($75,925.00 MXN) -> Descuadre real de $411,275.00 MXN.",
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
                  <strong>El objetivo de la sesión:</strong> Identificar el origen exacto de esta diferencia de $411,275 MXN y resolverla en vivo durante la sesión.
                </span>
              </div>
            </div>
            '''
        },
        # Slide 4: Causa Raíz #1 - La Trampa de las Configuraciones en Caliente
        {
            "id": 4,
            "title": "Causa Raíz #1: Cambios en Caliente",
            "bg": "white",
            "time": "00:09 - 00:15",
            "block": "Bloque 2",
            "notes": "Alerta técnica clave: Odoo 19 NO genera asientos contables retroactivos cuando se cambia de método de costeo o valuación en caliente si ya existen movimientos de stock.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CAUSA RAÍZ #1 · CONFIGURACIÓN</span>
                  <h2 class="slide-title">La Trampa de los Cambios de Configuración en Caliente</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Principio operativo en almacén: <strong>"Dos configuraciones malas no hacen una buena."</strong></p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">EL ERROR HABITUAL</div>
                  <h3>Cambiar Métodos sin Protocolo</h3>
                  <div class="detail-box">
                    Arrancar una empresa con valoración periódica (manual). Meses después, cambiar la categoría a automatizada/perpetua, o alternar entre métodos de costeo.
                    <br><br>
                    <strong>La suposición errónea:</strong> Asumir que el sistema recalculará automáticamente el histórico y creará los asientos retroactivos pendientes.
                  </div>
                </div>

                <div class="disaster-col-card" style="border: 2px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">COMPORTAMIENTO TÉCNICO EN ODOO 19</div>
                  <h3>Odoo 19 NO Genera Asientos Retroactivos</h3>
                  <div class="detail-box">
                    Al cambiar la categoría de producto con stock previo:
                    <ul class="styled-list" style="margin-top:8px;">
                      <li><strong>Sin pólizas automáticas:</strong> Odoo no genera asientos contables sobre las existencias anteriores.</li>
                      <li><strong>Brecha contable:</strong> El inventario previo queda sin registro en la cuenta 1150.</li>
                      <li><strong>Buenas prácticas:</strong> Los cambios de método en producción requieren corte de inventario y asientos de reclasificación programados.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 5: Bloque 3 - Caso 1: Flujo Limpio en MXN (WIDGET-MX)
        {
            "id": 5,
            "title": "Caso 1: Flujo Limpio en MXN",
            "bg": "white",
            "time": "00:15 - 00:25",
            "block": "Bloque 3",
            "notes": "Mostrar el flujo limpio en MXN con el producto [WIDGET-MX] Widget Nacional MX (AVCO). 50u @ $150 + 50u @ $170 = 100u @ $160 MXN. Venta y entrega de 30 unidades a $160 MXN -> Asiento directo: Cargo 501.01.01 / Abono 115.01.01 por $4,800.00 MXN.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 1</span>
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
                  <div class="step-avco">✅ En Odoo 19 el flujo contable-logístico es directo y sin cuentas intermedias.</div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 6: Bloque 3 - Caso 2: Compras en USD y Costos en Destino (Landed Costs)
        {
            "id": 6,
            "title": "Caso 2: Compras USD y Landed Costs",
            "bg": "gradient",
            "time": "00:25 - 00:37",
            "block": "Bloque 3",
            "notes": "Mostrar compras en USD y Costos en Destino: PO a $100 USD. Al recibir en almacén, Odoo toma el TC DOF de recepción ($18.50) -> $1,850.00 MXN/u. Llega la factura de fletes por $5,000 MXN vía Costos en Destino (Landed Costs). Se reparten +$250 MXN/u, subiendo el AVCO a $2,100.00 MXN.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 2</span>
                  <h2 class="slide-title" style="color: #fff;">Compras en USD y Landed Costs (Gastos de Importación)</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                Órdenes de compra en USD y asignación de gastos de logística y fletes al costo del producto:
              </p>
              
              <div class="usd-timeline" style="grid-template-columns: repeat(3, 1fr);">
                <div class="timeline-step">
                  <div class="timeline-dot">1</div>
                  <div class="timeline-header">RECEPCIÓN FÍSICA EN USD</div>
                  <div class="timeline-body">
                    <p>PO en dólares a $100 USD (20 unidades).</p>
                    <div class="tc-badge" style="background:#AC0340;">TC Fecha Recepción: $18.50 MXN</div>
                    <div class="timeline-val">Costo Inicial: $1,850.00 MXN / u</div>
                    <small>El costo lo fija la fecha de recepción física en almacén.</small>
                  </div>
                </div>

                <div class="timeline-step">
                  <div class="timeline-dot">2</div>
                  <div class="timeline-header">GASTOS DE IMPORTACIÓN</div>
                  <div class="timeline-body">
                    <p>Factura de fletes y maniobras por <strong>$5,000.00 MXN</strong>.</p>
                    <div class="tc-badge">Landed Cost Reparto</div>
                    <div class="timeline-val">Prorrateo: +$250.00 MXN / unidad</div>
                    <small>Asignación vinculada al albarán de entrada correspondiente.</small>
                  </div>
                </div>

                <div class="timeline-step">
                  <div class="timeline-dot">3</div>
                  <div class="timeline-header">RECÁLCULO AVCO EN ODOO 19</div>
                  <div class="timeline-body">
                    <p>El sistema actualiza el valor unitario en almacén.</p>
                    <div class="tc-badge" style="background:#16A34A;">Nuevo AVCO Calculado</div>
                    <div class="timeline-val doodle-wrap">$2,100.00 MXN / unidad {doodle_underline}</div>
                    <small>Costo unitario capitalizado en el producto.</small>
                  </div>
                </div>
              </div>

              <div class="usd-verdict-box">
                <div class="verdict-col">
                  <h4>💡 Buenas Prácticas de Costeo</h4>
                  <p>Incorporar fletes y maniobras al costo del inventario permite reflejar el valor real de reposición y margen comercial de los productos adquiridos en el extranjero.</p>
                </div>
                <div class="verdict-col">
                  <h4>🛡️ Automatización en Odoo 19</h4>
                  <p>En Odoo 19, Costos en Destino inyecta el valor monetario directamente al movimiento de almacén correspondiente sin requerir cálculos externos.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 7: Resumen de Errores Operativos Comunes (Sin mención a NIF C-4)
        {
            "id": 7,
            "title": "Errores Operativos Comunes en Inventario",
            "bg": "white",
            "time": "00:37 - 00:45",
            "block": "Bloque 4",
            "notes": "Revisión de errores operativos habituales: Stock negativo con AVCO, desfase cambiario en recepciones y manejo de mermas físicas.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">BLOQUE 4 · OPERACIÓN</span>
                  <h2 class="slide-title">Errores Operativos Comunes en la Gestión de Inventarios</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Situaciones de la operativa diaria que distorsionan el costo y la contabilidad:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(2, 1fr); gap: 20px;">
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">OPERACIÓN #1</div>
                  <div class="agenda-title">Stock Negativo con AVCO</div>
                  <p class="agenda-desc">Producto <code>[VALVULA-NEG]</code>: Permitir despachos sin existencias en almacén altera el cálculo del promedio ponderado al ingresar nuevas compras.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">OPERACIÓN #2</div>
                  <div class="agenda-title">Desfase Cambiario en Recepciones</div>
                  <p class="agenda-desc">Usar tipos de cambio desactualizados al momento de recibir mercancía en USD genera inconsistencias en la valoración inicial del almacén.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">OPERACIÓN #3</div>
                  <div class="agenda-title">Mermas y Ajustes de Conteo Físico</div>
                  <p class="agenda-desc">Producto <code>[CABLE-MERMA]</code>: El ajuste por conteo físico debe reducir únicamente cantidad, preservando el costo unitario del inventario restante.</p>
                </div>
                <div class="agenda-card" style="border-left: 4px solid #B91C1C;">
                  <div class="agenda-time">OPERACIÓN #4</div>
                  <div class="agenda-title">Artículos de Lento Movimiento</div>
                  <p class="agenda-desc">Producto <code>[TARJETA-OBS]</code>: Evitar modificar el costo unitario a cero en la ficha del producto; los ajustes de valor deben manejarse mediante cuentas contables correspondientes.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 8: Desastre Operativo - Stock Negativo con AVCO (Sin Contingencia Fiscal SAT)
        {
            "id": 8,
            "title": "Stock Negativo con AVCO (VALVULA-NEG)",
            "bg": "white",
            "time": "00:45 - 00:53",
            "block": "Bloque 4",
            "notes": "Demostración de VALVULA-NEG: Existencia en 0, entrega física por -10 unidades. Al recibir compra posterior a precio distinto, la fórmula ponderada sufre distorsión. Regla: Prohibir entregas sin stock.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">OPERACIÓN · CASO PRÁCTICO</span>
                  <h2 class="slide-title">Impacto Matemático del Stock Negativo en AVCO</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[VALVULA-NEG] Válvula Reguladora</code>. Comportamiento del costo al despachar sin existencias:</p>
              
              <div class="two-col-grid">
                <div class="disaster-main">
                  <h3>Secuencia de la Distorsión Matemática:</h3>
                  <div class="disaster-sequence">
                    <div class="seq-step">
                      <span class="seq-num">1</span>
                      <div>Existencia inicial en 0. Se confirma venta y entrega de <strong>10 unidades sin stock</strong>.</div>
                    </div>
                    <div class="seq-step">
                      <span class="seq-num">2</span>
                      <div>Odoo procesa la salida provisional con el costo de referencia anterior ($200.00 MXN).</div>
                    </div>
                    <div class="seq-step">
                      <span class="seq-num">3</span>
                      <div>Días después ingresa compra real de 15 piezas a $350.00 MXN.</div>
                    </div>
                    <div class="seq-step" style="background: #FEE2E2; border: 1px solid #FCA5A5;">
                      <span class="seq-num" style="background:#B91C1C;">⚠️</span>
                      <div><strong>Distorsión del promedio:</strong> El recálculo combina existencias negativas con positivas, generando fluctuaciones anómalas en el costo unitario resultante.</div>
                    </div>
                  </div>
                </div>

                <div class="disaster-sat">
                  <div class="sat-warn-card" style="border-left: 4px solid var(--azul-marino);">
                    <h4 style="color:var(--azul-marino);">🛡️ Recomendación Operativa</h4>
                    <ul class="styled-list">
                      <li><strong>Bloqueo de despachos:</strong> Configurar las rutas y almacenes para evitar salidas automáticas cuando la existencia sea insuficiente.</li>
                      <li><strong>Integridad del Kardex:</strong> Mantener saldos positivos garantiza que el valor del inventario en balance refleje existencias reales comprobables.</li>
                      <li><strong>Conciliación clara:</strong> Facilita el cruce entre los conteos físicos de almacén y los registros del libro mayor.</li>
                    </ul>
                    <div class="sat-rule-badge">REGLA VAUXOO: Prohibir salidas sin existencias en categorías AVCO</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 9: Bloque 5 - Causa Raíz #3: La Matriz de Cadencia
        {
            "id": 9,
            "title": "Causa Raíz #3: Matriz de Cadencia",
            "bg": "gradient",
            "time": "00:53 - 00:58",
            "block": "Bloque 5",
            "notes": "Parte A del Bloque 5: La Causa Raíz #3 - La Cadencia de Auditoría (5 min). Presentar la Matriz de Cadencia Vauxoo (Diaria, Semanal, Mensual, Anual).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · PARTE A</span>
                  <h2 class="slide-title" style="color: #fff;">Causa Raíz #3: La Cadencia de Auditoría</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                La frecuencia con la que se concilia el inventario contable contra el almacén determina el tiempo y costo de resolución:
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
                      <td>Estándar indispensable para el cierre formal y reporte contable.</td>
                    </tr>
                    <tr>
                      <td><strong>Anual</strong></td>
                      <td>❌ <span class="pill-badge" style="background:#B91C1C;">EVITARLO A TODA COSTA</span></td>
                      <td>Semanas de reconstrucción</td>
                      <td>Miles de movimientos acumulados; rastreo complejo y alto desgaste para el equipo.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            '''
        },
        # Slide 10: Bloque 5 - Causa Raíz #2: Caza de la Póliza Manual (MISC/2026/09/0001)
        {
            "id": 10,
            "title": "Caza de la Póliza Manual Intrusa",
            "bg": "white",
            "time": "00:58 - 01:03",
            "block": "Bloque 5",
            "notes": "Parte B del Bloque 5: Causa Raíz #2 - Caza de la Póliza Manual y Resolución del Hook. Regreso a las pantallas del Hook: diferencia de $411,275 MXN. Descubrimiento de la póliza MISC/2026/09/0001 por $487,000.00 MXN en la 1150 sin documento logístico.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · PARTE B</span>
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
                    Un apunte contable manual fue registrado directamente en la cuenta <strong>115.01.01</strong> sin documento logístico de soporte para forzar un cuadre provisional de fin de periodo.
                  </div>
                  <div class="culprit-flaw">
                    ❌ La "aspirina manual": Una póliza contable manual NUNCA crea un movimiento de almacén. Modifica el saldo contable pero deja intacto el reporte de existencias.
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
                      ✅ CUADRE EXACTO (Diferencia: $0.00 MXN)
                    </div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 11: Bloque 5 - Las 3 Reglas de Oro Blindadas de Vauxoo
        {
            "id": 11,
            "title": "Las 3 Reglas de Oro Blindadas",
            "bg": "white",
            "time": "01:03 - 01:07",
            "block": "Bloque 5",
            "notes": "Parte C del Bloque 5: Las 3 Reglas de Oro Blindadas de Vauxoo. 1. Cero Asientos Manuales en la 1150; 2. Cero Stock Negativo en AVCO; 3. Configuración y Cadencia Disciplinada.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MEJORES PRÁCTICAS VAUXOO</span>
                  <h2 class="slide-title">Las 3 Reglas de Oro Blindadas de Vauxoo</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Tres lineamientos clave para mantener alineados la contabilidad y el almacén:</p>
              
              <div class="golden-rules-grid">
                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #1</div>
                  <h3>Cero Asientos Manuales en la 1150</h3>
                  <p>Restringir por permisos de seguridad que los usuarios creen pólizas manuales de diario en cuentas de inventario. Todo ajuste debe nacer de un movimiento logístico documentado.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #2</div>
                  <h3>Cero Stock Negativo en AVCO</h3>
                  <p>Bloquear salidas y despachos sin existencia física en todas las categorías con Costo Promedio para preservar la coherencia matemática de la ponderación.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA BLINDADA #3</div>
                  <h3>Configuración y Cadencia Disciplinada</h3>
                  <p>Evitar cambiar métodos de categorías con inventario activo sin corte formal, y mantener revisiones periódicas cruzando <em>Balanza vs Existencias</em>.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 12: Bloque 6 - Q&A Hot Seat (Consultoría en Vivo)
        {
            "id": 12,
            "title": "Bloque 6: Q&A Hot Seat (Consultoría en Vivo)",
            "bg": "gradient",
            "time": "01:07 - 01:28",
            "block": "Bloque 6",
            "notes": "Bloque 6: Q&A Hot Seat - Consultoría en Vivo (23 minutos). Los asistentes exponen sus dudas, casuísticas de comercio exterior o descuadres reales en vivo. Julio responde en pantalla sobre Odoo 19.",
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
                  <p>Espacio abierto para analizar casuísticas reales de valoración e importaciones en Odoo 19.</p>
                </div>
                <div class="hotseat-topics">
                  <h4>Temas Abiertos para Consulta:</h4>
                  <ul class="styled-list" style="color: rgba(255,255,255,0.9);">
                    <li>¿Tienes descuadres acumulados en versiones previas de Odoo?</li>
                    <li>¿Dudas con el prorrateo de Landed Costs en recepciones parciales?</li>
                    <li>¿Cómo corregir categorías de producto sin generar vacíos de saldos?</li>
                    <li>¿Mejores prácticas para cortes logísticos de fin de mes en almacén?</li>
                  </ul>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 13: Paquete de Entregables Oficiales
        {
            "id": 13,
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
        # Slide 14: Cierre y Contacto
        {
            "id": 14,
            "title": "Cierre y Agradecimientos",
            "bg": "gradient",
            "time": "01:30",
            "block": "Cierre",
            "notes": "Agradecimiento final. Contacto y cierre de la sesión.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-logo-wrap">
                {logo_white}
              </div>
              <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 12px; color: #fff;">
                Aprende. Evoluciona. Transforma.
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

print("Adjusted slides module compiled successfully (14 slides).")
