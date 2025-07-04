from odoo import fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'
    name = fields.Char(string='Number', required=False, readonly=False, copy=False, default='/')