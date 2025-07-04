from odoo import fields, models

class AccountTaxGroup(models.Model):
    _inherit = 'account.tax'
    show_in_report = fields.Boolean(string='Mostrar en reporte', default=True)