# Copyright 2024 Dixmit
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Pos Prescription",
    "summary": """
        Add prescription information to PoS Order line""",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
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
