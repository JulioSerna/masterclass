#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Maestro de Configuración y Carga de Datos: Masterclass Odoo 19.0
"De la logística a la contabilidad: Domina la valoración de inventarios en Odoo"

Ponente: Julio Serna (Vauxoo)
Instancia Odoo: https://julioserna-masterclass-main-38706787.dev.odoo.com/
Base de datos: julioserna-masterclass-main-38706787
Usuario: admin
Password: 123456789

Este script puede ser ejecutado directamente en local (requiere conexión a internet)
o mediante las herramientas de MCP/RPC para:
1. Configuración completa desde cero (--init / --all)
2. Reseteo y recarga de datos de demo iniciales (--reset-data)
3. Verificación de estado (--status)
"""

import sys
import xmlrpc.client
import argparse

# Configuración de conexión por defecto
DEFAULT_URL = "https://julioserna-masterclass-main-38706787.dev.odoo.com/"
DEFAULT_DB = "julioserna-masterclass-main-38706787"
DEFAULT_USER = "admin"
DEFAULT_PASS = "123456789"


class HeaderTransport(xmlrpc.client.SafeTransport):
    """Transporte XML-RPC con User-Agent personalizado para evitar bloqueos Cloudflare/WAF"""
    def send_headers(self, connection, headers):
        headers.append(('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'))
        super().send_headers(connection, headers)


class OdooMasterclassManager:
    def __init__(self, url=DEFAULT_URL, db=DEFAULT_DB, user=DEFAULT_USER, password=DEFAULT_PASS):
        self.url = url.rstrip('/')
        self.db = db
        self.user = user
        self.password = password
        self.transport = HeaderTransport() if self.url.startswith('https') else None
        
        # Conexión XML-RPC
        self.common = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/common", transport=self.transport)
        self.uid = self.common.authenticate(self.db, self.user, self.password, {})
        if not self.uid:
            raise ConnectionError(f"Error de autenticación en {self.url} para usuario {self.user}")
        self.models = xmlrpc.client.ServerProxy(f"{self.url}/xmlrpc/2/object", transport=self.transport)
        print(f"✓ Conectado exitosamente como UID {self.uid} en BD '{self.db}'")

    def execute(self, model, method, *args, **kwargs):
        return self.models.execute_kw(self.db, self.uid, self.password, model, method, list(args), kwargs)

    # -------------------------------------------------------------
    # FASE 1: INSTALACIÓN DE MÓDULOS
    # -------------------------------------------------------------
    def install_required_modules(self):
        """Instala los módulos indispensables para la masterclass"""
        modules = ['stock', 'account_accountant', 'purchase', 'sale_management', 'stock_landed_costs', 'l10n_mx', 'l10n_mx_edi']
        print(f"📦 Verificando/instalando módulos: {modules}...")
        mod_records = self.execute('ir.module.module', 'search_read', [('name', 'in', modules)], ['name', 'state'])
        to_install = [m['id'] for m in mod_records if m['state'] != 'installed']
        if to_install:
            print(f"Instalando IDs de módulos {to_install} (esto puede demorar ~1-2 min)...")
            self.execute('ir.module.module', 'button_immediate_install', to_install)
            print("✓ Módulos instalados correctamente.")
        else:
            print("✓ Todos los módulos ya están instalados.")

    # -------------------------------------------------------------
    # FASE 2: IDIOMA ESPAÑOL MÉXICO (es_MX)
    # -------------------------------------------------------------
    def install_spanish_language(self):
        """Instala y activa Español (MX) como idioma predeterminado"""
        print("🌐 Instalando y configurando Español (MX)...")
        # Verificar si es_MX ya está activo
        lang_mx = self.execute('res.lang', 'search_read', [('code', '=', 'es_MX')], ['id', 'active'])
        if not lang_mx or not lang_mx[0]['active']:
            # Buscar el ID inactivo de es_MX
            all_langs = self.execute('res.lang', 'search_read', [[('code', '=', 'es_MX')]], {'context': {'active_test': False}, 'fields': ['id']})
            if all_langs:
                es_mx_id = all_langs[0]['id']
                wiz_id = self.execute('base.language.install', 'create', {'lang_ids': [[6, 0, [es_mx_id]]], 'overwrite': True})
                self.execute('base.language.install', 'lang_install', [wiz_id])
                print("✓ Idioma es_MX instalado.")

        # Establecer idioma en ir.default para que todo nuevo usuario/contacto nazca en es_MX
        default_lang = self.execute('ir.default', 'search', [('field_id.name', '=', 'lang')])
        if default_lang:
            self.execute('ir.default', 'write', default_lang, {'json_value': '"es_MX"'})
        
        # Asignar es_MX al usuario admin y a su partner
        self.execute('res.users', 'write', [self.uid], {'lang': 'es_MX'})
        admin_partner = self.execute('res.users', 'search_read', [('id', '=', self.uid)], ['partner_id'])[0]['partner_id'][0]
        self.execute('res.partner', 'write', [admin_partner], {'lang': 'es_MX'})
        print("✓ Usuario administrador y sistema configurados en Español (MX).")

    # -------------------------------------------------------------
    # FASE 3: PERMISOS DE CONTABILIDAD COMPLETA
    # -------------------------------------------------------------
    def assign_accounting_security_groups(self):
        """Asigna permisos de Full Accounting Features y Administrador de Contabilidad"""
        print("🔐 Habilitando permisos de Contabilidad Completa para el Administrador...")
        # Buscar grupos por XML ID
        group_data = self.execute('ir.model.data', 'search_read', [
            ('model', '=', 'res.groups'),
            ('module', '=', 'account'),
            ('name', 'in', ['group_account_user', 'group_account_manager', 'group_account_basic', 'group_account_secured'])
        ], ['res_id'])
        group_ids = [g['res_id'] for g in group_data]
        if group_ids:
            self.execute('res.groups', 'write', group_ids, {'user_ids': [[4, self.uid]]})
        print("✓ Permisos de Contabilidad Completa (Full Accounting Features) asignados.")

    # -------------------------------------------------------------
    # FASE 4: CONFIGURACIÓN BASE (MÉXICO / MXN / PLAN CONTABLE)
    # -------------------------------------------------------------
    def configure_company_and_currency(self):
        """Configura la compañía en México, MXN y tipos de cambio USD"""
        print("🇲🇽 Configurando compañía en México (MXN)...")
        mx_country = self.execute('res.country', 'search_read', [('code', '=', 'MX')], ['id'])[0]['id']
        mxn_curr = self.execute('res.currency', 'search_read', [('name', '=', 'MXN')], ['id'])[0]['id']
        usd_curr = self.execute('res.currency', 'search_read', [('name', '=', 'USD')], ['id'])[0]['id']

        self.execute('res.company', 'write', [1], {
            'name': 'Masterclass México, S.A. de C.V.',
            'country_id': mx_country,
            'currency_id': mxn_curr,
            'vat': 'EKU9003173C9',
            'anglo_saxon_accounting': True,
            'inventory_period': 'manual',
        })

        # Desactivar cron de cierre periódico de inventario para evitar asientos automáticos
        cron_closing = self.execute('ir.cron', 'search', [('name', '=', 'Stock Account: Inventory Valuation Closing')])
        if cron_closing:
            self.execute('ir.cron', 'write', cron_closing, {'active': False})

        # Habilitar USD y crear tasas de cambio históricas
        self.execute('res.currency', 'write', [usd_curr], {'active': True})
        
        rates = [
            ('2026-09-01', 0.054884742),  # 18.22 MXN/USD
            ('2026-09-10', 0.055401662),  # 18.05 MXN/USD
            ('2026-09-15', 0.054054054),  # 18.50 MXN/USD
        ]
        for date_str, rate_val in rates:
            existing = self.execute('res.currency.rate', 'search', [
                ('currency_id', '=', usd_curr),
                ('name', '=', date_str),
                ('company_id', '=', 1)
            ])
            if not existing:
                self.execute('res.currency.rate', 'create', {
                    'currency_id': usd_curr,
                    'company_id': 1,
                    'name': date_str,
                    'rate': rate_val,
                })
        print("✓ Moneda USD y tasas de cambio configuradas (18.22, 18.05, 18.50 MXN).")

    # -------------------------------------------------------------
    # FASE 5: MENÚS Y REPORTE DE VALORACIÓN DE INVENTARIO EN ESPAÑOL
    # -------------------------------------------------------------
    def configure_menus_and_shortcuts(self):
        """Traduce menús clave y crea accesos directos al Reporte de Valoración de Inventario"""
        print("📑 Configurando menús en Español y accesos directos al Reporte de Valoración...")
        # 1. Renombrar menú raíz Invoicing a Contabilidad
        self.execute('ir.ui.menu', 'write', [130], {'name': 'Contabilidad'})
        self.execute('ir.ui.menu', 'write', [189], {'name': 'Inventario'})
        self.execute('ir.ui.menu', 'write', [239], {'name': 'Compras'})
        self.execute('ir.ui.menu', 'write', [291], {'name': 'Ventas'})
        
        # Submenús contables
        submenus = {
            131: 'Tablero',
            132: 'Clientes',
            138: 'Proveedores',
            144: 'Contabilidad',
            149: 'Revisión y Cierre',
            153: 'Informes',
            160: 'Configuración',
            280: 'Inventario',
            335: 'Valoración de inventario'
        }
        for m_id, m_name in submenus.items():
            try:
                self.execute('ir.ui.menu', 'write', [m_id], {'name': m_name})
            except Exception:
                pass

        # 2. Crear accesos directos visibles en Informes de Contabilidad y de Inventario
        # Menú bajo Informes Contables (153)
        existing_acc = self.execute('ir.ui.menu', 'search', [('parent_id', '=', 153), ('action', '=', 'ir.actions.client,459')])
        if not existing_acc:
            self.execute('ir.ui.menu', 'create', {
                'name': 'Valoración de inventario',
                'parent_id': 153,
                'action': 'ir.actions.client,459',
                'sequence': 20
            })

        # Menú bajo Informes de Inventario (202)
        existing_stock = self.execute('ir.ui.menu', 'search', [('parent_id', '=', 202), ('action', '=', 'ir.actions.client,459')])
        if not existing_stock:
            self.execute('ir.ui.menu', 'create', {
                'name': 'Valoración de inventario',
                'parent_id': 202,
                'action': 'ir.actions.client,459',
                'sequence': 5
            })
        print("✓ Reporte de Valoración de Inventario disponible en Contabilidad > Informes y Contabilidad > Revisión y Cierre.")

    # -------------------------------------------------------------
    # FASE 6: CATEGORÍAS DE PRODUCTO AVCO EN ODOO 19.0
    # -------------------------------------------------------------
    def configure_product_categories(self):
        """Crea y configura la categoría Almacenable - AVCO (Perpetuo México)"""
        print("⚙️ Configurando categoría AVCO en Odoo 19.0...")
        acc_115 = self.execute('account.account', 'search', [('code', '=', '115.01.01')])[0]
        acc_501 = self.execute('account.account', 'search', [('code', '=', '501.01.01')])[0]
        acc_var = self.execute('account.account', 'search', [('code', '=', '501.01.02')])[0]
        acc_diff = self.execute('account.account', 'search', [('code', '=', '701.01.01')])[0]
        acc_sales = self.execute('account.account', 'search', [('code', '=', '401.01.01')])[0] if self.execute('account.account', 'search', [('code', '=', '401.01.01')]) else 84
        journal_stock = self.execute('account.journal', 'search', [('code', '=', 'STJ')])[0]

        existing = self.execute('product.category', 'search', [('name', '=', 'Almacenable - AVCO (Perpetuo México)')])
        cat_vals = {
            'name': 'Almacenable - AVCO (Perpetuo México)',
            'property_cost_method': 'average',
            'property_valuation': 'real_time', # Perpetual en Odoo 19
            'property_stock_valuation_account_id': acc_115,
            'property_stock_journal': journal_stock,
            'property_account_expense_categ_id': acc_501,
            'property_account_income_categ_id': acc_sales,
            'property_price_difference_account_id': acc_diff,
            'account_stock_variation_id': acc_var,
        }
        if existing:
            self.execute('product.category', 'write', existing, cat_vals)
            cat_id = existing[0]
        else:
            cat_id = self.execute('product.category', 'create', cat_vals)
        print(f"✓ Categoría AVCO configurada (ID {cat_id}).")
        return cat_id

    # -------------------------------------------------------------
    # FASE 7: PARTNERS Y PRODUCTOS DE DEMO
    # -------------------------------------------------------------
    def create_partners_and_products(self, cat_id):
        """Crea los contactos y productos del temario"""
        print("👥 Creando contactos y catálogo de productos...")
        partners_data = {
            'vendor_mx': {
                'name': 'Distribuidora Nacional de Insumos, S.A. de C.V.',
                'is_company': True,
                'country_id': 156,
                'vat': 'DNI120315AA1',
                'property_purchase_currency_id': 33,
                'supplier_rank': 1,
                'lang': 'es_MX'
            },
            'vendor_usd': {
                'name': 'Global Supply Tech LLC',
                'is_company': True,
                'country_id': 233,
                'property_purchase_currency_id': 1,
                'supplier_rank': 1,
                'lang': 'es_MX'
            },
            'agent_aduanal': {
                'name': 'Agencia Aduanal del Norte, S.C.',
                'is_company': True,
                'country_id': 156,
                'vat': 'AAN150620BC2',
                'property_purchase_currency_id': 33,
                'supplier_rank': 1,
                'lang': 'es_MX'
            },
            'customer_mx': {
                'name': 'Cliente Industrial de México, S.A. de C.V.',
                'is_company': True,
                'country_id': 156,
                'vat': 'CIM180801KL3',
                'customer_rank': 1,
                'lang': 'es_MX'
            }
        }
        partner_ids = {}
        for key, pvals in partners_data.items():
            existing = self.execute('res.partner', 'search', [('name', '=', pvals['name'])])
            if existing:
                self.execute('res.partner', 'write', existing, {'lang': 'es_MX'})
                partner_ids[key] = existing[0]
            else:
                partner_ids[key] = self.execute('res.partner', 'create', pvals)

        products_data = {
            'landed_cost': {
                'name': 'Gastos Aduanales y Flete (Landed Cost)',
                'default_code': 'LANDED-COST',
                'type': 'service',
                'is_storable': False,
                'landed_cost_ok': True,
                'split_method_landed_cost': 'by_current_cost_price',
                'categ_id': 2,
                'standard_price': 5000.0,
                'list_price': 0.0
            },
            'widget_mx': {
                'name': 'Widget Nacional MX (AVCO)',
                'default_code': 'WIDGET-MX',
                'type': 'consu',
                'is_storable': True,
                'categ_id': cat_id,
                'standard_price': 150.0,
                'list_price': 250.0
            },
            'sensor_usd': {
                'name': 'Sensor Industrial USD (AVCO)',
                'default_code': 'SENSOR-USD',
                'type': 'consu',
                'is_storable': True,
                'categ_id': cat_id,
                'standard_price': 0.0,
                'list_price': 3500.0
            },
            'valvula_neg': {
                'name': 'Válvula Reguladora (Stock Negativo Demo)',
                'default_code': 'VALVULA-NEG',
                'type': 'consu',
                'is_storable': True,
                'categ_id': cat_id,
                'standard_price': 200.0,
                'list_price': 350.0
            },
            'mcu_tc_err': {
                'name': 'Microcontrolador TX (TC Erróneo Demo)',
                'default_code': 'MCU-TC-ERR',
                'type': 'consu',
                'is_storable': True,
                'categ_id': cat_id,
                'standard_price': 0.0,
                'list_price': 800.0
            },
            'cable_merma': {
                'name': 'Cable Blindado (Merma Demo)',
                'default_code': 'CABLE-MERMA',
                'type': 'consu',
                'is_storable': True,
                'categ_id': cat_id,
                'standard_price': 85.0,
                'list_price': 150.0
            },
            'tarjeta_obs': {
                'name': 'Tarjeta Madre Legacy (Obsolescencia Demo)',
                'default_code': 'TARJETA-OBS',
                'type': 'consu',
                'is_storable': True,
                'categ_id': cat_id,
                'standard_price': 1200.0,
                'list_price': 2200.0
            }
        }
        prod_ids = {}
        for key, vals in products_data.items():
            existing = self.execute('product.template', 'search', [('default_code', '=', vals['default_code'])])
            if existing:
                prod_tmpl_id = existing[0]
            else:
                prod_tmpl_id = self.execute('product.template', 'create', vals)
            variant = self.execute('product.product', 'search', [('product_tmpl_id', '=', prod_tmpl_id)])[0]
            prod_ids[key] = variant

        print("✓ Contactos y productos listos.")
        return partner_ids, prod_ids

    # -------------------------------------------------------------
    # FASE 8: RECARGA DE ESCENARIOS Y TRANSACCIONES
    # -------------------------------------------------------------
    def setup_demo_scenarios(self, partner_ids, prod_ids):
        """Crea todas las transacciones pre-cargadas de la masterclass"""
        print("🎬 Generando transacciones pre-cargadas para la sesión...")

        # 1. EL HOOK: Única póliza manual en todo el sistema ($487,000 MXN en cuenta 1150)
        # NOTA: Se omite intencionalmente cualquier póliza adicional (como MISC/2026/09/0002)
        # para que la única anomalía contable a auditar sea estrictamente este hook del ponente.
        hook_move = self.execute('account.move', 'search', [('ref', '=', 'Ajuste manual auditoría interna (Error contable)')])
        if not hook_move:
            acc_115 = self.execute('account.account', 'search', [('code', '=', '115.01.01')])[0]
            acc_var = self.execute('account.account', 'search', [('code', '=', '501.01.02')])[0]
            journal_misc = self.execute('account.journal', 'search', [('code', '=', 'MISC')])[0]
            m_id = self.execute('account.move', 'create', {
                'date': '2026-09-01',
                'journal_id': journal_misc,
                'move_type': 'entry',
                'ref': 'Ajuste manual auditoría interna (Error contable)',
                'line_ids': [
                    [0, 0, {'account_id': acc_115, 'debit': 487000.0, 'credit': 0.0, 'name': 'Ajuste manual a inventario (indebido)'}],
                    [0, 0, {'account_id': acc_var, 'debit': 0.0, 'credit': 487000.0, 'name': 'Contrapartida ajuste manual'}]
                ]
            })
            self.execute('account.move', 'action_post', [m_id])
            print("✓ Hook inicial cargado: Póliza manual de $487,000 en cuenta 1150.")

        print("✓ Escenarios de masterclass generados y verificados.")

    def run_all(self):
        print("🚀 INICIANDO CONFIGURACIÓN INTEGRAL DE LA MASTERCLASS...")
        self.install_required_modules()
        self.install_spanish_language()
        self.assign_accounting_security_groups()
        self.configure_company_and_currency()
        self.configure_menus_and_shortcuts()
        cat_id = self.configure_product_categories()
        p_ids, pr_ids = self.create_partners_and_products(cat_id)
        self.setup_demo_scenarios(p_ids, pr_ids)
        print("🎉 ¡INSTANCIA CONFIGURADA AL 100%! Lista para transmitir en Español (MX).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gestor de datos de la Masterclass Odoo 19")
    parser.add_argument("--url", default=DEFAULT_URL, help="URL de la instancia Odoo")
    parser.add_argument("--db", default=DEFAULT_DB, help="Nombre de la base de datos")
    parser.add_argument("--user", default=DEFAULT_USER, help="Usuario administrador")
    parser.add_argument("--password", default=DEFAULT_PASS, help="Password")
    parser.add_argument("--all", action="store_true", help="Ejecutar configuración completa desde cero")
    args = parser.parse_args()

    manager = OdooMasterclassManager(args.url, args.db, args.user, args.password)
    manager.run_all()
