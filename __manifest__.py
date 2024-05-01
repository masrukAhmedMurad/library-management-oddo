# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Library Management System',
    'version': '1.0.0',
    'author': "M. A. Murad",
    'summary': 'Library Management System......',
    'sequence': -100,
    'description': """This is A demo module creation""",
    'category': 'Education',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/member_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
