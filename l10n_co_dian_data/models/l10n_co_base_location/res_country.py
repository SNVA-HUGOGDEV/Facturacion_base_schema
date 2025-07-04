from odoo import models, fields

class ResCountry(models.Model):
    _inherit = 'res.country'
    code_dian = fields.Char('Code DIAN')