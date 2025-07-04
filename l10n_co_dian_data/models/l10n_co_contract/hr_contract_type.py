from odoo import models, fields

class HrContractType(models.Model):
    _inherit = 'hr.contract.type'
    dian_contract_type = fields.Selection(string='Tipo de contrato DIAN', selection=[('1', 'Termino Fijo'), ('2', 'Termino Indefinido'), ('3', 'Obra o Labor'), ('4', 'Aprendizaje'), ('5', 'Practicas o Pasantias')], required=False)