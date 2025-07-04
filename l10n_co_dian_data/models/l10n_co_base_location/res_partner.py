from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    zip_id = fields.Many2one('res.city.zip', 'ZIP Location')
    country_code = fields.Char(related='country_id.code', store=False)