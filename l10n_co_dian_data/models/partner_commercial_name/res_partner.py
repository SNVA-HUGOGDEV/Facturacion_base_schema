from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    commercial_name = fields.Char(string='Commercial Name')