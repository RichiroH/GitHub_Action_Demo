{
    'name': 'Restaurant Menu',
    'version': '19.0.1.0.0',
    'category': 'Restaurant/Menu',
    'summary': 'Design restaurant menus and dishes',
    'description': """
Restaurant Menu
===============

Build digital menus composed of dishes grouped by category,
with allergens, prices and availability flags.
""",
    'author': 'Example Author',
    'website': 'https://github.com/example/restaurant_menu',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/restaurant_security.xml',
        'security/ir.model.access.csv',
        'views/restaurant_dish_views.xml',
        'views/restaurant_menu_views.xml',
        'data/restaurant_data.xml',
    ],
    'demo': [
        'demo/restaurant_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'restaurant_menu/static/src/scss/restaurant_menu.scss',
        ],
    },
    'application': True,
    'installable': True,
}
