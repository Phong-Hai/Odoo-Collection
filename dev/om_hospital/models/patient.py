from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
#This is how you create models
    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    gender = fields.Selection([{'male', 'Male'}, {'female', 'Female'}], string="Gender")
#This were add to the models in setting > technical > models > Hospital