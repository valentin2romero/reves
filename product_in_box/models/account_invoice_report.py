from openerp import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    in_box_qty = fields.Float(
        string="m/m2",
    )

    def _select(self):
        return (
            super()._select()
            + """
            ,line.in_box_qty
            """
        )
