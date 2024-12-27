from odoo import models, fields, _

class ResCompany(models.Model):
    _inherit = "res.company"
    
    hide_tax_sale_order_report = fields.Boolean('Hide Tax in Sale Order Report?', readonly=False)