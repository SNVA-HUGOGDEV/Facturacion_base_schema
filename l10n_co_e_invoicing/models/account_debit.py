from odoo import models
import logging
_logger = logging.getLogger(__name__)

class AccountDebitNote(models.TransientModel):
    _name = 'account.debit.note'
    _description = 'Add Debit Note wizard'
    _inherit = 'account.debit.note'