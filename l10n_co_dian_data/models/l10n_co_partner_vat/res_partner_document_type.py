from odoo import fields, models

class ResPartnerDocumentType(models.Model):
    _name = 'res.partner.document.type'
    _description = 'Partner Document Type'
    name = fields.Char(string='Document Type', size=100, required=False)
    code = fields.Char(string='Code', size=2, required=False)
    checking_required = fields.Boolean(string='VAT Check Required', default=False)
    active = fields.Boolean(default=True)