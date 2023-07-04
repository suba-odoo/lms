from odoo import fields, models

class learning_system_user_types(models.Model):
    _name = 'learning.system.user.types'
    _description = 'Learning Management System'
    _log_access = False

    name = fields.Char(string ='Name', required=True)