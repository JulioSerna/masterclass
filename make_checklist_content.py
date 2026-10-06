#!/usr/bin/env python3
# Content for Entregable #1: Checklist de Auditoría Logística-Contable (Odoo 19.0 MX)

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
          <p class="doc-subtitle">Odoo 19.0 · Localización México · Método Costo Promedio (AVCO)</p>
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
          <input type="text" class="meta-input" placeholder="Nombre de la Compañía SA de CV" id="metaEmpresa" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>FECHA DE CORTE (CUT-OFF):</label>
          <input type="date" class="meta-input" id="metaFecha" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>RESPONSABLE LOGÍSTICO:</label>
          <input type="text" class="meta-input" placeholder="Nombre del Jefe de Almacén" id="metaLogistica" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>CONTADOR GENERAL / AUDITOR:</label>
          <input type="text" class="meta-input" placeholder="Nombre del Auditor / Contador" id="metaContador" onchange="saveMeta()">
        </div>
      </div>

      <!-- Checklist Sections -->
      <div class="checklist-sections">
        <!-- Section 1 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">FASE 1</div>
            <h3>Validaciones Críticas de Inventario (AVCO)</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_1">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.1 Inexistencia de Stock Negativo</div>
                <div class="chk-desc">Verificar mediante filtro en el reporte de inventario que ninguna ubicación interna presente cantidades menores a 0.00. El inventario negativo corrompe el cálculo matemático del Costo Promedio Ponderado.</div>
              </div>
              <span class="chk-tag tag-critico">CRÍTICO SAT</span>
            </label>

            <label class="chk-item" data-id="chk_2">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.2 Ausencia de Productos con Costo $0.00</div>
                <div class="chk-desc">Confirmar que no existan recepciones o productos activos con costo unitario en cero (salvo muestras o promociones estrictamente documentadas con póliza no deducible).</div>
              </div>
              <span class="chk-tag tag-alto">ALTO IMPACTO</span>
            </label>

            <label class="chk-item" data-id="chk_3">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.3 Configuración de Categorías de Producto</div>
                <div class="chk-desc">Revisar que todas las categorías de mercancías operen con Método de Costeo "Average Cost (AVCO)" y Valoración de Inventario "Automated / Perpetuo".</div>
              </div>
              <span class="chk-tag tag-normativo">NORMATIVO</span>
            </label>

            <label class="chk-item" data-id="chk_4">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.4 Verificación de Unidades de Medida (UoM)</div>
                <div class="chk-desc">Asegurar que las conversiones de unidades entre compras (ej. cajas, tarimas) y consumo/venta (ej. piezas) mantengan factores exactos sin redondeos atípicos que desvíen el costo unitario.</div>
              </div>
              <span class="chk-tag tag-control">CONTROL</span>
            </label>
          </div>
        </div>

        <!-- Section 2 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">FASE 2</div>
            <h3>Operaciones y Cierre Logístico (Localización MX)</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_5">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.1 Cierre de Movimientos de Entrada y Salida (Cut-Off)</div>
                <div class="chk-desc">Validar que todos los Stock Moves de compras y entregas correspondientes al periodo estén en estado 'Hecho' (Done). No deben quedar albaranes en 'Borrador' o 'Esperando' con fecha del mes cerrado.</div>
              </div>
              <span class="chk-tag tag-critico">CRÍTICO</span>
            </label>

            <label class="chk-item" data-id="chk_6">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.2 Liquidación de Órdenes de Producción (MRP)</div>
                <div class="chk-desc">Revisar que no existan órdenes de ensamble con consumos registrados en estado inconcluso. La cuenta WIP (1160) debe cuadrar contra las órdenes efectivamente en proceso al último minuto del mes.</div>
              </div>
              <span class="chk-tag tag-alto">MANUFACTURA</span>
            </label>

            <label class="chk-item" data-id="chk_7">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.3 Tipo de Cambio Oficial en Recepciones USD</div>
                <div class="chk-desc">En compras extranjeras, constatar que la tasa cambiaria registrada en el movimiento de entrada coincida con la tasa del Pedimento Aduanal / DOF de la fecha oficial de despacho.</div>
              </div>
              <span class="chk-tag tag-critico">CRÍTICO SAT</span>
            </label>

            <label class="chk-item" data-id="chk_8">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.4 Asignación Total de Landed Costs (Gastos en Destino)</div>
                <div class="chk-desc">Confirmar que los fletes marítimos, honorarios de agente aduanal y gastos aduanales ya hayan sido prorrateados al AVCO del producto antes de proceder al cierre contable.</div>
              </div>
              <span class="chk-tag tag-alto">IMPORTACIÓN</span>
            </label>
          </div>
        </div>

        <!-- Section 3 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">FASE 3</div>
            <h3>Conciliación Contable en Odoo 19.0</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_9">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.1 Panel Centralizado: Accounting > Review > Inventory Valuation</div>
                <div class="chk-desc">Ejecutar la auditoría en Odoo 19.0 estableciendo la fecha exacta de corte. Validar que el total monetario de valoración coincida con la suma de los Stock Moves cerrados.</div>
              </div>
              <span class="chk-tag tag-normativo">ODOO 19</span>
            </label>

            <label class="chk-item" data-id="chk_10">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.2 Cuadre Balanza de Comprobación: Cuenta 1150 = Reporte</div>
                <div class="chk-desc">El saldo final deudor de la Cuenta 1150 (Inventarios) en la Balanza de Comprobación del SAT debe ser idéntico al monto reportado por la Valoración de Inventario al centavo.</div>
              </div>
              <span class="chk-tag tag-critico">INNEGOCIABLE</span>
            </label>

            <label class="chk-item" data-id="chk_11">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.3 Auditoría de Asientos Manuales Intrusos</div>
                <div class="chk-desc">Filtrar todos los apuntes contables (account.move.line) de la cuenta 1150 cuyo origen NO sea un movimiento de almacén. Cualquier póliza manual en la cuenta 1150 debe ser revertida o justificada.</div>
              </div>
              <span class="chk-tag tag-critico">DETECCIÓN</span>
            </label>

            <label class="chk-item" data-id="chk_12">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.4 Depuración de Cuentas Transitorias Históricas</div>
                <div class="chk-desc">Si la base de datos migró desde Odoo 18 o anterior, asegurar que las antiguas cuentas Interim (Stock Input/Output) no arrastren saldos residuales no conciliados.</div>
              </div>
              <span class="chk-tag tag-control">MIGRACIÓN</span>
            </label>
          </div>
        </div>
      </div>

      <!-- Section 4: Sign-off & Audit Log -->
      <div class="doc-signoff">
        <h4 style="margin-bottom: 12px; font-family:'Sora';">Dictamen de Cierre y Aprobación</h4>
        <div class="signoff-grid">
          <div class="signoff-box">
            <div class="signoff-role">RESPONSABLE DE ALMACÉN / LOGÍSTICA</div>
            <div class="signoff-line"></div>
            <div class="signoff-name">Firma y Fecha de Aprobación</div>
            <p class="signoff-clause">Certifico que todos los movimientos físicos del periodo están capturados y que el inventario no presenta existencias negativas.</p>
          </div>
          <div class="signoff-box">
            <div class="signoff-role">CONTADOR GENERAL / DIRECTOR FINANCIERO</div>
            <div class="signoff-line"></div>
            <div class="signoff-name">Firma y Fecha de Aprobación</div>
            <p class="signoff-clause">Certifico que la Balanza de Comprobación (Cuenta 1150) coincide con la Valoración Logística y cumple con NIF C-4 y Art. 41 LISR.</p>
          </div>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="doc-footer">
        <span>Vauxoo Academy · Masterclass 2026: De la Logística a la Contabilidad</span>
        <span>Documento oficial de auditoría mensual · Odoo 19.0 MX</span>
      </div>
    </div>
    '''

print("Checklist module ready.")
