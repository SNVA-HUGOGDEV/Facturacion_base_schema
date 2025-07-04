from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    hide_discount = fields.Boolean(string='Ocultar descuento', readonly=False, related='company_id.hide_discount')
    hide_uom = fields.Boolean(string='Ocultar unidad de medida', readonly=False, related='company_id.hide_uom')
    hide_iva = fields.Boolean(string='Ocultar IVA', readonly=False, related='company_id.hide_iva')
    report_header_info = fields.Text(string='Información de encabezado', readonly=False, related='company_id.report_header_info')