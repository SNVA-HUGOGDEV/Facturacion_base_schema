from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)

class HrContract(models.Model):
    _inherit = 'hr.contract'
    salario_integral = fields.Boolean(string='Salario Integral')