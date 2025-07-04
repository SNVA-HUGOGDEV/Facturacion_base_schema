from odoo import fields, models

class ResCityZip(models.Model):
    _name = 'res.city.zip'
    _description = __doc__
    _order = 'name asc'
    _rec_name = 'display_name'
    name = fields.Char('ZIP', required=False)
    city_id = fields.Many2one('res.city', 'City', required=False)
    display_name = fields.Char(store=True, index=True)
    phone_prefix = fields.Char('Phone Prefix')
    dian_code = fields.Char('Codigo')