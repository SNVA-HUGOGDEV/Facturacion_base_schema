from odoo import fields, models

class StreetCode(models.Model):
    _name = 'street.code'
    _description = 'Street Code'
    _rec_name = 'name'
    code = fields.Char(required=False)
    name = fields.Char(string='Description', required=False)
    company_id = fields.Many2one('res.company', string='Company', change_default=True, required=False)