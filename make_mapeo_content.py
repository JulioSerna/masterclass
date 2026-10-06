#!/usr/bin/env python3
# Content for Entregable #2: Tabla de Mapeo Conceptual v18 -> v19 & Guía de Arquitectura
# STRICT ALIGNMENT WITH masterclass-plan-final.md v5


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
          <h2>Tabla de Mapeo Conceptual v18 → v19 & Guía Operativa</h2>
          <p class="doc-subtitle">Análisis Arquitectónico, Flujo Comercial y Mitigación de Problemas Operativos</p>
        </div>
      </div>

      <!-- Action Toolbar (hidden on print) -->
      <div class="doc-toolbar no-print">
        <div class="toolbar-stats">
          <span class="stats-text">Guía de Referencia Rápida para Consultores, Contadores y Controllers de Odoo</span>
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
          <h3>Tabla de Mapeo Conceptual v18 → v19</h3>
        </div>
        <p class="section-intro">
          Odoo 19 simplifica radicalmente la pila de inventario y contabilidad. La siguiente tabla sintetiza la transición técnica y su impacto directo en la operación:
        </p>

        <div class="table-responsive">
          <table class="comparison-table">
            <thead>
              <tr>
                <th style="width: 22%;">Concepto</th>
                <th style="width: 25%;">Odoo ≤ 18</th>
                <th style="width: 25%;">Odoo 19.0</th>
                <th style="width: 28%;">Impacto Operativo</th>
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
                  Nomenclatura formal alineada a estándares de inventario perpetuo.
                </td>
                <td>
                  Claridad contable total para auditores y directores financieros.
                </td>
              </tr>
              <tr>
                <td><strong>Movimientos retroactivos</strong></td>
                <td>
                  <span class="badge-old">Prohibidos / Rígidos</span><br>
                  Bloqueo absoluto o inconsistencias severas en el histórico de movimientos.
                </td>
                <td>
                  <span class="badge-new">Back-dating controlado</span><br>
                  Permite corregir fechas con debida autorización de auditoría.
                </td>
                <td>
                  Permite subsanar recepciones con fecha efectiva bajo estricta autorización de control interno.
                </td>
              </tr>
              <tr>
                <td><strong>Cierre de inventario</strong></td>
                <td>
                  <span class="badge-old">Hojas de cálculo externas</span><br>
                  Archivos dispersos y scripts manuales para validar saldos.
                </td>
                <td>
                  <span class="badge-new">Menú guiado centralizado</span><br>
                  <em>Contabilidad > Informes > Inventario / Existencias</em>.
                </td>
                <td>
                  Validación de consistencia inmediata previa a la emisión de estados financieros.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Part 2: Flujo Comercial Completo -->
      <div class="doc-section" style="page-break-before: always;">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 2</span>
          <h3>El Ciclo Comercial Completo en Odoo 19 (Happy Path)</h3>
        </div>
        <p class="section-intro">
          Flujo operativo estricto de acuerdo al Bloque 3: Compra Progresiva AVCO, Venta, Entrega Física y Facturación Directa:
        </p>

        <div class="import-lifecycle-box">
          <div class="lifecycle-stage">
            <div class="stage-num">1</div>
            <div class="stage-info">
              <h4>Primera Compra (Lote Inicial)</h4>
              <p>Recepción de 50 piezas a <strong>$150.00 MXN/u</strong> ($7,500 MXN totales). Costo promedio inicial: $150.00 MXN.</p>
              <div class="stage-memo">📌 <em>Asiento en cuenta 115.01.01: Cargo por $7,500.00 MXN.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">2</div>
            <div class="stage-info">
              <h4>Segunda Compra (Precio Superior) — Ponderación AVCO</h4>
              <p>Recepción de 50 piezas a <strong>$170.00 MXN/u</strong> ($8,500 MXN totales). Total en almacén: 100 piezas.</p>
              <div class="asiento-mini">
                <div>(50 &times; $150 + 50 &times; $170) &divide; 100 = <strong>$160.00 MXN / pieza</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Saldo en cuenta 115.01.01: $16,000.00 MXN acumulados.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">3</div>
            <div class="stage-info">
              <h4>Venta y Entrega Física al Cliente</h4>
              <p>Pedido de venta por 30 piezas y validación de salida física en almacén (<code>WH/OUT/00001</code>).</p>
              <div class="asiento-mini">
                <div>Descuento físico: 30 piezas descargadas de existencias al costo ponderado de $160.00 MXN.</div>
              </div>
              <div class="stage-memo">📌 <em>Existencias remanentes: 70 piezas &times; $160 = $11,200.00 MXN.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">4</div>
            <div class="stage-info">
              <h4>Factura de Cliente y Reconocimiento del Costo</h4>
              <p>Factura emitida con asiento automático instantáneo de Costo de Ventas en Odoo 19:</p>
              <div class="asiento-mini">
                <div>CARGO: 501.01.01 Costo de Ventas → <strong>$4,800.00 MXN</strong> (30u &times; $160)</div>
                <div>ABONO: 115.01.01 Inventario → <strong>$4,800.00 MXN</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Resultado: Saldo en cuenta 1150 = $11,200.00 MXN. Cuadre exacto con almacén ($11,200.00 MXN).</em></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Part 3: Algoritmo AVCO y Alerta de Configuración -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 3</span>
          <h3>Fórmula Matemática y Alerta Técnica de Configuración</h3>
        </div>
        <div class="math-card">
          <h4>Fórmula Oficial de Recálculo AVCO en Odoo 19.0:</h4>
          <div class="math-formula">
            Costo Promedio Final = [ (Stock Existente &times; Costo Unitario Actual) + (Qty Recibida &times; Costo Recepción) ] &divide; [ Stock Existente + Qty Recibida ]
          </div>
          <div style="margin-top: 16px; padding: 12px; background: #FFF1F2; border-left: 4px solid #AC0340; border-radius: 4px;">
            <strong style="color: #AC0340;">⚠️ Alerta Crítica (Causa Raíz #1): "Dos malas no hacen una buena"</strong>
            <p style="margin: 6px 0 0; font-size: 0.9rem; color: #1E293B;">
              Cambiar en caliente una categoría de Periódico a Perpetuo o modificar métodos de costeo <strong>NO genera asientos retroactivos</strong> en Odoo 19. El inventario físico anterior queda sin póliza contable de soporte, divorciando permanentemente la cuenta 1150 del reporte de existencias.
            </p>
          </div>
        </div>
      </div>

      <!-- Part 4: Matriz de Mitigación de los 4 Problemas Operativos -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 4</span>
          <h3>Matriz de Mitigación de los 4 Problemas Operativos</h3>
        </div>
        <div class="table-responsive">
          <table class="mitigation-matrix-table">
            <thead>
              <tr>
                <th>Problema Operativo</th>
                <th>Mecanismo de Falla en Odoo</th>
                <th>Impacto Financiero / Contable</th>
                <th>Solución Blindada en Odoo 19</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Ajuste sin Cuenta Contable</strong></td>
                <td>Ubicación virtual de ajuste físico o merma sin cuenta contrapartida asignada.</td>
                <td>El almacén descuenta piezas pero la cuenta 1150 no genera asiento. Descuadre inmediato.</td>
                <td>Configurar cuentas contables en todas las ubicaciones virtuales de pérdida y en las categorías de producto.</td>
              </tr>
              <tr>
                <td><strong>2. Tipo de Cambio Erróneo</strong></td>
                <td>Captura errónea de tasa en compras en divisa al momento de recibir la mercancía.</td>
                <td>Distorsión del costo promedio en pesos que contamina los márgenes y ventas de las próximas semanas.</td>
                <td>Validar y sincronizar la tasa de cambio oficial aplicable estrictamente a la fecha de recepción física.</td>
              </tr>
              <tr>
                <td><strong>3. Entrega sin Compra Recibida o Facturada</strong></td>
                <td>Despachar la mercancía al cliente antes de que la recepción de compra o su factura estén registradas en el sistema.</td>
                <td>Salida sin costo base consolidado; revaloraciones abruptas al entrar la compra tardía.</td>
                <td>Respetar la secuencia operativa: Orden de Compra &rarr; Recepción en Sistema &rarr; Entrega al Cliente.</td>
              </tr>
              <tr>
                <td><strong>4. Pólizas Manuales de Ajuste</strong></td>
                <td>Registrar asientos manuales de diario directo a la cuenta 1150 para forzar el balance.</td>
                <td>Divorcio permanente: el libro mayor tiene un saldo que no corresponde a ningún movimiento físico.</td>
                <td>Bloquear por permisos los asientos manuales en cuentas de inventario; corregir siempre desde el documento logístico.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="doc-footer">
        <span>Vauxoo Academy · Masterclass 2026: Domina la valoración de inventarios en Odoo 19.0</span>
        <span>Plan Definitivo v5 · Control Contable-Logístico</span>
      </div>
    </div>
    '''

print("Updated mapeo module v5 ready.")
