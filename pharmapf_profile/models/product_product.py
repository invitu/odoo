

from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = "product.product"

    cip7 = fields.Char(
        'CIP7', copy=False, index='btree_not_null',
        readonly=True,
        help="French Old CIP code.")
