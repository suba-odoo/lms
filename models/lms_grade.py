from odoo import fields, models

class learning_system_grade(models.Model):
    _name = 'learning.system.grade'
    _description = 'Learning Management System'
    _log_access = False

    grade = fields.Selection(string="Grade",selection=[("a","A"),("b","B"),("c","C"),("d","D"),("e","E"),("f","Fail")])
    feedback = fields.Text(string = "Feedback", copy=False)
    student_id = fields.Many2one('res.users',string="Student",default=lambda self:self.env.user)
    assignment_id = fields.Many2one('learning.system.assignment',string= "Assignment Name",copy=False)
    course_id = fields.Many2one('learning.system.types',string= "Course Name",copy=False)
    enrollment_ids = fields.One2many('learning.system.enrollment','student_id',copy=False)

