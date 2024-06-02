from odoo.addons.product_in_box.tests.common import ProductInBoxCommon
from odoo.tests import tagged


@tagged(
    "post_install",
    "-at_install",
)
class TestProductInBox(ProductInBoxCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass()

    def test_01_crear_orden_venta(self):
        so = self._create_sale_order({"product_id": self.product})
        self.assertEqual(so.order_line.product_uom_qty, 1)
        self.assertEqual(so.order_line.name, "product normal Total 0.00 na")
