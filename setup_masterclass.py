#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Maestro de Configuración y Carga de Datos: Masterclass Odoo 19.0
"De la logística a la contabilidad: Domina la valoración de inventarios en Odoo 19"

Ponente: Julio Serna (Vauxoo)
Catálogo: Hardware y Cómputo (100% Unidades Enteras · Cero NIF · Cero Landed Costs)
Ejecución: Automatizada sobre la base de datos 'masterclass' usando odoo-mcp CLI.

Casos recreados (ÚNICOS 7 PRODUCTOS EN CATÁLOGO):
1. Operación Normal MXN: [TECL-INAL-USB] Teclado Ergonómico (Compras 50@150 + 50@170 = AVCO 160; Venta 30u @ 250)
2. Operación Normal USD: [MON-27-4K] Monitor 4K (Compra 20u @ 100 USD * TC DOF 18.50 = AVCO 1,850 MXN)
3. Desastre 1: [MOUS-OPT-USB] Mouse Óptico (Ajuste 100u en categoría periódica; omitió póliza contable de $8,500)
4. Desastre 2: [ROUT-WIFI4-LEG] Router Wi-Fi 4 Legacy (8u @ $300 = $2,400; archivado con existencias vivas)
5. Desastre 3: [CAM-WEB-4K] Cámara Web Pro 4K (Error de moneda: $1,500 MXN comprados como 1,500 USD @ 18.50 = $27,750 MXN)
6. Desastre 4: [MEM-RAM-16GB] Memoria RAM (Costo alterado a mano en ficha de $100 a $121 = brecha de $210)
7. Desastre 5: [DISC-SSD-1TB] Disco SSD (Salida forzada en negativo de 5u y compra posterior de 15u @ $350 = brecha de $1,500)
8. El Hook Inicial: Póliza manual indebida en cuenta 1150 de $487,000 MXN sin SKU
"""

import subprocess
import json
import time
import sys

PROFILE = "masterclass"

def call_kw(model, method, args=[], kwargs={}, retries=4):
    cmd = ["odoo-mcp", "execute-kw", "--profile", PROFILE, "--model", model, "--method", method, "--args", json.dumps(args)]
    if kwargs:
        cmd.extend(["--kwargs", json.dumps(kwargs)])
    for attempt in range(retries):
        r = subprocess.run(cmd, capture_output=True, text=True)
        try:
            data = json.loads(r.stdout)
            if isinstance(data, dict) and "result" in data:
                return data["result"]
            if data is not None:
                return data
        except Exception:
            if attempt < retries - 1:
                time.sleep(2)
                continue
            print(f"Error calling {model}.{method}: {r.stderr or r.stdout}")
            return None
    return None

def clean_previous_transactions():
    print("🧹 1. Limpiando transacciones y productos previos en Odoo (Purga Atómica Total)...")
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
    print(f"   ✓ Purga completa ejecutada: {json.dumps(res)}")

def setup_categories_and_partners():
    print("🏢 2. Configurando categorías, ubicaciones y contactos (100% Contabilidad Perpetua)...")
    # Categoría Perpetua AVCO única para todos los productos de la Masterclass
    cat_id = 4 # Almacenable - AVCO (Perpetuo México)
    call_kw("product.category", "write", [[cat_id], {
        "property_cost_method": "average",
        "property_valuation": "real_time"
    }])

    # Eliminar categoría periódica residual si existiera de pruebas anteriores
    cat_periodic = call_kw("product.category", "search", [[("name", "=", "Tecnología / Periódico (Error de Configuración)")]])
    if cat_periodic:
        try:
            call_kw("product.category", "unlink", [cat_periodic])
        except Exception:
            pass

    # Ubicación virtual Inventory adjustment (ID 11): dejar sin cuenta contable (como viene por defecto en Odoo 19)
    # para demostrar que aun en Contabilidad Perpetua, un ajuste sin cuenta en la ubicación virtual no genera póliza.
    call_kw("stock.location", "write", [[11], {"valuation_account_id": False}])

    partner_prov_mx = 8  # Distribuidora Nacional de Insumos
    partner_prov_usd = 9 # Global Supply Tech LLC
    partner_cli = 11     # Cliente Industrial de México

    return cat_id, partner_prov_mx, partner_prov_usd, partner_cli

def setup_cases(cat_id, prov_mx, prov_usd, cli):
    print("🚀 3. Creando los 7 escenarios oficiales de la Masterclass...")

    # -------------------------------------------------------------
    # CASO 1: FLUJO LIMPIO EN MXN (Teclado Ergonómico Inalámbrico)
    # -------------------------------------------------------------
    print("   -> Creando Caso 1: Teclado Ergonómico (MXN Limpio)...")
    tecl = call_kw("product.product", "create", [{
        "name": "Teclado Ergonómico Inalámbrico",
        "default_code": "TECL-INAL-USB",
        "is_storable": True,
        "active": True,
        "categ_id": cat_id,
        "standard_price": 150.0
    }])
    # PO 1: 50 @ 150
    po1 = call_kw("purchase.order", "create", [{"partner_id": prov_mx}])
    call_kw("purchase.order.line", "create", [{"order_id": po1, "product_id": tecl, "product_qty": 50.0, "price_unit": 150.0, "tax_ids": [[6, 0, []]]}])
    call_kw("purchase.order", "button_confirm", [[po1]])
    pk1 = call_kw("purchase.order", "search_read", [[("id", "=", po1)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk1)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk1]])
    call_kw("purchase.order", "action_create_invoice", [[po1]])
    b1 = call_kw("purchase.order", "search_read", [[("id", "=", po1)]], {"fields": ["invoice_ids"]})[0]["invoice_ids"][0]
    call_kw("account.move", "write", [[b1], {"invoice_date": "2026-10-14"}])
    call_kw("account.move", "action_post", [[b1]])

    # PO 2: 50 @ 170 (Recibida pero PENDIENTE DE FACTURAR para auditoría)
    po2 = call_kw("purchase.order", "create", [{"partner_id": prov_mx}])
    call_kw("purchase.order.line", "create", [{"order_id": po2, "product_id": tecl, "product_qty": 50.0, "price_unit": 170.0, "tax_ids": [[6, 0, []]]}])
    call_kw("purchase.order", "button_confirm", [[po2]])
    pk2 = call_kw("purchase.order", "search_read", [[("id", "=", po2)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk2)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk2]])
    # NOTA: Omitimos la factura intencionalmente para demostrar "Facturas por Recibir" en la auditoría ($8,500 MXN)

    # Venta de 30 unidades
    so = call_kw("sale.order", "create", [{"partner_id": cli}])
    call_kw("sale.order.line", "create", [{"order_id": so, "product_id": tecl, "product_uom_qty": 30.0, "price_unit": 250.0, "tax_ids": [[6, 0, []]]}])
    call_kw("sale.order", "action_confirm", [[so]])
    pk_s = call_kw("sale.order", "search_read", [[("id", "=", so)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk_s)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk_s]])
    wiz = call_kw("sale.advance.payment.inv", "create", [{}], {"context": {"active_ids": [so], "active_model": "sale.order"}})
    call_kw("sale.advance.payment.inv", "create_invoices", [[wiz]], {"context": {"active_ids": [so], "active_model": "sale.order"}})
    so_inv = call_kw("sale.order", "search_read", [[("id", "=", so)]], {"fields": ["invoice_ids"]})[0]["invoice_ids"][0]
    call_kw("account.move", "write", [[so_inv], {"invoice_date": "2026-10-14"}])
    call_kw("account.move", "action_post", [[so_inv]])

    # -------------------------------------------------------------
    # CASO 2: FLUJO LIMPIO EN USD (Monitor Profesional 27" 4K)
    # -------------------------------------------------------------
    print("   -> Creando Caso 2: Monitor Profesional 27\" 4K (USD Limpio)...")
    mon = call_kw("product.product", "create", [{
        "name": "Monitor Profesional 27\" 4K",
        "default_code": "MON-27-4K",
        "is_storable": True,
        "active": True,
        "categ_id": cat_id,
        "standard_price": 0.0
    }])
    po_mon = call_kw("purchase.order", "create", [{"partner_id": prov_usd, "currency_id": 1}])
    call_kw("purchase.order.line", "create", [{"order_id": po_mon, "product_id": mon, "product_qty": 20.0, "price_unit": 100.0, "tax_ids": [[6, 0, []]]}])
    call_kw("purchase.order", "button_confirm", [[po_mon]])
    pk_mon = call_kw("purchase.order", "search_read", [[("id", "=", po_mon)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk_mon)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk_mon]])
    call_kw("purchase.order", "action_create_invoice", [[po_mon]])
    b_mon = call_kw("purchase.order", "search_read", [[("id", "=", po_mon)]], {"fields": ["invoice_ids"]})[0]["invoice_ids"][0]
    call_kw("account.move", "write", [[b_mon], {"invoice_date": "2026-10-14"}])
    call_kw("account.move", "action_post", [[b_mon]])

    # -------------------------------------------------------------
    # DESASTRE 1: AJUSTE INICIAL SIN CUENTA CONTABLE EN UBICACIÓN (Mouse Óptico)
    # -------------------------------------------------------------
    print("   -> Creando Desastre 1: Mouse Óptico (En Contabilidad Perpetua, ajuste sin cuenta en ubicación virtual)...")
    mous = call_kw("product.product", "create", [{
        "name": "Mouse Óptico Ergonómico USB",
        "default_code": "MOUS-OPT-USB",
        "is_storable": True,
        "active": True,
        "categ_id": cat_id, # 100% Contabilidad Perpetua; no genera póliza porque la ubicación 11 no tiene cuenta asignada
        "standard_price": 85.0
    }])
    quant_m = call_kw("stock.quant", "create", [{
        "product_id": mous,
        "location_id": 5, # WH/Stock
        "inventory_quantity": 100.0
    }])
    call_kw("stock.quant", "action_apply_inventory", [[quant_m]])

    # -------------------------------------------------------------
    # DESASTRE 2: PRODUCTO ARCHIVADO CON SALDO (Router Wi-Fi 4 Legacy)
    # -------------------------------------------------------------
    print("   -> Creando Desastre 2: Router Legacy (Archivado con saldo)...")
    rout = call_kw("product.product", "create", [{
        "name": "Router Inalámbrico Wi-Fi 4 (Legacy)",
        "default_code": "ROUT-WIFI4-LEG",
        "is_storable": True,
        "active": True,
        "categ_id": cat_id,
        "standard_price": 300.0
    }])
    po_r = call_kw("purchase.order", "create", [{"partner_id": prov_mx}])
    call_kw("purchase.order.line", "create", [{"order_id": po_r, "product_id": rout, "product_qty": 8.0, "price_unit": 300.0, "tax_ids": [[6, 0, []]]}])
    call_kw("purchase.order", "button_confirm", [[po_r]])
    pk_r = call_kw("purchase.order", "search_read", [[("id", "=", po_r)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk_r)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk_r]])
    call_kw("purchase.order", "action_create_invoice", [[po_r]])
    b_r = call_kw("purchase.order", "search_read", [[("id", "=", po_r)]], {"fields": ["invoice_ids"]})[0]["invoice_ids"][0]
    call_kw("account.move", "write", [[b_r], {"invoice_date": "2026-10-14"}])
    call_kw("account.move", "action_post", [[b_r]])
    # Se archiva teniendo existencias y póliza activa:
    call_kw("product.product", "write", [[rout], {"active": False}])

    # -------------------------------------------------------------
    # DESASTRE 3: ERROR DE MONEDA (Cámara Web Pro 4K)
    # -------------------------------------------------------------
    print("   -> Creando Desastre 3: Cámara Web (Error de moneda USD)...")
    cam = call_kw("product.product", "create", [{
        "name": "Cámara Web Pro 4K",
        "default_code": "CAM-WEB-4K",
        "is_storable": True,
        "active": True,
        "categ_id": cat_id,
        "standard_price": 1500.0
    }])
    po_cam = call_kw("purchase.order", "create", [{"partner_id": prov_usd, "currency_id": 1}])
    call_kw("purchase.order.line", "create", [{"order_id": po_cam, "product_id": cam, "product_qty": 10.0, "price_unit": 1500.0, "tax_ids": [[6, 0, []]]}])
    call_kw("purchase.order", "button_confirm", [[po_cam]])
    pk_cam = call_kw("purchase.order", "search_read", [[("id", "=", po_cam)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk_cam)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk_cam]])
    # DEJAR SIN FACTURAR: Para demostrar en vivo cómo auditar el monto pendiente y corregir la moneda en la factura
    print("   -> [AUDITORÍA] Cámara Web 4K recibida pero DEJADA SIN FACTURAR para demo en vivo.")
    # call_kw("purchase.order", "action_create_invoice", [[po_cam]])
    # b_cam = call_kw("purchase.order", "search_read", [[("id", "=", po_cam)]], {"fields": ["invoice_ids"]})[0]["invoice_ids"][0]
    # call_kw("account.move", "write", [[b_cam], {"invoice_date": "2026-10-14"}])
    # call_kw("account.move", "action_post", [[b_cam]])

    # -------------------------------------------------------------
    # DESASTRE 4: CAMBIO DIRECTO DE COSTO EN FICHA (Memoria RAM 16GB)
    # -------------------------------------------------------------
    print("   -> Creando Desastre 4: Memoria RAM (Costo alterado a mano en ficha)...")
    ram = call_kw("product.product", "create", [{
        "name": "Memoria RAM DDR5 16GB",
        "default_code": "MEM-RAM-16GB",
        "is_storable": True,
        "active": True,
        "categ_id": cat_id,
        "standard_price": 100.0
    }])
    po_ram = call_kw("purchase.order", "create", [{"partner_id": prov_mx}])
    call_kw("purchase.order.line", "create", [{"order_id": po_ram, "product_id": ram, "product_qty": 10.0, "price_unit": 100.0, "tax_ids": [[6, 0, []]]}])
    call_kw("purchase.order", "button_confirm", [[po_ram]])
    pk_ram = call_kw("purchase.order", "search_read", [[("id", "=", po_ram)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk_ram)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk_ram]])
    call_kw("purchase.order", "action_create_invoice", [[po_ram]])
    b_ram = call_kw("purchase.order", "search_read", [[("id", "=", po_ram)]], {"fields": ["invoice_ids"]})[0]["invoice_ids"][0]
    call_kw("account.move", "write", [[b_ram], {"invoice_date": "2026-10-14"}])
    call_kw("account.move", "action_post", [[b_ram]])
    # Alterar costo a mano en la ficha sin póliza:
    call_kw("product.product", "write", [[ram], {"standard_price": 121.0}])

    # -------------------------------------------------------------
    # DESASTRE 5: STOCK NEGATIVO FORZADO (Disco Sólido SSD 1TB)
    # -------------------------------------------------------------
    print("   -> Creando Desastre 5: Disco SSD (Stock negativo con compra posterior)...")
    ssd = call_kw("product.product", "create", [{
        "name": "Disco Sólido SSD NVMe 1TB",
        "default_code": "DISC-SSD-1TB",
        "is_storable": True,
        "active": True,
        "categ_id": cat_id,
        "standard_price": 200.0
    }])
    # Salida forzada de 10 unidades dejando stock en -10
    so_ssd = call_kw("sale.order", "create", [{"partner_id": cli}])
    call_kw("sale.order.line", "create", [{"order_id": so_ssd, "product_id": ssd, "product_uom_qty": 10.0, "price_unit": 350.0, "tax_ids": [[6, 0, []]]}])
    call_kw("sale.order", "action_confirm", [[so_ssd]])
    pk_out = call_kw("sale.order", "search_read", [[("id", "=", so_ssd)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk_out)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk_out]])
    wiz_ssd = call_kw("sale.advance.payment.inv", "create", [{}], {"context": {"active_ids": [so_ssd], "active_model": "sale.order"}})
    call_kw("sale.advance.payment.inv", "create_invoices", [[wiz_ssd]], {"context": {"active_ids": [so_ssd], "active_model": "sale.order"}})
    inv_ssd = call_kw("sale.order", "search_read", [[("id", "=", so_ssd)]], {"fields": ["invoice_ids"]})[0]["invoice_ids"][0]
    call_kw("account.move", "write", [[inv_ssd], {"invoice_date": "2026-10-14"}])
    call_kw("account.move", "action_post", [[inv_ssd]])

    # Compra posterior de 20 unidades a $350 MXN (Stock remanente: -10 + 20 = 10 unidades @ $350 = $3,500)
    po_ssd = call_kw("purchase.order", "create", [{"partner_id": prov_mx}])
    call_kw("purchase.order.line", "create", [{"order_id": po_ssd, "product_id": ssd, "product_qty": 20.0, "price_unit": 350.0, "tax_ids": [[6, 0, []]]}])
    call_kw("purchase.order", "button_confirm", [[po_ssd]])
    pk_in = call_kw("purchase.order", "search_read", [[("id", "=", po_ssd)]], {"fields": ["picking_ids"]})[0]["picking_ids"][0]
    for m in call_kw("stock.move", "search_read", [[("picking_id", "=", pk_in)]], {"fields": ["id", "product_uom_qty"]}):
        call_kw("stock.move", "write", [[m["id"]], {"quantity": m["product_uom_qty"]}])
    call_kw("stock.picking", "button_validate", [[pk_in]])
    call_kw("purchase.order", "action_create_invoice", [[po_ssd]])
    b_ssd = call_kw("purchase.order", "search_read", [[("id", "=", po_ssd)]], {"fields": ["invoice_ids"]})[0]["invoice_ids"][0]
    call_kw("account.move", "write", [[b_ssd], {"invoice_date": "2026-10-14"}])
    call_kw("account.move", "action_post", [[b_ssd]])

    # -------------------------------------------------------------
    # EL HOOK INICIAL: PÓLIZA MANUAL INDEBIDA EN CUENTA 1150
    # -------------------------------------------------------------
    print("   -> Creando El Hook: Póliza manual de $487,000 MXN en cuenta 1150...")
    acc_115 = 14
    acc_var = 88
    m_hook = call_kw("account.move", "create", [{
        "date": "2026-09-01",
        "journal_id": 3, # MISC
        "move_type": "entry",
        "ref": "Ajuste manual auditoría interna (Error contable)",
        "line_ids": [
            [0, 0, {"account_id": acc_115, "debit": 487000.0, "credit": 0.0, "name": "Ajuste manual a inventario (indebido)"}],
            [0, 0, {"account_id": acc_var, "debit": 0.0, "credit": 487000.0, "name": "Contrapartida ajuste manual"}]
        ]
    }])
    call_kw("account.move", "action_post", [[m_hook]])

    print("🎉 ¡TODOS LOS ESCENARIOS CREADOS CON ÉXITO!")

def run_server_action_and_update_downloads():
    print("📊 4. Actualizando y ejecutando Acción de Servidor #589 para exportar CSV a Downloads...")
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
"""
    call_kw("ir.actions.server", "write", [[589], {"code": server_action_code}])
    call_kw("ir.actions.server", "run", [[589]])
    att = call_kw("ir.attachment", "search_read", [[("res_model", "=", "stock.quant")]], {"fields": ["raw"], "limit": 1, "order": "id desc"})
    if att:
        raw_csv = att[0]["raw"]
        with open("/Users/julioserna/Downloads/conciliacion_inventario.csv", "w", encoding="utf-8") as f:
            f.write(raw_csv)
        print("   ✓ conciliacion_inventario.csv actualizado en Downloads.")

if __name__ == "__main__":
    print("==================================================")
    print(" REINICIO Y RECARGA DE DATOS: MASTERCLASS ODOO 19 ")
    print("==================================================")
    clean_previous_transactions()
    cat_id, prov_mx, prov_usd, cli = setup_categories_and_partners()
    setup_cases(cat_id, prov_mx, prov_usd, cli)
    run_server_action_and_update_downloads()
    print("==================================================")
    print(" INSTANCIA 100% LIMPIA Y LISTA PARA LA SESIÓN    ")
    print("==================================================")
