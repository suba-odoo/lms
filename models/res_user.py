from odoo import fields, models

class res_users(models.Model):
    _inherit = "res.users"

    enroll_ids = fields.One2many("learning.system.enrollment", "student_id")
