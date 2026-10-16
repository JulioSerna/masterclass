#!/usr/bin/env python3
# Content for all slides of the Masterclass 2026
# Aligned strictly with masterclass-plan-final.md v8
# Duración: 150 minutos (120 min exposición + 30 min Q&A)
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
            "notes": "Bienvenida de Julio Serna (PM y Experto Funcional en Vauxoo). Masterclass 2026 de Vauxoo Academy. 150 minutos (2 horas de exposición + 30 min de Q&A en vivo) enfocados en la sincronía contable y logística en Odoo 19.0 Enterprise.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-logo-wrap">
                {logo_white}
              </div>
              <div class="cover-badge-row">
                <span class="pill-badge">MASTERCLASS 2026</span>
                <span class="pill-badge-outline">ODOO 19.0 ENTERPRISE · MÉXICO</span>
                <span class="pill-badge-outline">150 MINUTOS (120 MIN + 30 MIN Q&A)</span>
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

        # Slide 2: El Hook - Descuadre de $196,190 MXN
        {
            "id": 2,
            "title": "El Hook: Descuadre de $196,190 MXN",
            "bg": "white",
            "time": "00:01 - 00:06",
            "block": "Bloque 1",
            "notes": "Mostrar el split view en vivo en Odoo 19: Balanza 115.01.01 ($535,100.00 MXN) vs Reporte de Existencias ($338,910.00 MXN) -> Descuadre real de $196,190.00 MXN ($487k de póliza manual - facturas por recibir pendientes + descuadres operativos). Plantear el dolor de todo cierre contable.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 1 · 00:00 - 00:12</span>
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
                  <div class="audit-amount">$535,100.00 MXN</div>
                  <div class="audit-detail">Saldo deudor contable al corte mensual</div>
                  <div class="audit-status audit-err">⚠️ Generado por libro mayor contable</div>
                </div>

                <div class="audit-vs">
                  <div class="audit-diff-card">
                    <span class="diff-label">DESCUADRE REAL</span>
                    <span class="diff-amount doodle-wrap">
                      $196,190.00 MXN
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

              <div class="interactive-chat-prompt">
                <span class="prompt-icon">💬</span>
                <span class="prompt-text">
                  <strong>Pregunta al chat:</strong> ¿A quién le ha tocado explicarle este descuadre al Director General o al Auditor? Pongan <strong>🔥</strong> en el chat.
                </span>
              </div>
            </div>
            '''
        },

        # Slide 3: Las 3 Causas Raíz del Divorcio
        {
            "id": 3,
            "title": "Las 3 Causas Recurrentes del Divorcio",
            "bg": "white",
            "time": "00:06 - 00:10",
            "block": "Bloque 1",
            "notes": "Introducir las 3 causas raíz identificadas por Vauxoo: 1. Configuración errática (cambios en caliente); 2. Parches operativos (pólizas manuales del contador a la 1150); 3. Ceguera de auditoría (esperar al cierre anual).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">MARCO CONCEPTUAL · EL ORIGEN DE LA BRECHA</span>
                  <h2 class="slide-title">Las 3 Causas Raíz del Divorcio Contable-Logístico</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Lo que detectamos tras más de una década auditando bases de datos de Odoo en empresas de México:</p>
              
              <div class="root-causes-grid">
                <!-- Causa 1 -->
                <div class="root-cause-card" style="border-top: 4px solid #E4A900;">
                  <div class="cause-card-header">
                    <span class="cause-icon-pill">⚙️</span>
                    <span class="cause-number">01</span>
                  </div>
                  <span class="cause-category-tag" style="color:#B45309;">ERROR DE CONFIGURACIÓN</span>
                  <h3 class="cause-headline">Cambios de Categoría "en Caliente"</h3>
                  <div class="cause-subhead">"Dos malas no hacen una buena"</div>
                  
                  <div class="cause-blocks">
                    <div class="cause-block block-error">
                      <span class="block-label">❌ La Mala Práctica</span>
                      Cambiar una categoría de <em>Periódico a Perpetuo</em> o de <em>Estándar a AVCO</em> cuando ya existen existencias activas en almacén.
                    </div>
                    <div class="cause-block block-impact">
                      <span class="block-label">💥 El Impacto Real</span>
                      Odoo 19 <strong>NO genera pólizas retroactivas</strong>. El stock previo queda como inventario fantasma sin respaldo contable en la 1150.
                    </div>
                    <div class="cause-block block-rule">
                      <span class="block-label">🛡️ Regla de Oro</span>
                      <strong>Nunca edites la valoración de una categoría viva.</strong> Crea una categoría nueva y traslada existencias con un corte limpio.
                    </div>
                  </div>
                </div>

                <!-- Causa 2 -->
                <div class="root-cause-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="cause-card-header">
                    <span class="cause-icon-pill">🩹</span>
                    <span class="cause-number">02</span>
                  </div>
                  <span class="cause-category-tag" style="color:var(--rojo-vauxoo);">ERROR OPERATIVO</span>
                  <h3 class="cause-headline">El Parche Manual ("La Aspirina")</h3>
                  <div class="cause-subhead">"Cuadra el papel hoy, destruye el sistema mañana"</div>
                  
                  <div class="cause-blocks">
                    <div class="cause-block block-error">
                      <span class="block-label">❌ La Mala Práctica</span>
                      Ante la urgencia del cierre mensual, el contador mete un asiento manual directo en la cuenta 1150 para forzar el cuadre contra el reporte.
                    </div>
                    <div class="cause-block block-impact">
                      <span class="block-label">💥 El Impacto Real</span>
                      Cuadra la balanza en papel, pero <strong>fractura el sistema de por vida</strong>: existe dinero en contabilidad que ningún producto ni tarima respalda.
                    </div>
                    <div class="cause-block block-rule">
                      <span class="block-label">🛡️ Regla de Oro</span>
                      <strong>La cuenta 1150 es sagrada:</strong> solo debe ser alimentada por compras y movimientos de almacén, jamás por pólizas manuales.
                    </div>
                  </div>
                </div>

                <!-- Causa 3 -->
                <div class="root-cause-card" style="border-top: 4px solid #172A45;">
                  <div class="cause-card-header">
                    <span class="cause-icon-pill">⏳</span>
                    <span class="cause-number">03</span>
                  </div>
                  <span class="cause-category-tag" style="color:#0D9488;">ERROR DE CONTROL</span>
                  <h3 class="cause-headline">Ceguera por Falta de Cadencia</h3>
                  <div class="cause-subhead">"Esperar al cierre anual para auditar"</div>
                  
                  <div class="cause-blocks">
                    <div class="cause-block block-error">
                      <span class="block-label">❌ La Mala Práctica</span>
                      Revisar la concordancia entre almacén y balanza una sola vez al año cuando llega el auditor externo o la declaración fiscal.
                    </div>
                    <div class="cause-block block-impact">
                      <span class="block-label">💥 El Impacto Real</span>
                      Tras 12 meses y 20,000 transacciones, rastrear qué recepción, ajuste o nota de crédito causó el desvío es una pesadilla forense interminable.
                    </div>
                    <div class="cause-block block-rule">
                      <span class="block-label">🛡️ Regla de Oro</span>
                      <strong>Auditoría diaria de 3 minutos:</strong> comparar Balanza vs Existencias todos los días detecta anomalías al vuelo con costo cero.
                    </div>
                  </div>
                </div>
              </div>

              <div class="cause-takeaway-banner">
                💡 <strong>Axioma Fundamental de la Masterclass:</strong> El inventario no se arregla en el libro diario contable; se cuida, audita y sanea en la disciplina operativa del almacén.
              </div>
            </div>
            '''
        },

        # Slide 4: Cadencia de Auditoría
        {
            "id": 4,
            "title": "Matriz de Cadencia de Auditoría",
            "bg": "white",
            "time": "00:10 - 00:12",
            "block": "Bloque 1",
            "notes": "La importancia de la frecuencia de auditoría. Diario = 2 min (fácil). Semanal = 15 min (recomendado). Mensual = 1-2 hrs (cierre). Anual = semanas de sufrimiento (evitar).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">DISCIPLINA OPERATIVA</span>
                  <h2 class="slide-title">La Regla de Oro de la Cadencia (Vauxoo Standard)</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">¿Con qué frecuencia deberías comparar la Balanza de Comprobación con el Reporte de Existencias?</p>
              
              <div class="table-wrap">
                <table class="cadencia-table">
                  <thead>
                    <tr>
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
                      <td>Detección inmediata de cualquier desvío (1-2 movimientos); cero sorpresas a fin de mes.</td>
                    </tr>
                    <tr>
                      <td><strong>Semanal</strong></td>
                      <td>⭐⭐⭐⭐ <span class="pill-badge" style="background:#0D9488;">RECOMENDADO</span></td>
                      <td>15 minutos</td>
                      <td>Corrección oportuna de recepciones o tipos de cambio erróneos sin fricción.</td>
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
            "time": "00:12 - 00:16",
            "block": "Bloque 2",
            "notes": "Explicar las 4 grandes razones arquitectónicas de Odoo 19: sin tabla SVL (valoración vive directamente en stock.move), sin cuentas interim en flujos directos, terminología formal Periódico/Perpetuo, y auditoría transparente directa en stock.move y balanza.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 2 · 00:12 - 00:30</span>
                  <h2 class="slide-title">Odoo 19.0: La Gran Simplificación de la Auditoría</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Por qué elegimos la versión 19.0 para esta masterclass: auditoría 10 veces más limpia, transparente y directa:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(2, 1fr); gap: 18px;">
                <div class="agenda-card" style="border-top: 4px solid var(--rojo-vauxoo);">
                  <div class="agenda-time">ARQUITECTURA DE DATOS</div>
                  <div class="agenda-title">Adiós Capas Ocultas (stock_valuation_layer)</div>
                  <p class="agenda-desc">En versiones previas, la valoración dependía de una tabla intermedia separada propensa a desincronizarse. En Odoo 19 el valor y costo unitario residen <strong>directamente en cada movimiento de stock (<code>stock.move</code>)</strong>.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #1E293B;">
                  <div class="agenda-time">SIMPLIFICACIÓN CONTABLE</div>
                  <div class="agenda-title">Adiós Cuentas Puente Interim</div>
                  <p class="agenda-desc">En compras y flujos directos desaparecen las cuentas intermedias de tránsito no conciliadas. El apunte contable va limpio y directo a la <strong>cuenta 1150 de Inventario</strong>.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #0D9488;">
                  <div class="agenda-time">ESTÁNDAR FINANCIERO</div>
                  <div class="agenda-title">Terminología Periódico vs Perpetuo</div>
                  <p class="agenda-desc">Se elimina la ambigüedad continental/anglosajona. Odoo adopta la formalidad contable internacional: <strong>Inventario Periódico</strong> (cierre) vs <strong>Inventario Perpetuo</strong> (tiempo real).</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #3B82F6;">
                  <div class="agenda-time">AUDITORÍA FORENSE</div>
                  <div class="agenda-title">Trazabilidad Nativa en stock.move</div>
                  <p class="agenda-desc">Cada movimiento de stock expone su costo y póliza asociada. Desde <em>Inventario > Informes > Movimientos de existencias</em> puedes auditar qué albarán generó el asiento con precisión quirúrgica.</p>
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
            "time": "00:16 - 00:20",
            "block": "Bloque 2",
            "notes": "Mensaje de tranquilidad: la lógica de Costo Promedio (AVCO) y el principio de cuadre Balanza vs Existencias son idénticos. Destacar el gran cambio en v19: la entrega de cliente NO genera póliza, el costo de venta se descarga en la factura.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#1E293B;">BLOQUE 2 · TRANQUILIDAD Y RIGOR TÉCNICO</span>
                  <h2 class="slide-title">¿Y si Mi Empresa Está en Odoo 16, 17 o 18?</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead"><strong>Respiren tranquilos: los principios de control y las matemáticas son 100% universales.</strong></p>
              
              <div class="two-col-grid" style="gap: 18px;">
                <div class="disaster-col-card" style="border-left: 4px solid #16A34A;">
                  <div class="card-pill" style="color:#16A34A;">LÓGICA CONTABLE UNIVERSAL</div>
                  <h3>Las Matemáticas No Cambian</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li><strong>Fórmula de Costo Promedio (AVCO):</strong> Idéntica en todas las versiones: <code>(Stock &times; Costo + Entrada &times; Costo) &divide; Total</code>.</li>
                      <li><strong>Principio Sagrado del Cuadre:</strong> En cualquier Odoo, Saldo deudor en Balanza (1150) = Valor total en reporte de existencias.</li>
                      <li><strong>Mismos Vicios Operativos:</strong> Ajustes de stock sin cuenta contrapartida o compras con moneda equivocada destruyen la conciliación en v16 tanto como en v19.</li>
                    </ul>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">EL GRAN CAMBIO DE FLUJO EN ODOO 19</div>
                  <h3>¿Cuándo se Descarga el Inventario?</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li><strong>En Odoo 16, 17 y 18 (Flujo con Tránsito):</strong> La entrega física (<code>picking OUT</code>) generaba un asiento automático provisional a cuentas puente de salida. La factura luego cancelaba el puente contra Costo de Ventas (501).</li>
                      <li><strong>En Odoo 19 (Flujo Directo Simplificado):</strong> <strong>¡La entrega física NO genera póliza contable!</strong> Es un evento puramente logístico.</li>
                      <li><strong>El Costo de Ventas se reconoce en la FACTURA:</strong> Al validar la factura de cliente (<code>out_invoice</code>) se genera directamente: <code>Cargo 501 Costo de Ventas | Abono 1150 Inventario</code>.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 7: NUEVA SLIDE - Matriz Maestra de Movimientos Logísticos en Odoo 19
        {
            "id": 7,
            "title": "Matriz Maestra de Movimientos: ¿Cuáles Sí y Cuáles No Generan Contabilidad?",
            "bg": "white",
            "time": "00:20 - 00:30",
            "block": "Bloque 2",
            "notes": "Desmitificar en vivo cuáles movimientos disparan pólizas a la cuenta 1150 y cuáles no. Explicar facturas de compra/venta, landed costs, MOs, ajustes con cuenta vs eventos neutros (entregas, recepciones directas, traslados, pedidos).",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#16A34A;">BLOQUE 2 · REGLAS DEL JUEGO CONTABLE</span>
                  <h2 class="slide-title">Matriz Maestra de Movimientos: ¿Cuáles SÍ y Cuáles NO Generan Contabilidad?</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">La brújula de auditoría en Odoo 19.0: nunca busques pólizas contables en eventos puramente operativos:</p>
              
              <div class="movements-matrix-container">
                <table class="movements-matrix-table">
                  <thead>
                    <tr>
                      <th style="width: 24%;">Operación / Evento</th>
                      <th style="width: 17%;">Documento Odoo</th>
                      <th style="width: 12%; text-align:center;">¿Físico?</th>
                      <th style="width: 15%; text-align:center;">¿Póliza 1150?</th>
                      <th style="width: 32%;">Impacto Financiero / Regla en Odoo 19</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>Factura de Proveedor</strong></td>
                      <td><span class="matrix-doc-code">Factura de Compra</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-no">➖ No</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-yes">✅ SÍ GENERA</span></td>
                      <td><strong>Cargo 1150 · Abono 201</strong>. Fija el costo real de adquisición en la ponderación AVCO.</td>
                    </tr>
                    <tr>
                      <td><strong>Costes en Destino (Landed)</strong></td>
                      <td><span class="matrix-doc-code">Coste en Destino (Landed)</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-no">➖ No</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-yes">✅ SÍ GENERA</span></td>
                      <td><strong>Cargo 1150 · Abono Gastos</strong>. Capitaliza fletes y aranceles sumando valor al activo.</td>
                    </tr>
                    <tr>
                      <td><strong>Factura de Cliente</strong></td>
                      <td><span class="matrix-doc-code">Factura de Cliente</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-no">➖ No</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-yes">✅ SÍ GENERA</span></td>
                      <td><strong>Cargo 501 · Abono 1150</strong>. <em>¡Aquí se descarga el inventario en v19 al costo AVCO!</em></td>
                    </tr>
                    <tr>
                      <td><strong>Orden de Producción (MO)</strong></td>
                      <td><span class="matrix-doc-code">Orden de Producción</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-yes">📦 SÍ</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-yes">✅ SÍ GENERA</span></td>
                      <td><strong>Cargo 1150 PT · Abono 1150 MP</strong>. Transforma materias primas en producto terminado.</td>
                    </tr>
                    <tr>
                      <td><strong>Ajuste de Inventario</strong></td>
                      <td><span class="matrix-doc-code">Ajuste de Conteo Físico</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-yes">📦 SÍ</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-warn">⚠️ CONDICIONAL</span></td>
                      <td><strong>¡Peligro!</strong> Solo genera póliza si la ubicación virtual de desecho/ajuste tiene cuenta asignada.</td>
                    </tr>
                    <tr>
                      <td><strong>Recepción de Proveedor</strong></td>
                      <td><span class="matrix-doc-code">Albarán de Recepción</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-yes">📦 SÍ</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-no">❌ NO GENERA</span></td>
                      <td>Suma existencias físicas; en flujo directo sin cuentas puente, la contabilidad se asienta con la factura.</td>
                    </tr>
                    <tr>
                      <td><strong>Entrega a Cliente</strong></td>
                      <td><span class="matrix-doc-code">Albarán de Entrega</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-yes">📦 SÍ</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-no">❌ NO GENERA</span></td>
                      <td><strong>Puramente operativo.</strong> Descuenta unidades físicas; la póliza contable se genera al facturar.</td>
                    </tr>
                    <tr>
                      <td><strong>Traslado Interno</strong></td>
                      <td><span class="matrix-doc-code">Transferencia Interna</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-yes">📦 SÍ</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-no">❌ NO GENERA</span></td>
                      <td>Mover mercancía entre estantes del mismo almacén/compañía no altera el saldo de la cuenta 1150.</td>
                    </tr>
                    <tr>
                      <td><strong>Pedidos Venta / Compra</strong></td>
                      <td><span class="matrix-doc-code">Pedido de Venta / Compra</span></td>
                      <td style="text-align:center;"><span class="badge-phys badge-no">➖ No</span></td>
                      <td style="text-align:center;"><span class="badge-acc badge-no">❌ NO GENERA</span></td>
                      <td>Compromiso comercial y contractual puro; cero impacto físico y cero apunte financiero.</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div class="matrix-summary-callout">
                📌 <strong>Regla de Oro para el Auditor en Odoo 19:</strong> No busques pólizas contables en las entregas físicas ni en los traslados internos. Si la Balanza 1150 difiere del Almacén, el origen está en <strong>facturas no generadas, ajustes sin cuenta contable, costos forzados en caliente o pólizas manuales</strong>.
              </div>
            </div>
            '''
        },

        # Slide 8: Bloque 3 - Operación Normal Paso 1 (Compra Limpia MXN)
        {
            "id": 8,
            "title": "Operación Normal: Compra Progresiva en MXN",
            "bg": "white",
            "time": "00:30 - 00:38",
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
                    <strong>Pendiente de Facturar</strong> (para auditoría)
                  </div>
                </div>

                <div class="flow-step-card" style="border: 2px solid var(--azul-marino);">
                  <div class="step-badge" style="background:var(--azul-marino);">RESULTADO EN ODOO 19</div>
                  <h4>Ponderación Automática</h4>
                  <p>Total en Almacén: 100 piezas</p>
                  <div class="asiento-box" style="background:#EEF2F6; color:var(--azul-marino);">
                    (50&times;$150 + 50&times;$170) &divide; 100 =<br>
                    <strong>Costo Promedio: $160.00 MXN</strong><br>
                    Valor Físico Almacén: <strong>$16,000.00 MXN</strong>
                  </div>
                </div>
              </div>

              <div class="formula-banner">
                FÓRMULA MATEMÁTICA OFICIAL: <code>Costo Promedio = [ (Stock Actual &times; Costo Actual) + (Qty Recibida &times; Costo Entrada) ] &divide; [ Stock Total ]</code>
              </div>
            </div>
            '''
        },

        # Slide 9: Bloque 3 - Operación Normal Paso 2 (Venta y Factura MXN)
        {
            "id": 9,
            "title": "Operación Normal: Venta y Costo de Ventas",
            "bg": "white",
            "time": "00:38 - 00:45",
            "block": "Bloque 3",
            "notes": "Mostrar la venta de 30 unidades de [TECL-INAL-USB] @ $160 MXN. Costo de ventas = $4,800. Saldo remanente en almacén = 70 u @ $160 = $11,200 MXN. Contabilidad tiene $2,700 y Facturas por Recibir tiene $8,500. Cuadre perfecto: $2,700 + $8,500 = $11,200.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 3 · CASO 1 (CONT.)</span>
                  <h2 class="slide-title">Venta, Entrega y Reconocimiento del Costo de Ventas</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Entrega de 30 unidades al cliente y emisión de la factura de venta en Odoo 19:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card" style="border-left: 4px solid var(--azul-marino);">
                  <div class="card-pill" style="color:var(--azul-marino);">EL ASIENTO CONTABLE AUTOMÁTICO</div>
                  <h3>Póliza de Costo de Ventas</h3>
                  <div class="detail-box">
                    <p>Odoo 19 descarga automáticamente el valor al costo promedio ponderado ($160.00 MXN):</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      <div>CARGO: <strong>501.01.01 Costo de Ventas</strong> → <strong>$4,800.00 MXN</strong> (30 u &times; $160)</div>
                      <div style="margin-top:4px;">ABONO: <strong>115.01.01 Inventario Almacén</strong> → <strong>$4,800.00 MXN</strong></div>
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid #16A34A;">
                  <div class="card-pill" style="color:#16A34A;">ESTADO POST-VENTA (CONCILIACIÓN FORENSE)</div>
                  <h3>Sincronía Total con Factura por Recibir</h3>
                  <div class="detail-box">
                    <ul class="styled-list">
                      <li><strong>Existencias Físicas:</strong> 70 unidades @ $160 = <strong>$11,200.00 MXN</strong>.</li>
                      <li><strong>Saldo en Balanza (1150):</strong> $7,500 (PO 1) - $4,800 (Venta) = <strong>$2,700.00 MXN</strong>.</li>
                      <li><strong>Facturas por Recibir (PO 2):</strong> 50 u @ $170 = <strong>$8,500.00 MXN</strong>.</li>
                      <li><strong>Fórmula de Conciliación:</strong> $2,700 (1150) + $8,500 (Por Facturar) = <strong>$11,200.00 MXN</strong> (Dif: <span style="color:#16A34A; font-weight:700;">$0.00</span>).</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 10: Bloque 3 - Operación Normal Paso 3 (Compras en USD)
        {
            "id": 10,
            "title": "Operación Normal: Compra de Importación en USD",
            "bg": "white",
            "time": "00:45 - 00:55",
            "block": "Bloque 3",
            "notes": "Mostrar la compra en USD con [MON-27-4K]. 20 u @ $100 USD (TC oficial $18.50) = $37,000 MXN. En Odoo 19 la recepción fija la valoración física en stock.move sin generar póliza, y la Factura del Proveedor asienta el Cargo 1150 / Abono 201.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#0D9488;">BLOQUE 3 · CASO 2 (USD)</span>
                  <h2 class="slide-title">Compras en Moneda Extranjera (USD) y Tipo de Cambio</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[MON-27-4K] Monitor Profesional 27" 4K</code> (20 piezas @ $100.00 USD):</p>
              
              <div class="flow-steps-grid" style="grid-template-columns: repeat(3, 1fr);">
                <div class="flow-step-card">
                  <div class="step-badge">1. ORDEN DE COMPRA (PO)</div>
                  <h4>Pacto Comercial</h4>
                  <p>20 unidades @ $100.00 USD</p>
                  <div class="asiento-box">
                    Total: <strong>$2,000.00 USD</strong><br>
                    <em>Compromiso comercial (sin impacto físico ni contable)</em>
                  </div>
                </div>

                <div class="flow-step-card">
                  <div class="step-badge">2. RECEPCIÓN FÍSICA (WH/IN)</div>
                  <h4>Valoración Logística Inicial</h4>
                  <p>Tipo de Cambio Oficial: <strong>$18.50 MXN</strong></p>
                  <div class="asiento-box">
                    $100 USD &times; $18.50 = <strong>$1,850.00 MXN/u</strong><br>
                    Valor en <code>stock.move</code>: <strong>$37,000.00 MXN</strong><br>
                    <em>(En Odoo 19 la recepción NO genera póliza)</em>
                  </div>
                </div>

                <div class="flow-step-card" style="border: 2px solid var(--rojo-vauxoo);">
                  <div class="step-badge" style="background:var(--rojo-vauxoo);">3. FACTURA DEL PROVEEDOR</div>
                  <h4>Nace la Póliza Contable</h4>
                  <p>Factura validada con TC $18.50 MXN</p>
                  <div class="asiento-box" style="background:#FFF1F2; color:#991B1B;">
                    <strong>Cargo 1150 · Abono 201: $37,000.00 MXN</strong><br>
                    ¡Aquí se registra en Balanza y se confirma el costo!
                  </div>
                </div>
              </div>

              <div class="interactive-chat-prompt" style="background:#F0FDF4; border:1px solid #BBF7D0;">
                <span class="prompt-icon">💡</span>
                <span class="prompt-text" style="color:#166534;">
                  <strong>Regla de Oro en Odoo 19.0:</strong> La recepción física valora el stock en almacén al TC del día, pero la <strong>póliza en la cuenta 1150 nace al validar la Factura del Proveedor</strong> (ajustando automáticamente el costo si cambia el TC o la moneda).
                </span>
              </div>
            </div>
            '''
        },

        # Slide 11: Bloque 4 - Portada Clínica de Desastres
        {
            "id": 11,
            "title": "La Clínica de Desastres: 5 Errores Reales",
            "bg": "gradient",
            "time": "00:55 - 00:58",
            "block": "Bloque 4",
            "notes": "Entrada al Bloque 4: La Clínica de Desastres. 5 errores operativos y de configuración comunes que cuestan millones.",
            "html": f'''
            <div class="slide-content cover-slide">
              <div class="cover-badge-row">
                <span class="pill-badge" style="background:#B91C1C;">BLOQUE 4 · 00:55 - 01:25</span>
                <span class="pill-badge-outline">PARTE 2: CASOS FORENSES</span>
              </div>
              <h1 class="cover-title" style="color: #fff; margin-top:20px;">
                La Clínica de Desastres:
                <span class="doodle-wrap" style="color: #F87171;">
                  5 Errores que Cuestan Dinero
                </span>
              </h1>
              <p style="font-size: 1.15rem; color: rgba(255,255,255,0.85); max-width: 700px; margin: 20px auto 0;">
                Casos reales documentados en producción: ajustes huérfanos, productos archivados con saldo, compras en moneda errónea, edición directa de costos y stock negativo.
              </p>
            </div>
            '''
        },

        # Slide 12: Los 4 Modelos Esenciales de Auditoría ("El Cuadrilátero de Control")
        {
            "id": 12,
            "title": "Los 4 Modelos Esenciales de Auditoría ('El Cuadrilátero de Control')",
            "bg": "white",
            "time": "00:58 - 01:06",
            "block": "Bloque 4",
            "notes": "Presentar los 4 reportes obligatorios para auditar inventarios en Odoo: Existencias, Facturas por recibir, Balanza 1150 y Movimientos stock.move. El mapa de coordenadas del auditor antes de abrir los casos de desastres. Resaltar cómo en el Teclado tenemos $8,500 en Facturas por Recibir que explican el cuadre.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#0D9488;">BLOQUE 4 · HERRAMIENTAS DE AUDITORÍA</span>
                  <h2 class="slide-title">Los 4 Modelos Esenciales de Auditoría ("El Cuadrilátero de Control")</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">La caja de herramientas obligatoria: antes de analizar cualquier descuadre, cruzamos estas 4 fuentes de verdad:</p>
              
              <div class="agenda-grid" style="grid-template-columns: repeat(2, 1fr); gap: 16px;">
                <div class="agenda-card" style="border-top: 4px solid #345D90;">
                  <div class="agenda-time">1. ALMACÉN</div>
                  <div class="agenda-title">Reporte de Existencias</div>
                  <p class="agenda-desc"><em>Inventario > Informes > Existencias</em> (<code>stock.quant</code> / <code>stock.valuation</code>). Cantidades físicas reales en mano multiplicadas por el coste unitario.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #AC0340;">
                  <div class="agenda-time">2. COMPRAS EN TRÁNSITO</div>
                  <div class="agenda-title">Facturas por Recibir</div>
                  <p class="agenda-desc">Cruce de compras con <code>qty_received > qty_invoiced</code>. Mercancía física en almacén pendiente de provisión contable (ej. los <strong>$8,500 MXN</strong> de Teclados y la compra en USD de <strong>Cámara Web</strong>).</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #E4A900;">
                  <div class="agenda-time">3. CONTABILIDAD</div>
                  <div class="agenda-title">Mayor de la Cuenta 115.01.01</div>
                  <p class="agenda-desc">Balanza de Comprobación y Apuntes Contables individuales. Revela asientos huérfanos sin producto y pólizas manuales de diario.</p>
                </div>
                <div class="agenda-card" style="border-top: 4px solid #16A34A;">
                  <div class="agenda-time">4. TRAZABILIDAD GRANULAR</div>
                  <div class="agenda-title">Movimientos (stock.move)</div>
                  <p class="agenda-desc">Histórico de cada entrada, salida y ajuste con fecha efectiva, origen, destino y valor monetario unitario registrado en Odoo 19.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 13: Desastres 1 y 2 (Mouse y Router)
        {
            "id": 13,
            "title": "Desastres 1 y 2: Ajuste Huérfano y Producto Archivado",
            "bg": "white",
            "time": "01:06 - 01:14",
            "block": "Bloque 4",
            "notes": "Detalle del Desastre 1 (Mouse Óptico en categoría Perpetua AVCO, pero la ubicación virtual Inventory adjustment viene vacía de cuenta contable por defecto en Odoo 19) y Desastre 2 (Router Legacy archivado con existencias vivas).",
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
                <div class="disaster-col-card" style="border-left: 4px solid #B91C1C;">
                  <div class="card-pill" style="color:#B91C1C;">CASO 1 · MOUSE ÓPTICO (MOUS-OPT-USB)</div>
                  <h3>Ajuste sin Cuenta en Ubicación Virtual</h3>
                  <div class="detail-box">
                    <p>El producto <strong>sí está en Categoría Perpetua AVCO</strong>, pero en Odoo 19 la ubicación <em>Inventory adjustment</em> viene sin cuenta contable asignada de fábrica:</p>
                    <ul class="styled-list">
                      <li><strong>En Almacén:</strong> 100 piezas valoradas en <strong>$8,500.00 MXN</strong>.</li>
                      <li><strong>En Contabilidad:</strong> <strong>$0.00 MXN</strong> (ajuste físico sin póliza).</li>
                      <li><strong>Diagnóstico:</strong> "Valor no reconocido" de -$8,500 MXN pese a tener contabilidad perpetua.</li>
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
                      <li><strong>Diagnóstico:</strong> Saldo contable fantasma imposible de cuadrar a simple vista (+2,400 MXN).</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 14: Desastres 3 y 4 (Cámara Web y Memoria RAM)
        {
            "id": 14,
            "title": "Desastres 3 y 4: Error de Moneda y Costo Manual en Ficha",
            "bg": "white",
            "time": "01:14 - 01:21",
            "block": "Bloque 4",
            "notes": "Detalle del Desastre 3 (Cámara Web con error de moneda USD, recibida y dejada sin facturar para corregir en vivo la moneda en la factura) y Desastre 4 (Memoria RAM con costo cambiado a mano).",
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
                      Total Activo Inflado: <strong>$277,500.00 MXN</strong> (¡$262.5k de sobrecosto!).
                    </div>
                    <div style="margin-top:10px; padding:8px 12px; background:#FEF3C7; border-left:3px solid #D97706; border-radius:4px; font-size:0.85rem; color:#92400E;">
                      <strong>🔴 Dejado Sin Facturar en Odoo:</strong> En vivo demostramos cómo al crear la Factura de Proveedor se puede <strong>corregir la moneda y monto</strong> antes de validar, sanando el pasivo y recalculando la valoración.
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card">
                  <div class="card-pill">CASO 4 · MEMORIA RAM (MEM-RAM-16GB)</div>
                  <h3>La Edición Manual en Ficha</h3>
                  <div class="detail-box">
                    <p>Compra de 10 u @ $100.00 MXN ($1,000 MXN). El usuario edita directamente el campo <em>Coste</em> en la ficha a <strong>$121.00 MXN</strong>:</p>
                    <ul class="styled-list" style="margin-top:10px;">
                      <li><strong>Almacén:</strong> Sube a <strong>$1,210.00 MXN</strong>.</li>
                      <li><strong>Contabilidad:</strong> Se queda en <strong>$1,000.00 MXN</strong> (sin póliza).</li>
                      <li><strong>Descuadre silencioso:</strong> -$210.00 MXN en libros.</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 15: Desastre 5 (Disco SSD - Stock Negativo)
        {
            "id": 15,
            "title": "Desastre 5: Stock Negativo con Compra Posterior",
            "bg": "white",
            "time": "01:21 - 01:28",
            "block": "Bloque 4",
            "notes": "Detalle del Desastre 5 (Disco SSD NVMe con stock negativo): Salida urgente de 10 unidades sin stock previo. Cuando entra la compra después de 20 u a $350, se pierde la deducción contable real. Descuadre de -$1,500 MXN.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#B91C1C;">CLÍNICA · CASO 5</span>
                  <h2 class="slide-title">Venta Forzada Dejando Stock Negativo</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">Producto demo: <code>[DISC-SSD-1TB] Disco Sólido SSD NVMe 1TB</code>. La fractura matemática de entregar antes de recibir:</p>
              
              <div class="two-col-grid">
                <div class="disaster-col-card" style="border-left: 4px solid #B91C1C;">
                  <div class="card-pill" style="color:#B91C1C;">PASO 1 · SALIDA FORZADA (-10 UNIDADES)</div>
                  <h3>La Entrega a Ciegas</h3>
                  <div class="detail-box">
                    <p>Urgencia de entrega: se valida la salida de 10 piezas teniendo existencia en 0. Odoo descarga a costo provisional ($0 o desfasado):</p>
                    <div class="asiento-box" style="margin-top:10px;">
                      Stock Físico: <strong>-10 piezas</strong><br>
                      Deducción en Costo de Ventas: <strong>Subvaluada o nula</strong>
                    </div>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid var(--rojo-vauxoo);">
                  <div class="card-pill" style="color:var(--rojo-vauxoo);">PASO 2 · COMPRA TARDÍA (20 UNIDADES)</div>
                  <h3>El Costo que Quedó en el Limbo</h3>
                  <div class="detail-box">
                    <p>Días después se recibe la compra de 20 piezas a $350.00 MXN ($7,000 MXN). El costo real debió deducirse en la venta pero ya quedó cerrado:</p>
                    <div class="asiento-box" style="margin-top:10px; background:#FFF1F2; color:#991B1B;">
                      Distorsión permanente en Cuenta 1150: <strong>-$1,500.00 MXN</strong><br>
                      Costo de Ventas subvaluado en el ejercicio fiscal.
                    </div>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 16: Bloque 5 - Caza de la Póliza Manual y Server Action 589
        {
            "id": 16,
            "title": "Metodología de Auditoría Forense: SKU por SKU",
            "bg": "white",
            "time": "01:33 - 01:40",
            "block": "Bloque 5",
            "notes": "Paso a paso de la resolución forense: 1. Aislar póliza manual de $487,000 MXN en cuenta 1150 sin SKU; 2. Ejecutar Acción de Servidor 589 con 1 clic; 3. Regularización SKU por SKU con plantilla CSV.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 5 · AUDITORÍA</span>
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
                  <div class="agenda-time">PASO 3 · REGULARIZACIÓN QUIRÚRGICA</div>
                  <div class="agenda-title">Plantilla CSV con <code>product_id</code></div>
                  <p class="agenda-desc"><strong>Solo cuando el stock y costo en almacén son correctos:</strong> importar póliza asignando obligatoriamente el SKU para alinear contabilidad.</p>
                </div>

                <div class="agenda-card" style="border-top: 4px solid #475569;">
                  <div class="agenda-time">PASO 4 · CANDADOS PREVENTIVOS</div>
                  <div class="agenda-title">Bloqueo de Modificaciones y Negativos</div>
                  <p class="agenda-desc">Prohibir asientos manuales, configurar cuenta en ubicación de ajuste y bloquear stock negativo.</p>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 17: Bloque 5 - Cuadre Perfecto al Centavo
        {
            "id": 17,
            "title": "Cuadre Perfecto al Centavo ($78,810 = $78,810)",
            "bg": "gradient",
            "time": "01:40 - 01:48",
            "block": "Bloque 5",
            "notes": "Celebrar el cuadre perfecto al centavo tras desinflar el error de USD en la Cámara Web (-$262,500), facturar pendientes, desarchivar el Router (+$2,400), cancelar la póliza manual (-$487,000) y regularizar por SKU: Balanza ($78,810.00) = Existencias ($78,810.00). Diferencia $0.00 MXN.",
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
                Tras corregir la factura en USD de las Cámaras Web a MXN, desarchivar el Router, cancelar el parche manual y regularizar SKU por SKU:
              </p>
              
              <div class="split-audit-container" style="margin-top:20px;">
                <div class="audit-col" style="background: rgba(255,255,255,0.1); border: 2px solid #16A34A; color:#fff;">
                  <div class="audit-col-badge" style="background:#16A34A; color:#fff;">Libro Mayor Saneado</div>
                  <h3 class="audit-col-title" style="color:#fff;">Balanza de Comprobación</h3>
                  <div class="audit-code" style="color:rgba(255,255,255,0.8);">Cuenta 115.01.01 · Inventario Real</div>
                  <div class="audit-amount" style="color:#fff;">$78,810.00 MXN</div>
                  <div class="audit-status audit-ok" style="background:rgba(22,163,74,0.2); color:#4ADE80;">✅ Sin Pólizas Huérfanas ni Sobrecostos</div>
                </div>

                <div class="audit-vs">
                  <div class="audit-diff-card" style="background:#fff; border-color:#16A34A;">
                    <span class="diff-label" style="color:#16A34A;">CONCILIACIÓN 100% CUADRADA</span>
                    <span class="diff-amount" style="color:#16A34A; font-size:2.2rem;">$0.00 MXN</span>
                    <span class="diff-warn" style="color:#16A34A; font-weight:600;">7 de 7 SKUs en $0.00</span>
                  </div>
                </div>

                <div class="audit-col" style="background: rgba(255,255,255,0.1); border: 2px solid #16A34A; color:#fff;">
                  <div class="audit-col-badge" style="background:#16A34A; color:#fff;">Almacén Saneado</div>
                  <h3 class="audit-col-title" style="color:#fff;">Reporte de Existencias</h3>
                  <div class="audit-code" style="color:rgba(255,255,255,0.8);">Valoración Real de los 7 Productos</div>
                  <div class="audit-amount" style="color:#fff;">$78,810.00 MXN</div>
                  <div class="audit-status audit-ok" style="background:rgba(22,163,74,0.2); color:#4ADE80;">📦 Costo AVCO Real Auditado</div>
                </div>
              </div>

              <div style="margin-top:18px; padding:12px 16px; background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.25); border-radius:8px; color:#fff; font-size:0.88rem; text-align:center;">
                <strong>Puente de Saneamiento:</strong> Almacén Inicial (<strong>$338,910</strong>) &minus; Sobrevaluación USD Cámara Web (<strong>$262,500</strong>) + Router Desarchivado (<strong>$2,400</strong>) = <strong>$78,810.00 MXN</strong>
              </div>
            </div>
            '''
        },

        # Slide 18: Estrategias de Saneamiento: Cuándo Regularizar vs Borrón y Cuenta Nueva
        {
            "id": 18,
            "title": "Estrategias de Saneamiento: ¿Cuándo Regularizar vs Borrón y Cuenta Nueva?",
            "bg": "white",
            "time": "01:48 - 01:56",
            "block": "Bloque 5",
            "notes": "Regla de decisión clara para no confundir al participante entre la Plantilla CSV con product_id (Slide 16) y el Protocolo Borrón y Cuenta Nueva (Slide 18), dejando claro por qué el Parche Manual sin SKU siempre está prohibido.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:var(--rojo-vauxoo);">BLOQUE 5 · REGLA DE DECISIÓN EN PRODUCCIÓN</span>
                  <h2 class="slide-title">¿Cuándo Usar Regularización por SKU vs. Borrón y Cuenta Nueva?</h2>
                </div>
                <div class="slide-header-logo">{logo_light}</div>
              </div>
              <p class="slide-lead">No todos los descuadres se curan igual. Esta es la matriz de decisión para elegir la cirugía correcta:</p>
              
              <div class="two-col-grid" style="gap:16px;">
                <div class="disaster-col-card" style="border-left: 4px solid #0D9488;">
                  <div class="card-pill" style="color:#0D9488; background:#CCFBF1;">🎯 ESCENARIO 1: ALMACÉN SANO, CONTABILIDAD DESFASADA</div>
                  <h3>Regularización Quirúrgica con <code>product_id</code></h3>
                  <div class="detail-box" style="font-size:0.85rem;">
                    <p><strong>¿Cuándo aplica?</strong> Cuando las existencias y el costo promedio (AVCO) en almacén <strong>ya son correctos</strong> y los casos están identificados (ej. un ajuste inicial sin cuenta o un cambio puntual de costo).</p>
                    <ul class="styled-list" style="margin-top:8px;">
                      <li><strong>Qué hacer:</strong> Usar la Plantilla CSV asignando <strong>obligatoriamente <code>product_id</code></strong> en la cuenta 1150.</li>
                      <li><strong>Qué JAMÁS hacer ("La Aspirina"):</strong> Meter una póliza manual ciega <strong>sin <code>product_id</code></strong> o cuando el costo unitario en almacén sigue corrupto (en la próxima venta volverá a descuadrar).</li>
                    </ul>
                  </div>
                </div>

                <div class="disaster-col-card" style="border-left: 4px solid #16A34A;">
                  <div class="card-pill" style="color:#16A34A; background:#DCFCE7;">🔄 ESCENARIO 2: COSTOS AVCO O STOCK HISTÓRICO CORRUPTOS</div>
                  <h3>Protocolo "Borrón y Cuenta Nueva" (Vauxoo)</h3>
                  <div class="detail-box" style="font-size:0.85rem;">
                    <p><strong>¿Cuándo aplica?</strong> Cuando hay meses/años de negativos crónicos, cambios de categoría en caliente o cientos de SKUs con costo promedio contaminado:</p>
                    <ol style="margin:6px 0 0 16px; padding:0; line-height:1.42;">
                      <li><strong>Corte Operativo:</strong> Congelar almacén en fecha de corte.</li>
                      <li><strong>Descarga Física y Contable a Cero:</strong> Llevar stock y cuenta 1150 a <strong>$0.00</strong>.</li>
                      <li><strong>Blindar Fase 0:</strong> Categorías Perpetuas AVCO, cuenta en ubicación de ajuste y candados.</li>
                      <li><strong>Carga Inicial Limpia:</strong> Conteo físico real con costos unitarios auditados.</li>
                    </ol>
                  </div>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 19: Las 5 Reglas de Oro Blindadas de Vauxoo
        {
            "id": 19,
            "title": "Las 5 Reglas de Oro Blindadas de Vauxoo",
            "bg": "white",
            "time": "01:56 - 02:00",
            "block": "Bloque 5",
            "notes": "Las 5 Reglas de Oro Blindadas de Vauxoo: 1. Cero Asientos Manuales en la 1150; 2. Cero Salidas sin Recepción; 3. Configuración y Cadencia; 4. Cero Cambios Manuales de Coste; 5. Auditoría SKU y product_id.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge" style="background:#16A34A;">MEJORES PRÁCTICAS VAUXOO</span>
                  <h2 class="slide-title">Las 5 Reglas de Oro para Blindar tu Inventario</h2>
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

        # Slide 20: Bloque 6 - Q&A Hot Seat (30 min)
        {
            "id": 20,
            "title": "Bloque 6: Q&A Hot Seat (Consultoría en Vivo)",
            "bg": "gradient",
            "time": "02:00 - 02:27",
            "block": "Bloque 6",
            "notes": "Bloque 6: Q&A Hot Seat - Consultoría en Vivo (30 minutos completos). Los asistentes exponen sus dudas operativas, configuraciones o descuadres reales en vivo. Julio responde en pantalla sobre Odoo 19.",
            "html": f'''
            <div class="slide-content">
              <div class="slide-header">
                <div>
                  <span class="pill-badge">BLOQUE 6 · 02:00 - 02:30</span>
                  <h2 class="slide-title" style="color: #fff;">Q&A Hot Seat: Consultoría en Vivo (30 Minutos)</h2>
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
                    <li>¿Cómo planear un protocolo de Borrón y Cuenta Nueva sin parar la empresa?</li>
                  </ul>
                </div>
              </div>
            </div>
            '''
        },

        # Slide 21: Suite de Entregables Oficiales
        {
            "id": 21,
            "title": "Paquete de Entregables Oficiales",
            "bg": "white",
            "time": "02:27 - 02:29",
            "block": "Bloque 6",
            "notes": "Presentación de los entregables: 1. Checklist de Auditoría Logística-Contable con Matriz de Cadencia; 2. Tabla de Mapeo Conceptual v18 -> v19 y Matriz de Movimientos; 3. Kit Técnico de Regularización y Acción de Servidor; 4. Grabación HD y Certificado.",
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
                  <p>Guía de 18 puntos de validación operativa para auditorías diarias, semanales y mensuales en Odoo 19.</p>
                  <a href="#tab-checklist" onclick="switchTab('checklist')" class="btn btn-sm">Ver Checklist</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">📊</div>
                  <h4>Entregable #2: Mapeo 18 → 19 & Tabla de Movimientos</h4>
                  <p>Comparativa conceptual de arquitectura y tabla de cuáles eventos generan contabilidad y cuáles no.</p>
                  <a href="#tab-mapeo" onclick="switchTab('mapeo')" class="btn btn-sm">Ver Mapeo</a>
                </div>

                <div class="deliv-card">
                  <div class="deliv-icon">🛠️</div>
                  <h4>Entregable #4: Kit Técnico de Auditoría</h4>
                  <p>Plantilla CSV de regularización con product_id y código de la Acción de Servidor Odoo 19 (#589).</p>
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

        # Slide 22: Cierre y Agradecimientos
        {
            "id": 22,
            "title": "Cierre y Agradecimientos",
            "bg": "gradient",
            "time": "02:30",
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

print("make_slides_content.py updated successfully (22 slides).")
