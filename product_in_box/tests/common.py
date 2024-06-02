# Part of Odoo. See LICENSE file for full copyright and licensing details.
import time

from odoo.addons.account.tests.common import AccountTestInvoicingCommon
from odoo.tests.common import Form


class ProductInBoxCommon(AccountTestInvoicingCommon):

    @classmethod
    def setUpClass(cls, chart_template_ref="l10n_ar.l10nar_ri_chart_template"):
        super().setUpClass(chart_template_ref=chart_template_ref)

        # ==== Company ====
        cls.company_data["company"].write(
            {
                "parent_id": cls.env.ref("base.main_company").id,
                "currency_id": cls.env.ref("base.ARS").id,
                "name": "(AR) Responsable Inscripto (Unit Tests)",
                "l10n_ar_afip_start_date": time.strftime("%Y-01-01"),
                "l10n_ar_gross_income_type": "local",
                "l10n_ar_gross_income_number": "901-21885123",
            }
        )
        cls.company_ri = cls.company_data["company"]

        cls.company_ri.partner_id.write(
            {
                "name": "(AR) Responsable Inscripto (Unit Tests)",
                "l10n_ar_afip_responsibility_type_id": cls.env.ref(
                    "l10n_ar.res_IVARI"
                ).id,
                "l10n_latam_identification_type_id": cls.env.ref("l10n_ar.it_cuit").id,
                "vat": "30111111118",
                "street": "Calle Falsa 123",
                "city": "Rosario",
                "country_id": cls.env.ref("base.ar").id,
                "state_id": cls.env.ref("base.state_ar_s").id,
                "zip": "2000",
                "phone": "+1 555 123 8069",
                "email": "info@example.com",
                "website": "www.example.com",
            }
        )
        cls.partner_ri = cls.company_ri.partner_id

        # Create user.
        user = cls.env["res.users"].create(
            {
                "name": "Because I am accountman!",
                "login": "test_user",
                "password": "mypassword",
                "groups_id": [
                    (6, 0, cls.env.user.groups_id.ids),
                    (4, cls.env.ref("account.group_account_manager").id),
                    (4, cls.env.ref("account.group_account_user").id),
                ],
            }
        )

        # Shadow the current environment/cursor with one having the report user.
        # This is mandatory to test access rights.
        cls.env = cls.env(user=user)

        # ---------------- Productos ----------------------

        cls.product = cls.env["product.product"].create(
            {
                "name": "product normal",
                "prod_in_box_uom": "na",
            }
        )
        cls.product_m = cls.env["product.product"].create(
            {
                "name": "product metros",
                "prod_in_box": 3.5,
                "prod_in_box_uom": "mt",
            }
        )
        cls.product_m2 = cls.env["product.product"].create(
            {
                "name": "product_metros cuadrados",
                "prod_in_box": 2.4,
                "prod_in_box_uom": "mt2",
            }
        )

        # ---------------- partners ----------------------

        cls.res_partner_expresso = cls.env["res.partner"].create(
            {
                "name": "Expresso",
                "is_company": 1,
                "city": "Barcelona",
                "zip": "11002",
                "country_id": cls.env.ref("base.es").id,
                "street": "La gran avenida 123",
                "email": "info@expresso.com",
                "phone": "(+00) (11) 222 3333",
                "website": "http://www.expresso.com/",
                "l10n_latam_identification_type_id": cls.env.ref(
                    "l10n_latam_base.it_fid"
                ).id,
                "vat": "2222333344445555",
                "l10n_ar_afip_responsibility_type_id": cls.env.ref(
                    "l10n_ar.res_EXT"
                ).id,
            }
        )

    # ---------------- Orden de Venta ----------------------

    def _create_sale_order(cls, data):
        """Crear una orden de venta con productos"""
        data = data if data else {}
        with Form(cls.env["sale.order"].with_company(cls.company_ri)) as so:
            so.partner_id = cls.res_partner_expresso
            with so.order_line.new() as ol:
                ol.product_id = data.get("product_id")
                ol.price_unit = 250.0
                ol.product_uom_qty = 1
        return so.save()
