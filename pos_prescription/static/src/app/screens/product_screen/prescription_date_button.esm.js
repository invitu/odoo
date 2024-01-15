/** @odoo-module */
/*
    Copyright 2024 Dixmit
    License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
*/
import {Component} from "@odoo/owl";
import {DatePickerPopup} from "@point_of_sale/app/utils/date_picker_popup/date_picker_popup";
import {ProductScreen} from "@point_of_sale/app/screens/product_screen/product_screen";
import {_t} from "@web/core/l10n/translation";

import {usePos} from "@point_of_sale/app/store/pos_hook";
import {useService} from "@web/core/utils/hooks";
const {DateTime} = luxon;

export class PrescriptionDatePickerPopup extends DatePickerPopup {
    _today() {
        console.log(DateTime.now().toISODate());
        return DateTime.now().toISODate();
    }
}
PrescriptionDatePickerPopup.template = "pos_prescription.PrescriptionDatePickerPopup";

export class PrescriptionDateButton extends Component {
    setup() {
        this.pos = usePos();

        this.popup = useService("popup");
    }
    get date() {
        const order = this.pos.get_order();
        return order ? order.prescription_date : null;
    }

    async click() {
        if (this.date) {
            this.pos.get_order().setPrescriptionDate(false);
        } else {
            const {confirmed, payload: prescriptionDate} = await this.popup.add(
                PrescriptionDatePickerPopup,
                {
                    title: _t("Select the prescription date"),
                }
            );
            if (confirmed) {
                console.log(prescriptionDate);
                this.pos.get_order().setPrescriptionDate(prescriptionDate);
            }
        }
    }
}
PrescriptionDateButton.template = "pos_prescription.PrescriptionDateButton";

ProductScreen.addControlButton({
    component: PrescriptionDateButton,
});
