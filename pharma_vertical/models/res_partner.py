# Copyright 2024 Dixmit
# Copyright 2024 INVITU
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    creg = fields.Selection(
        selection_add=[
            ("S", "RGS"),
            ("V", "Vol"),
            ("T", "RSPF"),
            ("N", "RNS"),
            ("M", "RSS"),
        ],
    )
