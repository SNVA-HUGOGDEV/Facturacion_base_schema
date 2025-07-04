import sys
import importlib
importlib.reload(sys)
from odoo import models
import logging
_logger = logging.getLogger(__name__)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
DIAN = {'wsdl-hab': 'https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?wsdl', 'wsdl': 'https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?wsdl', 'catalogo-hab': 'https://catalogo-vpfe-hab.dian.gov.co/Document/FindDocument?documentKey={}&partitionKey={}&emissionDate={}', 'catalogo': 'https://catalogo-vpfe.dian.gov.co/Document/FindDocument?documentKey={}&partitionKey={}&emissionDate={}'}

class AccountInvoiceDianDocument(models.Model):
    _inherit = 'account.invoice.dian.document'