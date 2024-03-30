# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library Management',
    'version': '1.0.0',
    'author': "M. A. Murad",
    'summary': 'Library Management Demo......',
    'sequence': -100,
    'description': """This is A demo module creation""",
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/member_views.xml',
        'views/transaction_views.xml',
        'views/book_views.xml',


    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
