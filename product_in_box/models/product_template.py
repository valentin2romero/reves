from openerp import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    prod_in_box = fields.Float(
        "Cant. de producto por caja",
        help="Cantidad de metros cuadrados o lineales que entran en una caja",
    )
    prod_in_box_uom = fields.Selection(
        [
            ("na", "N/D"),
            ("mt", "mt"),
            ("mt2", "mt2"),
        ],
        "Unidad",
        required=True,
        default="na",
    )

    @api.constrains("prod_in_box_uom")
    def check_prod_in_box(self):
        for rec in self:
            if rec.prod_in_box_uom == "na":
                rec.prod_in_box = 0
