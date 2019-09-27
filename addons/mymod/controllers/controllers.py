# -*- coding: utf-8 -*-
from odoo import http

# class Mymod(http.Controller):
#     @http.route('/mymod/mymod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mymod/mymod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mymod.listing', {
#             'root': '/mymod/mymod',
#             'objects': http.request.env['mymod.mymod'].search([]),
#         })

#     @http.route('/mymod/mymod/objects/<model("mymod.mymod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mymod.object', {
#             'object': obj
#         })