/** @odoo-module */
/*
    Copyright 2024 Dixmit
    License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
*/
import {PartnerDetailsEdit} from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import {CheckBox} from "@web/core/checkbox/checkbox";

import {patch} from "@web/core/utils/patch";
patch(PartnerDetailsEdit.prototype, {
    setup() {
        super.setup(...arguments);
        this.changes.is_prescriptor = this.props.partner.is_prescriptor;
    },
});
PartnerDetailsEdit.components = {
    ...PartnerDetailsEdit.components,
    CheckBox,
};
