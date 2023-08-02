from odoo import http
from odoo.http import request

class Estate(http.Controller):
    @http.route(['/courses','/courses/page/<int:page>'],type='http', auth='public', website=True)
    def course(self, page=0, **kwargs):
        total = http.request.env['learning.system.types'].sudo().search_count([])
        per_page = 6
        pager = request.website.pager(
            url='/courses',
            total = total,
            page = page,
            step = per_page,
        )
        courses= http.request.env['learning.system.types']
        return http.request.render('lms.index',{
            'courses': courses.search([],limit =per_page, offset=pager['offset']),'pager':pager })
    
    @http.route('/courses/<int:id>', auth="public", website=True)
    def property(self, id):
        courses= http.request.env['learning.system.types']
        return http.request.render('lms.description', {
            'courses': courses.search([('id', '=', id)])
        })
