#!/usr/bin/env python3
# Content for Entregable #2: Tabla de Mapeo Conceptual v18 -> v19 y Guía SAT
# EXACT ALIGNMENT WITH PLAN FINAL FUSIONADO V2 (plan_v2_critico.md + setup_masterclass.py)

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
          <p class="doc-subtitle">Análisis Arquitectónico, Mega-Caso de Importaciones USD y Mitigación de Riesgos Fiscales</p>
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
                  <strong>Cero desincronización:</strong> Se elimina el error clásico donde existía un Stock Move sin capa SVL. Trazabilidad 1 a 1 por UUID y pedimento.
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
                  Revisión manual en informes de inventario y cruce externo en hojas de cálculo.
                </td>
                <td>
                  <span class="badge-new">Contabilidad > Revisión y Cierre</span><br>
                  Menú: <em>Valoración de inventario</em> con panel nativo guiado de corte.
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
          El núcleo de la Masterclass: Compras en USD a Global Supply Tech LLC con pedimento de Agencia Aduanal del Norte, S.C. y moneda base MXN:
        </p>

        <div class="import-lifecycle-box">
          <div class="lifecycle-stage">
            <div class="stage-num">1</div>
            <div class="stage-info">
              <h4>Anticipo en USD (Art. 20 CFF & NIF B-15)</h4>
              <p>Se emite anticipo de $3,000 USD a TC DOF de $18.22 MXN/USD ($54,660.00 MXN).</p>
              <div class="stage-memo">📌 <em>Efecto Fiscal: El anticipo es una partida no monetaria que congela la tasa histórica para el 30% del valor de las mercancías.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">2</div>
            <div class="stage-info">
              <h4>Recepción Aduanal Física (Stock Move IN)</h4>
              <p>Ingreso de 100 Sensores USD a aduana mexicana. Tipo de cambio oficial DOF: <strong>$18.05 MXN/USD</strong>.</p>
              <div class="asiento-mini">
                <div>CARGO: 115.01.01 Mercancías en Almacén → <strong>$180,500.00 MXN</strong> (100u × $100 × 18.05)</div>
                <div>ABONO: 2110 Proveedores Extranjeros en Tránsito → <strong>$180,500.00 MXN</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Efecto en AVCO: El costo unitario promedio del producto absorbe inicialmente $1,805.00 MXN / pieza.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">3</div>
            <div class="stage-info">
              <h4>Factura del Proveedor Extranjero (Vendor Bill)</h4>
              <p>Llega el Invoice comercial con fecha posterior. Tipo de cambio del día de la factura: <strong>$18.50 MXN/USD</strong>.</p>
              <div class="asiento-mini">
                <div>CARGO: 2110 Proveedores Extranjeros en Tránsito → <strong>$180,500.00 MXN</strong></div>
                <div>CARGO: 701.01.01 Fluctuación Cambiaria (Gasto) → <strong>$4,500.00 MXN</strong></div>
                <div>ABONO: 201.01.02 Proveedores Extranjeros → <strong>$185,000.00 MXN</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Regla de Oro: La variación de $4,500 MXN NO contamina el inventario físico, protegiendo el kardex aduanal.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">4</div>
            <div class="stage-info">
              <h4>Pedimento Aduanal & Costos en Destino (Landed Costs)</h4>
              <p>Factura de Agencia Aduanal del Norte, S.C. por <strong>$5,000.00 MXN</strong> (LANDED-COST) con DTA e impuestos aduanales.</p>
              <div class="asiento-mini">
                <div>CARGO: 115.01.01 Mercancías en Almacén → <strong>$5,000.00 MXN</strong></div>
                <div>ABONO: 201.01.01 Proveedores Nacionales (Agencia Aduanal) → <strong>$5,000.00 MXN</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Nuevo AVCO Final: $1,805.00 + ($5,000 / 100u) = <strong>$1,855.00 MXN / pieza</strong> (Cumple Art. 39 LISR).</em></div>
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
            <strong>Nota técnica de Odoo 19:</strong> Si el Stock Existente es menor o igual a 0.00 (condición anómala de stock negativo con producto VALVULA-NEG), el denominador colapsa o distorsiona el costo promedio a cifras astronómicas o negativas. Por ello, la regla de oro #1 de Vauxoo prohíbe terminantemente operar con existencias negativas.
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
                <td><strong>Stock Negativo</strong> (VALVULA-NEG)</td>
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
                <td>Odoo 19 canaliza automáticamente la porción sin stock hacia Costo de Ventas (501.01.01).</td>
              </tr>
              <tr>
                <td><strong>Mermas Físicas</strong> (CABLE-MERMA)</td>
                <td>Ajustar faltantes a costo de ventas ordinario.</td>
                <td>Presunción de venta omitida con determinación de IVA trasladado e ISR omitido.</td>
                <td>Direccionar ubicaciones de pérdida a cuentas de <strong>Gastos No Deducibles</strong> con acta circunstanciada.</td>
              </tr>
              <tr>
                <td><strong>Inventario Obsoleto</strong> (TARJETA-OBS)</td>
                <td>Cambiar el costo unitario a cero en el producto.</td>
                <td>Márgenes ficticios del 100% y distorsión de utilidades en ejercicios fiscales futuros.</td>
                <td>Crear cuentas complementarias de activo de <strong>Provisión por Obsolescencia</strong> cumpliendo NIF C-4.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="doc-footer">
        <span>Vauxoo Academy · Masterclass 2026: Domina AVCO y Desastres de Importación en Odoo 19.0</span>
        <span>Guía técnica de arquitectura Odoo 19.0 y fiscalidad mexicana</span>
      </div>
    </div>
    '''

print("Updated mapeo module ready.")
