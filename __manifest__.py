# __manifest__.py
{
    'name': 'Custom WooCommerce API2',
    'version': '1.0',
    'category': 'Custom',
    'author': 'Tu Nombre',
    'description': 'Módulo para integrar WooCommerce con Odoo a través de una API personalizada.',
    'depends': ['base','sale'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
