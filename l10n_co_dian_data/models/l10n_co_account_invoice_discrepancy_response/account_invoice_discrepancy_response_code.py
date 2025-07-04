from odoo import fields, models

class AccountInvoiceDiscrepancyResponseCode(models.Model):
    _name = 'account.invoice.discrepancy.response.code'
    _description = 'Conceptos de corrección para notas Crédito y Débito'
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    type = fields.Selection([('credit', 'Credit Note'), ('debit', 'Debit Note')], string='Type')