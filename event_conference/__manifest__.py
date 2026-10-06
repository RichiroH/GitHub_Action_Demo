{
    'name': 'Event Conference',
    'version': '19.0.1.0.0',
    'category': 'Events',
    'summary': 'Organize conferences and sessions',
    'description': """
Event Conference
================

Manage conferences, their sessions, speakers and registrations
with a simple public endpoint listing upcoming events.
""",
    'author': 'Example Author',
    'website': 'https://github.com/example/event_conference',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/event_security.xml',
        'security/ir.model.access.csv',
        'views/event_conference_views.xml',
        'views/event_session_views.xml',
        'data/event_data.xml',
    ],
    'demo': [
        'demo/event_demo.xml',
    ],
    'application': True,
    'installable': True,
}
