# -*- coding: utf-8 -*-
{
    'name': "Client Spec",
    'summary': """Gestion Clients Grossistes""",
    'description': """
Gestion client grossiste module pour :
- Gérer les clients et commandes
- Gérer les assurances
""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Test',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/clientspec.xml',
        'reports.xml',
    ],
    'demo': ['demo.xml'],
}
