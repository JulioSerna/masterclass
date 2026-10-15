#!/usr/bin/env python3
# Content for Entregable #2: Tabla de Mapeo Conceptual v18 -> v19 & Guía de Arquitectura
# STRICT ALIGNMENT WITH masterclass-plan-final.md v8


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
                  <span class="badge-new">Auditoría nativa directa</span><br>
                  <em>Inventario > Informes > Movimientos de existencias y Balanza de Comprobación</em>.
                </td>
                <td>
                  Validación de consistencia inmediata previa a la emisión de estados financieros.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Part 1.B: Tabla Maestra de Movimientos Logísticos -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 1.B</span>
          <h3>Tabla Maestra de Movimientos Logísticos en Odoo 19.0</h3>
        </div>
        <p class="section-intro">
          ¿Cuáles eventos operativos generan pólizas automáticas a la cuenta de inventarios <code>115.01.01</code> y cuáles son neutros en Odoo 19?
        </p>
        <div class="table-responsive">
          <table class="comparison-table">
            <thead>
              <tr>
                <th style="width: 24%;">Movimiento / Evento</th>
                <th style="width: 20%;">Documento Funcional</th>
                <th style="width: 16%;">¿Genera Póliza a 1150?</th>
                <th style="width: 40%;">Justificación Técnica en Odoo 19</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Factura de Proveedor</strong></td>
                <td><code>Factura de Compra</code></td>
                <td><span class="pill-badge" style="background:#16A34A;">SÍ GENERA</span></td>
                <td><strong>Cargo 1150 · Abono 201</strong>. Fija el costo real de adquisición en la ponderación AVCO.</td>
              </tr>
              <tr>
                <td><strong>Costes en Destino (Landed Costs)</strong></td>
                <td><code>Coste en Destino (Landed)</code></td>
                <td><span class="pill-badge" style="background:#16A34A;">SÍ GENERA</span></td>
                <td><strong>Cargo 1150 · Abono Gastos</strong>. Incrementa el activo capitalizando fletes, seguros y aranceles sobre las recepciones.</td>
              </tr>
              <tr>
                <td><strong>Factura de Cliente</strong></td>
                <td><code>Factura de Cliente</code></td>
                <td><span class="pill-badge" style="background:#16A34A;">SÍ GENERA</span></td>
                <td><strong>Cargo 501 · Abono 1150</strong>. <em>¡Aquí se descarga el inventario en v19!</em> Reconoce el Costo de Ventas directamente al facturar.</td>
              </tr>
              <tr>
                <td><strong>Órdenes de Producción (MO)</strong></td>
                <td><code>Orden de Producción</code></td>
                <td><span class="pill-badge" style="background:#16A34A;">SÍ GENERA</span></td>
                <td><strong>Cargo 1150 PT · Abono 1150 MP</strong>. Transforma materias primas en producto terminado sin alterar el valor activo neto.</td>
              </tr>
              <tr>
                <td><strong>Ajustes de Inventario (Mermas/Conteos)</strong></td>
                <td><code>Ajuste de Conteo Físico</code></td>
                <td><span class="pill-badge" style="background:#D97706;">⚠️ CONDICIONAL</span></td>
                <td><strong>¡Peligro!</strong> Solo genera póliza contable si la ubicación virtual de desecho/ajuste tiene cuenta contrapartida asignada.</td>
              </tr>
              <tr>
                <td><strong>Entrega a Cliente (Salida)</strong></td>
                <td><code>Albarán de Entrega</code></td>
                <td><span class="pill-badge" style="background:#64748B;">NO GENERA</span></td>
                <td><strong>Puramente operativo.</strong> Descuenta existencias físicas del almacén; la póliza contable se genera al emitir la factura.</td>
              </tr>
              <tr>
                <td><strong>Recepción de Proveedor (Entrada)</strong></td>
                <td><code>Albarán de Recepción</code></td>
                <td><span class="pill-badge" style="background:#64748B;">NO GENERA</span></td>
                <td>Registra la entrada física; en flujos directos sin cuentas puente, la valoración se asienta con la factura de compra.</td>
              </tr>
              <tr>
                <td><strong>Traslados Internos entre Ubicaciones</strong></td>
                <td><code>Transferencia Interna</code></td>
                <td><span class="pill-badge" style="background:#64748B;">NO GENERA</span></td>
                <td>Mover de un estante a otro dentro del mismo almacén/compañía no altera el valor patrimonial de la cuenta 1150.</td>
              </tr>
              <tr>
                <td><strong>Pedidos de Venta (SO) / Compra (PO)</strong></td>
                <td><code>Pedido de Venta / Compra</code></td>
                <td><span class="pill-badge" style="background:#64748B;">NO GENERA</span></td>
                <td>Compromisos comerciales y contractuales; no alteran existencias físicas ni saldos contables.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Part 2: Flujo Comercial Completo -->
      <div class="doc-section" style="page-break-before: always;">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 2</span>
          <h3>La Operación Normal en Odoo 19 (Happy Path MXN y USD)</h3>
        </div>
        <p class="section-intro">
          Flujo operativo estricto de acuerdo al Bloque 3: Compra Progresiva AVCO, Venta y Entrega Física en MXN, y Compra/Facturación en USD:
        </p>

        <div class="import-lifecycle-box">
          <div class="lifecycle-stage">
            <div class="stage-num">1</div>
            <div class="stage-info">
              <h4>Primera Compra MXN — [TECL-INAL-USB] Teclado Ergonómico Inalámbrico</h4>
              <p>Recepción de 50 piezas a <strong>$150.00 MXN/u</strong> ($7,500 MXN totales). Costo promedio inicial: $150.00 MXN.</p>
              <div class="stage-memo">📌 <em>Asiento en cuenta 115.01.01: Cargo por $7,500.00 MXN.</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">2</div>
            <div class="stage-info">
              <h4>Segunda Compra MXN (Precio Superior) — Ponderación AVCO</h4>
              <p>Recepción de 50 piezas a <strong>$170.00 MXN/u</strong> ($8,500 MXN totales). Total en almacén: 100 piezas. <em>Mercancía recibida pero pendiente de facturar para auditoría.</em></p>
              <div class="asiento-mini">
                <div>(50 &times; $150 + 50 &times; $170) &divide; 100 = <strong>$160.00 MXN / pieza</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Valor físico en almacén: $16,000.00 MXN acumulados.</em></div>
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
              <h4>Factura de Cliente y Conciliación Forense</h4>
              <p>Factura emitida con asiento automático instantáneo de Costo de Ventas en Odoo 19:</p>
              <div class="asiento-mini">
                <div>CARGO: 501.01.01 Costo de Ventas → <strong>$4,800.00 MXN</strong> (30u &times; $160)</div>
                <div>ABONO: 115.01.01 Inventario → <strong>$4,800.00 MXN</strong></div>
              </div>
              <div class="stage-memo">📌 <em>Resultado: Saldo en cuenta 1150 = $2,700.00 MXN + Facturas por Recibir (PO 2) = $8,500.00 MXN $\rightarrow$ Total conciliado: $11,200.00 MXN (Almacén). Cuadre perfecto (Dif: $0.00 MXN).</em></div>
            </div>
          </div>

          <div class="lifecycle-stage">
            <div class="stage-num">5</div>
            <div class="stage-info">
              <h4>Operación en Moneda Extranjera USD — [MON-27-4K] Monitor Profesional 27" 4K</h4>
              <p>Compra de 20 unidades a <strong>$100.00 USD</strong> con tipo de cambio oficial de <strong>18.50 MXN/USD</strong> ($1,850.00 MXN/u).</p>
              <div class="asiento-mini">
                <div>Recepción de almacén: 20 u &times; $1,850 = $37,000.00 MXN cargados a cuenta 115.01.01.<br>
                Factura de proveedor procesada a la misma tasa: Cero desvío cambiario contable-logístico.</div>
              </div>
              <div class="stage-memo">📌 <em>Resultado: 20 u en almacén ($37,000.00 MXN) = Saldo contable ($37,000.00 MXN).</em></div>
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

      <!-- Part 4: Matriz de Mitigación de la Clínica de Desastres -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 4</span>
          <h3>Matriz de Mitigación: 5 Desastres Operativos + Póliza Manual</h3>
        </div>
        <div class="table-responsive">
          <table class="mitigation-matrix-table">
            <thead>
              <tr>
                <th>Caso Clínico / SKU</th>
                <th>Mecanismo de Falla en Odoo</th>
                <th>Impacto Financiero</th>
                <th>Solución Blindada en Odoo 19</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1. Ajuste sin Cuenta Contable</strong><br><small>[MOUS-OPT-USB]</small></td>
                <td>Ubicación virtual de ajuste físico o merma sin cuenta contrapartida asignada.</td>
                <td>El almacén registra 100 piezas ($8,500) pero la cuenta 1150 tiene $0. Descuadre: -$8,500 MXN.</td>
                <td>Configurar cuenta de contrapartida en la ubicación virtual y usar la Plantilla CSV de regularización.</td>
              </tr>
              <tr>
                <td><strong>2. Producto Archivado con Existencias</strong><br><small>[ROUT-WIFI4-LEG]</small></td>
                <td>El usuario archiva el producto (active=False) teniendo saldo físico y contable.</td>
                <td>Desaparece del reporte estándar de existencias, pero el saldo de $2,400 MXN sigue vivo en la 1150.</td>
                <td>Desarchivar temporalmente para dar salida formal o regularizar por script/acción de servidor.</td>
              </tr>
              <tr>
                <td><strong>3. Costo MXN en OC de USD</strong><br><small>[CAM-WEB-4K]</small></td>
                <td>El producto cuesta $1,500 MXN pero por descuido se seleccionó divisa USD en la orden de compra.</td>
                <td>Recepción a $1,500 USD &times; 18.50 = $27,750 MXN/u. Inflación masiva del costo de inventario ($277,500 vs $15,000).</td>
                <td>Rectificación de albarán o ajuste de valoración controlado antes de despachar mercancía.</td>
              </tr>
              <tr>
                <td><strong>4. Edición Directa de Costo en Ficha</strong><br><small>[MEM-RAM-16GB]</small></td>
                <td>Modificar manualmente el campo standard_price en la ficha sin asiento de revaloración contable.</td>
                <td>El almacén sube de $100 a $121 ($1,210 para 10 u) pero la contabilidad se queda en $1,000. Descuadre: -$210 MXN.</td>
                <td>Bloquear permisos de edición de coste unitario y canalizar ajustes a través de movimientos contables formales.</td>
              </tr>
              <tr>
                <td><strong>5. Venta Forzada con Stock Negativo</strong><br><small>[DISC-SSD-1TB]</small></td>
                <td>Despachar al cliente sin existencias previas (-5 u), recibiendo la compra después de la entrega.</td>
                <td>La venta anticipada sale a costo provisional o $0, perdiendo la deducción contable real al entrar la compra.</td>
                <td>Prohibir entregas con stock en negativo mediante reglas estrictas de disponibilidad de almacén.</td>
              </tr>
              <tr>
                <td><strong>6. Póliza Manual del Contador en 1150</strong><br><small>MISC/2026/09/0001</small></td>
                <td>Asiento manual directo al debe de la cuenta 115.01.01 sin producto ni movimiento logístico.</td>
                <td>Inflación de +$487,000 MXN en el balance general que no corresponde a ningún bien físico en almacén.</td>
                <td>Desmarcar 'Permitir asientos manuales' en la cuenta 115.01.01 y cancelar pólizas intrusas.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Part 5: Los 4 Modelos Esenciales de Auditoría -->
      <div class="doc-section" style="page-break-before: always;">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 5</span>
          <h3>Los 4 Modelos Esenciales de Auditoría ("El Cuadrilátero de Control")</h3>
        </div>
        <p class="section-intro">
          Para realizar una conciliación integral e identificar cualquier desvío contable-logístico, es obligatorio cruzar estas 4 fuentes de verdad:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-bottom: 24px;">
          <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:4px solid #345D90; border-radius:8px; padding:16px;">
            <strong style="color:#172A45; font-size:1rem;">1. Reporte de Existencias</strong>
            <p style="font-size:0.85rem; color:#475569; margin:8px 0;">Menú: <em>Inventario > Informes > Existencias</em> (o movimientos de existencias). Muestra unidades físicas $\times$ coste unitario de la ficha.</p>
            <small style="color:#345D90; font-weight:600;">Objetivo: Conocer el valor físico en bodega.</small>
          </div>

          <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:4px solid #AC0340; border-radius:8px; padding:16px;">
            <strong style="color:#172A45; font-size:1rem;">2. Facturas por Recibir</strong>
            <p style="font-size:0.85rem; color:#475569; margin:8px 0;">Cruce de líneas de compra con <code>qty_received > qty_invoiced</code>. Refleja mercancía física en almacén pendiente de factura del proveedor (como los <strong>$8,500.00 MXN</strong> de Teclados).</p>
            <small style="color:#AC0340; font-weight:600;">Objetivo: Auditar provisiones en tránsito.</small>
          </div>

          <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:4px solid #E4A900; border-radius:8px; padding:16px;">
            <strong style="color:#172A45; font-size:1rem;">3. Reporte Contable (Mayor 1150)</strong>
            <p style="font-size:0.85rem; color:#475569; margin:8px 0;">Balanza de Comprobación y Apuntes Contables en la cuenta <code>115.01.01</code>. Revela asientos sin producto y pólizas manuales intrusas.</p>
            <small style="color:#B45309; font-weight:600;">Objetivo: Auditar el saldo financiero en libros.</small>
          </div>

          <div style="background:#FFFFFF; border:1px solid #CBD5E1; border-top:4px solid #16A34A; border-radius:8px; padding:16px;">
            <strong style="color:#172A45; font-size:1rem;">4. Movimientos (stock.move)</strong>
            <p style="font-size:0.85rem; color:#475569; margin:8px 0;">Histórico granular de cada entrada, salida y ajuste con fecha efectiva, origen, destino y valor monetario unitario registrado.</p>
            <small style="color:#166534; font-weight:600;">Objetivo: Rastrear la causa raíz forense.</small>
          </div>
        </div>
      </div>

      <!-- Part 6: Recomendaciones de Saneamiento en la Vida Real -->
      <div class="doc-section">
        <div class="section-title-wrap">
          <span class="pill-badge">PARTE 6</span>
          <h3>Estrategias de Saneamiento en Producción: Parche Manual vs Borrón y Cuenta Nueva</h3>
        </div>
        
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-bottom: 24px;">
          <!-- Opción A -->
          <div style="background:#FEF2F2; border:1px solid #FECACA; border-left:5px solid #B91C1C; border-radius:8px; padding:20px;">
            <h4 style="color:#991B1B; margin-top:0;">❌ Vía A: El Parche Manual ("La Aspirina Destructiva")</h4>
            <p style="font-size:0.88rem; color:#7F1D1D; line-height:1.45;">
              <strong>Práctica común:</strong> El contador inyecta un asiento de diario directo cargando o abonando a la cuenta <code>115.01.01</code> para forzar el cuadre contra el reporte de almacén.
            </p>
            <div style="background:#FFFFFF; border:1px solid #FECACA; padding:12px; border-radius:6px; font-size:0.85rem; color:#991B1B; margin-top:10px;">
              <strong>Por qué fracasa:</strong> No modifica en nada las existencias del almacén ni el costo promedio de las fichas. En la siguiente venta o recepción, Odoo volverá a calcular salidas con costos erróneos, reabriendo la brecha contable de inmediato.
            </div>
          </div>

          <!-- Opción B -->
          <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-left:5px solid #16A34A; border-radius:8px; padding:20px;">
            <h4 style="color:#166534; margin-top:0;">✅ Vía B: Protocolo "Borrón y Cuenta Nueva" (Vauxoo)</h4>
            <p style="font-size:0.88rem; color:#14532D; line-height:1.45;">
              <strong>La solución definitiva:</strong> Recomendada para bases de datos con meses de descuadre acumulado donde la reconstrucción histórica es inviable:
            </p>
            <ol style="font-size:0.85rem; color:#14532D; margin:10px 0 0 16px; padding:0; line-height:1.5;">
              <li><strong>Corte Operativo:</strong> Detener movimientos de bodega durante la ventana de auditoría.</li>
              <li><strong>Descarga a Cero:</strong> Ajuste de inventario llevando todas las cantidades físicas a <code>0.00</code>.</li>
              <li><strong>Ajuste Contable a Cero:</strong> Regularizar la cuenta <code>115.01.01</code> a <code>$0.00</code> contra Pérdidas por Inventario.</li>
              <li><strong>Congelación de Categorías:</strong> Validar Fase 0 (AVCO, Perpetuo, Cuentas y permisos bloqueados).</li>
              <li><strong>Carga de Conteo Físico Real:</strong> Importar inventario físico real con coste promedio auditado.</li>
            </ol>
          </div>
        </div>

        <!-- Alerta Principio de Auditoría SKU por SKU -->
        <div style="padding: 14px 18px; background: #FFF1F2; border-left: 4px solid #AC0340; border-radius: 6px;">
          <strong style="color: #AC0340; font-size: 0.95rem;">⚠️ Principio de Auditoría Vauxoo: Cero Compensación Global (Auditoría SKU por SKU)</strong>
          <p style="margin: 6px 0 0; font-size: 0.88rem; color: #1E293B; line-height: 1.45;">
            Al auditar la cuenta 1150 contra el almacén, <strong>está estrictamente prohibido validar solo el gran total consolidado</strong>. Si un producto tiene un sobrante de +$1,500 y otro tiene un faltante de -$1,500, la suma arroja una diferencia engañosa de $0.00 que oculta dos contingencias operativas y fiscales graves. La conciliación solo es válida cuando se desglosa <strong>producto por producto</strong> y cada línea da una diferencia neta de $0.00.
          </p>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="doc-footer">
        <span>Vauxoo Academy · Masterclass 2026: Domina la valoración de inventarios en Odoo 19.0</span>
        <span>Plan Definitivo v8 · Control Contable-Logístico</span>
      </div>
    </div>
    '''

print("Updated mapeo module v8 ready.")
