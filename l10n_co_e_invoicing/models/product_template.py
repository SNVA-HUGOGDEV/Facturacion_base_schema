from odoo import models, fields
import odoo.addons.decimal_precision as dp

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    margin_percentage = fields.Float(string='Margin Percentage', help='The cost price + this percentage will be the reference price', digits=dp.get_precision('Discount'), default=10)
    reference_price = fields.Float(string='Reference Price', help='use this field if the reference price does not depend on the cost price', digits=dp.get_precision('Product Price'))
    product_scheme_id = fields.Many2one(comodel_name='product.scheme', string='Product Scheme')
    product_scheme_code = fields.Char(string='Standard code')
    brand_name = fields.Char(string='Brand name')
    model_name = fields.Char(string='Model name')