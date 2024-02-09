# Copyright 2024 Dixmit
# License OPL-1.0 or later (https://www.odoo.com/documentation/15.0/es/legal/licenses.html#odoo-apps).

{
    "name": "Pos Prescription",
    "summary": """
        Add prescription information to PoS Order line""",
    "version": "17.0.1.0.0",
    "license": "OPL-1",
    "author": "Dixmit,INVITU SARL",
    "website": "https://github.com/invitu/odoo-pharmapf",
    "depends": ["point_of_sale"],
    "data": [
        "views/res_partner.xml",
        "views/pos_order.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_prescription/static/src/app/**/*.esm.js",
            "pos_prescription/static/src/app/**/*.xml",
        ]
    },
    "demo": [],
}
