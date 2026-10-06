#!/usr/bin/env python3
# Content for Cronograma Minuto a Minuto & Guía del Ponente

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
          <p class="doc-subtitle">Estructura Detallada de Ejecución, Demos en Vivo, Puntos de Control e Interacción</p>
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
          <div class="cron-summary-label">STACK TECNOLÓGICO</div>
          <div class="cron-summary-val">Odoo 19.0 MX</div>
          <small>Moneda Base MXN · Catálogo SAT · AVCO</small>
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
              <strong>🎯 Objetivo del Bloque:</strong> Conectar emocionalmente con el dolor del cierre mensual de contabilidad e inventarios en México.
            </div>
            <div class="cron-element">
              <strong>🖥️ Pantalla en Vivo:</strong> Split-screen: A la izquierda, la Balanza de Comprobación en la cuenta 1150 ($1,450,000 MXN). A la derecha, el Reporte de Valoración ($1,210,000 MXN). Diferencia en rojo de $240,000 MXN.
            </div>
            <div class="cron-element">
              <strong>💬 Interacción con el Chat:</strong> "¿A quién le ha tocado explicarle este descuadre al Director Financiero o al Auditor del SAT? Pongan 🔥 en el chat".
            </div>
            <div class="cron-element">
              <strong>🎙️ Guión Clave:</strong> "En los próximos 90 minutos dominarán la valoración AVCO en Odoo 19.0. Y entenderán cómo las variaciones cambiarias no tienen por qué ser un dolor de cabeza ni una multa fiscal."
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
              <strong>🎯 Objetivo del Bloque:</strong> Explicar el cambio estructural de Odoo 19.0 y fundamentar por qué en México AVCO es el método indiscutible.
            </div>
            <div class="cron-element">
              <strong>⚙️ Puntos Clave de Explicación:</strong>
              <ul class="styled-list">
                <li>🚫 <strong>Adiós SVL (Stock Valuation Layers):</strong> La valoración vive dentro del Stock Move, eliminando tablas huérfanas.</li>
                <li>🚫 <strong>Adiós Cuentas Puente (Stock Input/Output):</strong> Contabilidad directa con menos pólizas transitorias.</li>
                <li>🔄 <strong>De Continental a Periódico vs Perpetuo:</strong> Adopción de terminología financiera internacional.</li>
                <li>✨ <strong>Nuevo Menú:</strong> Accounting > Review > Inventory Valuation.</li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Bloque 3 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:15 – 00:35 (20 min)</div>
            <h3>BLOQUE 3: BAJO EL CAPÓ — "Casos Prácticos en Vivo (AVCO + MXN)"</h3>
            <span class="pill-badge">DEMO EN VIVO</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>Caso 1: Distribución Comercial Pura (5 min)</strong> — Compra → Recepción → Venta → Factura (todo en MXN). Mostrar la afectación de las cuentas 1150 y 5100 sin cuentas intermedias.
            </div>
            <div class="cron-element">
              <strong>Caso 2: Manufactura MRP (7 min)</strong> — Flujo de componentes AVCO consumidos en Orden de Producción. La cuenta 1160 (WIP) y el peligro de órdenes inconclusas al cierre.
            </div>
            <div class="cron-element">
              <strong>Caso 3 (CRÍTICO): Importaciones USD en MXN (8 min)</strong> — PO confirmada a TC $18.50, recepción física aduanal a TC DOF $19.20 y factura del proveedor a TC $19.50. Demostrar el tratamiento de los $3,000 MXN de diferencia cambiaria y el blindaje del kardex fiscal.
            </div>
          </div>
        </div>

        <!-- Bloque 4 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:35 – 00:55 (20 min)</div>
            <h3>BLOQUE 4: LA CLÍNICA DE LOS DESASTRES — "Errores de Millones de Pesos"</h3>
            <span class="pill-badge" style="background:#B91C1C;">CASOS DE TRINCHERA</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🔥 Desastre #1: Stock Negativo con AVCO (5 min)</strong> — Demo de producto vendido en negativo. La corrupción matemática del costo promedio y multas del SAT.
            </div>
            <div class="cron-element">
              <strong>🔥 Desastre #2: Desfase Cambiario en Recepción vs Factura (7 min)</strong> — El inventario valorado con tipo de cambio irreal y su distorsión del margen operativo.
            </div>
            <div class="cron-element">
              <strong>🔥 Desastre #3: Landed Costs Tardíos (4 min)</strong> — Cómo prorratear gastos de importación cuando el producto ya fue despachado.
            </div>
            <div class="cron-element">
              <strong>🔥 Desastre #4: Ajustes Masivos e Implicaciones SAT (4 min)</strong> — La gravedad fiscal de cuadrar a la fuerza: ingresos acumulables o ventas presuntas sin CFDI.
            </div>
          </div>
        </div>

        <!-- Bloque 5 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:55 – 01:10 (15 min)</div>
            <h3>BLOQUE 5: EL MOMENTO DE LA VERDAD — "Auditoría y Corrección"</h3>
            <span class="pill-badge">CLÍMAX</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🔍 Auditoría Paso a Paso (8 min)</strong> — Demostración de Accounting > Review > Inventory Valuation y filtro contra Balanza 1150.
            </div>
            <div class="cron-element">
              <strong>🎯 Resolución del Hook Inicial (4 min)</strong> — Descubrir en vivo la póliza manual intrusa de $240,000 MXN, revertirla, registrar el ajuste logístico y lograr el 100% de cuadre al centavo.
            </div>
            <div class="cron-element">
              <strong>🥇 Las 3 Reglas de Oro de Vauxoo (3 min)</strong> — 1. Cero stock negativo en AVCO; 2. Cut-off logístico innegociable; 3. Tipo de cambio DOF exacto en recepciones.
            </div>
          </div>
        </div>

        <!-- Bloque 6 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">01:10 – 01:30 (20 min)</div>
            <h3>BLOQUE 6: Q&A "HOT SEAT" & ENTREGABLES</h3>
            <span class="pill-badge">CONSULTORÍA</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🎙️ Consultoría en Vivo (15 min):</strong> Respuestas directas de Julio Serna a las preguntas y escenarios de los asistentes.
            </div>
            <div class="cron-element">
              <strong>📦 Entrega de Recursos (5 min):</strong> Enlace al Checklist de Auditoría interactivo, Tabla de Mapeo conceptual, Certificado y Grabación de Vauxoo Academy.
            </div>
          </div>
        </div>
      </div>

      <!-- Checklist de Preparación del Ponente -->
      <div class="cron-prep-section">
        <h3 style="font-family:'Sora'; margin-bottom:12px;">Checklist Pre-Sesión del Ponente (Julio Serna)</h3>
        <div class="prep-grid">
          <div class="prep-item">✅ Instancia Odoo 19.0 lista con Localización Mexicana (Plan Contable MX y moneda base MXN).</div>
          <div class="prep-item">✅ Órdenes de compra pre-cargadas en USD con tipos de cambio desfasados para la demo en vivo.</div>
          <div class="prep-item">✅ Asiento manual ficticio de $240,000 MXN inyectado en cuenta 1150 para el hook de apertura.</div>
          <div class="prep-item">✅ Producto con stock negativo pre-configurado para mostrar el colapso del algoritmo AVCO.</div>
          <div class="prep-item">✅ Presentador interactivo abierto en pantalla secundaria con notas de orador y cronómetro activo.</div>
        </div>
      </div>

      <div class="doc-footer">
        <span>Vauxoo Academy · Documento de Control de Producción Masterclass 2026</span>
        <span>Alineado a lineamientos de marca Josefina / Vauxoo Academy</span>
      </div>
    </div>
    '''

print("Cronograma module ready.")
