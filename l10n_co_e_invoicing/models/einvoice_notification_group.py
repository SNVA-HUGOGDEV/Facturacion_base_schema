from odoo import fields, models

class EInvoiceNotificationGroup(models.Model):
    _name = 'einvoice.notification.group'
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    company_id = fields.Many2one(comodel_name='res.company', string='Company')