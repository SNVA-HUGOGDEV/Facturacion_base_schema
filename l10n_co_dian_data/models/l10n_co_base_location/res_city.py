from odoo import fields, models

class City(models.Model):
    _inherit = 'res.city'
    zip_ids = fields.One2many('res.city.zip', 'city_id', string='Zips in this city')