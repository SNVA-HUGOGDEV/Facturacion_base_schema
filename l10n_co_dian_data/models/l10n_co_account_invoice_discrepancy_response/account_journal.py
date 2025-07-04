from odoo import models, fields

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    debit_note_sequence = fields.Boolean(string='Dedicated Debit Note Sequence', help="Check this box if you don't want to share the same sequence for invoices and debit notes made from this journal", default=False)
    debit_note_sequence_id = fields.Many2one(comodel_name='ir.sequence', string='Debit Note Entry Sequence', help='This field contains the information related to the numbering of the debit note entries of this journal.', copy=False)
    debit_note_sequence_number_next = fields.Integer(string='Debit Notes Next Number', help='The next sequence number will be used for the next Debit note.')