#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Limpieza y Configuración Inicial: Instancia Secundaria Masterclass Odoo 19
"De la logística a la contabilidad: Domina la valoración de inventarios en Odoo 19"

Propósito:
- Instancia limpia para demostrar en vivo el ESCENARIO HAPPY PATH (Flujo sano desde cero).
- Purga atómica de todas las transacciones operativas y contables previas.
- Deja configuradas las categorías en AVCO Perpetuo, ubicaciones y las plantillas de producto
  con existencias en cero, listas para compras, recepciones, ventas y facturas desde cero.

Perfil MCP-Odoo: 'masterclass-julio121'
URL: https://julioserna-masterclass-julio121-39960335.dev.odoo.com/
"""

import subprocess
import json
import time
import sys

PROFILE = "masterclass-julio121"

def call_kw(model, method, args=[], kwargs={}):
    cmd = ["odoo-mcp", "execute-kw", "--profile", PROFILE, "--model", model, "--method", method, "--args", json.dumps(args)]
    if kwargs:
        cmd.extend(["--kwargs", json.dumps(kwargs)])
    r = subprocess.run(cmd, capture_output=True, text=True)
    try:
        data = json.loads(r.stdout)
        if isinstance(data, dict) and "result" in data:
            return data["result"]
        return data
    except Exception as e:
        print(f"Error calling {model}.{method}: {r.stderr or r.stdout}")
        return None

def clean_secondary_transactions():
    print("🧹 1. Limpiando transacciones previas en Instancia Secundaria (Purga Atómica Total)...")
    purge_code = """
tables = [
    'stock_landed_cost_lines',
    'stock_landed_cost',
    'account_partial_reconcile',
    'account_move_line',
    'account_move',
    'purchase_order_line',
    'purchase_order',
    'sale_order_line',
    'sale_order',
    'stock_quant',
    'stock_move_line',
    'stock_move',
    'stock_picking',
    'product_supplierinfo',
    'product_product',
    'product_template',
]
results = {}
for t in tables:
    env.cr.execute(f"DELETE FROM {t}")
    results[t] = f"deleted {env.cr.rowcount}"

try:
    env.cr.execute("UPDATE ir_sequence SET number_next = 1 WHERE code IN ('purchase.order', 'sale.order')")
except Exception:
    pass

action = {'results': results}
"""
    # Buscar o crear la acción de purga
    actions = call_kw("ir.actions.server", "search", [[("name", "=", "Purge Masterclass Database")]])
    if not actions:
        act_id = call_kw("ir.actions.server", "create", [{
            "name": "Purge Masterclass Database",
            "model_id": 548,
            "state": "code",
            "code": purge_code
        }])
    else:
        act_id = actions[0]
        call_kw("ir.actions.server", "write", [[act_id], {"code": purge_code}])

    res = call_kw("ir.actions.server", "run", [[act_id]])
    print(f"   ✓ Purga de transacciones ejecutada: {json.dumps(res)}")

def setup_clean_configuration():
    print("🏢 2. Configurando categorías y ubicaciones en Odoo 19 (AVCO Perpetuo)...")
    cat_id = 4 # Almacenable - AVCO (Perpetuo México)
    call_kw("product.category", "write", [[cat_id], {
        "property_cost_method": "average",
        "property_valuation": "real_time",
        "property_stock_valuation_account_id": 14 # Cuenta 115.01.01 Inventarios
    }])

    # Ubicación virtual Inventory adjustment (ID 11): configurada con cuenta de costo de ventas (ID 87)
    # para que en la instancia secundaria cualquier ajuste o prueba funcione 100% en tiempo real.
    call_kw("stock.location", "write", [[11], {"valuation_account_id": 87}])

    return cat_id

def create_clean_products(cat_id):
    print("📦 3. Creando plantillas de productos oficiales (Existencias en CERO, listos para Happy Path)...")
    
    products_to_create = [
        {
            "name": "Teclado Ergonómico Inalámbrico",
            "default_code": "TECL-INAL-USB",
            "is_storable": True,
            "active": True,
            "categ_id": cat_id,
            "standard_price": 0.0 # Listo para que la primera compra fije su costo inicial
        },
        {
            "name": "Monitor Profesional 27\" 4K",
            "default_code": "MON-27-4K",
            "is_storable": True,
            "active": True,
            "categ_id": cat_id,
            "standard_price": 0.0 # Listo para la compra en USD
        },
        {
            "name": "Mouse Óptico Ergonómico USB",
            "default_code": "MOUS-OPT-USB",
            "is_storable": True,
            "active": True,
            "categ_id": cat_id,
            "standard_price": 85.0
        },
        {
            "name": "Router Inalámbrico Wi-Fi 4 (Legacy)",
            "default_code": "ROUT-WIFI4-LEG",
            "is_storable": True,
            "active": True,
            "categ_id": cat_id,
            "standard_price": 300.0
        },
        {
            "name": "Cámara Web Pro 4K",
            "default_code": "CAM-WEB-4K",
            "is_storable": True,
            "active": True,
            "categ_id": cat_id,
            "standard_price": 1500.0
        },
        {
            "name": "Memoria RAM DDR5 16GB",
            "default_code": "MEM-RAM-16GB",
            "is_storable": True,
            "active": True,
            "categ_id": cat_id,
            "standard_price": 100.0
        },
        {
            "name": "Disco Sólido SSD NVMe 1TB",
            "default_code": "DISC-SSD-1TB",
            "is_storable": True,
            "active": True,
            "categ_id": cat_id,
            "standard_price": 200.0
        }
    ]

    for p in products_to_create:
        pid = call_kw("product.product", "create", [p])
        print(f"   ✓ Creado [{p['default_code']}] {p['name']} (ID: {pid}, Stock: 0.0 u)")

def setup_server_action_and_report():
    print("📊 4. Configurando Acción de Servidor #589 en Instancia Secundaria...")
    server_action_code = """# 1. Obtener productos activos en ubicaciones internas
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

