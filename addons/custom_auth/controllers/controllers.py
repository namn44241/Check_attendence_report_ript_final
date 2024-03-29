# # controllers.py
#
# from odoo import http
# from odoo.http import request
#
# class CustomAuthController(http.Controller):
#
#     @http.route('/web/session/authenticate', type='http', auth="none")
#     def web_login(self, redirect=None, **kw):
#         ensure_db()
#         request.params['login_success'] = False
#         if request.httprequest.method == 'GET' and redirect and request.session.uid:
#             return request.redirect(redirect)
#         # simulate hybrid auth=user/auth=public, despite using auth=none to be able
#         # to redirect users when no db is selected - cfr ensure_db()
#         if request.env.uid is None:
#             if request.session.uid is None:
#                 # no user -> auth=public with specific website public user
#                 request.env["ir.http"]._auth_method_public()
#             else:
#                 # auth=user
#                 request.update_env(user=request.session.uid)
#
#         values = {k: v for k, v in request.params.items() if k in SIGN_UP_REQUEST_PARAMS}
#         try:
#             values['databases'] = http.db_list()
#         except odoo.exceptions.AccessDenied:
#             values['databases'] = None
#
#         if request.httprequest.method == 'POST':
#             try:
#                 uid = request.session.authenticate(request.db, request.params['login'], request.params['password'])
#                 request.params['login_success'] = True
#                 return request.redirect(self._login_redirect(uid, redirect=redirect))
#             except odoo.exceptions.AccessDenied as e:
#                 if e.args == odoo.exceptions.AccessDenied().args:
#                     values['error'] = _("Wrong login/password")
#                 else:
#                     values['error'] = e.args[0]
#         else:
#             if 'error' in request.params and request.params.get('error') == 'access':
#                 values['error'] = _('Only employees can access this database. Please contact the administrator.')
#
#         if 'login' not in values and request.session.get('auth_login'):
#             values['login'] = request.session.get('auth_login')
#
#         if not odoo.tools.config['list_db']:
#             values['disable_database_manager'] = True
#
#         response = request.render('web.login', values)
#         response.headers['X-Frame-Options'] = 'SAMEORIGIN'
#         response.headers['Content-Security-Policy'] = "frame-ancestors 'self'"
#         return response

# controllers/controllers.py

# controllers/controllers.py

from odoo import http
from odoo.http import request
import odoo.exceptions  # Importing the exceptions module


class CustomAuthController(http.Controller):

    @http.route('/web/session/authenticate', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        # Removed ensure_db() as it's not defined
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return request.redirect(redirect)

        if request.env.uid is None:
            if request.session.uid is None:
                request.env["ir.http"]._auth_method_public()  # Ensure this method call is correct and necessary.
            else:
                request.update_env(user=request.session.uid)

        values = {k: v for k, v in request.params.items() if
                  k in SIGN_UP_REQUEST_PARAMS}  # SIGN_UP_REQUEST_PARAMS is not defined. Define it or remove this line.
        try:
            values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            values['databases'] = None

        if request.httprequest.method == 'POST':
            try:
                uid = request.session.authenticate(request.db, request.params['login'], request.params['password'])
                request.params['login_success'] = True
                return request.redirect(self._login_redirect(uid,
                                                             redirect=redirect))  # Ensure _login_redirect method is defined and works as expected.
            except odoo.exceptions.AccessDenied as e:
                if e.args == odoo.exceptions.AccessDenied().args:
                    values['error'] = _("Wrong login/password")
                else:
                    values['error'] = e.args[0]
        else:
            if 'error' in request.params and request.params.get('error') == 'access':
                values['error'] = _('Only employees can access this database. Please contact the administrator.')

        if 'login' not in values and request.session.get('auth_login'):
            values['login'] = request.session.get('auth_login')

        if not odoo.tools.config['list_db']:
            values['disable_database_manager'] = True

        response = request.render('web.login', values)
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self'"
        return response
