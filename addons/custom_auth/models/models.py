
from odoo import api, fields, models

class CustomUser(models.Model):
    _name = 'custom.user'
    _description = 'Custom User'

    login = fields.Char(string='Login', required=True)
    password = fields.Char(string='Password', required=True)

    @api.constrains('login')
    def _check_unique_login(self):
        if self.search_count([('login', '=', self.login)]) > 1:
            raise ValueError("Login must be unique.")

    is_admin = fields.Boolean(string='Is Admin', default=False)

# models/models.py

# from odoo import api, fields, models
#
# class CustomUser(models.Model):
#     _name = 'custom.user'
#     _description = 'Custom User'
#
#     login = fields.Char(string='Login', required=True)
#     password = fields.Char(string='Password', required=True)
#     is_administrator = fields.Boolean(string='Administrator', default=False)
#     is_member = fields.Boolean(string='Member', default=True)
#     is_intern = fields.Boolean(string='Intern', default=False)
#
#     @api.constrains('login')
#     def _check_unique_login(self):
#         if self.search_count([('login', '=', self.login)]) > 1:
#             raise ValueError("Login must be unique.")
