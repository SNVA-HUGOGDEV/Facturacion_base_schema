from odoo import fields, models
alphabet = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('Ñ', 'Ñ'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')]

class ResPartner(models.Model):
    _inherit = 'res.partner'
    field_1 = fields.Many2one('address.code')
    field_2 = fields.Char()
    field_3 = fields.Selection(alphabet)
    field_4 = fields.Many2one('street.code')
    field_5 = fields.Char()
    field_6 = fields.Selection(alphabet)
    field_7 = fields.Many2one('street.code')
    field_8 = fields.Char()
    field_9 = fields.Many2one('address.code')
    field_10 = fields.Char()
    field_11 = fields.Many2one('address.code')
    field_12 = fields.Char()
    ciiu = fields.Many2many('ciiu.value', 'ciiu_value_res_partner_rel', 'partner_id', 'ciiu_id', string='CIIU')