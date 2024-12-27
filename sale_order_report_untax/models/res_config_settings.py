# -*- coding: utf-8 -*-
from odoo import models, fields, api,_

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    hide_tax_sale_order_report = fields.Boolean('Hide Tax in Sale Order Report?', related="company_id.hide_tax_sale_order_report", readonly=False)