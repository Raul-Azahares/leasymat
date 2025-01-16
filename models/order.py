from odoo import models, fields,api
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #payment_method = fields.Char(string="WooCommerce Payment Method")
    installments = fields.Integer(string="Installments",required=False,readonly=False, help="Number of installments the customer will pay for this order",
                                  default=1)
    financing_duration = fields.Integer(
        string='Financing Duration (Months)',
        help='Duration of the financing contract in months.'
    )
    financing_start_date = fields.Date(
        string='Start Date',
        help='Start date of the financing contract.'
    )
    financing_end_date = fields.Date(
        string='End Date',
        compute='_compute_financing_end_date',
        store=True,
        help='End date of the financing contract, calculated based on the start date and duration.'
    )
    @api.depends('financing_start_date', 'financing_duration')
    def _compute_financing_end_date(self):
        for order in self:
            if order.financing_start_date and order.financing_duration:
                order.financing_end_date = order.financing_start_date + timedelta(days=order.financing_duration * 30)
            else:
                order.financing_end_date = False
