from odoo import fields, models

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    discrepancy_response_code_id = fields.Many2one(comodel_name='account.invoice.discrepancy.response.code', string='Correction concept for Refund Invoice')
    refund_type = fields.Selection([('debit', 'Debit Note'), ('credit', 'Credit Note')], index=True, string='Refund Type', track_visibility='always')
    debit_origin_id = fields.Many2one('account.move', 'Factura Debitada', readonly=False, copy=False)
    debit_note_ids = fields.One2many('account.move', 'debit_origin_id', 'Notas Débito', help='Las notas débito creadas a esta factura')
    debit_note_count = fields.Integer('Número de notas débito')