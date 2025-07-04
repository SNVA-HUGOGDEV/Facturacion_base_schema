from odoo import fields, models

class AccountFiscalPositionTaxScheme(models.Model):
    _name = 'account.fiscal.position.tax.scheme'
    _description = 'Tributos'
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')