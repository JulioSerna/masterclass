#!/usr/bin/env python3
# Content for Entregable #2: Tabla de Mapeo Conceptual v18 -> v19 y Guía SAT
# STRICT ALIGNMENT WITH masterclass-plan-final.md (Plan Definitivo v4)

def get_mapeo_html(logo_light, doodle_underline, doodle_arrow):
    return f'''
    <div class="deliverable-doc mapeo-doc">
      <!-- Header -->
      <div class="doc-header">
        <div class="doc-header-brand">
          {logo_light}
        </div>
        <div class="doc-header-title">
          <span class="pill-badge">ENTREGABLE OFICIAL #2</span>
          <h2>Tabla de Mapeo Conceptual v18 → v19 & Guía de Supervivencia SAT</h2>
          <p class="doc-subtitle">Análisis Arquitectónico, Compras USD con Landed Costs y Mitigación de Riesgos Fiscales (NIF C-4)</p>
        </div>
      </div>

      <!-- Action Toolbar (hidden on print) -->
      <div class="doc-toolbar no-print">
        <div class="toolbar-stats">
          <span class="stats-text">Guía de Referencia Rápida para Consultores, Contadores y Auditores de Odoo en México</span>
        </div>
        <div class="toolbar-actions">
          <button class="btn btn-sm" onclick="window.print()">
            🖨️ Imprimir / Guardar en PDF
          </button>
        </div>
      </div>

      <!-- Part 1: Arquitectura v18 vs v19 (Exact from masterclass-plan-final.md lines 221-230) -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 1</span>
          <h3>Tabla de Mapeo Conceptual v18 → v19 (México)</h3>
        </div>
        <p class="section-intro">
          Odoo 19 simplifica radicalmente la pila de inventario y contabilidad. La siguiente tabla sintetiza la transición técnica y su impacto directo en la contabilidad y fiscalidad mexicana:
        </p>

        <div class="table-responsive">
          <table class="comparison-table">
            <thead>
              <tr>
                <th style="width: 22%;">Concepto</th>
                <th style="width: 25%;">Odoo ≤ 18</th>
                <th style="width: 25%;">Odoo 19.0</th>
                <th style="width: 28%;">Impacto para México</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Almacenamiento de valoración</strong></td>
                <td>
                  <span class="badge-old">Stock Valuation Layers (SVL)</span><br>
                  Tabla intermedia separada que registraba el valor monetario de cada movimiento.
                </td>
                <td>
                  <span class="badge-new">Directo en stock.move</span><br>
                  Los campos de valor monetario residen directamente en el movimiento de almacén.
                </td>
                <td>
                  <strong>Menor peso en base de datos;</strong> rastreo contable directo por póliza sin capas huérfanas.
                </td>
              </tr>
              <tr>
                <td><strong>Cuentas puente interim</strong></td>
                <td>
                  <span class="badge-old">Interim Input / Output</span><br>
                  Cuentas puente obligatorias que requerían conciliación posterior.
                </td>
                <td>
                  <span class="badge-new">Flujo Directo a 1150</span><br>
                  Desaparecen en flujo directo; el movimiento va directo a la cuenta de inventarios 115.01.01.
                </td>
                <td>
                  <strong>Balanza limpia;</strong> se eliminan conciliaciones interminables de cuentas puente al cierre de mes.
                </td>
              </tr>
              <tr>
                <td><strong>Terminología contable</strong></td>
                <td>
                  <span class="badge-old">Continental / Anglo-Sajona</span><br>
                  Nomenclatura ambigua que causaba errores de configuración.
                </td>
                <td>
                  <span class="badge-new">Periódico / Perpetuo</span><br>
                  Nomenclatura formal alineada a estándares internacionales.
                </td>
                <td>
                  Alineado formalmente con <strong>NIF C-4</strong> y deducción de costo de ventas ante el SAT.
                </td>
              </tr>
              <tr>
                <td><strong>Movimientos retroactivos</strong></td>
                <td>
                  <span class="badge-old">Prohibidos / Rígidos</span><br>
                  Bloqueo absoluto o inconsistencias severas en el kardex histórico.
                </td>
                <td>
                  <span class="badge-new">Back-dating controlado</span><br>
                  Permite corregir fechas con debida autorización de auditoría.
                </td>
                <td>
                  Permite corregir recepciones con fechas de pedimento bajo estricta autorización de auditoría.
                </td>
              </tr>
              <tr>
                <td><strong>Cierre de inventario</strong></td>
                <td>
                  <span class="badge-old">Scripts y Excel</span><br>
                  Hojas de cálculo dispersas y scripts SQL de soporte para cuadrar.
                </td>
                <td>
                  <span class="badge-new">Menú guiado centralizado</span><br>
                  <em>Contabilidad > Informes > Inventario / Existencias</em>.
                </td>
                <td>
                  Validación de consistencia previa a la emisión de estados financieros y balanza SAT.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Part 2: Flujo de Compras en USD y Landed Costs (Plan Final v4) -->
      <div class="doc-section" style="page-break-before: always;">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 2</span>
          <h3>El Flujo Maestro de Compras en USD y Costos en Destino (Landed Costs)</h3>
        </div>
        <p class="section-intro">
          Flujo operativo estricto de acuerdo al Bloque 3 del Plan Definitivo v4: Moneda base MXN, Orden de Compra en USD a Global Supply Tech LLC y Landed Costs de Agencia Aduanal del Norte:
        </p>

        <div class="import-lifecycle-box">
          <div class="lifecycle-stage">
            <div class="stage-num">1</div>
            <div class="stage-info">
              <h4>Orden de Compra en USD (Purchase Order)</h4>
              <p>PO en dólares por 20 Sensores Industriales a <strong>$100.00 USD/u</strong> ($2,000 USD totales).</p>
              <div class="stage-memo">📌 <em>Regla Técnica: La Orden de Compra NO fija el costo de inventario. La fecha del PO es irrelevante para el costo contable.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">2</div>
            <div class="stage-info">
              <h4>Recepción Física en Almacén (Stock Move IN) — Fijación del AVCO Inicial</h4>
              <p>Recepción física validada. Odoo 19 toma automáticamente el Tipo de Cambio oficial del DOF a la <strong>fecha de recepción</strong> ($18.50 MXN/USD).</p>
              <div class="asiento-mini">
                <div>CARGO: 115.01.01 Mercancías en Almacén → <strong>$37,000.00 MXN</strong> (20u × $100 USD × $18.50)</div>
                <div>ABONO: 201.01.02 Proveedores Extranjeros en Tránsito → <strong>$37,000.00 MXN</strong></div>
              </div>
              <div class="stage-memo">📌 <em>AVCO Inicial en Odoo 19: $100 USD &times; $18.50 = <strong>$1,850.00 MXN / pieza</strong>.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">3</div>
            <div class="stage-info">
              <h4>Factura de Gastos de Importación y Fletes (Landed Costs)</h4>
              <p>Factura de Agencia Aduanal del Norte, S.C. por <strong>$5,000.00 MXN</strong> (fletes, maniobras y gastos aduanales asignables).</p>
              <div class="asiento-mini">
                <div>CARGO: 115.01.01 Mercancías en Almacén (Landed Cost) → <strong>$5,000.00 MXN</strong></div>
                <div>ABONO: 201.01.01 Proveedores Nacionales (Agencia Aduanal) → <strong>$5,000.00 MXN</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Distribución automática de Odoo 19: $5,000 MXN &divide; 20 unidades = <strong>+$250.00 MXN / unidad</strong>.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">4</div>
            <div class="stage-info">
              <h4>Cálculo del AVCO Final y Cumplimiento Fiscal</h4>
              <p>El Costo Promedio ponderado unitario en Odoo 19 sube matemáticamente de $1,850.00 a <strong>$2,100.00 MXN</strong>.</p>
              <div class="stage-memo">📌 <em>Impacto Fiscal: Sin Landed Costs, el inventario y el costo de ventas quedan artificialmente subvaluados en $250/u, violando el Art. 39 de la Ley del ISR.</em></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Part 3: Algoritmo AVCO -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 3</span>
          <h3>Fórmula Matemática y Alerta Técnica de Configuración en Caliente</h3>
        </div>
        <div class="math-card">
          <h4>Fórmula Oficial de Recálculo AVCO en Odoo 19.0:</h4>
          <div class="math-formula">
            Costo Promedio Final = [ (Stock Existente &times; Costo Unitario Actual) + (Qty Recibida &times; Costo Recepción) ] &divide; [ Stock Existente + Qty Recibida ]
          </div>
          <div style="margin-top: 16px; padding: 12px; background: #FFF1F2; border-left: 4px solid #AC0340; border-radius: 4px;">
            <strong style="color: #AC0340;">⚠️ Alerta Crítica (Causa Raíz #1): "Dos malas no hacen una buena"</strong>
            <p style="margin: 6px 0 0; font-size: 0.9rem; color: #1E293B;">
              Cambiar en caliente una categoría de Periódico a Perpetuo o de Standard a AVCO <strong>NO genera asientos retroactivos</strong> en Odoo 19. El inventario físico anterior queda flotando sin póliza contable de soporte, divorciando permanentemente la cuenta 1150 del reporte de existencias.
            </p>
          </div>
        </div>
      </div>

      <!-- Part 4: Matriz de Mitigación de Desastres SAT -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 4</span>
          <h3>Matriz de Mitigación de Contingencias Fiscales (SAT México)</h3>
        </div>
        <div class="table-responsive">
          <table class="sat-matrix-table">
            <thead>
              <tr>
                <th>Desastre Operativo</th>
                <th>Mecanismo de Falla en Odoo</th>
                <th>Riesgo / Sanción SAT</th>
                <th>Solución Blindada en Odoo 19</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Stock Negativo</strong><br><code>[VALVULA-NEG]</code></td>
                <td>Despachar sin existencia en almacén (saldo en -10 u). Al ingresar nueva compra, la fórmula ponderada colapsa matemáticamente.</td>
                <td>Rechazo total de deducción de costo de lo vendido (Art. 39 LISR) y observación en auditoría de Kardex.</td>
                <td>Bloquear salidas sin stock en almacén y prohibir stock negativo en todas las categorías AVCO.</td>
              </tr>
              <tr>
                <td><strong>Tipo de Cambio Erróneo</strong><br>Importaciones USD</td>
                <td>Validar recepciones con TC comercial o fecha de orden de compra en vez del TC DOF de la fecha de recepción.</td>
                <td>Distorsión de costo fiscal, discrepancias en auditoría de comercio exterior y diferencias cambiarias ficticias.</td>
                <td>Configurar sincronización automática DOF y verificar que la recepción tome el TC DOF del día exacto de entrada.</td>
              </tr>
              <tr>
                <td><strong>Mermas y Faltantes</strong><br><code>[CABLE-MERMA]</code></td>
                <td>Faltan 15m. Reducir costo unitario o mandar la merma a costo de ventas ordinario sin acta de pérdida.</td>
                <td>Presunción de venta omitida con determinación presuntiva de IVA e ISR omitido por el SAT.</td>
                <td>Ajuste de inventario que reduce <strong>CANTIDAD</strong> manteniendo costo unitario ($85 MXN) contra cuenta de Gasto por Merma.</td>
              </tr>
              <tr>
                <td><strong>Inventario Obsoleto</strong><br><code>[TARJETA-OBS]</code></td>
                <td>Reducir manualmente el costo unitario del producto a $0.00 MXN en Odoo mediante ajuste de valoración.</td>
                <td>Distorsión irreversible del Kardex y márgenes brutos futuros inflados artificialmente al 100%.</td>
                <td>Preservar costo en Kardex y registrar la pérdida en cuenta complementaria de activo (<code>108.02.01 Estimación de obsolescencia</code>).</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="doc-footer">
        <span>Vauxoo Academy · Masterclass 2026: Domina AVCO y Desastres de Importación en Odoo 19.0</span>
        <span>Plan Definitivo v4 · Cumplimiento NIF C-4 y Código Fiscal de la Federación</span>
      </div>
    </div>
    '''

print("Updated mapeo module ready.")
