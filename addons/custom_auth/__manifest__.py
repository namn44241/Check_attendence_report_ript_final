# __manifest__.py

{
    'name': 'DANG NHAP',
    'version': '1.0',
    'summary': 'Module for custom authentication and API',
    'author': 'Nam',
    'website': 'Your Website',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_user_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
