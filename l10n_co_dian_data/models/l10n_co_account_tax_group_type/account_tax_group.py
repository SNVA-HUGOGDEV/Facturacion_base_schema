from odoo import fields, models

class AccountTaxGroup(models.Model):
    _inherit = 'account.tax.group'
    tax_group_type_id = fields.Many2one(string='Tax Group Type', comodel_name='account.tax.group.type')