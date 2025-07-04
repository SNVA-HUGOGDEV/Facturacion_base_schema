from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'
    city_id = fields.Many2one('res.city', string='City ID')
    zip_id = fields.Many2one('res.city.zip', string='ZIP Location', help='Use the city name or the zip code to search the location')
    country_enforce_cities = fields.Boolean(related='partner_id.country_id.enforce_cities')