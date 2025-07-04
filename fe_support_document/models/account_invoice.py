from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    operation_type_supplier = fields.Selection([('10', 'Residente'), ('11', 'No Residente')], string='Operation Type', default='10')