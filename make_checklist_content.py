#!/usr/bin/env python3
# Content for Entregable #1: Checklist de Auditoría Logística-Contable (Odoo 19.0 · México)
# STRICTLY FOLLOWING masterclass-plan-final.md v5


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
          <p class="doc-subtitle">Odoo 19.0 Enterprise · Con Matriz de Cadencia de Control</p>
        </div>
      </div>

      <!-- Action Toolbar (hidden on print) -->
      <div class="doc-toolbar no-print">
        <div class="toolbar-stats">
          <div class="progress-bar-wrap">
            <div class="progress-bar-fill" id="checklistProgress" style="width: 0%;"></div>
          </div>
          <span class="stats-text" id="checklistStats">0 de 14 puntos validados (0%)</span>
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
          <input type="text" class="meta-input" placeholder="Nombre de la Compañía" id="metaEmpresa" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>FECHA DE CORTE (CUT-OFF):</label>
          <input type="date" class="meta-input" id="metaFecha" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>RESPONSABLE DE ALMACÉN / LOGÍSTICA:</label>
          <input type="text" class="meta-input" placeholder="Nombre del Responsable de Almacén" id="metaLogistica" onchange="saveMeta()">
        </div>
        <div class="meta-field">
          <label>CONTADOR GENERAL / AUDITOR:</label>
          <input type="text" class="meta-input" placeholder="Julio Serna / Auditor Responsable" id="metaContador" onchange="saveMeta()">
        </div>
      </div>

      <!-- Matriz de Cadencia Recomendada -->
      <div class="doc-section" style="margin-bottom: 28px;">
        <div class="section-title-wrap">
          <span class="pill-badge">DISCIPLINA DE CONTROL</span>
          <h3 style="font-size: 1.15rem;">Matriz de Cadencia de Auditoría Recomendada (Vauxoo)</h3>
        </div>
        <div class="table-responsive">
          <table class="cadencia-table" style="font-size: 0.85rem;">
            <thead>
              <tr style="background: #1E293B;">
                <th>Frecuencia</th>
                <th>Calificación</th>
                <th>Esfuerzo de Revisión</th>
                <th>Impacto Operativo en el Negocio</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Diaria</strong></td>
                <td>⭐⭐⭐⭐⭐ <span class="pill-badge" style="background:#16A34A;">EXCELENTE</span></td>
                <td>2 a 5 minutos</td>
                <td>Detección inmediata de desvíos (1-2 movimientos); cero sorpresas a fin de mes.</td>
              </tr>
              <tr>
                <td><strong>Semanal</strong></td>
                <td>⭐⭐⭐⭐ <span class="pill-badge" style="background:#0D9488;">RECOMENDADO</span></td>
                <td>15 minutos</td>
                <td>Corrección oportuna de recepciones o tipos de cambio erróneos sin fricción.</td>
              </tr>
              <tr>
                <td><strong>Mensual</strong></td>
                <td>⭐⭐⭐ <span class="pill-badge" style="background:#3B82F6;">BUENO</span></td>
                <td>1 a 2 horas</td>
                <td>Estándar indispensable para el cierre contable formal y reporte gerencial.</td>
              </tr>
              <tr>
                <td><strong>Anual</strong></td>
                <td>❌ <span class="pill-badge" style="background:#B91C1C;">EVITARLO A TODA COSTA</span></td>
                <td>Semanas de reconstrucción</td>
                <td>Miles de movimientos acumulados; descuadres prácticamente irrastreables y costosos.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Checklist Sections (14 items) -->
      <div class="checklist-sections">
        <!-- SECCIÓN 1 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">SECCIÓN 1</div>
            <h3>Configuración e Integridad de Categorías</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_1">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.1 Categorías en AVCO y Valoración Perpetua</div>
                <div class="chk-desc">Todas las categorías de producto almacenables operan con Método de Costo "Average Cost (AVCO)" y Valoración "Automated / Perpetua".</div>
              </div>
              <span class="chk-tag tag-normativo">ESTÁNDAR</span>
            </label>

            <label class="chk-item" data-id="chk_2">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.2 Cero Modificaciones en Caliente</div>
                <div class="chk-desc">Ninguna categoría de producto fue modificada en caliente (cambio de método de costeo o valuación) sin protocolo formal de corte.</div>
              </div>
              <span class="chk-tag tag-critico">INMUTABILIDAD</span>
            </label>

            <label class="chk-item" data-id="chk_3">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.3 Asientos Manuales Restringidos en Cuenta 115.01.01</div>
                <div class="chk-desc">La cuenta contable de inventarios (115.01.01) tiene desmarcada la opción de "Permitir asientos manuales" para evitar parches directos.</div>
              </div>
              <span class="chk-tag tag-critico">SEGURIDAD</span>
            </label>

            <label class="chk-item" data-id="chk_4">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">1.4 Ubicaciones de Ajuste con Cuentas Contables Configuradas</div>
                <div class="chk-desc">Se verificó que las ubicaciones virtuales de pérdida, merma y ajuste físico cuenten con su cuenta contable contrapartida debidamente asignada.</div>
              </div>
              <span class="chk-tag tag-critico">CONFIGURACIÓN</span>
            </label>
          </div>
        </div>

        <!-- SECCIÓN 2 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">SECCIÓN 2</div>
            <h3>Validaciones Logísticas y Existencias</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_5">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.1 Cero Productos con Existencias Negativas</div>
                <div class="chk-desc">Filtro de existencias aplicado: 0 productos con existencias menores a 0.00 en almacén para asegurar la validez matemática del costo promedio.</div>
              </div>
              <span class="chk-tag tag-critico">INTEGRIDAD</span>
            </label>

            <label class="chk-item" data-id="chk_6">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.2 Ausencia de Productos Activos con Costo $0.00 MXN</div>
                <div class="chk-desc">No existen productos activos con costo unitario en $0.00 MXN en el sistema sin una justificación formal documentada.</div>
              </div>
              <span class="chk-tag tag-alto">ALTO IMPACTO</span>
            </label>

            <label class="chk-item" data-id="chk_7">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.3 Albaranes de Entrada y Salida en Estado 'Hecho' (Done)</div>
                <div class="chk-desc">Todos los movimientos físicos del periodo fueron validados antes de la fecha de corte. Cero albaranes flotando en borrador.</div>
              </div>
              <span class="chk-tag tag-critico">CORTE LOGÍSTICO</span>
            </label>

            <label class="chk-item" data-id="chk_8">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">2.4 Entregas Respaldadas con Recepción Previa</div>
                <div class="chk-desc">Verificación de que ninguna entrega a cliente se haya despachado sin la confirmación y registro previo de la recepción de compra.</div>
              </div>
              <span class="chk-tag tag-alto">SECUENCIA</span>
            </label>
          </div>
        </div>

        <!-- SECCIÓN 3 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">SECCIÓN 3</div>
            <h3>Operaciones Cambiarias y Recepciones</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_9">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.1 Tipo de Cambio Oficial Validado en Recepciones</div>
                <div class="chk-desc">Recepciones de compra en moneda extranjera capturadas con el tipo de cambio oficial correspondiente a la fecha de recepción en almacén.</div>
              </div>
              <span class="chk-tag tag-critico">TIPO DE CAMBIO</span>
            </label>

            <label class="chk-item" data-id="chk_10">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">3.2 Compras Registradas Previo a Despachos Asociados</div>
                <div class="chk-desc">Órdenes de compra y facturas de proveedor procesadas ordenadamente para garantizar costo base correcto en cada salida.</div>
              </div>
              <span class="chk-tag tag-control">TRAZABILIDAD</span>
            </label>
          </div>
        </div>

        <!-- SECCIÓN 4 -->
        <div class="chk-section">
          <div class="chk-section-header">
            <div class="section-badge">SECCIÓN 4</div>
            <h3>Conciliación Contable (Odoo 19.0)</h3>
          </div>
          <div class="chk-list">
            <label class="chk-item" data-id="chk_11">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">4.1 Panel Centralizado: Contabilidad > Informes > Inventario</div>
                <div class="chk-desc">Revisión formal del reporte de valoración de inventario nativo de Odoo 19 estableciendo la fecha exacta de corte.</div>
              </div>
              <span class="chk-tag tag-normativo">ODOO 19</span>
            </label>

            <label class="chk-item" data-id="chk_12">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">4.2 Saldo de Existencias = Saldo de Cuenta 115.01.01 en Balanza</div>
                <div class="chk-desc">El total de existencias coincide al 100% con el saldo deudor de la cuenta 115.01.01 en la Balanza de Comprobación oficial.</div>
              </div>
              <span class="chk-tag tag-critico">CUADRE TOTAL</span>
            </label>

            <label class="chk-item" data-id="chk_13">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">4.3 Cero Apuntes Manuales Intrusos (Filtro MISC sin Documento Logístico)</div>
                <div class="chk-desc">Filtro de seguridad aplicado: cero apuntes contables en la cuenta 1150 con origen manual (asientos tipo MISC sin Stock Move asociado).</div>
              </div>
              <span class="chk-tag tag-critico">DETECCIÓN</span>
            </label>

            <label class="chk-item" data-id="chk_14">
              <input type="checkbox" onchange="updateProgress(this)">
              <div class="chk-content">
                <div class="chk-title">4.4 Ajustes Físicos con Movimiento Logístico Respaldado</div>
                <div class="chk-desc">Todo ajuste de inventario o merma cuenta con su documento de almacén correspondiente respaldando el apunte contable generado.</div>
              </div>
              <span class="chk-tag tag-control">CONTROL</span>
            </label>
          </div>
        </div>
      </div>

      <!-- Signoff -->
      <div class="doc-signoff">
        <h4 style="margin-bottom: 12px; font-family:'Sora';">Dictamen de Cierre y Aprobación de Auditoría</h4>
        <div class="signoff-grid">
          <div class="signoff-box">
            <div class="signoff-role">RESPONSABLE DE ALMACÉN / LOGÍSTICA</div>
            <div class="signoff-line"></div>
            <div class="signoff-name">Firma y Fecha de Aprobación</div>
            <p class="signoff-clause">Certifico que todos los albaranes físicos, recepciones y ajustes del periodo fueron registrados sin existencias negativas.</p>
          </div>
          <div class="signoff-box">
            <div class="signoff-role">CONTADOR GENERAL / AUDITOR FINANCIERO</div>
            <div class="signoff-line"></div>
            <div class="signoff-name">Firma y Fecha de Aprobación</div>
            <p class="signoff-clause">Certifico que la Balanza de Comprobación (Cuenta 115.01.01) cuadra exactamente con el Reporte de Existencias del almacén.</p>
          </div>
        </div>
      </div>

      <!-- Footer Note -->
      <div class="doc-footer">
        <span>Vauxoo Academy · Masterclass 2026: Domina la valoración de inventarios en Odoo 19.0</span>
        <span>Plan Definitivo v5 · Control Contable-Logístico</span>
      </div>
    </div>
    '''

print("Checklist module v5 compiled successfully.")
