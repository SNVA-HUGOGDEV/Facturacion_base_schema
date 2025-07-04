import sys
import importlib
importlib.reload(sys)
from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
DIAN = {'wsdl-hab': 'https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?wsdl', 'wsdl': 'https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?wsdl', 'catalogo-hab': 'https://catalogo-vpfe-hab.dian.gov.co/Document/FindDocument?documentKey={}&partitionKey={}&emissionDate={}', 'catalogo': 'https://catalogo-vpfe.dian.gov.co/Document/FindDocument?documentKey={}&partitionKey={}&emissionDate={}'}

class AccountMoveDianDocument(models.Model):
    _name = 'account.invoice.dian.document'
    _inherit = ['mail.thread']
    state = fields.Selection([('draft', 'Draft'), ('sent', 'Sent'), ('done', 'Done'), ('cancel', 'Cancel')], string='State', readonly=False, default='draft')
    invoice_id = fields.Many2one('account.move', string='Invoice')
    company_id = fields.Many2one('res.company', string='Company')
    invoice_url = fields.Char(string='Invoice Url')
    cufe_cude_uncoded = fields.Char(string='CUFE/CUDE Uncoded')
    cufe_cude = fields.Char(string='CUFE/CUDE')
    origin_cufe_cude = fields.Char(string='CUFE/CUDE original')
    software_security_code_uncoded = fields.Char(string='SoftwareSecurityCode Uncoded')
    software_security_code = fields.Char(string='SoftwareSecurityCode')
    xml_filename = fields.Char(string='XML Filename')
    xml_file = fields.Binary(string='XML File')
    zipped_filename = fields.Char(string='Zipped Filename')
    zipped_file = fields.Binary(string='Zipped File')
    exp_accepted_file = fields.Binary(string='Explicit Accepted File')
    zip_key = fields.Char(string='ZipKey')
    mail_sent = fields.Boolean(string='Mail Sent?')
    ar_xml_filename = fields.Char(string='ApplicationResponse XML Filename')
    ar_xml_file = fields.Binary(string='ApplicationResponse XML File')
    get_status_zip_status_code = fields.Selection([('00', 'Procesado Correctamente'), ('66', 'NSU no encontrado'), ('90', 'TrackId no encontrado'), ('99', 'Validaciones contienen errores en campos mandatorios'), ('other', 'Other')], string='StatusCode', default=False)
    get_status_zip_response = fields.Text(string='Response')
    qr_image = fields.Binary('QR Code')
    dian_document_line_ids = fields.One2many('account.invoice.dian.document.line', 'dian_document_id', string='DIAN Document Lines')
    profile_execution_id = fields.Selection(string='Destination Environment of Document', related='company_id.profile_execution_id', store=False)
    type_account = fields.Selection([('debit', 'Debit Note'), ('credit', 'Credit Note'), ('support_document', 'Documento Soporte'), ('invoice', 'Invoice')])