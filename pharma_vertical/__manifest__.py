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
    'images': [
    ],
    'depends': [
        'base',
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
    'licence': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
