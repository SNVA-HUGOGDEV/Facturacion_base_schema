from odoo import models, fields

class AccountInvoiceRefund(models.TransientModel):
    _inherit = 'account.move.reversal'
    discrepancy_response_code_id = fields.Many2one(comodel_name='account.invoice.discrepancy.response.code', string='Correction concept for Refund Invoice')