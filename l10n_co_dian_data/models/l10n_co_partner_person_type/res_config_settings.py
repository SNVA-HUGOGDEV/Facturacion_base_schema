import logging
from odoo import fields, models
_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    partner_names_order = fields.Selection(string='Partner names order', selection=[], help='Order to compose partner fullname', config_parameter='partner_names_order', required=False)
    partner_names_order_changed = fields.Boolean(config_parameter='partner_names_order_changed')