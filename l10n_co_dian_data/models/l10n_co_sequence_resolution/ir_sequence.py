from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)

class IrSequence(models.Model):
    _inherit = 'ir.sequence'
    use_dian_control = fields.Boolean(string='Use DIAN Resolutions Control?')
    remaining_numbers = fields.Integer(string='Remaining Numbers', default=False)
    remaining_days = fields.Integer(string='Remaining Days', default=False)
    dian_type = fields.Selection([('computer_generated_invoice', 'Computer Generated Invoice'), ('pos_invoice', 'POS Invoice')], string='DIAN Type')