from odoo import models, fields

class lms_wizard(models.TransientModel):
    _name = "lms.wizard"
    _description = "Lms Wizard"

    name = fields.Char(string ='Name')
    aname = fields.Char(string = 'Assignment Name',required = True)
    validity = fields.Integer(string = 'validity(days)', default= 10)
    status = fields.Selection(string = 'Status', selection=[('N','New'), ('P','Process'), ('C','Completed')], default="N")


    def add_assignment(self):
        course_ids = self.env.context.get('active_ids', [])
        assignment= self.env['learning.system.assignment']
        for course_id in course_ids:
            assignments = {
                'name': self.aname,
                'validity': self.validity,
                'status': self.status,
                'course_id': course_id,
            }
            assignment.create(assignments)


            

