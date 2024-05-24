# Copyright 2024 Dixmit
# Copyright 2024 INVITU
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

{
    "name": "Pos Order Split Invoice Medical",
    "summary": """
        Add extra fields specifically to Medical Industry in Split Invoice Context""",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "author": "Dixmit,INVITU SARL",
    "website": "https://github.com/invitu/odoo-pharmapf",
    "depends": ["pos_order_split_invoice"],
    "data": [
        "views/res_partner_views.xml",
        "views/pos_order_views.xml",
    ],
    "assets": {},
    "demo": [],
}
