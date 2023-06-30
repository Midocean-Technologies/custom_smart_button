from odoo import api, fields, models
from datetime import datetime


class appointmentsmartbtn(models.Model):
    _name = "appointment.smart.btn"
    _description = "Hospital Patient Appointments"
    _rec_name = "patient_id"

    appointment_id = fields.Integer(string='Appointment Id')
    patient_id= fields.Many2one(comodel_name='patient.smart.btn', string="Patient")
    a_time = fields.Datetime(string='Appointment Time')
    state = fields.Selection([('done', 'Done'), ('wait', 'Waiting')], string='state')

