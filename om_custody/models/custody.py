from odoo import api, fields, models

class Custody(models.Model):
    _name = "custody"
    _description = ("Custody")

    name = fields.Char(string='Employee')
    ref = fields.Char(string='Code')
    reason = fields.Char(string="Reason")
    rqdate = fields.Date(string="Requested Date", required=True)
    rtdate = fields.Date(string="Return Date", required=True)
    note = fields.Text(string='Note')

    custody = fields.Char(string='Custody')
    image = fields.Char(string='Image')
    ssi = fields.Char(string='Small-size Image')
    description = fields.Text(string='Description')
    company = fields.Text(string='Company')
    product = fields.Text(string='Product')
    lsnum = fields.Text(string='Lot/Serial Number')
    quan = fields.Char(string='Quantity')
    delivered = fields.Char(string='Delivered')
    uom = fields.Text(string='Unit of Measure')

    ppn = fields.Char(string='Property Name')
    msi = fields.Char(string='Medium-sized Image')
    ppf = fields.Char(string='Property Form')
    sno = fields.Char(string='Serial No')
    source = fields.Char(string='Source')
    returned = fields.Char(string='Returned')
    aqty = fields.Char(string='Available QTY')
    job = fields.Char(string='job')

    active = fields.Boolean(string="Active", default=True)