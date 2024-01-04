{
    'name': 'Pharma Vertical',
    'version': '1.0',
    'summary': 'Verticalisation for Pharmacies',
    'sequence': 30,
    'description': """
""",
    'category': 'Customization',
    "author": "INVITU SARL",
    'website': 'https://www.invitu.com',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'base',
        'product_expiry',
        'purchase',
        'partner_second_lastname',  # to be replaced by pos_partner_second_lastname
        'partner_firstname',  # to be replaced by pos_partner_firstname
        'partner_ref_unique',
        'pos_partner_ref',
        'pos_lot_selection',
        'pos_lot_barcode',
        'pos_partner_birthdate',
        'pos_order_split_invoice',
        'pos_multi_order_payment',
    ],
    'data': [
        'data/res_config_settings.xml',
        'data/product_category.xml',
        'data/product_pricelist.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
