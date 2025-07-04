from odoo import fields, models

class AccountFiscalPositionTaxLevelCode(models.Model):
    _name = 'account.fiscal.position.tax.level.code'
    _description = 'Fiscal Responsibilities'
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')