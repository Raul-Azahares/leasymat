from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #payment_method = fields.Char(string="WooCommerce Payment Method")
    installments = fields.Integer(string="Installments",required=False,readonly=False, help="Number of installments the customer will pay for this order",
                                  default=1)
