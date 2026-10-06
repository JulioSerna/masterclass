#!/usr/bin/env python3
# Content for Cronograma Minuto a Minuto & Guía del Ponente
# STRICT ALIGNMENT WITH masterclass-plan-final.md v5


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
          <p class="doc-subtitle">Estructura Oficial del Plan Definitivo v5 · Odoo 19.0 México</p>
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
                <div>• Balanza de Comprobación (Cuenta <code>115.01.01</code>): <strong>$487,200.00 MXN</strong></div>
                <div>• Reporte de Existencias / Valoración de Inventario: <strong>$75,925.00 MXN</strong></div>
                <div style="color:#AC0340; font-weight:700; margin-top:4px;">• Descuadre real e inaceptable: $411,275.00 MXN</div>
              </div>
            </div>
            <div class="cron-element">
              <strong>🗺️ Mapa de Causas Recurrentes:</strong> Configuración errática (Fase 0), parches operativos (pólizas manuales) y ceguera de auditoría por falta de revisión periódica.
            </div>
            <div class="cron-element">
              <strong>💬 Encuesta Relámpago al Chat:</strong> "¿Cada cuánto auditan ustedes el reporte de existencias del almacén contra el saldo contable de inventarios? ¿Diario, semanal, mensual o anual?".
            </div>
            <div class="cron-element">
              <strong>🎙️ Guión de Promesa:</strong> "En los próximos 90 minutos van a dominar el Costo Promedio en Odoo 19.0, blindarán su operación contra errores comunes y resolveremos este descuadre en vivo en el Bloque 5".
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
            <h3>BLOQUE 3: EL HAPPY PATH COMERCIAL — "AVCO, Venta y Entrega en Acción"</h3>
            <span class="pill-badge">CICLO COMERCIAL COMPLETO</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>1. Compra Progresiva y Ponderación AVCO (8 min — 00:17 a 00:25):</strong>
              <p>Producto <code>[WIDGET-MX] Widget Nacional MX (AVCO)</code>. Recepción 1: 50 u @ $150 = $7,500 MXN. Recepción 2: 50 u @ $170 = $8,500 MXN. Total 100 piezas @ <strong>$160.00 MXN</strong>. Saldo en cuenta 115.01.01 = $16,000.00 MXN.</p>
            </div>
            <div class="cron-element">
              <strong>2. Pedido de Venta, Entrega Física y Facturación (10 min — 00:25 a 00:35):</strong>
              <p>Venta <code>S00001</code> de 30 unidades. Entrega de almacén (<code>WH/OUT/00001</code>) descarga 30 piezas. Factura con asiento directo: Cargo a 501.01.01 Costo de Ventas ($4,800.00 MXN) y Abono a 115.01.01 ($4,800.00 MXN). Saldo en almacén: 70 u @ $160 = $11,200 MXN = Balanza contable $11,200 MXN. Cuadre perfecto.</p>
            </div>
          </div>
        </div>

        <!-- Bloque 4 -->
        <div class="cron-block-card">
          <div class="cron-block-header">
            <div class="cron-time-pill" style="background:#B91C1C;">00:35 – 00:55 (20 min)</div>
            <h3>BLOQUE 4: LA CLÍNICA DE PROBLEMAS OPERATIVOS — "Los 4 Casos Reales"</h3>
            <span class="pill-badge" style="background:#B91C1C;">4 CASOS CLÍNICOS (5 MIN C/U)</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>Caso 1: Ajuste de Inventario sin Cuenta Contable (5 min — 00:35 a 00:40):</strong>
              <p>Ubicación virtual de ajuste o categoría sin cuenta contrapartida. El reporte de almacén descuenta piezas pero la cuenta 1150 no genera asiento contable. Descuadre inmediato.</p>
            </div>
            <div class="cron-element">
              <strong>Caso 2: Recepción de Compra con Tipo de Cambio Erróneo (5 min — 00:40 a 00:45):</strong>
              <p>Capturar tasas erróneas al recibir compras en divisa. El valor en moneda base entra adulterado y envenena la fórmula ponderada de las existencias y futuras ventas.</p>
            </div>
            <div class="cron-element">
              <strong>Caso 3: Mercancía Entregada sin Recibir o sin Facturar Compra (5 min — 00:45 a 00:50):</strong>
              <p>Despachar al cliente antes de que la recepción o factura de compra estén en el sistema. Alteración de secuencia temporal que ocasiona revaloraciones desfasadas y saltos bruscos en el costo de ventas.</p>
            </div>
            <div class="cron-element">
              <strong>Caso 4: Las Pólizas Manuales de Ajuste (5 min — 00:50 a 00:55):</strong>
              <p>El contador registra asientos manuales directos en la cuenta 1150 para forzar el balance. La aspirina manual que no genera movimiento físico y divorcia permanentemente el libro mayor del almacén.</p>
            </div>
          </div>
        </div>

        <!-- Bloque 5 -->
        <div class="cron-block-card" style="border: 2px solid var(--rojo-vauxoo);">
          <div class="cron-block-header" style="background:#FFF1F2;">
            <div class="cron-time-pill" style="background:var(--rojo-vauxoo);">00:55 – 01:07 (12 min)</div>
            <h3>BLOQUE 5: AUDITORÍA Y CORRECCIÓN — "El Momento de la Verdad"</h3>
            <span class="pill-badge" style="background:var(--rojo-vauxoo);">RESOLUCIÓN EN VIVO</span>
          </div>
          <div class="cron-block-body">
            <div class="cron-element">
              <strong>Intro Verbal de Julio & Caza de la Póliza Manual (6 min — 00:55 a 01:01):</strong>
              <div style="margin-top:6px; padding:10px; background:#FFFFFF; border-radius:6px; border:1px solid #CBD5E1;">
                <p style="font-style:italic; margin-bottom:8px;">"Bueno, ya vimos en el Bloque 1 las principales causas que hay que evitar para no tener un divorcio contable y logístico. En los bloques anteriores entendimos cómo es la valoración con el Happy Path y qué pasa con los problemas comunes. Pero muchos de los que están aquí, o todos, ya tienen Odoo en producción, ya iniciaron operaciones y YA TIENEN el problema encima. Vamos a ver entonces cómo lo auditamos y sobre todo cómo lo corregimos."</p>
                <div>• Filtro en cuenta <code>115.01.01</code>: <code>Documento Origen = Vacío</code>.</div>
                <div>• Caza del asiento manual: Póliza <strong><code>MISC/2026/09/0001</code></strong> por <strong>$487,000.00 MXN</strong>.</div>
              </div>
            </div>
            <div class="cron-element">
              <strong>Corrección en Vivo y Cuadre al Centavo (3 min — 01:01 a 01:04):</strong>
              <p>Cancelación de la póliza manual intrusa. Actualización de la Balanza de Comprobación: saldo de la cuenta 1150 regresa a <strong>$75,925.00 MXN</strong>, cuadrando al centavo con el reporte de existencias ($0.00 MXN de diferencia).</p>
            </div>
            <div class="cron-element">
              <strong>Las 3 Reglas de Oro Blindadas de Vauxoo (3 min — 01:04 a 01:07):</strong>
              <ol class="styled-list">
                <li>🥇 <strong>Cero Asientos Manuales en la 1150:</strong> Restringir por permisos de usuario pólizas manuales en cuentas de inventario.</li>
                <li>🥇 <strong>Cero Salidas sin Recepción Registrada:</strong> Asegurar que toda entrega a cliente cuente con su recepción y compra procesadas.</li>
                <li>🥇 <strong>Configuración Congelada y Auditoría Disciplinada:</strong> Categorías inmutables en caliente y revisión periódica con el checklist oficial.</li>
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
              <strong>🎙️ Consultoría en Pantalla Compartida (21 min — 01:07 a 01:28):</strong> Los asistentes exponen sus dudas operativas, configuraciones y descuadres reales en vivo. Julio Serna responde en pantalla navegando en la base de datos de Odoo 19.
            </div>
            <div class="cron-element">
              <strong>📦 Cierre y Enlaces (2 min — 01:28 a 01:30):</strong> Agradecimientos, enlaces de descarga de los entregables (Checklist y Guía de Mapeo), constancias oficiales e invitación a proyectos de diagnóstico e implementación con Vauxoo.
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
          <div class="prep-item">✅ Flujo comercial limpio con [WIDGET-MX] ($160 MXN) y factura de venta con costo de ventas listo.</div>
          <div class="prep-item">✅ Presentador interactivo abierto con notas de orador y cronómetro activo sincronizado.</div>
        </div>
      </div>

      <div class="doc-footer">
        <span>Vauxoo Academy · Documento de Control de Producción Masterclass 2026</span>
        <span>Alineado estrictamente a masterclass-plan-final.md (Plan Definitivo v5)</span>
      </div>
    </div>
    '''

print("Updated cronograma module v5 ready.")
