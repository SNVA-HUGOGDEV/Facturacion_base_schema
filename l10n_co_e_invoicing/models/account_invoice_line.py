from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'
    valor_en_pesos = fields.Float(string='Valor en Pesos', store=True)