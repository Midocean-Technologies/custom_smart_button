from odoo import api, fields, models


class patientsmartbtn(models.Model):
    _name = "patient.smart.btn"
    _description = "Hospital patient"
    _rec_name = "name"

    patient_id = fields.Integer(string="Patient Id")
    name = fields.Char(string="Name")
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age")
    ph_no = fields.Char(string="Phone Number")
    appointment_ids = fields.One2many('appointment.smart.btn', 'patient_id', string='Appointments')
    appointment_count = fields.Integer(compute='_compute_appointment_count', string='Appointment Count', store=True)
    appointment_count = fields.Integer(compute='_compute_appointment_count', string='Appointment Count', store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], String="Gender")

    @api.depends('appointment_ids')
    def _compute_appointment_count(self):
        appointment_group = self.env['appointment.smart.btn'].read_group(domain=[],
                                                                         fields=['patient_id'], groupby=['patient_id'])
        for appointment in appointment_group:
            patient_id = appointment.get('patient_id')[0]
            patient_rec = self.browse(patient_id)
            patient_rec.appointment_count = appointment['patient_id_count']
            self -= patient_rec
        self.appointment_count = 0

    def action_view_appointments(self):
        return{
            'name': 'Appointment',
            'res_model': 'appointment.smart.btn',
            'view_mode': 'list,form',
            'content': {},
            'domain': [('patient_id', '=', self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window',
        }
