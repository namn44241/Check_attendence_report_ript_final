# -*- coding: utf-8 -*-

{
    'name': 'Create Account Type',
    'category': 'Accounting',
    'summary': 'Chart of Accounts "Type" create/edit option',
    'author': 'Srikesh Infotech',
    'license': "AGPL-3",
    'website': 'http://www.srikeshinfotech.com',
    'description': """
        Enable Account Type create/edit option into Chart of Accounts Screen
==========================

""",
    'images': ['images/main_screenshot.png'],
    'depends': ['account'],
    'data': [
        'views/skit_account_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
