# Copyright 2024 Dixmit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    prescription_date = fields.Date(readonly=True)
    prescriber_id = fields.Many2one("res.partner", readonly=True)

    def _export_for_ui(self, order):
        result = super()._export_for_ui(order)
        result.update(
            {
                "prescription_date": order.prescription_date
                and str(order.prescription_date),
                "prescriber_id": order.prescriber_id.id,
            }
        )
        return result

    @api.model
    def _order_fields(self, ui_order):
        result = super()._order_fields(ui_order)
        result.update(
            {
                "prescriber_id": ui_order.get("prescriber_id", False),
                "prescription_date": ui_order.get("prescription_date", False),
            }
        )
        return result
