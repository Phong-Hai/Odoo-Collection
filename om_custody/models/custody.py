from odoo import api, fields, models

class Custody(models.Model):
    _name = "custody"
    _description = ("Custody")

    code = fields.Char(string='Code')
    employee_id = fields.Many2one('hr.employee', string='Employee')
    reason = fields.Char(string="Reason")
    project_id = fields.Many2one('project.project', string='Project')
    rqdate = fields.Date(string="Requested Date", required=True)
    rtdate = fields.Date(string="Return Date", required=True)
    note = fields.Text(string='Note')
    source = fields.Char(string='Source')

    active = fields.Boolean(string="Active", default=True)