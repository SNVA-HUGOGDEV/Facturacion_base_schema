from odoo import fields, models

class ProductUomCode(models.Model):
    _name = 'product.uom.code'
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')