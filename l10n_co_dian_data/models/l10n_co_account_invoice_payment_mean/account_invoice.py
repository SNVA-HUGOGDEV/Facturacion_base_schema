from odoo import fields, models

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    payment_mean_id = fields.Many2one(comodel_name='account.payment.mean', string='Payment Method', copy=False, default=False)
    payment_mean_code_id = fields.Many2one('account.payment.mean.code', string='Mean of Payment', copy=False)
    invoice_date = fields.Date(default=fields.Date.today())