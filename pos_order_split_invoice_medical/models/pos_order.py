# Copyright 2024 Dixmit
# Copyright 2024 INVITU
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    creg = fields.Selection(
        selection=[],
        string="Social Regime",
    )
