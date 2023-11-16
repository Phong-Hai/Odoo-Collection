from odoo import api, fields, models

class Property(models.Model):
    _name = "property"
    _description = ("Property")

    custody = fields.Char(string='Custody')
    image = fields.Image(string='Image')

    ssi = fields.Image(string='Small-size Image')
    description = fields.Html(string='Description')
    company = fields.Text(string='Company')
    product = fields.Text(string='Product')
    quan = fields.Char(string='Quantity')
    delivered = fields.Char(string='Delivered')

    ppn = fields.Char(string='Property Name')
    msi = fields.Char(string='Medium-sized Image')
    ppf = fields.Char(string='Property Form')
    sno = fields.Char(string='Serial No')
    source = fields.Selection([('it', 'IT'), ('stock', 'Inventory')], string='Source')
    returned = fields.Char(string='Returned')
    aqty = fields.Char(string='Available QTY')
    delivered = fields.Integer(string='Delivered')

    rqdate = fields.Date(string="Requested Date", required=True)
    rtdate = fields.Date(string="Return Date", required=True)
    note = fields.Text(string='Note')
    ref = fields.Char(string='Code')
    reason = fields.Char(string="Reason")
    name = fields.Char(string='Name')

    custody_id = fields.Many2one('custody', string='Custody')
    product_id = fields.Many2one('product.product', string='Product')
    lsnum_id = fields.Many2one('stock.lot', string='Lot/Serial Number')
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    job_id = fields.Many2one('hr.job', string='Job')
