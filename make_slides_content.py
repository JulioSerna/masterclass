#!/usr/bin/env python3
# Content for all 18 slides of the Masterclass 2026
# EXACT EXECUTION OF PLAN FINAL FUSIONADO V2 (plan_v2_critico.md + setup_masterclass.py)
# - No MRP / Manufactura
# - Mega-Caso: Importación, USD y Pedimentos (30 min)
# - Descuadre real: Cuenta 115.01.01 ($487,200 MXN) vs Reporte ($200 MXN) -> Descuadre de $487,000 MXN
# - Casos de prueba reales: WIDGET-MX, SENSOR-USD, VALVULA-NEG, MCU-TC-ERR, CABLE-MERMA, TARJETA-OBS, LANDED-COST

def get_slides(doodle_oval, doodle_arrow, doodle_underline, logo_white, logo_light):
    return [
        # Slide 1: Portada Oficial
        {
            "id": 1,
            "title": "Portada Oficial",
            "bg": "gradient",
            "time": "00:00",
            "block": "Apertura",
            "notes": "Bienvenida formal de Julio Serna (PM y Experto Funcional en Vauxoo). Contexto de Vauxoo Academy. Reglas de la sesión: 90 minutos de pura trinchera contable y logística en México, sin teoría vacía. Enfoque exclusivo en Odoo 19.0, Costo Promedio (AVCO) y desastres de importación.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-logo-wrap">
                {logo_white}
              </div>
              <div class="cover-badge-row">
                <span class="pill-badge">MASTERCLASS 2026</span>
                <span class="pill-badge-outline">ODOO 19.0 · MÉXICO</span>
                <span class="pill-badge-outline">90 MINUTOS</span>
              </div>
              <h1 class="cover-title">
                De la Logística a la Contabilidad:
                <span class="doodle-wrap">
                  Domina AVCO y Desastres de Importación
                  {doodle_underline}
                </span>
                en Odoo 19.0
              </h1>
              <p class="cover-subtitle">
                Arquitectura de Costo Promedio, Compras en USD, Pedimentos Aduanales (Landed Costs), Resolución de Desastres Reales y Cierre Contable SAT.
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
                  <span class="price-label">Acceso Total · Grabación · Entregables</span>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 2: Mapa de Ruta Minuto a Minuto
        {
            "id": 2,
            "title": "Mapa de Ruta (90 Minutos)",
            "bg": "white",
            "time": "00:00 - 00:03",
            "block": "Estructura",
            "notes": "Presentar los 6 bloques cronometrados del Plan Final Fusionado v2. Enfatizar que se eliminó el relleno y la manufactura para dedicar 30 minutos completos al Mega-Caso de Importaciones en USD, que es donde el 90% de las empresas mexicanas tienen contingencias con el SAT.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">AGENDA EJECUTIVA</span>
                  <h2 class="slide-title">Cronograma de Batalla: 90 Minutos</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <div class="agenda-grid">
                <div class="agenda-card">
                  <div class="agenda-time">00:00 – 00:07 (7 min)</div>
                  <div class="agenda-num">01</div>
                  <div class="agenda-title">EL HOOK: El Dolor que Todos Conocen</div>
                  <p class="agenda-desc">Pantalla dividida: Cuenta 115.01.01 vs Reporte de Valoración. Descuadre real de casi medio millón de pesos.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:07 – 00:15 (8 min)</div>
                  <div class="agenda-num">02</div>
                  <div class="agenda-title">EL NUEVO PARADIGMA: Odoo 19.0</div>
                  <p class="agenda-desc">Foco 100% en AVCO. Adiós SVL, adiós cuentas puente interim. Interfaz guiada de valoración y corte.</p>
                </div>
                <div class="agenda-card" style="border: 2px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">00:15 – 00:45 (30 min)</div>
                  <div class="agenda-num">03</div>
                  <div class="agenda-title">EL MEGA-CASO: USD Y PEDIMENTOS</div>
                  <p class="agenda-desc">El núcleo de la sesión: Anticipos en USD, recepción aduanal vs factura, Landed Costs del pedimento y CFDI de pago.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:45 – 01:05 (20 min)</div>
                  <div class="agenda-num">04</div>
                  <div class="agenda-title">LA CLÍNICA DE DESASTRES</div>
                  <p class="agenda-desc">Stock negativo con AVCO, ajustes físicos por merma (gastos no deducibles) y provisión de inventario obsoleto.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">01:05 – 01:15 (10 min)</div>
                  <div class="agenda-num">05</div>
                  <div class="agenda-title">EL MOMENTO DE LA VERDAD</div>
                  <p class="agenda-desc">Auditoría en vivo: rastreo y reversa del asiento manual intruso de $487,000 MXN. Las 3 Reglas de Oro.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">01:15 – 01:30 (15 min)</div>
                  <div class="agenda-num">06</div>
                  <div class="agenda-title">HOT SEAT & ENTREGABLES</div>
                  <p class="agenda-desc">Consultoría en directo con preguntas de la audiencia. Distribución de Checklist y Tabla de Mapeo 18→19.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 3: Bloque 1 - El Hook: "El Descuadre que Todos Conocen"
        {
            "id": 3,
            "title": "El Descuadre que Todos Conocen",
            "bg": "white",
            "time": "00:00 - 00:07",
            "block": "Bloque 1",
            "notes": "Mostrar el split view con los datos EXACTOS de la base de datos de Masterclass México SA de CV. Preguntar en el chat: '¿A quién le ha tocado ver esto al final de mes? Pongan 🔥 en el chat'. Enfatizar el dolor del director contable ante una auditoría del SAT.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 1 · 00:00 - 00:07</span>
                  <h2 class="slide-title">El Dolor que Todos Conocen (Caso Real)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Compañía: <strong>Masterclass México, S.A. de C.V.</strong> (RFC: EKU9003173C9). Cierre mensual en Odoo 19.0:</p>
              
              <div class="split-audit-container">
                <div class="audit-col audit-contable">
                  <div class="audit-col-badge">Módulo de Contabilidad</div>
                  <h3 class="audit-col-title">Balanza de Comprobación SAT</h3>
                  <div class="audit-code">Cuenta 115.01.01 · Mercancías en Almacén</div>
                  <div class="audit-amount">$487,200.00 MXN</div>
                  <div class="audit-detail">Saldo deudor contable al cierre de periodo</div>
                  <div class="audit-status audit-err">⚠️ Generado por apuntes contables</div>
                </div>

                <div class="audit-vs">
                  <div class="audit-diff-card">
                    <span class="diff-label">DESCUADRE CRÍTICO</span>
                    <span class="diff-amount doodle-wrap">
                      $487,000.00 MXN
                      {doodle_oval}
                    </span>
                    <span class="diff-warn">Casi medio millón de pesos sin cuadrar</span>
                  </div>
                </div>

                <div class="audit-col audit-logistica">
                  <div class="audit-col-badge">Módulo de Inventario</div>
                  <h3 class="audit-col-title">Reporte de Valoración</h3>
                  <div class="audit-code">Valoración Física de Stock (Valuation)</div>
                  <div class="audit-amount">$200.00 MXN</div>
                  <div class="audit-detail">Suma real de existencias en almacén</div>
                  <div class="audit-status audit-ok">📦 Generado por Stock Moves</div>
                </div>
              </div>

              <div class="interactive-chat-prompt">
                <span class="prompt-icon">💬</span>
                <span class="prompt-text">
                  <strong>Pregunta al chat:</strong> "¿A quién le ha tocado explicarle este descuadre de casi medio millón de pesos al SAT o a los socios de la empresa? Pongan 🔥 en el chat."
                </span>
              </div>
            </div>
            '''
        },
        # Slide 4: ¿Por qué esta Masterclass vale $100 USD?
        {
            "id": 4,
            "title": "¿Por qué vale $100 USD?",
            "bg": "gradient",
            "time": "00:05 - 00:07",
            "block": "Bloque 1",
            "notes": "Establecer la enorme diferencia entre contenido genérico y conocimiento de trinchera. Por qué se descartó la manufactura para enfocarse al 100% en importaciones, pedimentos aduanales y el nuevo motor de Odoo 19.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">VALOR ESTRATÉGICO</span>
                  <h2 class="slide-title" style="color: #fff;">¿Por qué esta Masterclass vale $100 USD?</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                Conocimiento especializado para consultores, directores financieros y contadores en México:
              </p>
              <div class="value-cards-grid">
                <div class="value-card">
                  <div class="value-icon">🏗️</div>
                  <h4>Arquitectura Odoo 19.0 Real</h4>
                  <p>Muerte definitiva de Stock Valuation Layers (SVL) y cuentas intermedias interim. Los Stock Moves gobiernan la valoración directa.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">🇲🇽</div>
                  <h4>Especialización México & AVCO</h4>
                  <p>Por qué en México ignoramos FIFO y Estándar. Costo Promedio Ponderado alineado con NIF C-4 y Art. 41 de la Ley del ISR.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">💵</div>
                  <h4>El Mega-Caso: USD y Pedimentos</h4>
                  <p>30 minutos analizando anticipos en USD, tipos de cambio DOF (Art. 20 CFF), facturas extranjeras y Landed Costs del pedimento.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">🛡️</div>
                  <h4>Mermas y Obsolescencia SAT</h4>
                  <p>Cómo registrar mermas como no deducibles y provisiones de lento movimiento sin corromper el AVCO del inventario activo.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">🔍</div>
                  <h4>Auditoría y Corrección en Vivo</h4>
                  <p>Localización con bisturí de la póliza manual intrusa de $487,000 MXN en la cuenta 115.01.01 y su reversión sin tocar código.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">📋</div>
                  <h4>Entregables Profesionales</h4>
                  <p>Checklist de Cierre Mensual imprimible y Tabla de Mapeo conceptual Odoo 18 vs 19 para usar de inmediato en tu empresa.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 5: Bloque 2 - El Nuevo Paradigma Odoo 19.0
        {
            "id": 5,
            "title": "El Nuevo Paradigma en Odoo 19.0",
            "bg": "white",
            "time": "00:07 - 00:15",
            "block": "Bloque 2",
            "notes": "Explicar el cambio estructural. En Odoo 19.0 stock.valuation.layer ya no es la tabla independiente; el valor reside en stock.move. Las cuentas interim (Stock Input/Output) desaparecen del catálogo estándar.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 2 · 00:07 - 00:15</span>
                  <h2 class="slide-title">El Gran Cambio Arquitectónico en Odoo 19.0</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Odoo 19 simplifica radicalmente el motor contable-logístico eliminando capas intermedias:</p>
              
              <div class="paradigm-table-container">
                <table class="paradigm-table">
                  <thead>
                    <tr>
                      <th>Dimensión</th>
                      <th>Odoo 18 e Histórico</th>
                      <th>Odoo 19.0 (Nuevo Paradigma)</th>
                      <th>Impacto en México</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Capa de Valoración</strong></td>
                      <td><span class="tag-old">stock.valuation.layer (SVL)</span><br><small>Tabla separada que a menudo se desincronizaba</small></td>
                      <td><span class="tag-new">Directo en stock.move</span><br><small>El movimiento físico ES el registro de valor</small></td>
                      <td>Trazabilidad 1 a 1 por CFDI y póliza sin discrepancias de tablas</td>
                    </tr>
                    <tr>
                      <td><strong>Cuentas Puente</strong></td>
                      <td><span class="tag-old">Interim Input / Output</span><br><small>Cuentas temporales que acumulaban basura</small></td>
                      <td><span class="tag-new">Asiento Directo</span><br><small>Afectación directa a cuenta 115.01.01</small></td>
                      <td>Balanza de comprobación del SAT infinitamente más limpia</td>
                    </tr>
                    <tr>
                      <td><strong>Modelo Contable</strong></td>
                      <td><span class="tag-old">Continental vs Anglo-Sajón</span><br><small>Confuso para implementadores de LATAM</small></td>
                      <td><span class="tag-new">Periódico vs Perpetuo</span><br><small>Terminología contable internacional estándar</small></td>
                      <td>Claridad absoluta: en México siempre usamos Perpetuo con AVCO</td>
                    </tr>
                    <tr>
                      <td><strong>Auditoría & Cierre</strong></td>
                      <td><span class="tag-old">Vistas dispersas</span><br><small>Revisión manual en múltiples menús</small></td>
                      <td><span class="tag-new">Contabilidad > Revisión y Cierre</span><br><small>Menú: Valoración de inventario (guiado)</small></td>
                      <td>Bloqueo formal de movimientos posteriores a la fecha de corte</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            '''
        },
        # Slide 6: Bloque 2 - Dominio de AVCO en México
        {
            "id": 6,
            "title": "Por qué AVCO es el Rey en México",
            "bg": "white",
            "time": "00:10 - 00:15",
            "block": "Bloque 2",
            "notes": "Fundamento legal mexicano: NIF C-4 y Art. 41 de la Ley del ISR. Demostrar matemáticamente por qué el Costo Promedio es el único método viable y por qué FIFO y Estándar generan problemas fiscales.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 2 · AVCO Y SAT</span>
                  <h2 class="slide-title">Por qué en México Ignoramos FIFO y Estándar</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="avco-comparison-grid">
                <div class="avco-card avco-winner">
                  <div class="avco-card-badge">👑 ESTÁNDAR DE FACTO</div>
                  <h3>Costo Promedio (AVCO)</h3>
                  <div class="avco-legal">NIF C-4 · Art. 41 Ley del ISR</div>
                  <p>Es el método por excelencia aceptado por el SAT. Suaviza picos inflacionarios y tipos de cambio volátiles. En Odoo 19.0 recalcula dinámicamente en cada recepción.</p>
                  <div class="avco-formula-box">
                    <span class="formula-label">FÓRMULA MATEMÁTICA AVCO:</span>
                    <div class="formula-math">
                      Nuevo AVCO = [ (Stock Actual &times; AVCO Actual) + (Qty Recibida &times; Costo Unitario Factura) ] &divide; [ Stock Actual + Qty Recibida ]
                    </div>
                  </div>
                </div>

                <div class="avco-card avco-discarded">
                  <div class="avco-card-badge">🚫 NO RECOMENDADO</div>
                  <h3>FIFO (PEPS)</h3>
                  <p>Genera capas complejas que ante devoluciones parciales, notas de crédito o cancelaciones de pedimentos en México generan distorsiones en el kardex fiscal.</p>
                  <hr style="border:0; border-top: 1px solid #E2E8F0; margin: 12px 0;">
                  <div class="avco-card-badge">🚫 NO RECOMENDADO</div>
                  <h3>Costo Estándar</h3>
                  <p>Genera cuentas de variación en costo de ventas (501.01.02) que requieren reclasificación fiscal para no ser rechazadas en la Declaración Anual del SAT.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 7: Bloque 3 - El Mega-Caso: Introducción (30 min)
        {
            "id": 7,
            "title": "El Mega-Caso: Importación, USD y Pedimentos",
            "bg": "gradient",
            "time": "00:15 - 00:20",
            "block": "Bloque 3",
            "notes": "EL NÚCLEO DE LA MASTERCLASS (30 minutos). Presentar a la empresa: Masterclass México SA de CV (MXN base). Compra a Global Supply Tech LLC en USD del producto SENSOR-USD. Explicar los 4 pasos que se recorrerán en vivo.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · EL NÚCLEO DE LA SESIÓN (30 MIN)</span>
                  <h2 class="slide-title" style="color: #fff;">El Mega-Caso: Importación, USD y Pedimentos</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                El escenario real que vive el 90% de las empresas en México y que los tutoriales nunca muestran:
              </p>
              
              <div class="value-cards-grid" style="grid-template-columns: repeat(4, 1fr);">
                <div class="value-card">
                  <div class="value-icon">1️⃣</div>
                  <h4>Paso 1: Anticipo USD</h4>
                  <p>Pago anticipado a proveedor extranjero. Tipo de cambio DOF según Art. 20 del CFF.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">2️⃣</div>
                  <h4>Paso 2: Recepción vs Factura</h4>
                  <p>Mercancía ingresa a un TC y la factura extranjera llega a otro TC. Efecto en AVCO.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">3️⃣</div>
                  <h4>Paso 3: Pedimento & Landed Cost</h4>
                  <p>Agencia Aduanal del Norte: DTA, IGI e incremento de costo unitario en MXN.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">4️⃣</div>
                  <h4>Paso 4: CFDI de Pago</h4>
                  <p>Complemento de Pago, fluctuación cambiaria realizada y ajuste de IVA acreditable.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 8: Bloque 3 - Paso 1: Anticipo y Tipo de Cambio DOF
        {
            "id": 8,
            "title": "Paso 1: Anticipo y Tipo de Cambio DOF",
            "bg": "white",
            "time": "00:20 - 00:27",
            "block": "Bloque 3",
            "notes": "Mostrar el registro del anticipo en Odoo 19. Fundamento legal: Art. 20 del Código Fiscal de la Federación (CFF) y NIF B-15. Un anticipo en USD fija el tipo de cambio para la proporción pagada de los bienes futuros.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · PASO 1</span>
                  <h2 class="slide-title">Anticipo en USD y Tipo de Cambio Oficial (Art. 20 CFF)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Orden de Compra por <strong>$10,000 USD</strong> con Global Supply Tech LLC. Se emite un anticipo del 30% ($3,000 USD):</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">NORMATIVA FISCAL MÉXICO</div>
                  <h3>Artículo 20 del Código Fiscal de la Federación</h3>
                  <div class="detail-box">
                    <em>"Para determinar las contribuciones y sus accesorios se considerará el tipo de cambio a que se haya adquirido la moneda extranjera de que se trate y no habiendo adquisición, se estará al tipo de cambio que el Banco de México publique en el Diario Oficial de la Federación..."</em>
                    <br><br>
                    <strong>Criterio NIF B-15:</strong> Los anticipos a proveedores en moneda extranjera se consideran <strong>partidas no monetarias</strong> que fijan el tipo de cambio histórico para la porción anticipada.
                  </div>
                </div>

                <div class="disaster-col-card">
                  <div class="card-pill">REGISTRO EN ODOO 19.0</div>
                  <h3>Asiento Contable de Anticipo</h3>
                  <div class="detail-box">
                    Fecha 01/09/2026 · TC DOF: <strong>$18.22 MXN/USD</strong>
                    <div class="asiento-box">
                      <div class="asiento-row"><span class="cargo">CARGO</span> 205.01.01 Anticipo a Proveedores Extranjeros <strong>$54,660.00 MXN</strong> ($3,000 × 18.22)</div>
                      <div class="asiento-row"><span class="abono">ABONO</span> 102.01.01 Banco Moneda Extranjera <strong>$54,660.00 MXN</strong></div>
                    </div>
                    <strong>Resultado:</strong> El saldo queda fijado en pesos a $18.22 sin fluctuación no realizada sobre el anticipo.
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 9: Bloque 3 - Paso 2: Recepción vs Factura (Vendor Bill)
        {
            "id": 9,
            "title": "Paso 2: Recepción Aduanal vs Factura",
            "bg": "white",
            "time": "00:27 - 00:34",
            "block": "Bloque 3",
            "notes": "Mostrar el momento en que llega la mercancía a aduana y se valida la recepción. Días después llega la factura comercial. Cómo Odoo 19 calcula el AVCO con base en la recepción física y qué sucede con la diferencia contra la factura.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · PASO 2</span>
                  <h2 class="slide-title">Recepción Aduanal vs Factura Extranjera (Invoice)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">La mercancía cruza la frontera física el Día 10. La factura comercial del proveedor se recibe el Día 15:</p>
              
              <div class="two-col-grid">
                <div class="flow-step-card">
                  <div class="step-badge">DÍA 10: RECEPCIÓN FÍSICA (STOCK MOVE)</div>
                  <h4>Recepción en Aduana de 100 Sensores USD</h4>
                  <p>TC DOF del día de entrada: <strong>$18.05 MXN/USD</strong>.</p>
                  <div class="asiento-box">
                    <div class="asiento-row"><span class="cargo">CARGO</span> 115.01.01 Inventarios <strong>$180,500.00 MXN</strong> (100u × $100 × 18.05)</div>
                    <div class="asiento-row"><span class="abono">ABONO</span> 2110 Proveedores Extranjeros (Tránsito) <strong>$180,500.00 MXN</strong></div>
                  </div>
                  <div class="step-avco">Costo Unitario AVCO Inicial: <strong>$1,805.00 MXN / unidad</strong></div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">DÍA 15: FACTURA PROVEEDOR (VENDOR BILL)</div>
                  <h4>Registro de Invoice Comercial</h4>
                  <p>TC Fecha de Factura: <strong>$18.50 MXN/USD</strong>.</p>
                  <div class="asiento-box">
                    <div class="asiento-row"><span class="cargo">CARGO</span> 2110 Tránsito Proveedores <strong>$180,500.00 MXN</strong></div>
                    <div class="asiento-row"><span class="cargo">CARGO</span> 701.01.01 Fluctuación Cambiaria <strong>$4,500.00 MXN</strong></div>
                    <div class="asiento-row"><span class="abono">ABONO</span> 201.01.02 Proveedores Extranjeros <strong>$185,000.00 MXN</strong></div>
                  </div>
                  <div class="step-avco">✅ El AVCO del producto se mantiene blindado al costo de recepción fiscal.</div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 10: Bloque 3 - Paso 3: El Pedimento Aduanal (Landed Costs)
        {
            "id": 10,
            "title": "Paso 3: El Pedimento Aduanal (Landed Costs)",
            "bg": "white",
            "time": "00:34 - 00:40",
            "block": "Bloque 3",
            "notes": "LLEGA EL PEDIMENTO. Factura de Agencia Aduanal del Norte, SC con Landed Cost de $5,000 MXN más IGI/DTA. Cómo vincularlo en Odoo 19 sin duplicar cuentas contables para que el AVCO suba a su costo de importación real.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · PASO 3</span>
                  <h2 class="slide-title">El Pedimento Aduanal y Gastos en Destino (Landed Costs)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Factura del Agente Aduanal (Agencia Aduanal del Norte, S.C.): Honorarios, DTA e impuestos aduanales.</p>
              
              <div class="mrp-split">
                <div class="mrp-diagram">
                  <div class="mrp-box mrp-mat">
                    <span class="mrp-tag">1. FACTURA DE SERVICIO ADUANAL</span>
                    <p>Producto: <code>LANDED-COST</code> (Gastos Aduanales y Flete)<br>Monto: <strong>$5,000.00 MXN</strong></p>
                  </div>
                  <div class="mrp-arrow">⬇️ Botón: Crear Costo en Destino (Landed Cost)</div>
                  <div class="mrp-box mrp-wip">
                    <span class="mrp-tag">2. ASIGNACIÓN AL ALBARÁN DE IMPORTACIÓN</span>
                    <p>Método de reparto: <em>Por Costo Actual</em> (split_method_landed_cost)</p>
                    <strong style="color: #AC0340;">Prorrateo de $5,000 MXN sobre las 100 piezas recibidas</strong>
                  </div>
                  <div class="mrp-arrow">⬇️ Validación del Costo en Destino</div>
                  <div class="mrp-box mrp-pt">
                    <span class="mrp-tag">3. RECÁLCULO OFICIAL DE AVCO</span>
                    <p>Costo anterior: $1,805.00 MXN → <strong>Nuevo AVCO: $1,855.00 MXN / pza</strong></p>
                  </div>
                </div>

                <div class="mrp-insights">
                  <div class="alert-box">
                    <h4>⚖️ El Error Fatal en Pedimentos</h4>
                    <p>Muchos contadores mandan la factura aduanal a una cuenta de gastos generales (601) para no complicarse:</p>
                    <ul class="styled-list">
                      <li>Subvalúan el inventario en el balance general.</li>
                      <li>Distorsionan el costo de ventas al vender el producto.</li>
                      <li><strong>Violan el Art. 39 de la Ley del ISR</strong>, que obliga a capitalizar los gastos aduanales indispensables para adquirir los inventarios.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 11: Bloque 3 - Paso 4: CFDI de Pago y Complemento
        {
            "id": 11,
            "title": "Paso 4: CFDI de Pago y Complemento",
            "bg": "white",
            "time": "00:40 - 00:45",
            "block": "Bloque 3",
            "notes": "Liquidación final de la factura semanas después. Diferencia cambiaria realizada contra el banco, timbrado o registro del Complemento de Pago en Odoo y el traslado automático del IVA acreditable pagado efectivamente.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · PASO 4</span>
                  <h2 class="slide-title">Liquidación, Complemento de Pago e IVA Acreditable</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Día 30: Liquidación final del saldo remanente al proveedor extranjero mediante transferencia bancaria:</p>
              
              <div class="flow-steps-grid">
                <div class="flow-step-card">
                  <div class="step-badge">1. PAGO EFECTIVO</div>
                  <h4>Salida Bancaria USD</h4>
                  <p>TC Bancario real de liquidación: <strong>$18.60 MXN/USD</strong>.</p>
                  <div class="asiento-box">
                    <div class="asiento-row"><span class="cargo">CARGO</span> 201.01.02 Proveedores Ext. $185,000</div>
                    <div class="asiento-row"><span class="cargo">CARGO</span> 701.01.01 Pérdida Camb. $1,000</div>
                    <div class="asiento-row"><span class="abono">ABONO</span> 102.01.01 Banco USD $186,000</div>
                  </div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">2. CFDI / COMPLEMENTO</div>
                  <h4>Efecto Fiscal en México</h4>
                  <p>Conciliación y soporte de pago ante el SAT.</p>
                  <p style="font-size:0.85rem; color:#475569; margin-top:8px;">
                    En compras internacionales sin CFDI directo, el pago concilia contra la póliza de importación y el pedimento correspondiente.
                  </p>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">3. IVA ACREDITABLE</div>
                  <h4>Flujo de Impuestos Pagados</h4>
                  <p>Acreditamiento conforme a flujo de efectivo.</p>
                  <p style="font-size:0.85rem; color:#475569; margin-top:8px;">
                    El IVA de importación pagado en el pedimento aduanal (Paso 3) se vuelve plenamente acreditable al momento del pago del pedimento.
                  </p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 12: Bloque 4 - Desastre #1: Stock Negativo con AVCO
        {
            "id": 12,
            "title": "Desastre #1: Stock Negativo con AVCO",
            "bg": "white",
            "time": "00:45 - 00:52",
            "block": "Bloque 4",
            "notes": "Mostrar la demostración con el producto VALVULA-NEG pre-configurado en setup_masterclass.py. Demostrar cómo vender sin existencias corrompe matemáticamente el promedio ponderado y causa sanciones del SAT por kardex negativo.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA DE DESASTRES #1</span>
                  <h2 class="slide-title">El Veneno Matemático: Stock Negativo en AVCO</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>VALVULA-NEG</code> (Válvula Reguladora). ¿Qué pasa cuando vendes lo que no tienes?</p>
              
              <div class="disaster-grid">
                <div class="disaster-main">
                  <h3>Secuencia de la Catástrofe en Odoo:</h3>
                  <div class="disaster-sequence">
                    <div class="seq-step">
                      <span class="seq-num">1</span>
                      <div>Stock inicial: 0 piezas. Se confirma venta y entrega física por <strong>-10 piezas</strong>.</div>
                    </div>
                    <div class="seq-step">
                      <span class="seq-num">2</span>
                      <div>Odoo saca el producto con costo provisional ($0.00 o último conocido de $200 MXN).</div>
                    </div>
                    <div class="seq-step">
                      <span class="seq-num">3</span>
                      <div>Días después entra la compra real de 15 piezas a $350 MXN c/u.</div>
                    </div>
                    <div class="seq-step" style="background: #FEE2E2; border: 1px solid #FCA5A5;">
                      <span class="seq-num" style="background:#B91C1C;">💥</span>
                      <div><strong>Colapso del divisor matemático:</strong> El sistema promedia cantidades negativas con positivas, generando costos unitarios distorsionados de <strong>$1,850 MXN o números negativos</strong>.</div>
                    </div>
                  </div>
                </div>

                <div class="disaster-sat">
                  <div class="sat-warn-card">
                    <h4>⚖️ Contingencias Fiscales SAT</h4>
                    <ul class="styled-list">
                      <li><strong>Kardex Ilegal:</strong> El SAT prohíbe inventarios negativos en la contabilidad electrónica.</li>
                      <li><strong>Rechazo del Costo de lo Vendido:</strong> La deducción en la Declaración Anual queda invalidada (Art. 39 LISR).</li>
                      <li><strong>Multas por Inconsistencia:</strong> Hasta $45,000 MXN por mes dictaminado.</li>
                    </ul>
                    <div class="sat-rule-badge">REGLA VAUXOO: Prohibir entregas sin stock en categorías AVCO</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 13: Bloque 4 - Desastre #2: Ajustes Físicos y Mermas
        {
            "id": 13,
            "title": "Desastre #2: Ajustes Físicos y Mermas",
            "bg": "white",
            "time": "00:52 - 00:58",
            "block": "Bloque 4",
            "notes": "Producto CABLE-MERMA pre-configurado en setup_masterclass.py. El gran dilema del conteo físico de fin de año. Si haces un Inventory Adjustment directo a resultados ordinarios, el SAT lo objeta. Cómo canalizar faltantes a Gasto No Deducible sin romper el AVCO de las existencias restantes.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA DE DESASTRES #2</span>
                  <h2 class="slide-title">Ajustes Físicos y Mermas (El Conteo de Fin de Año)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>CABLE-MERMA</code>. Conteo físico revela 80 metros en almacén vs 100 metros en Odoo (Faltan 20m @ $85 MXN):</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">EL ERROR COMÚN</div>
                  <h3>Ajuste Automático a Costo de Ventas</h3>
                  <div class="detail-box">
                    Hacer clic en "Aplicar Inventario Físico" enviando la diferencia directamente a la cuenta 501.01.01 (Costo de Ventas ordinario).
                    <br><br>
                    <strong>El peligro SAT:</strong> El SAT audita el consumo de materias primas y ventas. Si el faltante no tiene CFDI de venta ni acta de destrucción de mermas autorizada, <strong>se presume como venta omitida con cobro de IVA e ISR omitido</strong>.
                  </div>
                </div>

                <div class="disaster-col-card">
                  <div class="card-pill">LA PRÁCTICA PROFESIONAL EN ODOO 19</div>
                  <h3>Canalización a Gasto No Deducible</h3>
                  <div class="detail-box">
                    Configurar la ubicación de pérdida de inventario (Scrap / Inventory Loss) vinculada a una cuenta específica: <strong>Gastos No Deducibles por Merma</strong>.
                    <br><br>
                    <strong>Beneficio:</strong> Las 80 unidades restantes conservan su AVCO exacto de $85.00 MXN sin alteraciones, y la contabilidad fiscal queda perfectamente blindada.
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 14: Bloque 4 - Desastre #3: Provisión de Inventario Obsoleto
        {
            "id": 14,
            "title": "Desastre #3: Inventario Obsoleto (NIF C-4)",
            "bg": "white",
            "time": "00:58 - 01:05",
            "block": "Bloque 4",
            "notes": "Producto TARJETA-OBS pre-configurado en setup_masterclass.py. Demostrar cómo manejar inventarios de lento movimiento u obsoletos. El error garrafal es cambiarle el costo a cero o hacer un ajuste negativo; la regla es crear una cuenta complementaria de activo (provisión de obsolescencia).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA DE DESASTRES #3</span>
                  <h2 class="slide-title">Inventario Obsoleto y Provisiones (NIF C-4)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>TARJETA-OBS</code>. Lote valorado en $120,000 MXN que perdió su valor de mercado por obsolescencia tecnológica:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">ERROR CATASTRÓFICO</div>
                  <h3>Cambiar el Costo o Ajustar a Cero</h3>
                  <div class="detail-box">
                    Modificar el <code>standard_price</code> del producto a $0.00 o dar de baja el inventario en el módulo de stock.
                    <br><br>
                    <strong>La catástrofe:</strong> Si el producto físicamente sigue en la bodega y se llega a vender como refacción o chatarra, el sistema generará márgenes absurdos del 100% o costos negativos que destruyen el histórico.
                  </div>
                </div>

                <div class="disaster-col-card">
                  <div class="card-pill">SOLUCIÓN CONTABLE CORRECTA</div>
                  <h3>Cuenta Complementaria de Activo</h3>
                  <div class="detail-box">
                    Mantener el AVCO en Odoo intacto ($1,200 MXN) y crear una póliza contable en una cuenta complementaria:
                    <div class="asiento-box">
                      <div class="asiento-row"><span class="cargo">CARGO</span> Gastos por Estimación de Obsolescencia</div>
                      <div class="asiento-row"><span class="abono">ABONO</span> 115.09 Provisión por Inventario Obsoleto (Acreedora)</div>
                    </div>
                    <strong>Resultado:</strong> El valor neto en balance baja a valor razonable (NIF C-4) sin desconfigurar la logística de Odoo.
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 15: Bloque 5 - El Momento de la Verdad: Auditoría en Vivo
        {
            "id": 15,
            "title": "El Momento de la Verdad: Auditoría en Vivo",
            "bg": "gradient",
            "time": "01:05 - 01:10",
            "block": "Bloque 5",
            "notes": "EL CLÍMAX DE LA AUDITORÍA. Entrar en vivo al menú Contabilidad > Revisión y Cierre > Valoración de inventario en la base de datos de Masterclass México SA de CV. Rastrear los $487,000 MXN del Bloque 1.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · 01:05 - 01:15</span>
                  <h2 class="slide-title" style="color: #fff;">El Momento de la Verdad: Auditoría en Vivo</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                Rastreando en tiempo real el descuadre de <strong>$487,000.00 MXN</strong> del Bloque 1:
              </p>
              
              <div class="audit-steps-grid">
                <div class="audit-step-card">
                  <div class="audit-step-num">PASO 1</div>
                  <h4>Abrir Valoración de Inventario</h4>
                  <p>Menú <code>Contabilidad > Revisión y Cierre > Valoración de inventario</code>. Odoo 19 unifica los datos de stock.move directamente.</p>
                </div>
                <div class="audit-step-card">
                  <div class="audit-step-num">PASO 2</div>
                  <h4>Fijar Fecha de Corte</h4>
                  <p>Establecer fecha exacta de corte (30/09/2026). Bloquear transacciones posteriores para congelar la fotografía de auditoría.</p>
                </div>
                <div class="audit-step-card">
                  <div class="audit-step-num">PASO 3</div>
                  <h4>Filtrar Cuenta 115.01.01</h4>
                  <p>Abrir la Balanza de Comprobación y desplegar los apuntes contables (account.move.line) de la cuenta de inventario.</p>
                </div>
                <div class="audit-step-card">
                  <div class="audit-step-num">PASO 4</div>
                  <h4>Rastrear Origen Huérfano</h4>
                  <p>Filtrar los apuntes cuyo origen de diario sea <strong>Operaciones Varias (MISC)</strong> en lugar del Diario de Stock (STJ).</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 16: Bloque 5 - Resolución del Descuadre Inicial
        {
            "id": 16,
            "title": "Resolución del Descuadre en Vivo",
            "bg": "white",
            "time": "01:10 - 01:13",
            "block": "Bloque 5",
            "notes": "DESCUBRIMIENTO EN PANTALLA: Póliza manual con ref 'Ajuste manual auditoría interna (Error contable)' por $487,000 MXN en el diario MISC. Al revertirla en vivo, la cuenta 115.01.01 queda en $200.00 MXN, exactamente igual que el Reporte de Valoración. Cuadre al 100%.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">RESOLUCIÓN EN VIVO</span>
                  <h2 class="slide-title">¡Misterio Resuelto! El Asiento Manual Intruso</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="resolution-container">
                <div class="culprit-box">
                  <div class="culprit-badge">🔍 ORIGEN EXACTO ENCONTRADO EN LA BD</div>
                  <h3>Póliza Manual: Ref "Ajuste manual auditoría interna (Error contable)"</h3>
                  <div class="culprit-desc">
                    El equipo contable anterior registró un asiento manual directo en la cuenta <strong>115.01.01</strong> por <strong>$487,000.00 MXN</strong> contra la cuenta 501.01.02 en el diario MISC.
                  </div>
                  <div class="culprit-flaw">
                    ❌ Una póliza de diario manual <strong>NUNCA genera un stock.move</strong>. Infló la contabilidad en $487,000 MXN mientras que el almacén físico solo tenía $200.00 MXN.
                  </div>
                </div>

                <div class="action-result-box">
                  <div class="result-step">
                    <strong>Acción Correctiva Ejecutada en Vivo:</strong> Revertir el asiento manual indebido. Si se requiere un ajuste de stock, se debe ejecutar exclusivamente desde el módulo de Inventario con su respectivo albarán.
                  </div>
                  <div class="balanced-state">
                    <div class="bal-item">
                      <span>Cuenta 115.01.01 (Balanza)</span>
                      <strong>$200.00 MXN</strong>
                    </div>
                    <div class="bal-equal">=</div>
                    <div class="bal-item">
                      <span>Reporte de Valoración</span>
                      <strong>$200.00 MXN</strong>
                    </div>
                    <div class="bal-status">
                      ✅ CUADRE PERFECTO AL 100% (Diferencia: $0.00 MXN)
                    </div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 17: Bloque 5 - Las 3 Reglas de Oro en México
        {
            "id": 17,
            "title": "Las 3 Reglas de Oro de Vauxoo",
            "bg": "white",
            "time": "01:13 - 01:15",
            "block": "Bloque 5",
            "notes": "Las 3 reglas de oro del Plan Final Fusionado v2: 1. Jamás permitir stock negativo; 2. Pedimentos obligatorios vía Landed Costs para subir el AVCO; 3. Cut-off logístico estricto antes del cierre contable de mes.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MEJORES PRÁCTICAS VAUXOO</span>
                  <h2 class="slide-title">Las 3 Reglas de Oro para Inventarios en México</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="golden-rules-grid">
                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA DE ORO #1</div>
                  <h3>Jamás Permitir Stock Negativo</h3>
                  <p>Desactiva las entregas sin existencia física en categorías AVCO. Si la mercancía ya está en bodega pero no se ha capturado, ingresa la recepción antes de despachar. El costo negativo corrompe el kardex fiscal.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA DE ORO #2</div>
                  <h3>Pedimentos Vía Landed Costs</h3>
                  <p>Los gastos aduanales (DTA, IGI, fletes internacionales) deben inyectarse al AVCO del producto mediante el módulo de Costos en Destino antes de que la mercancía se venda. Cumple con el Art. 39 LISR.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA DE ORO #3</div>
                  <h3>Cut-Off Logístico Estricto</h3>
                  <p>Innegociable antes del cierre contable mensual. Todo albarán físico ocurrido en el mes debe validarse antes de las 23:59:59 del último día para que el cruce de la cuenta 115.01.01 cuadre con exactitud de centavos.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 18: Bloque 6 - Cierre y Entregables
        {
            "id": 18,
            "title": "Cierre y Entregables Oficiales",
            "bg": "gradient",
            "time": "01:15 - 01:30",
            "block": "Bloque 6",
            "notes": "Hot Seat de consultoría en vivo: responder preguntas reales de los participantes durante 15 minutos. Entregar los accesos al Checklist de Auditoría interactivo, Tabla de Mapeo 18->19, grabación 4K y certificado oficial de Vauxoo Academy.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-logo-wrap">
                {logo_white}
              </div>
              <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 12px; color: #fff;">
                Aprende. Evoluciona. Transforma.
              </h2>
              <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); max-width: 700px; margin: 0 auto 28px;">
                Tus entregables oficiales de la Masterclass 2026 ya están disponibles para descarga y uso en tu empresa:
              </p>
              
              <div class="deliverables-grid" style="margin-bottom: 28px;">
                <div class="deliv-card" style="background: rgba(255,255,255,0.12); border-color: rgba(255,255,255,0.25);">
                  <div class="deliv-icon">📋</div>
                  <h4 style="color:#fff;">Checklist de Cierre</h4>
                  <p style="color:rgba(255,255,255,0.8);">Validación de 12 puntos para cierres de mes en Odoo 19 MX.</p>
                </div>
                <div class="deliv-card" style="background: rgba(255,255,255,0.12); border-color: rgba(255,255,255,0.25);">
                  <div class="deliv-icon">📊</div>
                  <h4 style="color:#fff;">Tabla Mapeo 18→19</h4>
                  <p style="color:rgba(255,255,255,0.8);">Arquitectura, importaciones USD y contingencias SAT.</p>
                </div>
                <div class="deliv-card" style="background: rgba(255,255,255,0.12); border-color: rgba(255,255,255,0.25);">
                  <div class="deliv-icon">🎥</div>
                  <h4 style="color:#fff;">Grabación en 4K</h4>
                  <p style="color:rgba(255,255,255,0.8);">Acceso permanente con índice por capítulos.</p>
                </div>
                <div class="deliv-card" style="background: rgba(255,255,255,0.12); border-color: rgba(255,255,255,0.25);">
                  <div class="deliv-icon">🎓</div>
                  <h4 style="color:#fff;">Certificado Digital</h4>
                  <p style="color:rgba(255,255,255,0.8);">Acreditación oficial emitida por Vauxoo Academy.</p>
                </div>
              </div>

              <div class="closing-contact-card">
                <div>
                  <strong>Julio Serna</strong> · Project Manager & Functional Specialist<br>
                  <span style="color: rgba(255,255,255,0.8);">Vauxoo — Odoo Gold Partner</span>
                </div>
                <div style="display:flex; gap:12px; justify-content:center; margin-top:14px;">
                  <span class="pill-badge">vauxoo.com/vauxoo-academy</span>
                  <span class="pill-badge-outline">#VauxooAcademy2026</span>
                </div>
              </div>
            </div>
            '''
        }
    ]

print("Updated slides content module ready.")
