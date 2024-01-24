# Copyright 2024 Dixmit
# License OPL-1.0 or later (https://www.odoo.com/documentation/15.0/es/legal/licenses.html#odoo-apps).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_prescriptor = fields.Boolean()
