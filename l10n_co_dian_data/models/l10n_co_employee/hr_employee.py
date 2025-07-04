from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    payment_method_id = fields.Many2one(string='Método de pago', comodel_name='payroll.metodo.pago')
    bank_name = fields.Char(string='Banco')
    account_type = fields.Selection(string='Tipo de cuenta', selection=[('corriente', 'Corriente'), ('ahorros', 'Ahorros')], default=False)
    account_number = fields.Char(string='Número de cuenta')
    employee_type_dian = fields.Selection(string='Tipo de empleado DIAN', selection=[('01', 'Dependiente'), ('02', 'Servicio domestico'), ('04', 'Madre comunitaria'), ('12', 'Aprendices del Sena en etapa lectiva'), ('18', 'Funcionarios públicos sin tope máximo de ibc'), ('19', 'Aprendices del SENA en etapa productiva'), ('21', 'Estudiantes de postgrado en salud'), ('22', 'Profesor de establecimiento particular'), ('23', 'Estudiantes aportes solo riesgos laborales'), ('30', 'Dependiente entidades o universidades públicas con régimen especial en salud'), ('31', 'Cooperados o pre cooperativas de trabajo asociado'), ('47', 'Trabajador dependiente de entidad beneficiaria del sistema general de participaciones'), ('51', 'Trabajador de tiempo parcial'), ('54', 'Pre pensionado de entidad en liquidación.'), ('56', 'Pre pensionado con aporte voluntario a salud'), ('58', 'Estudiantes de prácticas laborales en el sector público')], required=False)
    employee_subtype_dian = fields.Selection(string='Subtipo de empleado DIAN', selection=[('00', 'No Aplica'), ('01', 'Dependiente pensionado por vejez activo')], required=False)
    high_pension_risk = fields.Boolean(string='Alto riesgo pensional', default=False)
    country_id = fields.Many2one('res.country', 'Nacionalidad (País)', groups='hr.group_hr_user', readonly=False, related='address_id.country_id')
    state_id = fields.Many2one('res.country.state', 'Departamento', groups='hr.group_hr_user', readonly=False, related='address_id.state_id')
    city_id = fields.Many2one(string='Ciudad', comodel_name='res.city', related='address_id.city_id', readonly=False)