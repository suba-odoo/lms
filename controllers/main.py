from odoo import http
from odoo.http import request

class Estate(http.Controller):
     @http.route(['/courses','/courses/page/<int:page>'],type='http', auth='public', website=True)
     def course(self, page=0, domain=[],**kw):
        total = http.request.env['learning.system.types'].sudo().search_count([])
        date = kw.get('create_date')
        # domain= [('create_date', '>=', date)]
        if date:
            domain.append(('create_date', '>=', date))
        per_page = 6
        pager = request.website.pager(
            url='/courses',
            total = total,
            page = page,
            step = per_page,
        )
        courses= http.request.env['learning.system.types'].search([domain])
        return http.request.render('lms.index',{
               'courses': courses.search(domain,limit=per_page, offset=pager['offset'],order='id desc'),'pager': pager })


# class Estate(http.Controller):
#     @http.route(['/properties','/properties/page/<int:page>'],type='http', auth='public', website=True)
#     def properties_grid(self, page =0,**kw):
#             domain = [('state', 'in', ['N', 'R','A'])]
#             total = http.request.env['estate.property'].sudo().search_count([])
#             date = kw.get('create_date')
#             if date:
#                 domain.append(('create_date', '>=', date))
#             per_page=6
#             pager = request.website.pager(
#                 url='/properties',
#                 total=total,
#                 page=page,
#                 step=per_page
#                 )
#             properties = http.request.env['estate.property'].search(domain)
#             return http.request.render('estate.index',{
#             'properties': properties.search(domain,limit=per_page, offset=pager['offset'],order='id desc'),'pager':pager})

#     @http.route('/properties/<int:id>', auth="public", website=True)
#     def property(self, id):
#         properties = http.request.env['estate.property']
#         return http.request.render('estate.description', {
#             'properties': properties.search([('id', '=', id)])
#         })
