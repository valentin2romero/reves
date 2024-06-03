from odoo.tests import tagged
from odoo.tests.common import Form

from .common import ProductInBoxCommon


@tagged(
    "post_install",
    "-at_install",
)
class TestProductInBox(ProductInBoxCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass()

    def test_01_crear_orden_venta(self):
        data = [
            {
                "product_id": self.product,
            }
        ]
        so = self._create_sale_order(data)
        self.assertEqual(so.order_line.product_uom_qty, 1)
        self.assertEqual(so.order_line.name, "producto normal Total 0.00 na")

    def test_02_crear_orden_venta_m(self):
        data = [
            {
                "product_id": self.product_m,
                "prod_in_box_uom": "mt",
                "in_box_qty": 2.3,
                "price_unit": 10,
            }
        ]
        so = self._create_sale_order(data)
        self.assertEqual(so.order_line.product_uom_qty, 1)
        self.assertEqual(so.order_line.name, "product metros Total 3.50 mt")

    def test_03_crear_orden_venta_m2(self):
        data = [
            {
                "product_id": self.product_m,
                "prod_in_box_uom": "mt2",
                "in_box_qty": 4.1,
                "price_unit": 10,
            }
        ]
        so = self._create_sale_order(data)
        self.assertEqual(so.order_line.product_uom_qty, 1)
        self.assertEqual(so.order_line.name, "product metros Total 3.50 mt")

    def test_04_crear_orden_venta_m2(self):
        data = [
            {
                "product_id": self.product_m,
                "prod_in_box_uom": "mt2",
                "in_box_qty": 4.1,
                "price_unit": 10,
            }
        ]
        so = self._create_sale_order(data)
        self.assertEqual(so.order_line.product_uom_qty, 1)
        self.assertEqual(so.order_line.name, "product metros Total 3.50 mt")

        with Form(self.env["sale.advance.payment.inv"]) as inv_wizard:
            inv_wizard.advance_payment_method = "delivered"
            _ = inv_wizard.save()
            _.create_invoices()

        inv = self.env["account.move"].search([("invoice_origin", "=", so.name)])
