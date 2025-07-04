from odoo import fields, models

class AccountPayment(models.Model):
    _inherit = 'account.payment'
    name = fields.Char(readonly=False, copy=False, default='/')