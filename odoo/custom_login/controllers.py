from odoo import http
from odoo.http import request

class CustomLogin(http.Controller):
    @http.route('/custom_login', type='http', auth='public', website=True)
    def custom_login_page(self, **kw):
        # Trả về trang HTML của trang đăng nhập tùy chỉnh
        return http.request.render('custom_login.login_page')

    @http.route('/custom_login/authenticate', type='http', auth='public', website=True)
    def authenticate(self, **kw):
        # Xử lý thông tin đăng nhập, ví dụ kiểm tra tài khoản và mật khẩu
        # Nếu đúng, chuyển hướng đến trang chính của ứng dụng
        # Nếu không, hiển thị thông báo lỗi hoặc đăng nhập lại
        return http.request.redirect('/custom_login/main_page')