# Asegurar que aparezcan los 7 productos del catálogo aunque tengan stock 0
all_prods = env['product.product'].search([('default_code', 'in', [
    'TECL-INAL-USB', 'MON-27-4K', 'MOUS-OPT-USB', 'ROUT-WIFI4-LEG',
    'CAM-WEB-4K', 'MEM-RAM-16GB', 'DISC-SSD-1TB'
])])
for p in all_prods:
    product_ids_set.add(p.id)
    if p.id not in product_data:
        product_data[p.id] = {'product': p, 'qty': 0.0, 'stock_value': 0.0}

product_ids = list(product_ids_set)

# 3. Valor por facturar (purchase.order.line con bill_to_receive = True, convertido a moneda compañía)
val_por_facturar = {pid: 0.0 for pid in product_ids}
if product_ids:
    pols = env['purchase.order.line'].search([
        ('product_id', 'in', product_ids),
        ('bill_to_receive', '=', True)
    ])
    for pol in pols:
        pid = pol.product_id.id
        v = (pol.qty_received - pol.qty_invoiced) * pol.price_unit
        if pol.currency_id and pol.currency_id != pol.company_id.currency_id:
            v = pol.currency_id._convert(
                v,
                pol.company_id.currency_id,
                pol.company_id,
                pol.order_id.date_approve or pol.order_id.date_order
            )
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

lines = [",".join(f'"{h}"' for h in header)]
for pid in sorted(product_ids):
    data = product_data[pid]
    prod = data['product']
    name = (prod.display_name or prod.name or '').replace('"', '""')
    status = "Activo" if prod.active else "Archivado"
    cost = prod.standard_price or 0.0
    qty = data['qty']
    v_exist = data['stock_value']
    v_fact = val_por_facturar.get(pid, 0.0)
    v_cont = val_contabilidad.get(pid, 0.0)
    v_norec = val_no_reconocido.get(pid, 0.0)
    dif = v_exist - (v_fact + v_cont + v_norec)
    
    row = [
        f'"{name}"',
        f'"{status}"',
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
    'name': f'conciliacion_inventario_secundaria_{today_str}.csv',
    'raw': csv_content.encode('utf-8-sig'),
    'mimetype': 'text/csv',
    'res_model': 'stock.quant',
})

action = {
    'type': 'ir.actions.act_url',
    'url': f'/web/content/{attachment.id}?download=true',
    'target': 'self',
}
"""
    actions = call_kw("ir.actions.server", "search", [[("name", "=", "Descargar Reporte Conciliación Inventario (CSV)")]])
    if actions:
        call_kw("ir.actions.server", "write", [[actions[0]], {"code": server_action_code}])
        call_kw("ir.actions.server", "run", [[actions[0]]])
    else:
        act_id = call_kw("ir.actions.server", "create", [{
            "name": "Descargar Reporte Conciliación Inventario (CSV)",
            "model_id": 548,
            "state": "code",
            "code": server_action_code
        }])
        call_kw("ir.actions.server", "run", [[act_id]])

    att = call_kw("ir.attachment", "search_read", [[("res_model", "=", "stock.quant")]], {"fields": ["raw"], "limit": 1, "order": "id desc"})
    if att:
        raw_csv = att[0]["raw"]
        with open("/Users/julioserna/Downloads/conciliacion_inventario_secundaria.csv", "w", encoding="utf-8") as f:
            f.write(raw_csv)
        print("   ✓ conciliacion_inventario_secundaria.csv actualizado en Downloads.")

if __name__ == "__main__":
    print("==========================================================")
    print(" LIMPIEZA DE INSTANCIA SECUNDARIA (SOLO CONFIGURACIÓN)   ")
    print(" Instancia: https://julioserna-masterclass-julio121-39960335.dev.odoo.com/")
    print("==========================================================")
    clean_secondary_transactions()
    cat_id = setup_clean_configuration()
    create_clean_products(cat_id)
    setup_server_action_and_report()
    print("==========================================================")
    print(" INSTANCIA SECUNDARIA 100% LIMPIA PARA REPLICAR HAPPY PATH")
    print(" - Cero existencias, cero órdenes, cero apuntes contables.")
    print(" - 7 plantillas de producto creadas y configuradas en AVCO.")
    print("==========================================================")
