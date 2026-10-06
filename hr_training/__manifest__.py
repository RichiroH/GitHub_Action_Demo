{
    'name': 'HR Training',
    'version': '19.0.1.0.0',
    'category': 'Human Resources/Training',
    'summary': 'Manage training courses and enrollments',
    'description': """
HR Training
===========

Define training courses, sessions and enroll participants.
Includes a printable certificate of completion.
""",
    'author': 'Example Author',
    'website': 'https://github.com/example/hr_training',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/hr_training_security.xml',
        'security/ir.model.access.csv',
        'views/hr_training_course_views.xml',
        'views/hr_training_enrollment_views.xml',
        'report/hr_training_report_templates.xml',
        'data/hr_training_data.xml',
    ],
    'demo': [
        'demo/hr_training_demo.xml',
    ],
    'application': True,
    'installable': True,
}
