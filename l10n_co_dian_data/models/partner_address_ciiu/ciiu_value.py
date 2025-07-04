from odoo import fields, models

class CiiuValue(models.Model):
    _name = 'ciiu.value'
    _description = 'CIIU Optional Value'
    _rec_name = 'code'
    code = fields.Char(required=False)
    name = fields.Char(string='Description', required=False)
    company_id = fields.Many2one('res.company', string='Company', change_default=True, required=False)