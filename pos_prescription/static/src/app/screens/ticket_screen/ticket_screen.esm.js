/** @odoo-module */
/*
    Copyright 2024 Dixmit
    License OPL-1.0 or later (https://www.odoo.com/documentation/15.0/es/legal/licenses.html#odoo-apps).
*/
import {TicketScreen} from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import {formatDate} from "@web/core/l10n/dates";
import {patch} from "@web/core/utils/patch";

patch(TicketScreen.prototype, {
    getPrescriber(order) {
        var prescriber = order.get_prescriber();
        return prescriber ? prescriber.name : "";
    },

    getPrescriptionDate(order) {
        return order.prescription_date ? formatDate(order.prescription_date) : "";
    },
});
