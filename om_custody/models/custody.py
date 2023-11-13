from odoo import api, fields, models

class Custody(models.Model):
    _name = "custody"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = ("Custody")

    code = fields.Char(string='Code')
    reason = fields.Char(string="Reason")
    rqdate = fields.Date(string="Requested Date", required=True)
    rtdate = fields.Date(string="Return Date", required=True)
    note = fields.Text(string='Note')
    source = fields.Char(string='Source')


    state = fields.Selection([('draft', 'Draft'), ('to_approve', 'Waiting Stock Validate'), ('done', 'Done'), ('returned', 'Returned')], string='Status', default='draft')
    product_id = fields.Many2one('product.product', string='Product')
    project_id = fields.Many2one('project.project', string='Project')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    approve_user_id = fields.Many2one('res.users', string='Approve User')
    it_picking_type_id = fields.Many2one('stock.picking.type', string='It Picking Type')
    it_location_id = fields.Many2one('stock.location', string='It Location')
    stock_picking_type_id = fields.Many2one('stock.picking.type', string='Stock Picking Type')
    stock_location_id = fields.Many2one('stock.location', string='Stock Location')
    destination_location_id = fields.Many2one('stock.location', string='Destination Location')

    active = fields.Boolean(string="Active", default=True)
