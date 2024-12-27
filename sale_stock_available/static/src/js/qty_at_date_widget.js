/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { QtyAtDatePopover } from "@sale_stock/widgets/qty_at_date_widget";
patch(QtyAtDatePopover.prototype, "qty_at_date_widget_patch", {
  setup() {
    this._super.apply(this, arguments);
  },
  openForecast() {
    this.actionService.doAction({
      "type": "ir.actions.act_window",
      "res_model": "stock.quant",
      "views": [[false, "tree"]],
      "domain": [
        ['location_id.usage', '=', 'internal'],
        ["product_id", "=", this.props.record.data.product_id[0]],
      ],
      "context": {
        'group_by': 'location_id',
      },
      "target": "new",
    });
  },
});