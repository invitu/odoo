/** @odoo-module */
/*
    Copyright 2024 Dixmit
    License OPL-1.0 or later (https://www.odoo.com/documentation/15.0/es/legal/licenses.html#odoo-apps).
*/

import {PosStore} from "@point_of_sale/app/store/pos_store";
import {patch} from "@web/core/utils/patch";

patch(PosStore.prototype, {
    async selectPrescriber() {
        const currentOrder = this.get_order();
        if (!currentOrder) {
            return;
        }
        const currentPartner = currentOrder.get_prescriber();
        const {confirmed, payload: newPartner} = await this.showTempScreen(
            "PrescriptorListScreen",
            {
                partner: currentPartner,
            }
        );
        if (confirmed) {
            currentOrder.set_prescriber(newPartner);
        }
    },
});
