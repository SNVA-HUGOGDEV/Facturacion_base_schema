from odoo import fields, models

class AccountPaymentMean(models.Model):
    _name = 'account.payment.mean'
    _description = 'Ways to pay'
    name = fields.Char(string='Name', required=False, translate=True)
    code = fields.Char(string='Code', required=False)