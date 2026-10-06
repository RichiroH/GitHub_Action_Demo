{
    'name': 'Warehouse Bin Locator',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Warehouse',
    'summary': 'Locate products within warehouse bins',
    'description': """
Warehouse Bin Locator
=====================

Define bins inside warehouse zones and map products to bins.
A scheduled job periodically flags empty bins for cleanup.
""",
    'author': 'Example Author',
    'website': 'https://github.com/example/warehouse_bin_locator',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/warehouse_security.xml',
        'security/ir.model.access.csv',
        'views/warehouse_zone_views.xml',
        'views/warehouse_bin_views.xml',
        'data/warehouse_data.xml',
        'data/warehouse_cron_data.xml',
    ],
    'demo': [
        'demo/warehouse_demo.xml',
    ],
    'application': True,
    'installable': True,
}
