from odoo import fields, models

class AccountFiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'
    listname = fields.Selection([('48', 'Impuesto sobre las ventas – IVA'), ('49', 'No responsable de IVA')], string='Fiscal Regime', default=False)