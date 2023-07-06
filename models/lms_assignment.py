from odoo import fields, models, api
from dateutil.relativedelta import relativedelta

class learning_assignment(models.Model):
    _name = 'learning.system.assignment'
    _description = 'Learning Management System'


    name = fields.Selection(string = 'Assignment Type', selection=[('quiz', 'Quiz'), ('test', 'Test'), ('mcq', 'MCQ')],required = True)
    description = fields.Char(string = "description", required=True)
    course_id = fields.Many2one("learning.system.types", required=True)
    validity = fields.Integer(string = 'validity', default= 0)
    date_deadline = fields.Date(string = 'Assignment_deadline', compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    status = fields.Selection(string = 'Status', selection=[('N','New'), ('P','Process'), ('C','Completed')])

    @api.depends( "validity","create_date")
    def _compute_date_deadline(self):
        for offer in self:
            offer.date_deadline = fields.Date.today() + relativedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            offer.validity = (offer.date_deadline - fields.Date.today()).days
    