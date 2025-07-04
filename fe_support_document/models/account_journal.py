from odoo import fields, models

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    is_support_document = fields.Boolean(string='Documento Soporte?')