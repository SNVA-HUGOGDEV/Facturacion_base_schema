from odoo import fields, models

class AccountPaymentMeanCode(models.Model):
    _name = 'account.payment.mean.code'
    _description = 'Payment methods'
    name = fields.Char(string='Name', required=False, translate=True)
    code = fields.Char(string='Code', required=False)