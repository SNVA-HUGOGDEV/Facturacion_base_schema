from odoo import fields, models

class AccountJournal(models.Model):
    _inherit = 'account.journal'
    sequence_id = fields.Many2one('ir.sequence', string='Entry Sequence', help='This field contains the information related to the numbering of the journal entries of this journal.', required=False, copy=False)
    sequence_number_next = fields.Integer(string='Next Number', help='The next sequence number will be used for the next invoice.')
    refund_sequence_id = fields.Many2one('ir.sequence', string='Credit Note Entry Sequence', help='This field contains the information related to the numbering of the credit note entries of this journal.', copy=False)
    refund_sequence_number_next = fields.Integer(string='Credit Notes Next Number', help='The next sequence number will be used for the nextcredit note.')