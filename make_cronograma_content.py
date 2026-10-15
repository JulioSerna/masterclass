#!/usr/bin/env python3
# Content for Cronograma Minuto a Minuto & Guía del Ponente
# STRICT ALIGNMENT WITH masterclass-plan-final.md v7


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
          <p class="doc-subtitle">Estructura Oficial del Plan Definitivo v7 · Odoo 19.0 México</p>
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
          <div class="cron-summary-val">$482,190.00 MXN</div>
          <small>Balanza 1150: $821,100 vs Existencias: $338,910</small>
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
            <div class="cron-time-pill">00:00 – 00:09 (9 min)</div>
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
                <div>• Balanza de Comprobación (Cuenta <code>115.01.01</code>): <strong>$821,100.00 MXN</strong></div>
                <div>• Reporte de Existencias / Valoración de Inventario: <strong>$338,910.00 MXN</strong></div>
                <div style="color:#AC0340; font-weight:700; margin-top:4px;">• Descuadre real e inaceptable: $482,190.00 MXN</div>
              </div>
            </div>
            <div class="cron-element">
              <strong>🗺️ Mapa de Causas Recurrentes:</strong> Configuración errática (Fase 0), parches operativos (pólizas manuales del contador) y ceguera de auditoría por falta de revisión periódica.
            </div>
            <div class="cron-element">
              <strong>💬 Encuesta Relámpago al Chat:</strong> "¿Cada cuánto auditan ustedes el reporte de existencias del almacén contra el saldo contable de inventarios? ¿Diario, semanal, mensual o anual?".
            </div>
            <div class="cron-element">
              <strong>🎙️ Guión de Promesa:</strong> "En los próximos 90 minutos van a dominar el Costo Promedio en Odoo 19.0, blindarán su operación contra errores comunes y resolveremos este descuadre de casi medio millón de pesos en vivo en el Bloque 5".
            </div>
          </div>
        </div>

        <!-- Bloque 2 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill">00:09 – 00:17 (8 min)</div>
            <h3>BLOQUE 2: LA REVOLUCIÓN ODOO 19.0 — "¿Por qué v19 y qué pasa si estás en v16–v18?"</h3>
            <span class="pill-badge">ARQUITECTURA & TRANQUILIDAD</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>¿Por qué Odoo 19.0? (4 min — 00:09 a 00:13):</strong>
              <ul class="styled-list">
                <li>🚫 <strong>Adiós SVL (Stock Valuation Layers):</strong> La valoración vive integrada directamente en cada <code>stock.move</code>.</li>
                <li>🚫 <strong>Adiós cuentas puente interim:</strong> Asientos contables automáticos y directos a la cuenta de inventarios 1150 en flujos estándar.</li>
                <li>🔄 <strong>Terminología formal:</strong> De 'Anglo-Sajona/Continental' a 'Periódico vs Perpetuo'.</li>
                <li>✅ <strong>Auditoría Visual Inmediata:</strong> Menú <em>Contabilidad > Informes > Inventario / Existencias</em>.</li>
              </ul>
            </div>
            <div class="cron-element">
              <strong>Mensaje para Usuarios en v16, v17 y v18 (4 min — 00:13 a 00:17):</strong>
              <p>Tranquilidad absoluta: los principios contables, la fórmula ponderada de AVCO y la regla de cuadre entre la balanza contable y el reporte de existencias son idénticos. La metodología enseñada hoy permite sanear de inmediato cualquier versión anterior.</p>
            </div>
          </div>
        </div>

        <!-- Bloque 3 -->
        <div class="cron-block-card" style="border: 2px solid var(--azul-marino);">
          <div class="cron-block-header" style="background:#F0F4F9;">
            <div class="cron-time-pill" style="background:var(--azul-marino);">00:17 – 00:35 (18 min)</div>
            <h3>BLOQUE 3: LA OPERACIÓN NORMAL — "AVCO en Acción (MXN y USD)"</h3>
            <span class="pill-badge">PARTE 1: FLUJOS SANOS</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>1. Compra Progresiva, Venta y Margen en MXN (10 min — 00:17 a 00:27):</strong>
              <p>Producto <code>[TECL-INAL-USB] Teclado Ergonómico Inalámbrico</code>. Recepción 1: 50 u @ $150 = $7,500 MXN. Recepción 2: 50 u @ $170 = $8,500 MXN. Ponderación AVCO exacta: 100 u @ <strong>$160.00 MXN</strong>. Venta y entrega de 30 u descarga al costo promedio ($4,800 MXN). Saldo en almacén: 70 u @ $160 = $11,200 MXN = Balanza contable $11,200 MXN. Cuadre perfecto.</p>
            </div>
            <div class="cron-element">
              <strong>2. Compra, Recepción y Facturación en Moneda Extranjera USD (8 min — 00:27 a 00:35):</strong>
              <p>Producto <code>[MON-27-4K] Monitor Profesional 27" 4K</code>. Orden de compra por 20 u @ $100 USD (TC 18.50). Recepción genera entrada por $37,000.00 MXN a $1,850.00 MXN/u. Factura del proveedor recibida con el mismo TC (18.50). Saldo en almacén: 20 u @ $1,850 = $37,000 MXN = Balanza contable $37,000 MXN. Cero diferencial cambiario distorsivo.</p>
            </div>
          </div>
        </div>

        <!-- Bloque 4 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill" style="background:#B91C1C;">00:35 – 00:55 (20 min)</div>
            <h3>BLOQUE 4: LA CLÍNICA DE DESASTRES — "5 Errores que Cuestan Dinero"</h3>
            <span class="pill-badge" style="background:#B91C1C;">PARTE 2: 5 CASOS CLÍNICOS</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>Caso 1: Ajuste de Inventario sin Cuenta Contable (4 min):</strong>
              <p><code>[MOUS-OPT-USB] Mouse Óptico Ergonómico USB</code>. Ajuste de 100 u @ $85 = $8,500 MXN sin cuenta en ubicación de pérdida. Almacén tiene 100 piezas ($8,500), pero Contabilidad tiene $0.00. Descuadre: -$8,500 MXN.</p>
            </div>
            <div class="cron-element">
              <strong>Caso 2: Producto Archivado con Existencias (4 min):</strong>
              <p><code>[ROUT-WIFI4-LEG] Router Inalámbrico Wi-Fi 4 Legacy</code>. Se archivó con 8 u @ $300 = $2,400 MXN. Desaparece de los reportes estándar de existencias, pero los $2,400 MXN siguen vivos como saldo en la balanza 1150. Descuadre: +$2,400 MXN.</p>
            </div>
            <div class="cron-element">
              <strong>Caso 3: Costo MXN Comprado en USD por Error (4 min):</strong>
              <p><code>[CAM-WEB-4K] Cámara Web Pro 4K</code>. Su costo de referencia era $1,500 MXN, pero la OC se emitió en USD (10 u @ $1,500 USD = $277,500 MXN @ TC 18.50 en vez de $15,000 MXN). Inflación brutal del costo unitario a $27,750 MXN.</p>
            </div>
            <div class="cron-element">
              <strong>Caso 4: Cambio Directo de Costo desde la Ficha de Producto (4 min):</strong>
              <p><code>[MEM-RAM-16GB] Memoria RAM DDR5 16GB</code>. El usuario editó manualmente el campo Coste de $100 a $121 en la ficha (10 u). Almacén ahora vale $1,210 MXN, pero contabilidad se quedó en $1,000 MXN sin póliza. Descuadre: -$210 MXN.</p>
            </div>
            <div class="cron-element">
              <strong>Caso 5: Venta Forzada Dejando Stock Negativo (4 min):</strong>
              <p><code>[DISC-SSD-1TB] Disco Sólido SSD NVMe 1TB</code>. Se forzó entrega de 5 u sin existencia previa (-5 u). Al comprar después 15 u @ $350, se pierde la deducción contable de la venta anticipada. Descuadre: +$1,500 MXN.</p>
            </div>
          </div>
        </div>

        <!-- Bloque 5 -->
        <div class="cron-block-card" style="border: 2px solid var(--rojo-vauxoo);">
          <div class="cron-block-header" style="background:#FFF1F2;">
            <div class="cron-time-pill" style="background:var(--rojo-vauxoo);">00:55 – 01:07 (12 min)</div>
            <h3>BLOQUE 5: AUDITORÍA Y RESOLUCIÓN — "El Momento de la Verdad"</h3>
            <span class="pill-badge" style="background:var(--rojo-vauxoo);">RESOLUCIÓN EN VIVO</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>Intro Verbal de Julio & Caza de la Póliza Manual (4 min — 00:55 a 00:59):</strong>
              <div style="margin-top:6px; padding:10px; background:#FFFFFF; border-radius:6px; border:1px solid #CBD5E1;">
                <p style="font-style:italic; margin-bottom:8px;">"Bueno, ya vimos las causas comunes y la clínica de desastres. Pero en la vida real ya tienen el problema encima. ¿Cómo encontramos el descuadre de $482,190 MXN sin perder semanas en Excel?"</p>
                <div>• Filtro en cuenta <code>115.01.01</code>: <code>Sin Producto Asignado</code>.</div>
                <div>• Caza del asiento intruso del contador: Póliza <strong><code>MISC/2026/09/0001</code></strong> por <strong>+$487,000.00 MXN</strong>.</div>
              </div>
            </div>
            <div class="cron-element">
              <strong>La Acción de Servidor (Server Action 589) & Desglose SKU por SKU (5 min — 00:59 a 01:04):</strong>
              <p>Ejecución de la <strong>Acción de Servidor #589</strong> con 1 solo clic. Descarga el CSV de conciliación cruzando Almacén vs Contabilidad e identifica inmediatamente los 7 productos, incluyendo el archivado y los desvíos matemáticos exactos:</p>
              <div style="font-size:0.85rem; background:#F8FAFC; padding:8px; border-radius:4px; font-family:monospace; margin-top:4px;">
                + $487,000.00 (Póliza manual sin SKU)<br>
                - $8,500.00 (Mouse sin póliza contable)<br>
                + $2,400.00 (Router archivado con saldo)<br>
                - $210.00 (RAM costo manual sin póliza)<br>
                + $1,500.00 (SSD stock negativo)<br>
                = <strong>$482,190.00 MXN de descuadre explicado al centavo.</strong>
              </div>
            </div>
            <div class="cron-element">
              <strong>Regularización con Plantilla CSV & Cuadre al Centavo (3 min — 01:04 a 01:07):</strong>
              <p>Importación de la <strong>Plantilla CSV de Regularización</strong> para corregir los 4 productos desfasados y desarchivar/sanear el router. Cancelación de la póliza manual. Balanza y Almacén cuadran a $0.00 MXN de diferencia.</p>
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
              <strong>🎙️ Consultoría en Pantalla Compartida (21 min — 01:07 a 01:28):</strong> Los asistentes exponen sus dudas operativas, configuraciones y descuadres reales en vivo. Julio Serna responde en pantalla navegando en la base de datos de Odoo 19.
            </div>
            <div class="cron-element">
              <strong>📦 Cierre y Entrega del Kit (2 min — 01:28 a 01:30):</strong> Enlaces de descarga del <strong>Kit de Diagnóstico y Regularización</strong> (Plantilla CSV, Código de la Acción de Servidor, Checklist de Auditoría y Tabla de Mapeo).
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
          <div class="prep-item">✅ Existencias físicas de inventario en $338,910.00 MXN y Balanza en $821,100.00 MXN ($482,190.00 MXN de descuadre).</div>
          <div class="prep-item">✅ Operación normal lista con [TECL-INAL-USB] ($160 MXN) y [MON-27-4K] ($1,850 MXN).</div>
          <div class="prep-item">✅ Acción de Servidor 589 lista para demostración de 1 clic y exportación CSV.</div>
        </div>
      </div>

      <div class="doc-footer">
        <span>Vauxoo Academy · Documento de Control de Producción Masterclass 2026</span>
        <span>Alineado estrictamente a masterclass-plan-final.md (Plan Definitivo v7)</span>
      </div>
    </div>
    '''

print("Updated cronograma module v7 ready.")
