from odoo import fields, models

class learning_system_types(models.Model):
    _name = 'learning.system.types'
    _description = 'Learning Management System'
    _log_access = False

    name = fields.Char(string ='Name', required=True)
    course_duration = fields.Char(string ="Course Duration")
    assignment_ids=fields.One2many('learning.system.assignment','course_id')