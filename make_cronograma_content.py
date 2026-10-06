#!/usr/bin/env python3
# Content for Cronograma Minuto a Minuto & Guía del Ponente
# STRICT ALIGNMENT WITH masterclass-plan-final.md (Plan Definitivo v4)

def get_cronograma_html(logo_light):
    return f'''
    <div class="deliverable-doc cronograma-doc">
      <!-- Header -->
      <div class="doc-header">
        <div class="doc-header-brand">
          {logo_light}
        </div>
        <div class="doc-header-title">
          <span class="pill-badge">GUÍA INTERNA DEL PONENTE & PRODUCCIÓN</span>
          <h2>Cronograma Minuto a Minuto (90 Minutos)</h2>
          <p class="doc-subtitle">Estructura Oficial del Plan Definitivo v4 · Odoo 19.0 México</p>
        </div>
      </div>

      <!-- Overview Cards -->
      <div class="cron-summary-grid">
        <div class="cron-summary-card">
          <div class="cron-summary-label">PONENTE PRINCIPAL</div>
          <div class="cron-summary-val">Julio Serna</div>
          <small>Project Manager & Experto Funcional Vauxoo</small>
        </div>
        <div class="cron-summary-card">
          <div class="cron-summary-label">DURACIÓN TOTAL</div>
          <div class="cron-summary-val">90 Minutos</div>
          <small>6 Bloques Estratégicos rebalanceados</small>
        </div>
        <div class="cron-summary-card">
          <div class="cron-summary-label">DESCUADRE DEL HOOK</div>
          <div class="cron-summary-val">$411,275.00 MXN</div>
          <small>Balanza 1150: $487,200 vs Existencias: $75,925</small>
        </div>
        <div class="cron-summary-card">
          <div class="cron-summary-label">COMPAÑÍA DEMO BD</div>
          <div class="cron-summary-val">Masterclass México</div>
          <small>Moneda Base MXN · Odoo 19.0 Enterprise</small>
        </div>
      </div>

      <!-- Timeline Blocks -->
      <div class="cron-blocks-container">
        <!-- Bloque 1 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:00 – 00:07 (7 min)</div>
            <h3>BLOQUE 1: EL HOOK — "El Dolor que Todos Conocen"</h3>
            <span class="pill-badge">APERTURA</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🎯 Objetivo del Bloque:</strong> Conectar inmediatamente con la audiencia mostrando un descuadre real e impactante entre la contabilidad y el almacén.
            </div>
            <div class="cron-element">
              <strong>🖥️ Pantalla en Vivo (Split-Screen):</strong>
              <div style="margin-top:6px; padding:10px; background:#F8FAFC; border-radius:6px; border:1px solid #CBD5E1;">
                <div>• Balanza de Comprobación (Cuenta <code>115.01.01</code>): <strong>$487,200.00 MXN</strong></div>
                <div>• Reporte de Existencias / Valoración de Inventario: <strong>$75,925.00 MXN</strong></div>
                <div style="color:#AC0340; font-weight:700; margin-top:4px;">• Descuadre real e inaceptable: $411,275.00 MXN</div>
              </div>
            </div>
            <div class="cron-element">
              <strong>💬 Interacción con el Chat:</strong> "¿A quién le ha tocado explicarle este descuadre al Director General, al auditor externo o peor… al SAT? Pongan 🔥 en el chat".
            </div>
            <div class="cron-element">
              <strong>🎙️ Guión de Promesa:</strong> "En los próximos 90 minutos van a dominar el Costo Promedio en Odoo 19.0. Comprenderán las 3 causas raíz que divorcian almacén y contabilidad, aprenderán a blindar sus importaciones en dólares y resolveremos este descuadre en vivo en menos de 5 minutos".
            </div>
          </div>
        </div>

        <!-- Bloque 2 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:07 – 00:17 (10 min)</div>
            <h3>BLOQUE 2: EL NUEVO PARADIGMA — "Odoo 19.0 y la Trampa de la Configuración"</h3>
            <span class="pill-badge">ARQUITECTURA & CAUSA RAÍZ #1</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>Contexto México y Arquitectura (6 min — 00:07 a 00:13):</strong>
              <ul class="styled-list">
                <li>¿Por qué AVCO perpetuo es la norma en México? → NIF C-4 y deducción del costo de ventas ante el SAT.</li>
                <li>🚫 <strong>Adiós SVL (Stock Valuation Layers):</strong> La valoración vive integrada directamente en cada <code>stock.move</code>.</li>
                <li>🚫 <strong>Adiós cuentas puente interim:</strong> Asientos contables automáticos y directos a la cuenta de inventarios 1150.</li>
                <li>🔄 <strong>Terminología formal:</strong> De 'Anglo-Sajona/Continental' a 'Periódico vs Perpetuo'.</li>
                <li>✅ <strong>Nuevo menú:</strong> <em>Contabilidad > Informes > Inventario / Existencias</em>.</li>
              </ul>
            </div>
            <div class="cron-element">
              <strong>Causa Raíz #1: La Trampa de las Configuraciones en Caliente (4 min — 00:13 a 00:17):</strong>
              <div style="margin-top:6px; padding:10px; background:#FFF1F2; border-left:4px solid #AC0340; border-radius:4px;">
                <strong style="color:#AC0340;">Principio Innegociable: "Dos configuraciones malas no hacen una buena"</strong>
                <p style="margin:4px 0 0; font-size:0.9rem;">
                  El error típico de arrancar periódico, cambiar a perpetuo a mitad de año y luego probar FIFO o AVCO. <strong>Lección técnica de laboratorio:</strong> Odoo 19 NO genera pólizas retroactivas de ajuste por el simple cambio de categoría. El stock físico queda sin soporte contable, creando una brecha silenciosa permanente en el balance.
                </p>
              </div>
            </div>
          </div>
        </div>

        <!-- Bloque 3 -->
        <div class="cron-block-card" style="border: 2px solid var(--azul-marino);">
          <div class="cron-block-header" style="background:#F0F4F9;">
            <div class="cron-time-pill" style="background:var(--azul-marino);">00:17 – 00:37 (20 min)</div>
            <h3>BLOQUE 3: CASOS PRÁCTICOS — "AVCO en Acción"</h3>
            <span class="pill-badge">CASOS PRÁCTICOS</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>CASO 1: Flujo Limpio en MXN (8 min — 00:17 a 00:25):</strong>
              <p>Producto <code>[WIDGET-MX] Widget Nacional MX (AVCO)</code>. Ponderación matemática limpia: 50 u @ $150 + 50 u @ $170 = 100 u @ <strong>$160.00 MXN</strong>. Venta y entrega de 30 unidades: Asiento inmediato de Costo de Ventas (cargo 501.01.01, abono 115.01.01 por $4,800.00 MXN).</p>
            </div>
            <div class="cron-element">
              <strong>CASO 2: Compras en USD y Costos en Destino (12 min — 00:25 a 00:37):</strong>
              <div style="margin-top:6px; padding:10px; background:#FFFFFF; border-radius:6px; border:1px solid #CBD5E1;">
                <div>• <strong>Recepción en USD:</strong> PO a $100 USD. Al recibir en almacén, Odoo toma el TC DOF oficial del día de recepción ($18.50) → Costo inicial: $1,850.00 MXN/unidad.</div>
                <div style="font-size:0.85rem; color:#475569; margin:4px 0;">(Error común desmentido: El costo no lo fija la fecha de la orden de compra, sino la fecha de recepción física).</div>
                <div>• <strong>Landed Costs:</strong> Factura de fletes y maniobras por $5,000 MXN asignada vía Costos en Destino a la recepción. Odoo distribuye automaticamente +$250 MXN/u → AVCO final sube de $1,850 a <strong>$2,100.00 MXN</strong>.</div>
                <div style="color:#AC0340; font-weight:600; font-size:0.85rem; margin-top:4px;">Impacto fiscal: Sin Landed Costs, el inventario y el costo de ventas quedan artificialmente subvaluados (Art. 39 LISR).</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bloque 4 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill" style="background:#B91C1C;">00:37 – 00:53 (16 min)</div>
            <h3>BLOQUE 4: LA CLÍNICA DE DESASTRES — "4 Errores que Cuestan Millones"</h3>
            <span class="pill-badge" style="background:#B91C1C;">CLÍNICA DE TRINCHERA (4 MIN C/U)</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🔥 Desastre 1: Stock Negativo con AVCO (4 min — 00:37 a 00:41):</strong>
              <p>Venta de <code>[VALVULA-NEG]</code> con saldo en -10 u. Al recibir nueva compra a precio distinto, la fórmula ponderada colapsa matemáticamente. Kardex negativo = observación y rechazo de deducciones SAT.</p>
            </div>
            <div class="cron-element">
              <strong>🔥 Desastre 2: Tipo de Cambio Erróneo en Recepciones (4 min — 00:41 a 00:45):</strong>
              <p>Capturar tasas comerciales o valores por omisión en lugar del DOF. En importaciones de alto volumen, 50 centavos generan distorsiones de decenas de miles de pesos en el costo promedio.</p>
            </div>
            <div class="cron-element">
              <strong>🔥 Desastre 3: Mermas y Ajustes de Conteo Físico (4 min — 00:45 a 00:49):</strong>
              <p>Producto <code>[CABLE-MERMA]</code> (faltan 15 metros). El ajuste reduce CANTIDAD, preservando el costo unitario ($85 MXN). El faltante va a cuenta de gasto por merma.</p>
            </div>
            <div class="cron-element">
              <strong>🔥 Desastre 4: Inventario Obsoleto y Provisiones NIF C-4 (4 min — 00:49 a 00:53):</strong>
              <p>Producto <code>[TARJETA-OBS]</code>. Jamás reducir el costo unitario en Odoo a $0. La pérdida se reconoce mediante póliza en cuenta complementaria (<code>108.02.01 Estimación de obsolescencia</code>).</p>
            </div>
          </div>
        </div>

        <!-- Bloque 5 -->
        <div class="cron-block-card" style="border: 2px solid var(--rojo-vauxoo);">
          <div class="cron-block-header" style="background:#FFF1F2;">
            <div class="cron-time-pill" style="background:var(--rojo-vauxoo);">00:53 – 01:07 (14 min)</div>
            <h3>BLOQUE 5: EL MOMENTO DE LA VERDAD — "Cadencia, Caza de Pólizas y Resolución"</h3>
            <span class="pill-badge" style="background:var(--rojo-vauxoo);">CLÍMAX OPERATIVO</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>Parte A: La Causa Raíz #3 — La Cadencia de Auditoría (5 min — 00:53 a 00:58):</strong>
              <p>Encuesta relámpago al chat: <em>"¿Cada cuánto auditan el inventario contable contra el almacén?"</em> Presentación de la <strong>Matriz de Cadencia Vauxoo</strong> (Diaria = 2-5 min / Semanal = 15 min / Mensual = 1-2 hrs / Anual = Desastre de 3,000+ movimientos acumulados).</p>
            </div>
            <div class="cron-element">
              <strong>Parte B: Causa Raíz #2 — Caza de la Póliza Manual y Resolución del Hook (5 min — 00:58 a 01:03):</strong>
              <div style="margin-top:6px; padding:10px; background:#FFFFFF; border-radius:6px; border:1px solid #CBD5E1;">
                <div>1. Regreso a las pantallas del Hook: Descuadre de $411,275.00 MXN.</div>
                <div>2. Auditoría en vivo: Filtro en la cuenta <code>115.01.01</code> por asientos sin documento logístico (<code>Documento Origen = False</code>).</div>
                <div>3. Identificación de la póliza <strong><code>MISC/2026/09/0001</code></strong> por <strong>$487,000.00 MXN</strong>.</div>
                <div>4. Historia del error: La "aspirina manual" metida por el contador para forzar un cuadre a ciegas.</div>
                <div>5. Reversión en vivo: La cuenta 1150 regresa a <strong>$75,925.00 MXN</strong>, cuadrando al centavo con el reporte de existencias.</div>
              </div>
            </div>
            <div class="cron-element">
              <strong>Parte C: Las 3 Reglas de Oro Blindadas de Vauxoo (4 min — 01:03 a 01:07):</strong>
              <ol class="styled-list">
                <li>🥇 <strong>Cero Asientos Manuales en la 1150:</strong> Prohibir por permisos de usuario pólizas manuales directas a cuentas de existencias.</li>
                <li>🥇 <strong>Cero Stock Negativo:</strong> Bloquear salidas sin inventario en almacén para todas las categorías AVCO.</li>
                <li>🥇 <strong>Configuración y Cadencia Disciplinada:</strong> Categorías inmutables en caliente y auditoría periódica Balanza vs Existencias.</li>
              </ol>
            </div>
          </div>
        </div>

        <!-- Bloque 6 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">01:07 – 01:30 (23 min)</div>
            <h3>BLOQUE 6: Q&A "HOT SEAT" — Consultoría en Vivo & Cierre</h3>
            <span class="pill-badge">CONSULTORÍA EN VIVO</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🎙️ Consultoría en Pantalla Compartida (21 min — 01:07 a 01:28):</strong> Los asistentes exponen sus dudas, casuísticas de importación y descuadres reales en vivo. Julio Serna responde en pantalla sobre la base de datos de Odoo 19.
            </div>
            <div class="cron-element">
              <strong>📦 Cierre y Enlaces (2 min — 01:28 a 01:30):</strong> Agradecimientos, enlaces de descarga de los entregables (Checklist y Guía de Mapeo), constancias oficiales e invitación a diagnósticos e implementaciones con Vauxoo.
            </div>
          </div>
        </div>
      </div>

      <!-- Checklist de Preparación del Ponente -->
      <div class="cron-prep-section">
        <h3 style="font-family:'Sora'; margin-bottom:12px;">Checklist Pre-Sesión del Ponente (Julio Serna)</h3>
        <div class="prep-grid">
          <div class="prep-item">✅ Instancia Odoo 19.0 operativa con compañía de pruebas 'Masterclass México'.</div>
          <div class="prep-item">✅ Póliza intrusa <code>MISC/2026/09/0001</code> de $487,000.00 MXN activa en la cuenta 115.01.01 para el hook inicial.</div>
          <div class="prep-item">✅ Existencias reales de inventario cuadradas en $75,925.00 MXN.</div>
          <div class="prep-item">✅ Productos de demo listos: WIDGET-MX ($160 MXN), compras en USD con Landed Costs ($2,100 MXN), VALVULA-NEG, CABLE-MERMA ($85 MXN), TARJETA-OBS.</div>
          <div class="prep-item">✅ Presentador interactivo abierto con notas de orador y cronómetro activo sincronizado.</div>
        </div>
      </div>

      <div class="doc-footer">
        <span>Vauxoo Academy · Documento de Control de Producción Masterclass 2026</span>
        <span>Alineado estrictamente a masterclass-plan-final.md (Plan Definitivo v4)</span>
      </div>
    </div>
    '''

print("Updated cronograma module ready.")
