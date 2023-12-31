{
    'name': 'Custody',
    'author': 'ERP CAMBODIA',
    'version': '1.0.0',
    'cetegory': 'Custody',
    'sequence': -100,
    'summary':  'Custody',
    'website': 'https://www.erpcambodia.biz/',
    'description': """This module is combination of 3 apps together""",
    'depends': ['hr','project','product','mail','sale','stock', 'base'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/custody_view.xml',
        'views/property_view.xml',
        'views/custody_product.xml',
        'views/menu.xml',
        'reports/custody_report.xml',
    ],
    'demo':[],
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3',
}