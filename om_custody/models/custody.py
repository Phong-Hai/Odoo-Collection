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

    active = fields.Boolean(string="Active", default=True)