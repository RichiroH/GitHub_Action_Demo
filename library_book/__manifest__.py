{
    'name': 'Library Book Management',
    'version': '19.0.1.0.0',
    'category': 'Services/Library',
    'summary': 'Catalog and track books in a library',
    'description': """
Library Book Management
=======================

This module provides a simple catalog to record library books,
their authors, publishers and availability status.
""",
    'author': 'Example Author',
    'website': 'https://github.com/example/library_book',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/library_book_security.xml',
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'data/library_book_data.xml',
    ],
    'demo': [
        'demo/library_book_demo.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}
