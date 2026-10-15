#!/usr/bin/env python3
"""
Generates the HTML content for 'Entregable #4: Kit Técnico de Regularización & Acción de Servidor en Odoo 19'.
Compliant with Vauxoo Academy brand guidelines.
"""

def get_kit_html():
    return '''
    <div class="kit-wrapper" style="max-width: 1080px; margin: 0 auto; padding: 32px 20px;">
      
      <!-- Header Banner -->
      <div style="background: linear-gradient(90deg, #172A45 0%, #345D90 100%); color: #FFFFFF; border-radius: 12px; padding: 36px 32px; position: relative; overflow: hidden; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
        <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px;">
          <span class="pill-badge" style="background:#AC0340; color:#fff;">ENTREGABLE #4</span>
          <span class="pill-badge-outline">TOOLKIT OFICIAL DE AUDITORÍA</span>
          <span class="pill-badge-outline">ODOO 19.0 ENTERPRISE</span>
        </div>
        <h1 style="font-size: 2rem; font-weight: 700; color: #FFFFFF; margin-bottom: 10px; line-height: 1.25;">
          Kit Técnico: Regularización Manual & Acción de Servidor
        </h1>
        <p style="font-size: 1.05rem; color: #E2E8F0; max-width: 820px; margin-bottom: 0;">
          Los dos activos técnicos indispensables para garantizar el cuadre permanente entre Almacén y Contabilidad en México: la <strong>Plantilla CSV oficial de regularización con trazabilidad por SKU</strong> y el <strong>código fuente de la Acción de Servidor</strong> para auditar en 1 clic la fórmula de conciliación en Odoo 19.
        </p>
      </div>

      <!-- Quick Index Cards -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-bottom: 36px;">
        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 4px solid #AC0340; border-radius: 8px; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
          <span style="font-size: 0.8rem; font-weight: 700; color: #AC0340; text-transform: uppercase;">COMPONENTE A</span>
          <h3 style="font-size: 1.25rem; margin: 8px 0 10px 0; color: #27282F;">Plantilla CSV de Regularización</h3>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 16px;">
            Estructura estricta para importar pólizas de diario balanceadas en Odoo 19 con asignación obligatoria de <code>product_id</code> en cada apunte contable.
          </p>
          <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="plantilla_regularizacion_inventario.csv" download="plantilla_regularizacion_inventario.csv" class="btn btn-sm" style="background:#AC0340; color:#fff; text-decoration:none;">
              📥 Descargar Plantilla CSV
            </a>
            <a href="#componente-csv" class="btn btn-sm btn-secondary" style="color:#27282F; border-color:#CBD5E1; text-decoration:none;">
              Ver Especificación ↓
            </a>
          </div>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 4px solid #345D90; border-radius: 8px; padding: 24px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
          <span style="font-size: 0.8rem; font-weight: 700; color: #345D90; text-transform: uppercase;">COMPONENTE B</span>
          <h3 style="font-size: 1.25rem; margin: 8px 0 10px 0; color: #27282F;">Acción de Servidor (Reporte CSV)</h3>
          <p style="font-size: 0.9rem; color: #5A6578; margin-bottom: 16px;">
            Script en Python (compatible con <code>safe_eval</code>) para desplegar el reporte SKU por SKU con las columnas de conciliación, estado de producto y fórmula de cuadre.
          </p>
          <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="#componente-accion" class="btn btn-sm" style="background:#345D90; color:#fff; text-decoration:none;">
              📋 Copiar Código Fuente
            </a>
            <a href="#guia-instalacion" class="btn btn-sm btn-secondary" style="color:#27282F; border-color:#CBD5E1; text-decoration:none;">
              Paso a Paso de Instalación ↓
            </a>
          </div>
        </div>
      </div>

      <!-- COMPONENTE A: PLANTILLA CSV -->
      <section id="componente-csv" style="margin-bottom: 48px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px;">
          <span class="pill-badge" style="background:#AC0340; color:#fff; font-size: 0.85rem;">COMPONENTE A</span>
          <h2 style="font-size: 1.5rem; color: #27282F; margin: 0;">Plantilla Oficial de Importación de Pólizas (CSV)</h2>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 24px;">
          <h4 style="margin-top:0; color:#172A45; font-size:1.15rem;">¿Por qué una plantilla especializada?</h4>
          <p style="font-size:0.95rem; color:#475569; line-height:1.6;">
            Cuando existen ajustes de inventario físicos que por error de configuración histórica no generaron póliza contable (o cuando se requiere reclasificar variaciones de costo o productos archivados con saldo), <strong>NUNCA</strong> debe crearse un apunte ciego directo a la cuenta <code>115.01.01</code> sin asociar el producto. Si el producto se omite, el libro mayor registrará el saldo pero la auditoría por SKU quedará rota para siempre.
          </p>
          <p style="font-size:0.95rem; color:#475569; line-height:1.6;">
            Esta plantilla utiliza las cabeceras nativas de Odoo 19 para importar simultáneamente la cabecera del asiento (<code>account.move</code>) y el detalle balanceado de líneas (<code>account.move.line</code>) vinculando el código o referencia interna del producto:
          </p>

          <!-- Code preview of CSV -->
          <div style="position: relative; margin: 16px 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; background: #0F172A; color: #94A3B8; padding: 8px 16px; border-radius: 6px 6px 0 0; font-family: monospace; font-size: 0.8rem;">
              <span>plantilla_regularizacion_inventario.csv</span>
              <button onclick="navigator.clipboard.writeText(document.getElementById('csvCodeBlock').innerText); alert('CSV copiado al portapapeles');" style="background: #334155; color: #fff; border: none; padding: 4px 10px; border-radius: 4px; cursor: pointer; font-size: 0.75rem;">Copiar CSV</button>
            </div>
            <pre id="csvCodeBlock" style="margin: 0; background: #1E293B; color: #F8FAFC; padding: 16px; border-radius: 0 0 6px 6px; font-family: 'Consolas', 'Monaco', monospace; font-size: 0.85rem; overflow-x: auto; line-height: 1.5;">ref,date,journal_id,line_ids/account_id,line_ids/name,line_ids/product_id,line_ids/debit,line_ids/credit
REG-INV-2026-001,2026-10-14,MISC,115.01.01,Regularizacion ajuste omitido - Mouse Optico,MOUS-OPT-USB,8500.00,0.00
,,,501.01.02,Contrapartida variacion inventario - Mouse Optico,,0.00,8500.00
REG-INV-2026-002,2026-10-14,MISC,115.01.01,Regularizacion cambio costo manual - Memoria RAM,MEM-RAM-16GB,210.00,0.00
,,,501.01.02,Contrapartida variacion inventario - Memoria RAM,,0.00,210.00
REG-INV-2026-003,2026-10-14,MISC,115.01.01,Regularizacion producto archivado con saldo - Router Legacy,ROUT-WIFI4-LEG,0.00,2400.00
,,,501.01.02,Contrapartida variacion inventario - Router Legacy,,2400.00,0.00
REG-INV-2026-004,2026-10-14,MISC,115.01.01,Regularizacion stock negativo - Disco SSD 1TB,DISC-SSD-1TB,0.00,1500.00
,,,501.01.02,Contrapartida variacion inventario - Disco SSD 1TB,,1500.00,0.00</pre>
          </div>

          <!-- Explanation Table -->
          <h4 style="color:#172A45; margin: 24px 0 12px 0;">Campos y Reglas de Importación en Odoo 19</h4>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; text-align:left;">
              <thead>
                <tr style="background:#F8FAFC; border-bottom:2px solid #CBD5E1;">
                  <th style="padding:10px 12px; color:#172A45;">Columna CSV</th>
                  <th style="padding:10px 12px; color:#172A45;">Campo Técnico Odoo</th>
                  <th style="padding:10px 12px; color:#172A45;">Tipo / Mapeo</th>
                  <th style="padding:10px 12px; color:#172A45;">Descripción y Regla de Oro</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #E2E8F0;">
                  <td style="padding:10px 12px; font-family:monospace; font-weight:600; color:#AC0340;">ref</td>
                  <td style="padding:10px 12px; font-family:monospace;">account.move.ref</td>
                  <td style="padding:10px 12px;">Texto</td>
                  <td style="padding:10px 12px;">Identificador único de la póliza. La primera fila lo define; las líneas siguientes vacías indican que pertenecen a la misma póliza.</td>
                </tr>
                <tr style="border-bottom:1px solid #E2E8F0;">
                  <td style="padding:10px 12px; font-family:monospace; font-weight:600; color:#AC0340;">date</td>
                  <td style="padding:10px 12px; font-family:monospace;">account.move.date</td>
                  <td style="padding:10px 12px;">Fecha (YYYY-MM-DD)</td>
                  <td style="padding:10px 12px;">Fecha contable de reconocimiento del ajuste.</td>
                </tr>
                <tr style="border-bottom:1px solid #E2E8F0;">
                  <td style="padding:10px 12px; font-family:monospace; font-weight:600; color:#AC0340;">journal_id</td>
                  <td style="padding:10px 12px; font-family:monospace;">account.move.journal_id</td>
                  <td style="padding:10px 12px;">Código de Diario</td>
                  <td style="padding:10px 12px;">Diario de operaciones misceláneas (ej. <code>MISC</code> o diario específico de inventarios <code>STJ</code>).</td>
                </tr>
                <tr style="border-bottom:1px solid #E2E8F0;">
                  <td style="padding:10px 12px; font-family:monospace; font-weight:600; color:#AC0340;">line_ids/account_id</td>
                  <td style="padding:10px 12px; font-family:monospace;">account.move.line.account_id</td>
                  <td style="padding:10px 12px;">Código de Cuenta</td>
                  <td style="padding:10px 12px;"><code>115.01.01</code> para Inventarios y <code>501.01.02</code> para Variación de Inventarios (Resultados).</td>
                </tr>
                <tr style="border-bottom:1px solid #E2E8F0; background:#FFFBEB;">
                  <td style="padding:10px 12px; font-family:monospace; font-weight:600; color:#B45309;">line_ids/product_id</td>
                  <td style="padding:10px 12px; font-family:monospace;">account.move.line.product_id</td>
                  <td style="padding:10px 12px;">Referencia / SKU</td>
                  <td style="padding:10px 12px;"><strong>MANDATORIO EN LÍNEA DE INVENTARIO:</strong> Identifica el producto específico para que el reporte de conciliación lo reconozca.</td>
                </tr>
                <tr style="border-bottom:1px solid #E2E8F0;">
                  <td style="padding:10px 12px; font-family:monospace; font-weight:600; color:#AC0340;">line_ids/debit</td>
                  <td style="padding:10px 12px; font-family:monospace;">account.move.line.debit</td>
                  <td style="padding:10px 12px;">Decimal</td>
                  <td style="padding:10px 12px;">Importe cargado (aumento de inventario en la 1150).</td>
                </tr>
                <tr>
                  <td style="padding:10px 12px; font-family:monospace; font-weight:600; color:#AC0340;">line_ids/credit</td>
                  <td style="padding:10px 12px; font-family:monospace;">account.move.line.credit</td>
                  <td style="padding:10px 12px;">Decimal</td>
                  <td style="padding:10px 12px;">Importe abonado (disminución de inventario o contrapartida).</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- COMPONENTE B: ACCION DE SERVIDOR -->
      <section id="componente-accion" style="margin-bottom: 48px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px;">
          <span class="pill-badge" style="background:#345D90; color:#fff; font-size: 0.85rem;">COMPONENTE B</span>
          <h2 style="font-size: 1.5rem; color: #27282F; margin: 0;">Acción de Servidor: Auditoría de Conciliación en CSV</h2>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px; margin-bottom: 24px;">
          <h4 style="margin-top:0; color:#172A45; font-size:1.15rem;">La Fórmula Matemática de Cuadre</h4>
          <p style="font-size:0.95rem; color:#475569; line-height:1.6;">
            La acción de servidor ejecuta automáticamente la reconciliación entre 4 fuentes de datos de Odoo 19 para cada producto activo o archivado con saldo contable:
          </p>
          
          <div style="background:#F1F5F9; border-left:4px solid #345D90; padding:16px; border-radius:0 6px 6px 0; margin-bottom:20px; font-family:monospace; font-size:0.92rem; color:#1E293B;">
            <strong>Diferencia (Cuadre) =</strong> Valor en Existencias - (Valor por Facturar + Valor en Contabilidad + Valor No Reconocido)
          </div>

          <p style="font-size:0.95rem; color:#475569; line-height:1.6;">
            <strong>Detección de Productos Archivados:</strong> A diferencia de las vistas estándar que ocultan los productos inactivos, la acción audita automáticamente cualquier SKU archivado que conserve movimientos o saldo en la cuenta <code>115.01.01</code>.
          </p>

          <!-- Server Action Code -->
          <div style="position: relative; margin: 16px 0;">
            <div style="display: flex; justify-content: space-between; align-items: center; background: #0F172A; color: #94A3B8; padding: 8px 16px; border-radius: 6px 6px 0 0; font-family: monospace; font-size: 0.8rem;">
              <span>Código Python (Odoo 19 Server Action · safe_eval compliant)</span>
              <button onclick="navigator.clipboard.writeText(document.getElementById('pythonCodeBlock').innerText); alert('Código de Acción de Servidor copiado al portapapeles');" style="background: #334155; color: #fff; border: none; padding: 4px 10px; border-radius: 4px; cursor: pointer; font-size: 0.75rem;">Copiar Código</button>
            </div>
            <pre id="pythonCodeBlock" style="margin: 0; background: #1E293B; color: #F8FAFC; padding: 18px; border-radius: 0 0 6px 6px; font-family: 'Consolas', 'Monaco', monospace; font-size: 0.82rem; overflow-x: auto; line-height: 1.45;"># 1. Obtener productos activos en ubicaciones internas
quants = env['stock.quant'].search([
    ('location_id.usage', '=', 'internal'),
    ('product_id.active', '=', True)
])

product_ids_set = set()
product_data = {}

for q in quants:
    p = q.product_id
    product_ids_set.add(p.id)
    if p.id not in product_data:
        product_data[p.id] = {'product': p, 'qty': 0.0, 'stock_value': 0.0}
    product_data[p.id]['qty'] += q.quantity
    product_data[p.id]['stock_value'] += q.value

# 2. Agregar productos archivados que tengan saldo contable en la 1150
amls_archived = env['account.move.line'].search([
    ('account_id.code', '=', '115.01.01'),
    ('move_id.state', '=', 'posted'),
    ('product_id.active', '=', False),
    ('product_id', '!=', False)
])
for aml in amls_archived:
    p = aml.product_id
    product_ids_set.add(p.id)
    if p.id not in product_data:
        q_arch = env['stock.quant'].search([
            ('location_id.usage', '=', 'internal'),
            ('product_id', '=', p.id)
        ])
        q_sum = sum(q_arch.mapped('quantity'))
        v_sum = sum(q_arch.mapped('value'))
        product_data[p.id] = {'product': p, 'qty': q_sum, 'stock_value': v_sum}

product_ids = list(product_ids_set)

# 3. Valor por facturar (purchase.order.line con bill_to_receive = True)
val_por_facturar = {pid: 0.0 for pid in product_ids}
if product_ids:
    pols = env['purchase.order.line'].search([
        ('product_id', 'in', product_ids),
        ('bill_to_receive', '=', True)
    ])
    for pol in pols:
        pid = pol.product_id.id
        v = pol.amount_to_invoice_at_date or ((pol.qty_received - pol.qty_invoiced) * pol.price_unit)
        val_por_facturar[pid] = val_por_facturar.get(pid, 0.0) + v

# 4. Valor en contabilidad (cuenta 115.01.01)
val_contabilidad = {pid: 0.0 for pid in product_ids}
if product_ids:
    amls = env['account.move.line'].search([
        ('account_id.code', '=', '115.01.01'),
        ('move_id.state', '=', 'posted'),
        ('product_id', 'in', product_ids)
    ])
    for aml in amls:
        pid = aml.product_id.id
        val_contabilidad[pid] = val_contabilidad.get(pid, 0.0) + (aml.debit - aml.credit)

# 5. Valor no reconocido: stock.move.line de ajuste de inventario sin poliza
val_no_reconocido = {pid: 0.0 for pid in product_ids}
if product_ids:
    smls = env['stock.move.line'].search([
        ('product_id', 'in', product_ids),
        ('is_inventory', '=', True),
        ('state', '=', 'done'),
        ('move_id.account_move_id', '=', False)
    ])
    for sml in smls:
        pid = sml.product_id.id
        m = sml.move_id
        if m.quantity:
            v = (sml.quantity / m.quantity) * (m.value or (m.quantity * (m.price_unit or sml.product_id.standard_price)))
        else:
            v = sml.quantity * (m.price_unit or sml.product_id.standard_price)
        
        if sml.location_id.usage != 'internal' and sml.location_dest_id.usage == 'internal':
            val_no_reconocido[pid] = val_no_reconocido.get(pid, 0.0) + v
        elif sml.location_id.usage == 'internal' and sml.location_dest_id.usage != 'internal':
            val_no_reconocido[pid] = val_no_reconocido.get(pid, 0.0) - v

# 6. Generar reporte CSV
header = [
    "Producto",
    "Estado",
    "Costo",
    "Cantidad",
    "Valor en existencias",
    "Valor por facturar",
    "Valor en contabilidad",
    "Valor no reconocido",
    "Diferencia (Cuadre)"
]

lines = [",".join(f'\"{h}\"' for h in header)]
for pid in sorted(product_ids):
    data = product_data[pid]
    prod = data['product']
    name = (prod.display_name or prod.name or '').replace('\"', '\"\"')
    status = "Activo" if prod.active else "Archivado"
    cost = prod.standard_price or 0.0
    qty = data['qty']
    v_exist = data['stock_value']
    v_fact = val_por_facturar.get(pid, 0.0)
    v_cont = val_contabilidad.get(pid, 0.0)
    v_norec = val_no_reconocido.get(pid, 0.0)
    dif = v_exist - (v_fact + v_cont + v_norec)
    
    row = [
        f'\"{name}\"',
        f'\"{status}\"',
        f'{cost:.2f}',
        f'{qty:.2f}',
        f'{v_exist:.2f}',
        f'{v_fact:.2f}',
        f'{v_cont:.2f}',
        f'{v_norec:.2f}',
        f'{dif:.2f}'
    ]
    lines.append(",".join(row))

csv_content = "\\r\\n".join(lines)

today_str = time.strftime('%Y-%m-%d')
attachment = env['ir.attachment'].create({
    'name': f'conciliacion_inventario_{today_str}.csv',
    'raw': csv_content.encode('utf-8-sig'),
    'mimetype': 'text/csv',
    'res_model': 'stock.quant',
})

action = {
    'type': 'ir.actions.act_url',
    'url': f'/web/content/{attachment.id}?download=true',
    'target': 'self',
}
</pre>
          </div>
        </div>
      </section>

      <!-- GUIA DE INSTALACION -->
      <section id="guia-instalacion" style="margin-bottom: 48px;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px; border-bottom: 2px solid #E2E8F0; padding-bottom: 12px;">
          <span class="pill-badge" style="background:#455A64; color:#fff; font-size: 0.85rem;">GUÍA TÉCNICA</span>
          <h2 style="font-size: 1.5rem; color: #27282F; margin: 0;">Cómo Instalar la Acción de Servidor en Odoo 19</h2>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-radius: 8px; padding: 24px;">
          <ol style="margin: 0; padding-left: 20px; font-size: 0.95rem; color: #334155; line-height: 1.8;">
            <li><strong>Activar Modo Desarrollador:</strong> En Odoo 19, dirígete a <em>Ajustes</em> y en la parte inferior haz clic en <em>Activar modo desarrollador</em>.</li>
            <li><strong>Navegar a Acciones de Servidor:</strong> Ve al menú <em>Ajustes &gt; Técnico &gt; Acciones &gt; Acciones de Servidor</em> (<code>ir.actions.server</code>).</li>
            <li><strong>Crear Nueva Acción:</strong> Haz clic en <em>Nuevo</em> y completa los siguientes campos:
              <ul style="margin: 8px 0; padding-left: 20px; color: #475569;">
                <li><strong>Nombre de la acción:</strong> <code>Descargar Reporte Conciliación Inventario (CSV)</code></li>
                <li><strong>Modelo:</strong> Selecciona <code>Quants (stock.quant)</code> o <code>Producto (product.product)</code>.</li>
                <li><strong>Acción a realizar:</strong> Selecciona <code>Ejecutar código Python</code>.</li>
              </ul>
            </li>
            <li><strong>Pegar Código:</strong> En la pestaña <em>Código Python</em>, pega exactamente el bloque de código superior.</li>
            <li><strong>Crear Botón Contextual:</strong> Haz clic en el botón superior <strong>Crear Acción Contextual</strong>. Esto añadirá la opción al menú desplegable <em>⚙️ Acción</em> de la vista de Existencias.</li>
            <li><strong>Uso en Producción:</strong> Ve a <em>Inventario &gt; Informes &gt; Existencias</em>, selecciona cualquier casilla para habilitar el engrane <em>Acción</em>, y selecciona <em>Descargar Reporte Conciliación Inventario (CSV)</em>. Tu navegador descargará inmediatamente el archivo UTF-8 BOM compatible con Microsoft Excel.</li>
          </ol>
        </div>
      </section>

    </div>
    '''
