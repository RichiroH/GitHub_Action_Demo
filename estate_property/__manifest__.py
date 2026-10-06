{
    'name': 'Estate Property',
    'version': '19.0.1.0.0',
    'category': 'Real Estate',
    'summary': 'List properties for sale and rent',
    'description': """
Estate Property
===============

Maintain a portfolio of real estate properties, their types,
sellers, offers and selling status.
""",
    'author': 'Example Author',
    'website': 'https://github.com/example/estate_property',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_offer_views.xml',
        'wizard/estate_close_wizard_views.xml',
        'data/estate_data.xml',
    ],
    'demo': [
        'demo/estate_demo.xml',
    ],
    'application': True,
    'installable': True,
}
