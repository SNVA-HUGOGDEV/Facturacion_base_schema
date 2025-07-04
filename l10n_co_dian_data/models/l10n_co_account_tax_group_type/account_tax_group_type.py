from odoo import fields, models

class AccountTaxGroupType(models.Model):
    _name = 'account.tax.group.type'
    _description = 'Tributes'
    code = fields.Char(string='Code', required=False)
    name = fields.Char(string='Name', required=False)
    type = fields.Selection([('tax', 'Tax'), ('withholding_tax', 'Withholding Tax')], string='Type', required=False, default=False)
    description = fields.Char(string='Description')