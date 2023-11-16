from odoo import api, fields, models, _


class Custody(models.Model):
    _name = "custody"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Custody"

    ref = fields.Char(string='Code', default=lambda self: _('New'))
    reason = fields.Char(string="Reason")
    rqdate = fields.Date(string="Requested Date", required=True)
    rtdate = fields.Date(string="Return Date", required=True)
    note = fields.Text(string='Note')
    source = fields.Selection([('it', 'IT'), ('stock', 'Inventory')], string='Source')

    state = fields.Selection(
        [('draft', 'Draft'), ('to_approve', 'Waiting Stock Validate'), ('done', 'Done'), ('returned', 'Returned')],
        string='Status', default='draft')
    product_id = fields.Many2one('product.product', string='Product')
    project_id = fields.Many2one('project.project', string='Project')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    approve_user_id = fields.Many2one('res.users', string='Approve User')
    it_picking_type_id = fields.Many2one('stock.picking.type', string='It Picking Type')
    it_location_id = fields.Many2one('stock.location', string='It Location')
    stock_picking_type_id = fields.Many2one('stock.picking.type', string='Stock Picking Type')
    stock_location_id = fields.Many2one('stock.location', string='Stock Location')
    destination_location_id = fields.Many2one('stock.location', string='Destination Location')

    properties_one2many_ids = fields.One2many('custody.one2many.properties', 'prop_id', string='Properties')
    history_one2many_ids = fields.One2many('custody.one2many.history', 'his_id', string='History')

    active = fields.Boolean(string="Active", default=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('custody.seq')
        return super(Custody, self).create(vals_list)


class CustodyOne2ManyProperties(models.Model):
    _name = "custody.one2many.properties"
    _description = "custody.one2many.properties"

    product_id = fields.Many2one('product.product')
    source = fields.Selection([('it', 'IT'), ('stock', 'Inventory')], string='Source')
    property_name = fields.Char(string='Property Name')
    available_qty = fields.Integer(string='Available QTY')
    quantity = fields.Integer(string='Quantity')
    delivered = fields.Integer(string='Delivered')
    returned = fields.Integer(string='Returned')

    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    prop_id = fields.Many2one('custody', string='Prop')


class CustodyOne2ManyHistory(models.Model):
    _name = "custody.one2many.history"
    _description = "custody.one2many.history"

    employee_id = fields.Many2one('hr.employee', string='Employee')
    date = fields.Date(string='Date')
    state = fields.Selection([('active', 'Active'), ('done', 'Done')], string='Date')

    his_id = fields.Many2one('custody', string='His')
