from openerp import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # Sobreescribimos para quitarle el required
    product_uom_qty = fields.Float(
        string="Quantity",
        digits="Product Unit of Measure",
        required=False,
        default=1.0,
    )
    in_box_qty = fields.Float(
        string="m/m2",
        digits="Product Unit of Measure",
    )
    prod_in_box = fields.Float(
        string="m2 x caja",
        related="product_id.product_tmpl_id.prod_in_box",
        readonly=True,
    )
    prod_in_box_uom = fields.Selection(
        related="product_id.product_tmpl_id.prod_in_box_uom",
        help="Campo tecnico para mostrar u ocultar metros por caja en la linea de "
        "presupuesto",
    )

    @api.onchange("product_uom_qty")
    def onchange_product_uom_qty(self):
        for rec in self:
            if rec.prod_in_box_uom != "na":
                rec.in_box_qty = rec.product_uom_qty * rec.prod_in_box
            else:
                rec.in_box_qty = 0

    @api.onchange("in_box_qty")
    def onchange_in_box_qty(self):
        for rec in self:
            if rec.prod_in_box_uom != "na":
                qty = rec.in_box_qty / rec.prod_in_box if rec.prod_in_box else 0
                frac = qty - int(qty)
                if frac != 0:
                    qty += 1
                rec.product_uom_qty = int(qty)
            else:
                rec.product_uom_qty = 1

    def _prepare_invoice_line(self):
        """Sobreescribimos este método para agregar los campos relacionados con la
            cantidad de producto por caja

        Prepare the dict of values to create the new invoice line for a sales order
        line.
        :param qty: float quantity to invoice
        """
        res = super()._prepare_invoice_line()
        res["in_box_qty"] = self.in_box_qty

        return res

    def _compute_amount(self):
        """Sobreescribimos este método para agregar la cantidad en caja en las lineas
        de producto"""

        for line in self:
            line.name = "%s Total %.2f %s" % (
                line.product_id.name,
                line.product_id.prod_in_box * line.product_uom_qty,
                line.product_id.prod_in_box_uom,
            )

        return super()._compute_amount()
