#!/usr/bin/env python3
# Content for Cronograma Minuto a Minuto & Guía del Ponente
# STRICT ALIGNMENT WITH masterclass-plan-final.md v8


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
          <h2>Cronograma Minuto a Minuto (150 Minutos / 2h 30m)</h2>
          <p class="doc-subtitle">Estructura Oficial del Plan Definitivo v8 · Odoo 19.0 México</p>
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
          <div class="cron-summary-val">150 Minutos</div>
          <small>120 min Exposición + 30 min Q&A Hot Seat</small>
        </div>
        <div class="cron-summary-card">
          <div class="cron-summary-label">DESCUADRE DEL HOOK</div>
          <div class="cron-summary-val">$196,190.00 MXN</div>
          <small>Balanza 1150: $535,100 vs Existencias: $338,910</small>
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
            <div class="cron-time-pill">00:00 – 00:12 (12 min)</div>
            <h3>BLOQUE 1: EL HOOK & MAPA DEL DIVORCIO — "El Dolor que Todos Conocen"</h3>
            <span class="pill-badge">APERTURA & CADENCIA</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🎯 Objetivo del Bloque:</strong> Conectar inmediatamente con la audiencia mostrando un descuadre real e impactante entre la contabilidad y el almacén, mapear las causas recurrentes y medir la cadencia de auditoría del público.
            </div>
            <div class="cron-element">
              <strong>🖥️ Pantalla en Vivo (Split-Screen):</strong>
              <div style="margin-top:6px; padding:10px; background:#F8FAFC; border-radius:6px; border:1px solid #CBD5E1;">
                <div>• Balanza de Comprobación (Cuenta <code>115.01.01</code>): <strong>$535,100.00 MXN</strong></div>
                <div>• Reporte de Existencias / Valoración de Inventario: <strong>$338,910.00 MXN</strong></div>
                <div style="color:#AC0340; font-weight:700; margin-top:4px;">• Descuadre real e inaceptable: $196,190.00 MXN</div>
              </div>
            </div>
            <div class="cron-element">
              <strong>🗺️ Mapa de Causas Recurrentes:</strong> Configuración errática (Fase 0), parches operativos (pólizas manuales del contador) y ceguera de auditoría por falta de revisión periódica.
            </div>
            <div class="cron-element">
              <strong>💬 Encuesta Relámpago al Chat:</strong> "¿Cada cuánto auditan ustedes el reporte de existencias del almacén contra el saldo contable de inventarios? ¿Diario, semanal, mensual o anual?".
            </div>
            <div class="cron-element">
              <strong>🎙️ Guión de Promesa:</strong> "En las próximas 2 horas van a dominar el Costo Promedio en Odoo 19.0, blindarán su operación contra errores comunes y resolveremos este descuadre de casi doscientos mil pesos en vivo en el Bloque 5".
            </div>
          </div>
        </div>

        <!-- Bloque 2 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:12 – 00:30 (18 min)</div>
            <h3>BLOQUE 2: ARQUITECTURA & MOTOR CONTABLE — "Movimientos que Sí y No Generan Contabilidad"</h3>
            <span class="pill-badge">ARQUITECTURA & REGLAS DEL JUEGO</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>¿Por qué Odoo 19.0? (8 min — 00:12 a 00:20):</strong>
              <ul class="styled-list">
                <li>🚫 <strong>Adiós SVL (Stock Valuation Layers):</strong> La valoración vive integrada directamente en cada <code>stock.move</code>.</li>
                <li>🚫 <strong>Adiós cuentas puente interim:</strong> Asientos contables automáticos y directos a la cuenta de inventarios 1150 en flujos estándar.</li>
                <li>🔄 <strong>Terminología formal:</strong> De 'Anglo-Sajona/Continental' a 'Periódico vs Perpetuo'.</li>
                <li>✅ <strong>Auditoría Visual Inmediata:</strong> Menú <em>Contabilidad > Informes > Inventario / Existencias</em>.</li>
              </ul>
            </div>
            <div class="cron-element">
              <strong>Tabla Maestra de Movimientos Logísticos en v19 (10 min — 00:20 a 00:30):</strong>
              <p>Desmitificar en vivo cuáles movimientos disparan pólizas a la cuenta 1150 y cuáles no:</p>
              <div style="background:#F8FAFC; padding:10px; border-radius:6px; border:1px solid #CBD5E1; font-size:0.88rem;">
                <div>• <strong style="color:#16A34A;">SÍ Generan Contabilidad:</strong> Landed Costs (fletes/aranceles), Facturas de Proveedor/Cliente (costo de ventas/precio), Ajustes de Inventario (con cuenta en ubicación virtual), Órdenes de Producción (MO) y Revalorizaciones formales.</div>
                <div style="margin-top:4px;">• <strong style="color:#B91C1C;">NO Generan Contabilidad:</strong> Pedidos de Venta (SO), Pedidos de Compra (PO), Traslados Internos entre estantes/ubicaciones del mismo almacén.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bloque 3 -->
        <div class="cron-block-card" style="border: 2px solid var(--azul-marino);">
          <div class="cron-block-header" style="background:#F0F4F9;">
            <div class="cron-time-pill" style="background:var(--azul-marino);">00:30 – 00:55 (25 min)</div>
            <h3>BLOQUE 3: LA OPERACIÓN NORMAL — "AVCO en Acción (MXN y USD)"</h3>
            <span class="pill-badge">PARTE 1: FLUJOS SANOS</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>1. Compra Progresiva, Venta y Margen en MXN (12 min — 00:30 a 00:42):</strong>
              <p>Producto <code>[TECL-INAL-USB] Teclado Ergonómico Inalámbrico</code>. Recepción 1: 50 u @ $150 = $7,500 MXN. Recepción 2: 50 u @ $170 = $8,500 MXN (recibida en bodega, pendiente de facturar para auditoría). Ponderación AVCO exacta: 100 u @ <strong>$160.00 MXN</strong> ($16,000 en bodega). Venta y factura de 30 u descarga al costo promedio ($4,800 MXN). Saldo en almacén: 70 u @ $160 = $11,200 MXN. En Balanza 1150: $2,700 MXN y en Facturas por Recibir: $8,500 MXN. Cuadre perfecto: $2,700 + $8,500 = $11,200 MXN.</p>
            </div>
            <div class="cron-element">
              <strong>2. Compra, Recepción y Facturación en Moneda Extranjera USD (13 min — 00:42 a 00:55):</strong>
              <p>Producto <code>[MON-27-4K] Monitor Profesional 27" 4K</code>. Orden de compra por 20 u @ $100 USD (TC 18.50). Recepción fija valoración en <code>stock.move</code> por $37,000.00 MXN ($1,850.00 MXN/u) sin generar póliza aún. La Factura del Proveedor al mismo TC (18.50) genera el asiento <code>Cargo 1150 / Abono 201</code> por $37,000 MXN. Saldo en almacén: $37,000 MXN = Balanza contable: $37,000 MXN.</p>
            </div>
          </div>
        </div>

        <!-- Bloque 4 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill" style="background:#B91C1C;">00:55 – 01:30 (35 min)</div>
            <h3>BLOQUE 4: LA CLÍNICA DE DESASTRES — "Herramientas de Auditoría & 5 Errores"</h3>
            <span class="pill-badge" style="background:#B91C1C;">PARTE 2: AUDITORÍA & FORENSE</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>1. Los 4 Modelos Esenciales de Auditoría ("Cuadrilátero de Control" - 7 min — 00:55 a 01:02):</strong>
              <div style="margin-top:6px; padding:10px; background:#FFFFFF; border-radius:6px; border:1px solid #CBD5E1; font-size:0.88rem;">
                <div>1. <strong>Reporte de Existencias:</strong> Stock físico $\times$ costo unitario (Almacén).</div>
                <div>2. <strong>Reporte de Facturas por Recibir:</strong> Mercancía recibida pendiente de facturación ($8,500 de Teclados y $277,500 de Cámaras Web en USD).</div>
                <div>3. <strong>Reporte Contable (Mayor 115.01.01):</strong> Saldo oficial en Balanza y apuntes detallados.</div>
                <div>4. <strong>Movimientos de Inventario (<code>stock.move</code>):</strong> Trazabilidad granular de causa raíz.</div>
              </div>
            </div>
            <div class="cron-element">
              <strong>2. Los 5 Casos Clínicos de Desastres (28 min — 01:02 a 01:30):</strong>
              <div style="display:flex; flex-direction:column; gap:8px; margin-top:6px;">
                <div>• <strong>Caso 1: Ajuste de Inventario sin Cuenta en Ubicación Virtual (5 min):</strong> <code>[MOUS-OPT-USB]</code> (en Contabilidad Perpetua). 100 u @ $85 = $8,500 en bodega, $0 en 1150 porque la ubicación <em>Inventory adjustment</em> viene vacía de cuenta por defecto en Odoo 19.</div>
                <div>• <strong>Caso 2: Producto Archivado con Existencias (5 min):</strong> <code>[ROUT-WIFI4-LEG]</code>. 8 u @ $300 = $2,400 MXN vivos en 1150 pero ocultos en bodega. Brecha: +$2,400 MXN.</div>
                <div>• <strong>Caso 3: Costo MXN Comprado en USD por Error (6 min):</strong> <code>[CAM-WEB-4K]</code>. 10 u @ $1,500 USD = $277,500 MXN recibidos y <strong>dejados sin facturar</strong>. Demo en vivo: corrección de divisa a MXN ($15,000 MXN) en la factura del proveedor.</div>
                <div>• <strong>Caso 4: Cambio Directo de Costo desde Ficha (6 min):</strong> <code>[MEM-RAM-16GB]</code>. Coste alterado de $100 a $121 en 10 u. Bodega $1,210 vs Contabilidad $1,000. Brecha: -$210 MXN.</div>
                <div>• <strong>Caso 5: Venta Forzada Dejando Stock Negativo (6 min):</strong> <code>[DISC-SSD-1TB]</code>. Salida forzada de 10 u sin stock. Compra tardía de 20 u @ $350. Brecha: -$1,500 MXN.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bloque 5 -->
        <div class="cron-block-card" style="border: 2px solid var(--rojo-vauxoo);">
          <div class="cron-block-header" style="background:#FFF1F2;">
            <div class="cron-time-pill" style="background:var(--rojo-vauxoo);">01:30 – 02:00 (30 min)</div>
            <h3>BLOQUE 5: AUDITORÍA, RESOLUCIÓN Y SANEAMIENTO REAL — "El Momento de la Verdad"</h3>
            <span class="pill-badge" style="background:var(--rojo-vauxoo);">RESOLUCIÓN & PLAN DE RESCATE</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>1. Caza de la Póliza Manual, Acción #589 y Cuadre Real en $78,810.00 MXN (15 min — 01:30 a 01:45):</strong>
              <p>Caza y reversión de la póliza huérfana <strong><code>MISC/2026/09/0001</code></strong> ($487,000 MXN). Ejecución de la Acción de Servidor #589 (con conversión multimoneda). Corrección de factura de Cámara Web a MXN (-$262,500 de sobrevaluación), desarchivado de Router (+$2,400) e importación de Plantilla CSV por SKU, logrando el <strong>Cuadre Perfecto Real de $78,810.00 MXN = $78,810.00 MXN</strong> (Diferencia $0.00).</p>
            </div>
            <div class="cron-element">
              <strong>2. Regla de Decisión en Producción: Regularización Quirúrgica vs Borrón y Cuenta Nueva (15 min — 01:45 a 02:00):</strong>
              <div style="background:#F0FDFA; padding:10px; border-radius:6px; border-left:4px solid #0D9488; margin-bottom:8px;">
                <strong style="color:#115E59;">🎯 Escenario 1: Almacén Sano, Contabilidad Desfasada (Regularización Quirúrgica con <code>product_id</code>):</strong>
                <p style="margin:4px 0 0; font-size:0.85rem; color:#134E4A;">Cuando el costo promedio y stock en almacén son correctos y las diferencias están acotadas por SKU, se importa la Plantilla CSV con <code>product_id</code> obligatorio (prohibido meter asientos ciegos sin SKU).</p>
              </div>
              <div style="background:#F0FDF4; padding:10px; border-radius:6px; border-left:4px solid #16A34A;">
                <strong style="color:#166534;">🔄 Escenario 2: Costos AVCO o Stock Corruptos (Protocolo "Borrón y Cuenta Nueva" Vauxoo):</strong>
                <p style="margin:4px 0 0; font-size:0.85rem; color:#14532D;">Cuando hay meses de negativos o cambios de categoría en caliente: Corte operativo $\rightarrow$ Ajuste llevando existencias físicas y cuenta 1150 a $0.00 $\rightarrow$ Blindaje de Fase 0 $\rightarrow$ Carga de conteo físico real con costos auditados.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Bloque 6 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">02:00 – 02:30 (30 min)</div>
            <h3>BLOQUE 6: Q&A "HOT SEAT" — Consultoría en Vivo & Cierre</h3>
            <span class="pill-badge">CONSULTORÍA EN VIVO (30 MIN)</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>🎙️ Consultoría en Pantalla Compartida (27 min — 02:00 a 02:27):</strong> Los asistentes exponen sus dudas operativas, configuraciones y descuadres reales en vivo. Julio Serna responde en pantalla navegando en la base de datos de Odoo 19.
            </div>
            <div class="cron-element">
              <strong>📦 Cierre y Entrega del Kit (3 min — 02:27 a 02:30):</strong> Enlaces de descarga del <strong>Kit de Diagnóstico y Regularización</strong> (Plantilla CSV, Código de la Acción de Servidor, Checklist de Auditoría y Tabla de Mapeo).
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
          <div class="prep-item">✅ Existencias físicas de inventario en $338,910.00 MXN y Balanza en $812,600.00 MXN ($473,690.00 MXN de descuadre).</div>
          <div class="prep-item">✅ Operación normal lista con [TECL-INAL-USB] ($160 MXN) y [MON-27-4K] ($1,850 MXN).</div>
          <div class="prep-item">✅ Acción de Servidor 589 lista para demostración de 1 clic y exportación CSV.</div>
        </div>
      </div>

      <div class="doc-footer">
        <span>Vauxoo Academy · Documento de Control de Producción Masterclass 2026</span>
        <span>Alineado estrictamente a masterclass-plan-final.md (Plan Definitivo v8)</span>
      </div>
    </div>
    '''

print("Updated cronograma module v8 ready.")
