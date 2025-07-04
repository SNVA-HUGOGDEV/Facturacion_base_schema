from odoo import models, fields
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class ResCompany(models.Model):
    _inherit = 'res.company'
    einvoicing_enabled = fields.Boolean(string='E-Invoicing Enabled')
    out_invoice_sent = fields.Integer(string='out_invoice Sent')
    out_refund_sent = fields.Integer(string='out_refund Sent')
    in_refund_sent = fields.Integer(string='in_refund Sent')
    profile_execution_id = fields.Selection([('1', 'Production'), ('2', 'Test')], 'Destination Environment of Document', default='2', required=False)
    test_set_id = fields.Char(string='Test Set Id')
    software_id = fields.Char(string='Software Id')
    software_pin = fields.Char(string='Software PIN')
    certificate_filename = fields.Char(string='Certificate Filename')
    certificate_file = fields.Binary(string='Certificate File')
    certificate_password = fields.Char(string='Certificate Password')
    signature_policy_url = fields.Char(string='Signature Policy Url')
    signature_policy_description = fields.Char(string='Signature Policy Description')
    signature_policy_filename = fields.Char(string='Signature Policy Filename')
    signature_policy_file = fields.Binary(string='Signature Policy File')
    files_path = fields.Char(string='Files Path')
    einvoicing_email = fields.Char(string='E-invoice Email From', help="Enter the e-invoice sender's email.")
    einvoicing_partner_no_email = fields.Char(string='Failed Emails To', help='Enter the email where the invoice will be sent when the customer does not have an email.')
    report_template = fields.Many2one(string='Report Template', comodel_name='ir.actions.report')
    notification_group_ids = fields.One2many(comodel_name='einvoice.notification.group', inverse_name='company_id', string='Notification Group')
    get_numbering_range_response = fields.Text(string='GetNumberingRange Response')
    tributary_information = fields.Text(string='Información Tributaria')
    remaining_days_pfx = fields.Integer(string='Días alerta vencimiento certificado', default='20')
    date_due_pfx = fields.Date(string='Vencimiento Certificado')