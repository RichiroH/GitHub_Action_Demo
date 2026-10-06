{
    'name': 'Customer Feedback Survey',
    'version': '19.0.1.0.0',
    'category': 'Marketing/Surveys',
    'summary': 'Collect and analyze customer feedback',
    'description': """
Customer Feedback Survey
========================

Build simple surveys, send them to customers and review
submitted answers with a quick wizard summary.
""",
    'author': 'Example Author',
    'website': 'https://github.com/example/customer_feedback_survey',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/survey_security.xml',
        'security/ir.model.access.csv',
        'views/survey_survey_views.xml',
        'views/survey_question_views.xml',
        'views/survey_answer_views.xml',
        'wizard/survey_summary_wizard_views.xml',
        'data/survey_data.xml',
    ],
    'demo': [
        'demo/survey_demo.xml',
    ],
    'application': True,
    'installable': True,
}
