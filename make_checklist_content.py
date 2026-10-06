#!/usr/bin/env python3
# Content for Entregable #1: Checklist de Auditoría Logística-Contable (Odoo 19.0 MX)
# EXACT ALIGNMENT WITH PLAN FINAL FUSIONADO V2 (plan_v2_critico.md + setup_masterclass.py)

def get_checklist_html(logo_light, doodle_underline):
    return f'''
    <div class="deliverable-doc checklist-doc">
      <!-- Printable & Interactive Header -->
      <div class="doc-header">
        <div class="doc-header-brand">
          {logo_light}
        </div>
        <div class="doc-header-title">
          <span class="pill-badge">ENTREGABLE OFICIAL #1</span>
          <h2>Checklist de Auditoría Logística-Contable</h2>
          <p class="doc-subtitle">Odoo 19.0 · Localización México · Método Costo Promedio (AVCO) & Importaciones</p>
        </div>
      </div>

      <!-- Action Toolbar (hidden on print) -->
      <div class="doc-toolbar no-print">
        <div class="toolbar-stats">
          <div class="progress-bar-wrap">
            <div class="progress-bar-fill" id="checklistProgress" style="width: 0%;"></div>
          </div>
          <span class="stats-text" id="checklistStats">0 de 12 puntos validados (0%)</span>
        </div>
        <div class="toolbar-actions">
          <button class="btn btn-sm btn-light" onclick="checkAllItems(true)">Marcar Todos</button>
          <button class="btn btn-sm btn-light" onclick="resetChecklist()">Reiniciar</button>
          <button class="btn btn-sm" onclick="window.print()">
            🖨️ Imprimir / Guardar en PDF
          </button>
        </div>
      </div>

      <!-- Meta Information Grid -->
      <div class="doc-meta-grid">
        <div class="meta-field">
          <label>EMPRESA / RAZÓN SOCIAL:</label>
          <input type="text" class="meta-input" placeholder="Masterclass México, S.A. de C.V." id="metaEmpresa" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>FECHA DE CORTE (CUT-OFF):</label>
          <input type="date" class="meta-input" id="metaFecha" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>RESPONSABLE LOGÍSTICO / ALMACÉN:</label>
          <input type="text" class="meta-input" placeholder="Nombre del Jefe de Almacén" id="metaLogistica" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>CONTADOR GENERAL / AUDITOR:</label>
          <input type="text" class="meta-input" placeholder="Julio Serna / Auditor Responsable" id="metaContador" onchange="saveMeta()">
        </div>
      </div>

      <!-- Checklist Sections -->
      <div class="checklist-sections">
        <!-- Section 1 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">FASE 1</div>
            <h3>Validaciones Críticas de Inventario (AVCO en México)</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_1">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.1 Inexistencia de Stock Negativo (Producto VALVULA-NEG)</div>
                <div class="chk-desc">Verificar mediante filtro en el reporte de inventario que ninguna ubicación interna presente existencias menores a 0.00. El stock negativo destruye el divisor de la fórmula de Costo Promedio Ponderado e invalida el kardex fiscal ante el SAT.</div>
              </div>
              <span class="chk-tag tag-critico">CRÍTICO SAT</span>
            </label>

            <label class="chk-item" data-id="chk_2">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.2 Ausencia de Productos con Costo $0.00</div>
                <div class="chk-desc">Confirmar que ningún producto almacenable activo tenga costo unitario en cero (salvo muestras documentadas). Una recepción valorada en cero arrastra a la baja el AVCO del producto de manera irreversible.</div>
              </div>
              <span class="chk-tag tag-alto">ALTO IMPACTO</span>
            </label>

            <label class="chk-item" data-id="chk_3">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.3 Configuración de Categorías: Almacenable - AVCO (Perpetuo México)</div>
                <div class="chk-desc">Confirmar que las categorías operen con Método de Costeo "Average Cost (AVCO)", Valoración "Automated / Perpetuo" y cuenta de valoración asignada a la cuenta 115.01.01.</div>
              </div>
              <span class="chk-tag tag-normativo">NORMATIVO</span>
            </label>

            <label class="chk-item" data-id="chk_4">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.4 Verificación de Unidades de Medida (UoM)</div>
                <div class="chk-desc">Asegurar que las conversiones entre órdenes de compra (ej. cajas, millares) y consumo/venta interna mantengan factores de conversión exactos sin redondeos que alteren el costo unitario.</div>
              </div>
              <span class="chk-tag tag-control">CONTROL</span>
            </label>
          </div>
        </div>

        <!-- Section 2 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">FASE 2</div>
            <h3>Operaciones de Importación, Pedimentos y Tipos de Cambio</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_5">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.1 Cut-Off Logístico Estricto al Cierre de Mes</div>
                <div class="chk-desc">Validar que todos los Stock Moves de compras y entregas físicas correspondientes al periodo estén en estado 'Hecho' (Done) antes de las 23:59:59 del último día del mes. No deben existir albaranes pendientes en borrador.</div>
              </div>
              <span class="chk-tag tag-critico">INNEGOCIABLE</span>
            </label>

            <label class="chk-item" data-id="chk_6">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.2 Tasa Oficial DOF en Recepciones USD (Art. 20 CFF)</div>
                <div class="chk-desc">En compras extranjeras (ej. SENSOR-USD), constatar que la tasa cambiaria del albarán de entrada coincida exactamente con la tasa oficial del pedimento aduanal (DOF del día de despacho) para blindar el valor fiscal en aduanas.</div>
              </div>
              <span class="chk-tag tag-critico">CRÍTICO DOF</span>
            </label>

            <label class="chk-item" data-id="chk_7">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.3 Inyección de Pedimentos Aduanales vía Landed Costs (LANDED-COST)</div>
                <div class="chk-desc">Confirmar que las facturas de agencias aduanales (DTA, IGI, maniobras) se hayan procesado como Costos en Destino y prorrateado al AVCO del producto importado antes de que la mercancía sea entregada al cliente final.</div>
              </div>
              <span class="chk-tag tag-alto">PEDIMENTO</span>
            </label>

            <label class="chk-item" data-id="chk_8">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.4 Conciliación de Anticipos y Complementos de Pago</div>
                <div class="chk-desc">Verificar que los anticipos a proveedores extranjeros en USD (cuenta 205.01.01) hayan fijado la tasa histórica respectiva y que las diferencias al liquidar se hayan registrado como Fluctuación Cambiaria Realizada (cuenta 701.01.01).</div>
              </div>
              <span class="chk-tag tag-normativo">FINANCIERO</span>
            </label>
          </div>
        </div>

        <!-- Section 3 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">FASE 3</div>
            <h3>Conciliación Contable, Mermas y Cierre en Odoo 19.0</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_9">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.1 Panel Centralizado: Contabilidad > Revisión y Cierre > Valoración de inventario</div>
                <div class="chk-desc">Ejecutar el reporte de valoración nativo de Odoo 19 fijando la fecha exacta de corte. Validar que la suma total en pesos refleje las existencias físicas multiplicadas por su AVCO vigente.</div>
              </div>
              <span class="chk-tag tag-normativo">ODOO 19</span>
            </label>

            <label class="chk-item" data-id="chk_10">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.2 Cuadre Balanza SAT: Cuenta 115.01.01 = Reporte de Valoración</div>
                <div class="chk-desc">El saldo deudor final de la cuenta 115.01.01 (Mercancías) en la Balanza de Comprobación debe ser idéntico al total reportado por la Valoración de Inventario al centavo.</div>
              </div>
              <span class="chk-tag tag-critico">CUADRE TOTAL</span>
            </label>

            <label class="chk-item" data-id="chk_11">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.3 Auditoría de Asientos Manuales Intrusos (Póliza de $487,000 MXN)</div>
                <div class="chk-desc">Auditar los apuntes contables (account.move.line) de la cuenta 115.01.01. Confirmar que no existan pólizas de diario manuales del diario MISC sin Stock Move asociado. Toda póliza manual en la 115.01.01 debe revertirse.</div>
              </div>
              <span class="chk-tag tag-critico">DETECCIÓN</span>
            </label>

            <label class="chk-item" data-id="chk_12">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.4 Mermas a No Deducibles y Provisión de Obsolescencia (NIF C-4)</div>
                <div class="chk-desc">Validar que los ajustes por faltante de inventario (CABLE-MERMA) se canalicen a Gastos No Deducibles, y que el inventario de lento movimiento (TARJETA-OBS) se provisione en cuentas complementarias sin destruir el AVCO del producto.</div>
              </div>
              <span class="chk-tag tag-control">NIF C-4</span>
            </label>
          </div>
        </div>
      </div>

      <!-- Section 4: Sign-off & Audit Log -->
      <div class="doc-signoff">
        <h4 style="margin-bottom: 12px; font-family:'Sora';">Dictamen de Cierre y Aprobación de Auditoría</h4>
        <div class="signoff-grid">
          <div class="signoff-box">
            <div class="signoff-role">RESPONSABLE DE ALMACÉN / LOGÍSTICA</div>
            <div class="signoff-line"></div>
            <div class="signoff-name">Firma y Fecha de Aprobación</div>
            <p class="signoff-clause">Certifico que todos los movimientos físicos, recepciones aduanales y pedimentos del periodo fueron registrados sin existencias negativas.</p>
          </div>
          <div class="signoff-box">
            <div class="signoff-role">CONTADOR GENERAL / AUDITOR FINANCIERO</div>
            <div class="signoff-line"></div>
            <div class="signoff-name">Firma y Fecha de Aprobación</div>
            <p class="signoff-clause">Certifico que la Balanza de Comprobación (Cuenta 115.01.01) cuadra al centavo con el Reporte de Valoración, cumpliendo con NIF C-4 y Art. 41 LISR.</p>
          </div>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="doc-footer">
        <span>Vauxoo Academy · Masterclass 2026: Domina AVCO y Desastres de Importación en Odoo 19.0</span>
        <span>Documento oficial de auditoría de cierre · Localización México</span>
      </div>
    </div>
    '''

print("Updated checklist module ready.")
