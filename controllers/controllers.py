# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSmartButton(http.Controller):
#     @http.route('/custom_smart_button/custom_smart_button', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_smart_button/custom_smart_button/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_smart_button.listing', {
#             'root': '/custom_smart_button/custom_smart_button',
#             'objects': http.request.env['custom_smart_button.custom_smart_button'].search([]),
#         })

#     @http.route('/custom_smart_button/custom_smart_button/objects/<model("custom_smart_button.custom_smart_button"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_smart_button.object', {
#             'object': obj
#         })
