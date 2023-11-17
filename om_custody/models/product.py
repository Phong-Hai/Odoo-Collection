from odoo import api, fields, models


class CustodyProduct(models.Model):
    _name = "custody.product"
    _inherits = {'product.template': 'custody_product_id'}
    _inherits = {'product.template': 'custody_product_search_id'}
    _inherit = ['mail.thread']
    _description = "Product"

    custody_product_id = fields.Many2one('product.template', 'Product Template')
    custody_product_search_id = fields.Many2one('product.template', 'Product Template')

    def action_open_label_layout(self):
        return True

    def open_pricelist_rules(self):
        return True
