from odoo import fields, models

class learning_assignment(models.Model):
    _name = 'learning.system.assignment'
    _description = 'Learning Management System'
    _log_access = False

    name = fields.Char(string ="Name", required=True)
    description = fields.Char(string = "description", required=True)
    course_id = fields.Many2one("learning.system.types", required=True)
    