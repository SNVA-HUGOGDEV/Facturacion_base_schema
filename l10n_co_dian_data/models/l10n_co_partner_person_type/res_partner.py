import logging
from odoo import fields, models
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'
    firstname = fields.Char('Primer Nombre', index=True)
    lastname = fields.Char('Last name', index=True)
    lastname2 = fields.Char('Second last name')
    othernames = fields.Char('Other Names')
    name_intermediate = fields.Char('Name Intermediate', store=True)
    name = fields.Char(required=False, store=True, readonly=False)
    person_type = fields.Selection([('1', 'Juridical Person and assimilated'), ('2', 'Natural Person and assimilated')], string='Person Type')
    same_identification_document_partner_id = fields.Many2one('res.partner', string='Partner with same identification document', store=False)