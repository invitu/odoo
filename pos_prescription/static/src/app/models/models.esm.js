/** @odoo-module */

/*
    Copyright 2024 Dixmit
    License OPL-1.0 or later (https://www.odoo.com/documentation/15.0/es/legal/licenses.html#odoo-apps).
*/
import {Order} from "@point_of_sale/app/store/models";

import {patch} from "@web/core/utils/patch";

patch(Order.prototype, {
    setup() {
        this.prescriber = null;
        this.prescription_date = false;
        super.setup(...arguments);
    },
    init_from_JSON(json) {
        super.init_from_JSON(...arguments);
        var partner = null;
        if (json.prescriber_id) {
            partner = this.pos.db.get_partner_by_id(json.prescriber_id);
            if (!partner) {
                console.error(
                    "ERROR: trying to load a partner not available in the pos"
                );
            }
        }
        this.prescriber = partner;
        this.prescription_date = json.prescription_date
            ? json.prescription_date
            : false;
    },
    export_as_JSON() {
        var json = super.export_as_JSON();
        json.prescriber_id = this.get_prescriber() ? this.get_prescriber().id : false;
        json.prescription_date = this.prescription_date
            ? this.prescription_date
            : false;
        return json;
    },
    get_prescriber() {
        return this.prescriber;
    },
    set_prescriber(partner) {
        this.assert_editable();
        this.prescriber = partner;
    },
    setPrescriptionDate(date) {
        this.prescription_date = date;
    },
});
