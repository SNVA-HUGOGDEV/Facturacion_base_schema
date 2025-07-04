from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    warn_remaining = fields.Boolean(string='Warn About Remainings?', store=False)
    warn_inactive_resolution = fields.Boolean(string='Warn About Inactive Resolution?', store=False)
    einv_available_numbers = fields.Integer(string='Números disponibles', store=False)
    einv_available_days = fields.Integer(string='Días disponibles', store=False)