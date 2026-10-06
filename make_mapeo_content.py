#!/usr/bin/env python3
# Content for Entregable #2: Tabla de Mapeo Conceptual v18 -> v19 y Guía SAT

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
          <h2>Tabla de Mapeo v18 → v19 & Guía de Supervivencia SAT</h2>
          <p class="doc-subtitle">Análisis Arquitectónico, Flujo de Importaciones USD y Mitigación de Riesgos Fiscales</p>
        </div>
      </div>

      <!-- Action Toolbar (hidden on print) -->
      <div class="doc-toolbar no-print">
        <div class="toolbar-stats">
          <span class="stats-text">Guía de Referencia Rápida para Consultores, Contadores y Líderes de Proyecto</span>
        </div>
        <div class="toolbar-actions">
          <button class="btn btn-sm" onclick="window.print()">
            🖨️ Imprimir / Guardar en PDF
          </button>
        </div>
      </div>

      <!-- Part 1: Arquitectura v18 vs v19 -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 1</span>
          <h3>Mapeo Arquitectónico: Odoo 18 vs Odoo 19.0</h3>
        </div>
        <p class="section-intro">
          Odoo 19 simplifica radicalmente la pila de inventario y contabilidad. La siguiente tabla sintetiza la transición técnica y su impacto directo en la contabilidad mexicana:
        </p>

        <div class="table-responsive">
          <table class="comparison-table">
            <thead>
              <tr>
                <th style="width: 20%;">Concepto Operativo</th>
                <th style="width: 25%;">Odoo ≤ 18 (Arquitectura Clásica)</th>
                <th style="width: 25%;">Odoo 19.0 (Arquitectura Moderna)</th>
                <th style="width: 30%;">Impacto Práctico & Fiscal en México</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Motor de Valoración</strong></td>
                <td>
                  <span class="badge-old">stock.valuation.layer (SVL)</span><br>
                  Tabla intermedia separada que registraba el valor monetario de cada movimiento.
                </td>
                <td>
                  <span class="badge-new">stock.move unificado</span><br>
                  Los campos de valor monetario residen directamente en el movimiento de almacén.
                </td>
                <td>
                  <strong>Cero desincronización:</strong> Se elimina el error clásico donde existía un Stock Move sin capa de valoración SVL. Trazabilidad 1 a 1 por UUID y pedimento.
                </td>
              </tr>
              <tr>
                <td><strong>Cuentas Contables Temporales</strong></td>
                <td>
                  <span class="badge-old">Interim Accounts</span><br>
                  Stock Input (Entradas) y Stock Output (Salidas) requerían conciliación posterior.
                </td>
                <td>
                  <span class="badge-new">Asiento Directo</span><br>
                  El movimiento logístico afecta directamente contra Proveedores o Costo de Ventas.
                </td>
                <td>
                  <strong>Balanza SAT más limpia:</strong> Elimina saldos muertos en cuentas de orden o puente al final del ejercicio fiscal.
                </td>
              </tr>
              <tr>
                <td><strong>Modelo de Valoración</strong></td>
                <td>
                  <span class="badge-old">Continental vs Anglo-Saxon</span><br>
                  Configuración ambigua en los ajustes contables que confundía a implementadores.
                </td>
                <td>
                  <span class="badge-new">Periódico vs Perpetuo</span><br>
                  Nomenclatura alineada con las Normas Internacionales de Información Financiera.
                </td>
                <td>
                  En México siempre se selecciona <strong>Perpetuo</strong> junto con <strong>AVCO</strong> para dar pleno cumplimiento al Art. 41 de la Ley del ISR.
                </td>
              </tr>
              <tr>
                <td><strong>Panel de Cierre de Periodo</strong></td>
                <td>
                  <span class="badge-old">Disperso</span><br>
                  Revisión manual en informes de inventario y comparación externa en hojas de cálculo.
                </td>
                <td>
                  <span class="badge-new">Accounting > Review > Valuation</span><br>
                  Panel nativo guiado de corte con validación de diferencias y bloqueo de fechas.
                </td>
                <td>
                  Reducción de hasta un <strong>75% del tiempo invertido</strong> en la conciliación del cierre de mes antes de timbrar la contabilidad electrónica.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Part 2: Diagrama de Importaciones USD -->
      <div class="doc-section" style="page-break-before: always;">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 2</span>
          <h3>El Ciclo Maestro de Importaciones (USD en Moneda Base MXN)</h3>
        </div>
        <p class="section-intro">
          El talón de Aquiles de las empresas mexicanas es la adquisición de mercancías extranjeras. A continuación se detalla la mecánica contable oficial en Odoo 19:
        </p>

        <div class="import-lifecycle-box">
          <div class="lifecycle-stage">
            <div class="stage-num">1</div>
            <div class="stage-info">
              <h4>Orden de Compra (PO)</h4>
              <p>Compra pactada por <strong>$10,000 USD</strong>. Tipo de cambio del día de la cotización: <strong>$18.50 MXN</strong>.</p>
              <div class="stage-memo">📌 <em>Efecto Contable: Ninguno. Se trata de una orden de compromiso comercial sin afectación en pólizas.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">2</div>
            <div class="stage-info">
              <h4>Recepción Aduanal (Stock Move IN)</h4>
              <p>La mercancía cruza aduana mexicana. Tipo de cambio oficial del DOF (Pedimento): <strong>$19.20 MXN</strong>.</p>
              <div class="asiento-mini">
                <div>CARGO: 1150 Inventarios / Almacén → <strong>$192,000.00 MXN</strong> ($10,000 × $19.20)</div>
                <div>ABONO: 2110 Proveedores Extranjeros en Tránsito → <strong>$192,000.00 MXN</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Efecto en AVCO: El costo unitario promedio del producto absorbe exactamente los $19.20 MXN por dólar.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">3</div>
            <div class="stage-info">
              <h4>Factura del Proveedor Extranjero (Vendor Bill)</h4>
              <p>Se registra la factura final del proveedor con fecha posterior. Tipo de cambio fiscal del día de la factura: <strong>$19.50 MXN</strong>.</p>
              <div class="asiento-mini">
                <div>CARGO: 2110 Proveedores Extranjeros en Tránsito → <strong>$192,000.00 MXN</strong></div>
                <div>CARGO: 6100 Pérdida por Fluctuación Cambiaria → <strong>$3,000.00 MXN</strong> ($10,000 × ($19.50 - $19.20))</div>
                <div>ABONO: 2110 Cuentas por Pagar Proveedores → <strong>$195,000.00 MXN</strong> ($10,000 × $19.50)</div>
              </div>
              <div class="stage-memo">📌 <em>Regla de Oro: La variación de $3,000 MXN NO altera el inventario físico, sino que va a Resultados (Pérdida Cambiaria deducible).</em></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Part 3: Algoritmo AVCO -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 3</span>
          <h3>Fórmula Matemática y Algoritmo de Recálculo AVCO</h3>
        </div>
        <div class="math-card">
          <h4>Fórmula Oficial en Cada Recepción Validada:</h4>
          <div class="math-formula">
            Costo Promedio Final = [ (Stock Existente &times; Costo Unitario Actual) + (Qty Recibida &times; Costo Recepción) ] &divide; [ Stock Existente + Qty Recibida ]
          </div>
          <p style="margin-top: 12px; font-size: 0.9rem; color: #475569;">
            <strong>Nota técnica de Odoo 19:</strong> Si el Stock Existente es menor o igual a 0.00 (condición anómala de stock negativo), el denominador colapsa o distorsiona el costo promedio. Por ello, la regla de oro #1 de Vauxoo prohíbe terminantemente operar con existencias negativas.
          </p>
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
                <th>Error o Síntoma Operativo</th>
                <th>Mecanismo de Falla en Odoo</th>
                <th>Sanción o Contingencia SAT</th>
                <th>Acción de Mitigación en Odoo 19</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Stock Negativo</strong></td>
                <td>Despachar sin existencia física validada.</td>
                <td>Rechazo de deducción del costo de lo vendido (Art. 39 LISR) y multa por inconsistencia en Kardex.</td>
                <td>Desactivar ventas sin stock en categorías y configurar validaciones de seguridad previas a la entrega.</td>
              </tr>
              <tr>
                <td><strong>Desfase Cambiario en Aduana</strong></td>
                <td>Validar recepciones con tipo de cambio genérico.</td>
                <td>Diferencias no deducibles contra el pedimento de importación en auditorías de comercio exterior.</td>
                <td>Actualizar diariamente las tasas DOF en Odoo y auditar que la recepción coincida con el pedimento.</td>
              </tr>
              <tr>
                <td><strong>Landed Costs Tardíos</strong></td>
                <td>Prorratear fletes cuando el stock ya fue vendido.</td>
                <td>Inflar artificialmente inventarios que ya no existen, violando el principio de correlación contable.</td>
                <td>Odoo 19 canaliza automáticamente la porción sin stock hacia Costo de Ventas (5100).</td>
              </tr>
              <tr>
                <td><strong>Ajuste Físico no Documentado</strong></td>
                <td>Ajustes masivos de fin de año sin actas de merma.</td>
                <td>Sobrantes gravados como ingresos presuntos; faltantes gravados como venta omitida con IVA a pagar.</td>
                <td>Respaldar cada ajuste de inventario con bitácora circunstanciada y póliza de pérdida justificada.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="doc-footer">
        <span>Vauxoo Academy · Masterclass 2026: De la Logística a la Contabilidad</span>
        <span>Guía técnica de arquitectura Odoo 19.0 y fiscalidad mexicana</span>
      </div>
    </div>
    '''

print("Mapeo module ready.")
