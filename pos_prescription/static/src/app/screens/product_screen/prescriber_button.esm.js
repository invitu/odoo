/** @odoo-module */
/*
    Copyright 2024 Dixmit
    License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
*/
import {Component} from "@odoo/owl";
import {ProductScreen} from "@point_of_sale/app/screens/product_screen/product_screen";
import {usePos} from "@point_of_sale/app/store/pos_hook";

export class PrescriberButton extends Component {
    setup() {
        this.pos = usePos();
    }

    get prescriber() {
        const order = this.pos.get_order();
        return order ? order.get_prescriber() : null;
    }
}
PrescriberButton.template = "pos_prescription.PrescriberButton";

ProductScreen.addControlButton({
    component: PrescriberButton,
    position: ["before", "SetFiscalPositionButton"],
});
