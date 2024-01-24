# Copyright 2024 Dixmit
# License OPL-1.0 or later (https://www.odoo.com/documentation/15.0/es/legal/licenses.html#odoo-apps).

from odoo import models


class PosSession(models.Model):
    _inherit = "pos.session"

    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()
        result["search_params"]["fields"].append("is_prescriptor")
        return result
