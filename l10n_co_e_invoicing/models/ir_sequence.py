from odoo import fields, models, _

class IrSequence(models.Model):
    _inherit = 'ir.sequence'
    dian_type = fields.Selection(selection_add=[('e-invoicing', _('E-Invoicing'))])