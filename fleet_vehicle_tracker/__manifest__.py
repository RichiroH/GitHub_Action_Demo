{
    'name': 'Fleet Vehicle Tracker',
    'version': '19.0.1.0.0',
    'category': 'Fleet/Fleet',
    'summary': 'Track fleet vehicles and mileage',
    'description': """
Fleet Vehicle Tracker
=====================

Record vehicles, their drivers, mileage logs and maintenance
status for a simple fleet.
""",
    'author': 'Example Author',
    'website': 'https://github.com/example/fleet_vehicle_tracker',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/fleet_security.xml',
        'security/ir.model.access.csv',
        'views/fleet_vehicle_views.xml',
        'views/fleet_mileage_views.xml',
        'data/fleet_data.xml',
    ],
    'demo': [
        'demo/fleet_demo.xml',
    ],
    'application': True,
    'installable': True,
}
