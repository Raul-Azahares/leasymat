from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    woo_payment_method = fields.Char(string="WooCommerce Payment Method")
    woo_installments = fields.Integer(string="Installments")
