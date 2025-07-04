from odoo import fields, models
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'
    document_type_id = fields.Many2one(string='Document Type', comodel_name='res.partner.document.type')
    document_type_code = fields.Char(related='document_type_id.code', store=False)
    check_digit = fields.Char(string='Verification Digit', size=1)
    identification_document = fields.Char('Identification Document')