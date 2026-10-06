#!/usr/bin/env python3
# Content for all 18 slides of the Masterclass 2026

def get_slides(doodle_oval, doodle_arrow, doodle_underline, logo_white, logo_light):
    return [
        # Slide 1: Portada Oficial
        {
            "id": 1,
            "title": "Portada Oficial",
            "bg": "gradient",
            "time": "00:00",
            "block": "Apertura",
            "notes": "Bienvenida a todos los asistentes. Presentación de Julio Serna (PM y Experto Funcional en Vauxoo). Agradecimiento al equipo de Vauxoo Academy. Establecer las reglas: preguntas en el chat, sesión interactiva y enfocada en casos de trinchera mexicana.",
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
                  Domina la Valoración de Inventarios
                  {doodle_underline}
                </span>
                en Odoo 19.0
              </h1>
              <p class="cover-subtitle">
                Arquitectura AVCO (Costo Promedio), Compras en USD, Resolución de Desastres Reales y Cierre Contable alineado al SAT.
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
            "notes": "Presentar los 6 bloques estratégicos. Asegurar a la audiencia que no nos detendremos en teoría básica de Odoo, sino en arquitectura, casos prácticos y solución de errores costosos.",
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
                  <div class="agenda-time">00:00 – 00:07</div>
                  <div class="agenda-num">01</div>
                  <div class="agenda-title">EL HOOK: El Dolor que Todos Conocen</div>
                  <p class="agenda-desc">El descuadre clásico entre la Cuenta 1150 y el Reporte de Valoración. La pregunta incómoda ante el SAT.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:07 – 00:15</div>
                  <div class="agenda-num">02</div>
                  <div class="agenda-title">EL NUEVO PARADIGMA: Odoo 19 & AVCO</div>
                  <p class="agenda-desc">Adiós SVL, adiós cuentas puente interim. Por qué AVCO es el rey indiscutible para México.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:15 – 00:35</div>
                  <div class="agenda-num">03</div>
                  <div class="agenda-title">BAJO EL CAPÓ: Casos Prácticos en Vivo</div>
                  <p class="agenda-desc">Distribución pura, Manufactura WIP y el Caso Crítico: Importaciones USD con fluctuación de TC.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:35 – 00:55</div>
                  <div class="agenda-num">04</div>
                  <div class="agenda-title">LA CLÍNICA DE DESASTRES</div>
                  <p class="agenda-desc">Stock negativo, desfase cambiario en aduana, Landed Costs tardíos y contingencias fiscales con el SAT.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">00:55 – 01:10</div>
                  <div class="agenda-num">05</div>
                  <div class="agenda-title">EL MOMENTO DE LA VERDAD</div>
                  <p class="agenda-desc">Auditoría en vivo con la nueva interfaz de Odoo 19. Rastreo y corrección del descuadre inicial.</p>
                </div>
                <div class="agenda-card">
                  <div class="agenda-time">01:10 – 01:30</div>
                  <div class="agenda-num">06</div>
                  <div class="agenda-title">HOT SEAT & ENTREGABLES</div>
                  <p class="agenda-desc">Consultoría en vivo con preguntas de los asistentes. Entrega de Checklist y Tabla de Mapeo.</p>
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
            "notes": "Mostrar el split view. Preguntar en el chat: '¿A quién le ha tocado ver esto al final de mes? Pongan 🔥 en el chat'. Enfatizar el estrés de un cierre mensual cuando contabilidad y almacén se culpan mutuamente.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 1 · 00:00 - 00:07</span>
                  <h2 class="slide-title">El Dolor que Todos Conocen</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Cierre contable de mes. Dos reportes oficiales en el mismo sistema... arrojando datos distintos:</p>
              
              <div class="split-audit-container">
                <div class="audit-col audit-contable">
                  <div class="audit-col-badge">Módulo de Contabilidad</div>
                  <h3 class="audit-col-title">Balance General (Balanza)</h3>
                  <div class="audit-code">Cuenta 1150 · Inventarios / Almacén</div>
                  <div class="audit-amount">$1,450,000.00 MXN</div>
                  <div class="audit-detail">Saldo deudor al 30 de Septiembre</div>
                  <div class="audit-status audit-err">⚠️ Generado por asientos de diario</div>
                </div>

                <div class="audit-vs">
                  <div class="audit-diff-card">
                    <span class="diff-label">DESCUADRE DETECTADO</span>
                    <span class="diff-amount doodle-wrap">
                      $240,000.00 MXN
                      {doodle_oval}
                    </span>
                    <span class="diff-warn">¿Quién tiene la verdad contable?</span>
                  </div>
                </div>

                <div class="audit-col audit-logistica">
                  <div class="audit-col-badge">Módulo de Inventario</div>
                  <h3 class="audit-col-title">Reporte de Valoración</h3>
                  <div class="audit-code">Valoración Física de Stock (Valuation)</div>
                  <div class="audit-amount">$1,210,000.00 MXN</div>
                  <div class="audit-detail">Suma de productos existentes en almacén</div>
                  <div class="audit-status audit-ok">📦 Generado por Stock Moves</div>
                </div>
              </div>

              <div class="interactive-chat-prompt">
                <span class="prompt-icon">💬</span>
                <span class="prompt-text">
                  <strong>Pregunta al chat:</strong> "¿A quién le ha tocado explicarle este descuadre de $240,000 pesos al Director Financiero o al Auditor del SAT? Pongan 🔥 en el chat."
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
            "notes": "Marcar la diferencia entre un curso básico de YouTube (que solo muestra clicks ideales en base de datos demo) y una masterclass de consultoría real de Vauxoo donde se maneja dinero real, auditorías del SAT y arquitectura de Odoo 19.",
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
                Este <strong>no</strong> es un tutorial genérico. Es consultoría de trinchera para directores, contadores e implementadores:
              </p>
              <div class="value-cards-grid">
                <div class="value-card">
                  <div class="value-icon">🏗️</div>
                  <h4>Arquitectura Odoo 19.0</h4>
                  <p>Eliminación total de Stock Valuation Layers (SVL) y cuentas puente interim. Cómo cambia la lógica contable en la base de datos.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">🇲🇽</div>
                  <h4>Especialización México & AVCO</h4>
                  <p>Por qué en México ignoramos FIFO y Estándar. Costo Promedio Ponderado alineado a NIF C-4 y Art. 41 LISR.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">💵</div>
                  <h4>El Caso Crítico: USD en MXN</h4>
                  <p>Cómo resolver los desastres generados por recepción de mercancía extranjera con fluctuación de Tipo de Cambio vs Factura.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">⚙️</div>
                  <h4>Impacto en Manufactura (WIP)</h4>
                  <p>Por qué el 80% de las empresas industriales pierden el control de su AVCO al procesar órdenes de ensamble incompletas.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">🔍</div>
                  <h4>Auditoría y Corrección en Vivo</h4>
                  <p>Rastreo con precisión de bisturí del asiento manual intruso que causa el descuadre del Bloque 1 y su reversión sin tocar código.</p>
                </div>
                <div class="value-card">
                  <div class="value-icon">📋</div>
                  <h4>Entregables de Producción</h4>
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
            "notes": "Detallar el cambio de arquitectura. En Odoo 19.0 el modelo stock.valuation.layer ya no es el motor contable independiente; la valoración vive dentro de stock.move. Las cuentas interim (Stock Input/Output) desaparecen del catálogo predeterminado.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 2 · 00:07 - 00:15</span>
                  <h2 class="slide-title">El Gran Cambio Arquitectónico en Odoo 19.0</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Odoo 19 rediseña por completo el motor de inventario y contabilidad eliminando capas intermedias:</p>
              
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
                      <td><span class="tag-old">stock.valuation.layer (SVL)</span><br><small>Tabla separada que a menudo se desfasaba</small></td>
                      <td><span class="tag-new">Directo en stock.move</span><br><small>El movimiento físico ES el registro de valor</small></td>
                      <td>Trazabilidad directa por CFDI y póliza sin discrepancias de tablas</td>
                    </tr>
                    <tr>
                      <td><strong>Cuentas Puente</strong></td>
                      <td><span class="tag-old">Interim Input / Output</span><br><small>Cuentas temporales que acumulaban basura</small></td>
                      <td><span class="tag-new">Asiento Directo</span><br><small>Afectación directa entre Proveedores y 1150</small></td>
                      <td>Balanza de comprobación del SAT infinitamente más limpia</td>
                    </tr>
                    <tr>
                      <td><strong>Modelo Contable</strong></td>
                      <td><span class="tag-old">Continental vs Anglo-Sajón</span><br><small>Confuso para implementadores de LATAM</small></td>
                      <td><span class="tag-new">Periódico vs Perpetuo</span><br><small>Terminología contable estándar internacional</small></td>
                      <td>Claridad absoluta: en México siempre usamos Perpetuo con AVCO</td>
                    </tr>
                    <tr>
                      <td><strong>Auditoría & Cierre</strong></td>
                      <td><span class="tag-old">Vistas dispersas</span><br><small>Revisión manual en múltiples menús</small></td>
                      <td><span class="tag-new">Accounting > Review > Valuation</span><br><small>Panel centralizado de validación y corte</small></td>
                      <td>Bloqueo automático de movimientos fuera de fecha de corte</td>
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
            "notes": "Explicar el fundamento legal y técnico: NIF C-4 y Art. 41 de la Ley del ISR. Enfatizar por qué FIFO y Costo Estándar causan dolores de cabeza en empresas mexicanas con Odoo.",
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
                  <p>Genera cuentas de variación en costo de ventas que requieren reclasificación fiscal para no ser rechazadas en la Declaración Anual del SAT.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 7: Bloque 3 - Caso 1: Distribución Comercial
        {
            "id": 7,
            "title": "Caso Práctico 1: Distribución Comercial",
            "bg": "white",
            "time": "00:15 - 00:20",
            "block": "Bloque 3",
            "notes": "Demostrar en vivo el flujo compra -> recepción -> venta -> entrega en moneda base MXN. Mostrar las pólizas contables resultantes en Odoo 19 y verificar que la cuenta 1150 y 5100 reflejan la realidad.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 1</span>
                  <h2 class="slide-title">Distribución Pura en MXN (Compra y Venta)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Flujo comercial estándar: Compra de 100 unidades a $100 MXN, venta de 40 unidades a $250 MXN.</p>
              
              <div class="flow-steps-grid">
                <div class="flow-step-card">
                  <div class="step-badge">PASO 1: RECEPCIÓN FÍSICA</div>
                  <h4>Stock Move de Entrada (IN)</h4>
                  <p>Recepción de 100 piezas a almacén general.</p>
                  <div class="asiento-box">
                    <div class="asiento-row"><span class="cargo">CARGO</span> 1150 Inventarios <strong>$10,000 MXN</strong></div>
                    <div class="asiento-row"><span class="abono">ABONO</span> 2110 Proveedores (o Tránsito) <strong>$10,000 MXN</strong></div>
                  </div>
                  <div class="step-avco">Nuevo AVCO: <strong>$100.00 MXN</strong></div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">PASO 2: ENTREGA AL CLIENTE</div>
                  <h4>Stock Move de Salida (OUT)</h4>
                  <p>Despacho de 40 piezas según orden de venta.</p>
                  <div class="asiento-box">
                    <div class="asiento-row"><span class="cargo">CARGO</span> 5100 Costo de Ventas <strong>$4,000 MXN</strong></div>
                    <div class="asiento-row"><span class="abono">ABONO</span> 1150 Inventarios <strong>$4,000 MXN</strong></div>
                  </div>
                  <div class="step-avco">Stock Remanente: 60 pzas = <strong>$6,000 MXN</strong></div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">PASO 3: FACTURACIÓN & CFDI</div>
                  <h4>Factura de Cliente (INV)</h4>
                  <p>Timbrado CFDI 4.0 por $10,000 MXN + IVA.</p>
                  <div class="asiento-box">
                    <div class="asiento-row"><span class="cargo">CARGO</span> 1050 Clientes <strong>$11,600 MXN</strong></div>
                    <div class="asiento-row"><span class="abono">ABONO</span> 4010 Ingresos <strong>$10,000 MXN</strong></div>
                    <div class="asiento-row"><span class="abono">ABONO</span> 2080 IVA Trasladado <strong>$1,600 MXN</strong></div>
                  </div>
                  <div class="step-avco">Margen Bruto: <strong>$6,000 MXN (60%)</strong></div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 8: Bloque 3 - Caso 2: Manufactura MRP y Cuenta WIP
        {
            "id": 8,
            "title": "Caso Práctico 2: Manufactura MRP y WIP",
            "bg": "white",
            "time": "00:20 - 00:27",
            "block": "Bloque 3",
            "notes": "Mostrar el flujo de ensamble. El 80% de los errores industriales en Odoo se deben a órdenes de manufactura en estado 'En Proceso' al cierre de mes, dejando saldos flotantes en la cuenta 1160 (WIP) sin cerrar.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 2</span>
                  <h2 class="slide-title">Manufactura (MRP) y el Misterio de la Cuenta WIP (1160)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="mrp-split">
                <div class="mrp-diagram">
                  <div class="mrp-box mrp-mat">
                    <span class="mrp-tag">MATERIAS PRIMAS (1150)</span>
                    <p>Componente A: 2 pzas @ $50 = $100<br>Componente B: 1 pza @ $150 = $150</p>
                    <strong>Costo Total Insumos: $250 MXN</strong>
                  </div>
                  <div class="mrp-arrow">⬇️ Consumo en Orden de Producción</div>
                  <div class="mrp-box mrp-wip">
                    <span class="mrp-tag">PRODUCCIÓN EN PROCESO (WIP 1160)</span>
                    <p>Absorbe los insumos consumidos mientras la orden está en piso.</p>
                    <strong style="color: #AC0340;">⚠️ Riesgo si se queda abierta a fin de mes</strong>
                  </div>
                  <div class="mrp-arrow">⬇️ Validación Final (Mark as Done)</div>
                  <div class="mrp-box mrp-pt">
                    <span class="mrp-tag">PRODUCTO TERMINADO (1150)</span>
                    <p>1 Unidad Ensamblada entra al inventario a su AVCO exacto: <strong>$250 MXN</strong></p>
                  </div>
                </div>

                <div class="mrp-insights">
                  <div class="alert-box">
                    <h4>🚨 La Trampa de Cierre de Mes en Manufactura</h4>
                    <p>Si una Orden de Producción consume materias primas el 29 de Septiembre pero se valida hasta el 2 de Octubre:</p>
                    <ul class="styled-list">
                      <li>La materia prima ya salió de la cuenta 1150.</li>
                      <li>El producto terminado aún no entra a la cuenta 1150.</li>
                      <li>El valor está atrapado en la cuenta 1160 (WIP).</li>
                      <li><strong>El reporte de inventario físico marcará descuadre con el balance general</strong> si el contador no suma la cuenta 1160.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 9: Bloque 3 - Caso 3: Importaciones USD en MXN (CRÍTICO)
        {
            "id": 9,
            "title": "Caso Crítico: Importaciones USD en Cía MXN",
            "bg": "gradient",
            "time": "00:27 - 00:35",
            "block": "Bloque 3",
            "notes": "EL CASO ESTRELLA. Explicar la línea de tiempo: PO confirmada a TC1, Recepción aduanal a TC2, Factura a TC3. Mostrar cómo Odoo 19 calcula la diferencia cambiaria y por qué no debe contaminar el AVCO si no corresponde.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO CRÍTICO</span>
                  <h2 class="slide-title" style="color: #fff;">Importaciones en USD para Compañía en MXN</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                La magia y el terror de comprar a proveedores extranjeros con fluctuación del Tipo de Cambio:
              </p>
              
              <div class="usd-timeline">
                <div class="timeline-step">
                  <div class="timeline-dot">1</div>
                  <div class="timeline-header">DÍA 1: Orden de Compra</div>
                  <div class="timeline-body">
                    <p>PO confirmada por <strong>$10,000 USD</strong></p>
                    <div class="tc-badge">TC Pactado: $18.50</div>
                    <div class="timeline-val">Valor estimado: $185,000 MXN</div>
                    <small>No genera asiento contable aún</small>
                  </div>
                </div>

                <div class="timeline-step">
                  <div class="timeline-dot">2</div>
                  <div class="timeline-header">DÍA 15: Recepción Física</div>
                  <div class="timeline-body">
                    <p>Mercancía ingresa a aduana y se valida entrada.</p>
                    <div class="tc-badge" style="background:#AC0340;">TC DOF Oficial: $19.20</div>
                    <div class="timeline-val">Entrada Inventario: <strong>$192,000 MXN</strong></div>
                    <small>El AVCO absorbe $19.20 por unidad</small>
                  </div>
                </div>

                <div class="timeline-step">
                  <div class="timeline-dot">3</div>
                  <div class="timeline-header">DÍA 25: Factura Proveedor</div>
                  <div class="timeline-body">
                    <p>Llega Invoice / CFDI con pedimento.</p>
                    <div class="tc-badge">TC Fecha Factura: $19.50</div>
                    <div class="timeline-val">Deuda Proveedor: <strong>$195,000 MXN</strong></div>
                    <small>Diferencia de $3,000 MXN</small>
                  </div>
                </div>
              </div>

              <div class="usd-verdict-box">
                <div class="verdict-col">
                  <h4>¿A dónde van los $3,000 MXN de diferencia?</h4>
                  <p>En Odoo 19.0, la diferencia cambiaria entre recepción y factura <strong>NO recalcula el AVCO</strong> si el inventario ya se valuó a la tasa oficial de importación. Se registra como <strong>Pérdida Cambiaria (Cuenta 6100)</strong>.</p>
                </div>
                <div class="verdict-col">
                  <h4>Criterio SAT / Pedimento Aduanal</h4>
                  <p>El valor fiscal del inventario para efectos aduanales y deducción es el asentado en el <strong>Pedimento (Tipo de Cambio Oficial del DOF)</strong> al momento de cruce.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 10: Bloque 4 - Desastre #1: Stock Negativo
        {
            "id": 10,
            "title": "Desastre #1: Stock Negativo con AVCO",
            "bg": "white",
            "time": "00:35 - 00:40",
            "block": "Bloque 4",
            "notes": "Mostrar qué ocurre matemáticamente cuando se permite vender en negativo con Costo Promedio. El promedio ponderado se corrompe porque se multiplica o divide por cantidades negativas.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">ERROR CATASTRÓFICO #1</span>
                  <h2 class="slide-title">El Veneno Matemático: Stock Negativo en AVCO</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="disaster-grid">
                <div class="disaster-main">
                  <h3>¿Qué pasa cuando vendes lo que no tienes?</h3>
                  <div class="disaster-sequence">
                    <div class="seq-step">
                      <span class="seq-num">1</span>
                      <div>Stock inicial en cero. Se realiza venta y entrega de <strong>-10 unidades</strong>.</div>
                    </div>
                    <div class="seq-step">
                      <span class="seq-num">2</span>
                      <div>El sistema no sabe a qué costo sacar el producto. Asigna un costo provisional de $0.00 o último conocido.</div>
                    </div>
                    <div class="seq-step">
                      <span class="seq-num">3</span>
                      <div>Días después entra la compra de 15 unidades a $200 MXN.</div>
                    </div>
                    <div class="seq-step" style="background: #FEE2E2; border: 1px solid #FCA5A5;">
                      <span class="seq-num" style="background:#B91C1C;">💥</span>
                      <div><strong>La fórmula de AVCO se corrompe:</strong> El sistema intenta promediar con un saldo negativo, resultando en costos unitarios de <strong>$1,800 MXN o costos negativos</strong>.</div>
                    </div>
                  </div>
                </div>

                <div class="disaster-sat">
                  <div class="sat-warn-card">
                    <h4>⚖️ Consecuencias Fiscales SAT</h4>
                    <ul class="styled-list">
                      <li><strong>Kardex Ilegal:</strong> El SAT prohíbe inventarios negativos en la contabilidad electrónica.</li>
                      <li><strong>Rechazo de Deducción:</strong> El Costo de lo Vendido calculado con AVCO corrompido es rechazado por la autoridad.</li>
                      <li><strong>Multas por Inconsistencia:</strong> Sanciones de hasta $45,000 MXN por reporte distorsionado.</li>
                    </ul>
                    <div class="sat-rule-badge">REGLA VAUXOO: Desactivar ventas sin stock en categorías AVCO</div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 11: Bloque 4 - Desastre #2 & #3: Desfase y Landed Costs
        {
            "id": 11,
            "title": "Desastre #2 & #3: Desfase Cambiario y Landed Costs",
            "bg": "white",
            "time": "00:40 - 00:47",
            "block": "Bloque 4",
            "notes": "Detallar el error de los Costos en Destino (Landed Costs) aplicados tarde. Si la mercancía ya se vendió y se entregó al cliente, el Landed Cost ya no puede agregarse al inventario porque físicamente ya no existe en el almacén.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA DE DESASTRES #2 Y #3</span>
                  <h2 class="slide-title">Desfase Cambiario & Landed Costs Tardíos</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="two-col-grid">
                <div class="disaster-col-card">
                  <div class="card-pill">DESASTRE #2</div>
                  <h3>Desfase Cambiario en Recepciones</h3>
                  <p class="card-lead">Validar recepciones con el tipo de cambio del sistema desactualizado.</p>
                  <div class="detail-box">
                    <strong>El error:</strong> Odoo tiene configurado un TC fijo de $17.50 desde hace 3 semanas. Llega una importación y se valida. El producto queda valuado a $17.50 en lugar de los $19.30 reales.
                    <br><br>
                    <strong>La consecuencia:</strong> Subvaluación del inventario en balance y sobrefacturación de utilidad contable artificial sujeta a más impuestos.
                  </div>
                </div>

                <div class="disaster-col-card">
                  <div class="card-pill">DESASTRE #3</div>
                  <h3>Landed Costs Cuando Ya Se Vendió el Stock</h3>
                  <p class="card-lead">Aplicar gastos aduanales a mercancía que ya no está en almacén.</p>
                  <div class="detail-box">
                    <strong>El error:</strong> Llegan 50 máquinas importadas. Se venden las 50 en la misma semana. Tres semanas después llega la factura del Agente Aduanal ($80,000 MXN) y se aplica como Costo en Destino.
                    <br><br>
                    <strong>En Odoo 19:</strong> El sistema detecta que el stock es 0 y desvía el valor directamente a <strong>Costo de Ventas (5100)</strong>, evitando inflar un inventario inexistente.
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 12: Bloque 4 - Desastre #4: Ajustes Masivos y SAT
        {
            "id": 12,
            "title": "Desastre #4: Ajustes Masivos y el SAT",
            "bg": "white",
            "time": "00:47 - 00:55",
            "block": "Bloque 4",
            "notes": "Alerta crítica de cierre anual. Los contadores o directores que hacen ajustes masivos de inventario para cuadrar números a mano sin saber que el SAT grava los sobrantes como ingresos y los faltantes como ventas omitidas.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">ERROR CATASTRÓFICO #4</span>
                  <h2 class="slide-title">Ajustes Masivos e Implicaciones Fiscales SAT</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">La tentación peligrosa: "Haz un ajuste de inventario para que cuadre el balance general".</p>
              
              <div class="sat-fiscal-table-container">
                <table class="sat-fiscal-table">
                  <thead>
                    <tr>
                      <th>Tipo de Ajuste Físico</th>
                      <th>Causa Operativa</th>
                      <th>Interpretación Legal del SAT (México)</th>
                      <th>Riesgo Fiscal & Multa</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><span class="pill-badge" style="background:#0D9488;">SOBRANTE DE STOCK</span></td>
                      <td>Mercancía recibida no registrada o conteo superior</td>
                      <td><strong>Ingreso Acumulable Presunto</strong><br>El SAT asume que compraste sin factura fiscal.</td>
                      <td>Pago de ISR sobre el valor del sobrante + actualización y recargos.</td>
                    </tr>
                    <tr>
                      <td><span class="pill-badge" style="background:#DC2626;">FALTANTE DE STOCK</span></td>
                      <td>Robo hormiga, merma no documentada o extravío</td>
                      <td><strong>Venta Omitida Presunta</strong><br>El SAT presume que vendiste en efectivo sin emitir CFDI.</td>
                      <td>Determinación presuntiva de IVA no trasladado e ISR omitido.</td>
                    </tr>
                    <tr>
                      <td><span class="pill-badge" style="background:#4B5563;">CAMBIO DE MÉTODO</span></td>
                      <td>Pasar de Costo Estándar a AVCO sin dictamen</td>
                      <td><strong>Infracción al Código Fiscal</strong><br>El Art. 41 LISR exige conservar el método por 5 años.</td>
                      <td>Nulidad de deducciones de costo de venta del ejercicio auditado.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            '''
        },
        # Slide 13: Bloque 5 - El Momento de la Verdad: Auditoría
        {
            "id": 13,
            "title": "El Momento de la Verdad: Auditoría en Vivo",
            "bg": "gradient",
            "time": "00:55 - 01:05",
            "block": "Bloque 5",
            "notes": "Iniciar la resolución en vivo. Mostrar la nueva pantalla de Odoo 19: Accounting > Review > Inventory Valuation. Demostrar cómo se filtran los movimientos y se cruza contra la cuenta 1150.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · 00:55 - 01:10</span>
                  <h2 class="slide-title" style="color: #fff;">El Momento de la Verdad: Auditoría en Vivo</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              <p class="slide-lead" style="color: rgba(255,255,255,0.9);">
                Metodología estandarizada de Vauxoo para auditar la valoración en Odoo 19.0:
              </p>
              
              <div class="audit-steps-grid">
                <div class="audit-step-card">
                  <div class="audit-step-num">PASO 1</div>
                  <h4>Acceder a Inventory Valuation</h4>
                  <p>Menú <code>Contabilidad > Revisión > Valoración de Inventario</code>. Odoo 19 unifica los datos de stock.move directamente.</p>
                </div>
                <div class="audit-step-card">
                  <div class="audit-step-num">PASO 2</div>
                  <h4>Fijar Fecha de Corte</h4>
                  <p>Establecer fecha exacta de corte (ej. 30/09 23:59:59). Bloquear transacciones posteriores para evitar ruido.</p>
                </div>
                <div class="audit-step-card">
                  <div class="audit-step-num">PASO 3</div>
                  <h4>Comparar contra Balanza</h4>
                  <p>Abrir en pestaña paralela la Balanza de Comprobación filtrada a la cuenta <strong>1150 (Inventarios)</strong>.</p>
                </div>
                <div class="audit-step-card">
                  <div class="audit-step-num">PASO 4</div>
                  <h4>Rastrear Pólizas Manuales</h4>
                  <p>Filtrar en los apuntes contables (account.move.line) de la 1150 aquellos cuyo campo <strong>stock_move_id esté vacío</strong>.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 14: Bloque 5 - Resolución del Descuadre Inicial
        {
            "id": 14,
            "title": "Resolución del Descuadre en Vivo",
            "bg": "white",
            "time": "01:05 - 01:10",
            "block": "Bloque 5",
            "notes": "Resolver el hook del inicio. Encontramos la póliza manual #AS/2026/09/0042 de $240,000 MXN que contabilidad metió directamente a la cuenta 1150. Al revertirla y generar el ajuste logístico formal, ambos reportes cuadran al centavo exacto.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">RESOLUCIÓN EN VIVO</span>
                  <h2 class="slide-title">¡Misterio Resuelto! El Asiento Fantasma</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="resolution-container">
                <div class="culprit-box">
                  <div class="culprit-badge">🔍 ORIGEN DEL DESCUADRE DETECTADO</div>
                  <h3>Póliza Manual Indebida: #AS/2026/09/0042</h3>
                  <div class="culprit-desc">
                    El equipo contable intentó registrar un "ajuste financiero" directo con una póliza de diario manual en la cuenta 1150 por <strong>$240,000.00 MXN</strong>.
                  </div>
                  <div class="culprit-flaw">
                    ❌ Una póliza manual en la cuenta 1150 <strong>NO crea movimientos de inventario (stock.move)</strong>. Rompe la paridad física y contable.
                  </div>
                </div>

                <div class="action-result-box">
                  <div class="result-step">
                    <strong>Acción Correctiva:</strong> Reversión inmediata de la póliza manual + Registro del ajuste mediante el módulo de Inventario con su Stock Move correspondiente.
                  </div>
                  <div class="balanced-state">
                    <div class="bal-item">
                      <span>Cuenta 1150 (Balanza)</span>
                      <strong>$1,210,000.00 MXN</strong>
                    </div>
                    <div class="bal-equal">=</div>
                    <div class="bal-item">
                      <span>Reporte de Valoración</span>
                      <strong>$1,210,000.00 MXN</strong>
                    </div>
                    <div class="bal-status">
                      ✅ CUADRE PERFECTO (Diferencia: $0.00)
                    </div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 15: Bloque 5 - Las 3 Reglas de Oro en México
        {
            "id": 15,
            "title": "Las 3 Reglas de Oro de Vauxoo",
            "bg": "white",
            "time": "01:08 - 01:10",
            "block": "Bloque 5",
            "notes": "Presentar las 3 reglas de oro que todo director, contador o implementador debe tatuarse para operar inventarios en México con Odoo 19.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MEJORES PRÁCTICAS</span>
                  <h2 class="slide-title">Las 3 Reglas de Oro de Vauxoo para México</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="golden-rules-grid">
                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA DE ORO #1</div>
                  <h3>Cero Stock Negativo en AVCO</h3>
                  <p>Jamás permitas vender o despachar sin existencias físicas en el sistema para categorías valuadas en Costo Promedio. Si la logística va tarde, captura la recepción antes de confirmar la entrega.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA DE ORO #2</div>
                  <h3>El "Cut-Off" de Fin de Mes es Innegociable</h3>
                  <p>Todo movimiento físico ocurrido en el mes debe tener su Stock Move validado antes de las 23:59:59 del último día. Ninguna factura de proveedor debe timbrarse con fecha posterior a la recepción física sin conciliar.</p>
                </div>

                <div class="golden-rule-card">
                  <div class="rule-medal">🥇</div>
                  <div class="rule-num">REGLA DE ORO #3</div>
                  <h3>Tipo de Cambio Riguroso al Validar Recepciones</h3>
                  <p>Al recibir compras de importación en USD, verifica que la tasa de cambio en Odoo coincida con la tasa oficial del pedimento aduanal (DOF). Esto blinda el kardex fiscal ante cualquier auditoría del SAT.</p>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 16: Bloque 6 - Hot Seat Q&A
        {
            "id": 16,
            "title": "Hot Seat Q&A: Consultoría en Vivo",
            "bg": "gradient",
            "time": "01:10 - 01:25",
            "block": "Bloque 6",
            "notes": "Abrir el micrófono y el chat para el Hot Seat. Julio responde los casos más complejos de la audiencia en vivo aplicando la lógica de Odoo 19 y normativa mexicana.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 6 · 01:10 - 01:30</span>
                  <h2 class="slide-title" style="color: #fff;">Q&A Hot Seat: Consultoría en Vivo</h2>
                </div>
                <div class="slide-header-logo">{logo_white}</div>
              </div>
              
              <div class="hotseat-container">
                <div class="hotseat-badge-col">
                  <div class="hotseat-icon">🔥</div>
                  <h3>Tu Turno en el Micrófono</h3>
                  <p>Expón tu caso más crítico de inventarios, importaciones o descuadres contables.</p>
                </div>
                <div class="hotseat-topics">
                  <h4>Temas Prioritarios para la Sesión:</h4>
                  <ul class="styled-list" style="color: rgba(255,255,255,0.9);">
                    <li>¿Tienes discrepancias históricas arrastradas desde Odoo 16, 17 o 18?</li>
                    <li>¿Dudas con el tratamiento de pedimentos aduanales consolidados?</li>
                    <li>¿Problemas de valoración con subproductos o mermas en manufactura?</li>
                    <li>¿Cómo preparar la migración limpia a Odoo 19.0 sin contaminar la cuenta 1150?</li>
                  </ul>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 17: Paquete de Entregables
        {
            "id": 17,
            "title": "Paquete de Entregables Oficiales",
            "bg": "white",
            "time": "01:25 - 01:28",
            "block": "Bloque 6",
            "notes": "Mostrar los recursos incluidos con los $100 USD de la Masterclass: Checklist de Auditoría interactivo e imprimible, Tabla de Mapeo conceptual Odoo 18 vs 19, Grabación 4K y Certificado oficial emitido por Vauxoo Academy.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MATERIALES DE LA MASTERCLASS</span>
                  <h2 class="slide-title">Recursos Oficiales Incluidos</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              
              <div class="deliverables-grid">
                <div class="deliv-card">
                  <div class="deliv-icon">📋</div>
                  <h4>Entregable #1: Checklist de Auditoría</h4>
                  <p>Guía de validación paso a paso de 2 páginas en PDF para ejecutar en cada cierre de mes con tu equipo contable y logístico.</p>
                  <a href="#tab-checklist" onclick="switchTab('checklist')" class="btn btn-sm">Ver Checklist Interactivo</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">📊</div>
                  <h4>Entregable #2: Tabla de Mapeo 18 → 19</h4>
                  <p>Matriz de arquitectura técnica y fiscal comparando el comportamiento de Stock Moves, cuentas puente y kardex SAT.</p>
                  <a href="#tab-mapeo" onclick="switchTab('mapeo')" class="btn btn-sm">Ver Guía & Mapeo</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">🎥</div>
                  <h4>Grabación en Alta Definición</h4>
                  <p>Acceso permanente a la grabación completa de la sesión con índice interactivo por capítulos para consulta continua.</p>
                  <span class="pill-badge-outline" style="color:#64748B; border-color:#CBD5E1;">Acceso de por vida</span>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">🎓</div>
                  <h4>Certificado Vauxoo Academy</h4>
                  <p>Acreditación digital oficial con verificación blockchain de asistencia a la Masterclass 2026 de Odoo 19.0.</p>
                  <span class="pill-badge-outline" style="color:#64748B; border-color:#CBD5E1;">Emisión personalizada</span>
                </div>
              </div>
            </div>
            '''
        },
        # Slide 18: Cierre y Agradecimiento
        {
            "id": 18,
            "title": "Cierre y Agradecimientos",
            "bg": "gradient",
            "time": "01:28 - 01:30",
            "block": "Cierre",
            "notes": "Agradecer a todos los asistentes. Recordar que los materiales están disponibles en el portal. Recomendar seguir a Vauxoo Academy para las próximas Masterclasses del ciclo 2026.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-logo-wrap">
                {logo_white}
              </div>
              <h2 style="font-size: 2.2rem; font-weight: 700; margin-bottom: 12px; color: #fff;">
                Aprende. Evoluciona. Transforma.
              </h2>
              <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); max-width: 650px; margin: 0 auto 32px;">
                Gracias por acompañarnos en esta Masterclass de Vauxoo Academy. Tu contabilidad y tu inventario ahora hablan el mismo idioma.
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

print("Slide generator module ready.")
