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
    image = fields.Binary(string ='image')



