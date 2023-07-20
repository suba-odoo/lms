from odoo import fields, models, api


class learning_assignment_submission(models.Model):
    _name = 'learning.system.assignment.submission'
    _description = 'Learning Management System'

    submission_date = fields.Date(string='Submission Date',required=True)
    file_type = fields.Selection(string="File Type",selection=[('P','Pdf'),('D','Doc'),('T','Text')])
    student_id = fields.Many2one('res.users',string="Student",default=lambda self:self.env.user)
    assignment_id = fields.Many2one('learning.system.assignment',string="Assignment Name",copy=False)
    course_id = fields.Many2one('learning.system.types',string="Course Name",required = True,copy=False)
    file = fields.Binary(string="File",required=True,copy=False)