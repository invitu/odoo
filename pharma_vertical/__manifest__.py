{
    "name": "Pharma Vertical",
    "version": "17.0.1.0.0",
    "summary": "Verticalisation for Pharmacies",
    "sequence": 30,
    "category": "Customization",
    "author": "INVITU SARL",
    "website": "https://github.com/invitu/odoo-pharmapf",
    "license": "AGPL-3",
    "images": [],
    "depends": [
        "base",
        "purchase",
        "pos_product_expiry",
        "pos_partner_second_lastname",
        "pos_partner_firstname",
        "partner_ref_unique",
        "pos_partner_ref",
        "pos_lot_selection",
        "pos_lot_barcode",
        "pos_partner_birthdate",
        "pos_order_split_invoice",
        "pos_multi_order_payment",
        "pos_prescription",
        "pos_order_attachment",
        "pos_split_invoice_partner_expiry_date",

    ],
    "data": [
        "data/res_config_settings.xml",
        "data/product_category.xml",
        "data/product_pricelist.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pharma_vertical/static/src/models/order.esm.js",
        ]
    },
    "demo": [],
    "qweb": [],
    "installable": True,
    "application": False,
    "auto_install": False,
}
