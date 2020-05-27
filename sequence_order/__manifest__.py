{
    'name': "Sequence_order_module",
    'version': '1.0',
    'author': "Kanak Infosystems",
    'website': "info@nothing.com",
    'summary': "It is a shopping module",
    'description': """
     This Module is use to create sequential field in Odoo.
    """,
    'depends': ['base'],
    'data': [
        'data/seq.xml',
        'views/sequence_order.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'images': [],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
