from odoo import fields, models

class learning_system(models.Model):
    _name = 'learning.system'
    _description = 'Learning Management System'
    _log_access = False

    name = fields.Char(string ='Name', required=True)
    email = fields.Char(string ='Email', required=True)
    phone = fields.Char(string ='Phone', required=True)
    address = fields.Char(string ='Address', required=True)
    gender = fields.Selection(string ='Gender', selection =[('M', 'male'), ('F', 'female')])
    postcode = fields.Char(string = 'postcode', required = True)
    description = fields.Text(string ='description', required = True)
    date  = fields.Date(string ='date', default=lambda self:fields.Date.today())
    course_type_id=fields.Many2one('learning.system.types',string='Course Type', copy = False)
    user_ids=fields.Many2many("learning.system.user.types", string="User Type")
    assignment_ids=fields.One2many('learning.system.assignment','course_id')


