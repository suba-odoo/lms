from odoo import fields, models
from odoo.exceptions import UserError

class learning_enrollment(models.Model):
    _name = 'learning.system.enrollment'
    _description = 'Learning Management System'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _log_access = False


    date = fields.Date(string="EnrollmentDate",default=lambda self:fields.Date.today())
    status=fields.Selection(selection=[("CO","conform"),("CA","cancel")],copy= False)
    student_id = fields.Many2one('res.users',string="Student",default=lambda self:self.env.user)
    course_id = fields.Many2one('learning.system.types',string="Course Name",required = True,copy=False)
    state = fields.Selection(string = 'State', selection=[('N','New'), ('P','Process'), ('C','Completed'),('CO','Close')],default='N')


    def action_conform(self):
        for i in self:
            if i.status == 'CA':
                raise UserError("canceled Course can't be Enroll")
        else:
            i.status = 'CO'
            i.state = 'P'

    def action_cancel(self):
        for i in self:
            if i.status == 'CO':
                raise UserError("Enrolled Course can't be Cancel")
                    
        else:
            i.status = 'CA'
            i.state = 'CO'

