from odoo import models, fields, api, _, exceptions, tools

class rohit(models.Model):
    _name = 'rohit'

    name = fields.Char(string='Name', required=True, )
    fame = fields.Char(string='Fame' )



print("rohit")