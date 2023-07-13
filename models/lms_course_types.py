from odoo import fields, models, api

class learning_system_types(models.Model):
    _name = 'learning.system.types'
    _description = 'Learning Management System'
    _log_access = False

    name = fields.Char(string ='Name', required=True)
    course_duration = fields.Char(string ="Course Duration")
    assignment_ids=fields.One2many('learning.system.assignment','course_id')
    Institute_id = fields.Many2one('res.users',string="Institute name",default=lambda self:self.env.user)
    enroll_ids = fields.One2many('learning.system.enrollment','course_id')
    enroll_count = fields.Integer(compute="_compute_offer_count")

    @api.depends('enroll_ids')
    def _compute_offer_count(self):
        for record in self:
            record.enroll_count = self.env['learning.system.enrollment'].search_count([('course_id','=',self.id)])




