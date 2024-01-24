/** @odoo-module */
/*
    Copyright 2024 Dixmit
    License OPL-1.0 or later (https://www.odoo.com/documentation/15.0/es/legal/licenses.html#odoo-apps).
*/

import {PartnerListScreen} from "@point_of_sale/app/screens/partner_list/partner_list";
import {registry} from "@web/core/registry";

class PrescriptorListScreen extends PartnerListScreen {
    get partners() {
        var res = super.partners;
        var selectedPartner = this.state.selectedPartner;
        return res.filter((partner) => {
            return (
                Boolean(partner.is_prescriptor) ||
                (selectedPartner && partner.id === selectedPartner.id)
            );
        });
    }
    activateEditMode() {
        if (!this.state.editModeProps.partner.id) {
            // Set it as prescriptor in case of creation
            this.state.editModeProps.partner.is_prescriptor = true;
        }
        super.activateEditMode();
    }
}

registry.category("pos_screens").add("PrescriptorListScreen", PrescriptorListScreen);
