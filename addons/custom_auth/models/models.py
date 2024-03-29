# from odoo import api, fields, models
#
# class CustomUser(models.Model):
#     _name = 'custom.user'
#     _description = 'Custom User'
#
#     login = fields.Char(string='Login', required=True)
#     password = fields.Char(string='Password', required=True)
#
#     @api.constrains('login')
#     def _check_unique_login(self):
#         for record in self:
#             if self.search_count([('login', '=', record.login)]) > 1:
#                 raise ValueError("Login must be unique.")
#
#     is_admin = fields.Boolean(string='Is Admin', default=False)

# models/models.py

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
