#!/usr/bin/env python3
# Content for Cronograma Minuto a Minuto & Guía del Ponente
# EXACT ALIGNMENT WITH PLAN FINAL FUSIONADO V2 (plan_v2_critico.md + setup_masterclass.py)

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
          <p class="doc-subtitle">Estructura Oficial del Plan Final Fusionado v2 · Odoo 19.0 México</p>
        </div>
      </div>

      <!-- Overview Cards -->
      <div class="cron-summary-grid">
        <div class="cron-summary-card">
          <div class="cron-summary-label">PONENTE PRINCIPAL</div>
          <div class="cron-summary-val">Julio Serna</div>
          <small>Project Manager & Experto Funcional</small>
        </div>
        <div class="cron-summary-card">
          <div class="cron-summary-label">DURACIÓN TOTAL</div>
          <div class="cron-summary-val">90 Minutos</div>
          <small>6 Bloques Estratégicos cronometrados</small>
        </div>
        <div class="cron-summary-card">
          <div class="cron-summary-label">PRECIO & FORMATO</div>
          <div class="cron-summary-val">$100 USD</div>
          <small>Virtual en vivo · Grabación · Entregables</small>
        </div>
        <div class="cron-summary-card">
          <div class="cron-summary-label">COMPAÑÍA DEMO BD</div>
          <div class="cron-summary-val">Masterclass México</div>
          <small>RFC: EKU9003173C9 · Moneda Base MXN</small>
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
              <strong>🎯 Objetivo del Bloque:</strong> Conectar inmediatamente con el contador y director financiero mostrando un descuadre real e impactante en una base de datos de producción mexicana.
            </div>
            <div class="cron-element">
              <strong>🖥️ Pantalla en Vivo:</strong> Split-screen: A la izquierda, la Balanza de Comprobación en la cuenta <strong>115.01.01 ($487,200.00 MXN)</strong>. A la derecha, el Reporte de Valoración de Inventario de Odoo 19 <strong>($200.00 MXN)</strong>. Diferencia visible en rojo de casi medio millón de pesos: <strong>$487,000.00 MXN</strong>.
            </div>
            <div class="cron-element">
              <strong>💬 Interacción con el Chat:</strong> "¿A quién le ha tocado explicarle este descuadre de casi medio millón de pesos al SAT o a los socios? Pongan 🔥 en el chat".
            </div>
            <div class="cron-element">
              <strong>🎙️ Guión Clave:</strong> "En los próximos 90 minutos dominarán la valoración AVCO en Odoo 19.0 y los peores escenarios de importación, tipos de cambio y pedimentos aduanales para que nunca vuelvan a tener un cierre con descuadres."
            </div>
          </div>
        </div>

        <!-- Bloque 2 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:07 – 00:15 (8 min)</div>
            <h3>BLOQUE 2: EL NUEVO PARADIGMA — "Odoo 19.0 y el Dominio del Costo Promedio"</h3>
            <span class="pill-badge">ARQUITECTURA</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🎯 Objetivo del Bloque:</strong> Presentar la nueva arquitectura de Odoo 19.0 y fundamentar por qué en México AVCO es el estándar innegociable bajo NIF C-4 y Art. 41 de la Ley del ISR.
            </div>
            <div class="cron-element">
              <strong>⚙️ Puntos Clave de Explicación:</strong>
              <ul class="styled-list">
                <li>🚫 <strong>Muerte de SVL (Stock Valuation Layers):</strong> Todo el valor monetario vive ahora dentro del propio `stock.move`. Se eliminan las tablas huérfanas.</li>
                <li>🚫 <strong>Adiós Cuentas Puente (Interim Accounts):</strong> Registro directo a la cuenta de inventarios 115.01.01.</li>
                <li>🔄 <strong>Adopción de "Periódico vs Perpetuo":</strong> Superación definitiva del confuso modelo Continental vs Anglo-Sajón.</li>
                <li>✨ <strong>Menú Centralizado:</strong> <code>Contabilidad > Revisión y Cierre > Valoración de inventario</code>.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Bloque 3 -->
        <div class="cron-block-card" style="border: 2px solid var(--rojo-vauxoo);">
          <div class="cron-block-header" style="background:#FFF1F2;">
            <div class="cron-time-pill" style="background:var(--rojo-vauxoo);">00:15 – 00:45 (30 min)</div>
            <h3>BLOQUE 3: EL MEGA-CASO — "Importación, USD y Pedimentos" (El Núcleo de la Sesión)</h3>
            <span class="pill-badge">MEGA-CASO</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🎯 Objetivo del Bloque:</strong> Resolver el caso más complejo de México en 4 pasos continuos con datos reales: Compra en USD a Global Supply Tech LLC del producto <code>SENSOR-USD</code> con pedimento de Agencia Aduanal del Norte, S.C.
            </div>
            <div class="cron-element">
              <strong>Paso 1: Anticipo y Tipo de Cambio DOF (7 min)</strong> — Registro del anticipo de $3,000 USD a TC $18.22 MXN/USD. Aplicación del Art. 20 CFF y NIF B-15 (partida no monetaria que congela la tasa histórica).
            </div>
            <div class="cron-element">
              <strong>Paso 2: Recepción vs Factura (Vendor Bill) (8 min)</strong> — Recepción física en aduana a TC DOF de $18.05 MXN vs Factura del proveedor extranjero a TC $18.50 MXN. Demostración de cómo Odoo 19 blinda el AVCO de recepción y envía la diferencia a Pérdida Cambiaria (cuenta 701.01.01).
            </div>
            <div class="cron-element">
              <strong>Paso 3: El Pedimento Aduanal y Landed Costs (8 min)</strong> — Factura de $5,000 MXN del agente aduanal (DTA, IGI, flete). Inyección directa al AVCO del producto importado sin duplicar cuentas contables (Art. 39 LISR).
            </div>
            <div class="cron-element">
              <strong>Paso 4: El CFDI de Pago / Complemento (7 min)</strong> — Liquidación final a TC $18.60 MXN. Diferencia cambiaria realizada e IVA acreditable pagado efectivamente.
            </div>
          </div>
        </div>

        <!-- Bloque 4 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:45 – 01:05 (20 min)</div>
            <h3>BLOQUE 4: LA CLÍNICA DE DESASTRES — "Errores que Cuestan Millones"</h3>
            <span class="pill-badge" style="background:#B91C1C;">CLÍNICA DE TRINCHERA</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🔥 Desastre #1: Stock Negativo con AVCO (7 min)</strong> — Demo en vivo con <code>VALVULA-NEG</code>: Colapso del promedio ponderado al vender existencias inexistentes y multas por kardex negativo del SAT.
            </div>
            <div class="cron-element">
              <strong>🔥 Desastre #2: Ajustes Físicos y Mermas (7 min)</strong> — Demo con <code>CABLE-MERMA</code>: Conteo de fin de año. Cómo canalizar faltantes hacia Gastos No Deducibles con acta de pérdida sin destruir el AVCO del inventario remanente.
            </div>
            <div class="cron-element">
              <strong>🔥 Desastre #3: Inventario Obsoleto (6 min)</strong> — Demo con <code>TARJETA-OBS</code>: Manejo de productos descontinuados o lentos mediante cuentas complementarias de provisión sin usar Inventory Adjustment que alteraría el costo unitario activo (NIF C-4).
            </div>
          </div>
        </div>

        <!-- Bloque 5 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">01:05 – 01:15 (10 min)</div>
            <h3>BLOQUE 5: EL MOMENTO DE LA VERDAD — "Auditoría en Vivo y Resolución"</h3>
            <span class="pill-badge">CLÍMAX</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🔍 Auditoría en Vivo (6 min):</strong> Acceso al menú <code>Contabilidad > Revisión y Cierre > Valoración de inventario</code> en la base de datos de Masterclass México SA de CV. Rastreo con bisturí de la póliza manual intrusa de <strong>$487,000.00 MXN</strong> con ref <em>"Ajuste manual auditoría interna (Error contable)"</em> en la cuenta 115.01.01.
            </div>
            <div class="cron-element">
              <strong>🎯 Reversión y Cuadre al 100% (2 min):</strong> Cancelación y reversa del asiento manual en vivo → Saldo Cuenta 115.01.01 = $200.00 MXN = Saldo Reporte de Valoración ($200.00 MXN). Diferencia: $0.00 MXN.
            </div>
            <div class="cron-element">
              <strong>🥇 Las 3 Reglas de Oro de Vauxoo (2 min):</strong> 1. Jamás permitir stock negativo; 2. Pedimentos obligatorios vía Landed Costs para subir el AVCO; 3. Cut-off logístico innegociable a fin de mes.
            </div>
          </div>
        </div>

        <!-- Bloque 6 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">01:15 – 01:30 (15 min)</div>
            <h3>BLOQUE 6: Q&A "HOT SEAT" & ENTREGABLES</h3>
            <span class="pill-badge">CONSULTORÍA</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🎙️ Consultoría en Directo (12 min):</strong> Julio Serna responde preguntas de los asistentes sobre pedimentos consolidados, diferencias cambiarias y migraciones a Odoo 19.
            </div>
            <div class="cron-element">
              <strong>📦 Entrega de Recursos (3 min):</strong> Distribución del Checklist de Cierre mensual, Tabla de Mapeo 18→19, certificado oficial y grabación.
            </div>
          </div>
        </div>
      </div>

      <!-- Checklist de Preparación del Ponente -->
      <div class="cron-prep-section">
        <h3 style="font-family:'Sora'; margin-bottom:12px;">Checklist Pre-Sesión del Ponente (Julio Serna)</h3>
        <div class="prep-grid">
          <div class="prep-item">✅ Instancia Odoo 19.0 operativa: <code>https://julioserna-masterclass-main-38706787.dev.odoo.com/</code></div>
          <div class="prep-item">✅ Póliza manual intrusa de $487,000.00 MXN inyectada en cuenta 115.01.01 para el hook de apertura.</div>
          <div class="prep-item">✅ Contactos de demo configurados: Global Supply Tech LLC (USD), Agencia Aduanal del Norte, SC, Distribuidora Nacional de Insumos.</div>
          <div class="prep-item">✅ Productos de demo listos: SENSOR-USD, LANDED-COST, VALVULA-NEG, CABLE-MERMA, TARJETA-OBS.</div>
          <div class="prep-item">✅ Presentador interactivo abierto en pantalla secundaria con notas de orador y cronómetro activo.</div>
        </div>
      </div>

      <div class="doc-footer">
        <span>Vauxoo Academy · Documento de Control de Producción Masterclass 2026</span>
        <span>Alineado al Plan Final Fusionado v2 y branding oficial Josefina</span>
      </div>
    </div>
    '''

print("Updated cronograma module ready.")
