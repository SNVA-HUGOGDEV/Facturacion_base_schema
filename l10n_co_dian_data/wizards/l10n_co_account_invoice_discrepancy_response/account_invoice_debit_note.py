from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)

class AccountInvoiceDebitNote(models.TransientModel):
    _name = 'account.invoice.debit.note'
    _description = 'Debit Note'
    date_invoice = fields.Date(string='Debit Note Date', default=fields.Date.context_today, required=False)
    date = fields.Date(string='Accounting Date')
    description = fields.Char(string='Reason', required=False)
    discrepancy_response_code_id = fields.Many2one(comodel_name='account.invoice.discrepancy.response.code', string='Correction concept for Refund Invoice')
    filter_debit_note = fields.Selection([('debit', 'Create a draft debit note')], default='debit', string='Debit Note Method', required=False, help='Debit Note base on this type. You can not Modify and Cancel if the invoice is already reconciled')
    reason = fields.Char(string='Reason')