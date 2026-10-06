from odoo.tests.common import TransactionCase


class TestSurvey(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.survey = cls.env['feedback.survey'].create({'name': 'Test Survey'})
        cls.question = cls.env['feedback.question'].create({
            'survey_id': cls.survey.id,
            'name': 'Did you enjoy?',
            'question_type': 'yesno',
        })

    def test_open_close(self):
        self.survey.action_open()
        self.assertEqual(self.survey.state, 'open')
        self.assertTrue(self.survey.date_open)
        self.survey.action_close()
        self.assertEqual(self.survey.state, 'closed')

    def test_answer_count(self):
        self.env['feedback.answer'].create({
            'survey_id': self.survey.id,
            'question_id': self.question.id,
            'boolean_value': True,
        })
        self.assertEqual(self.survey.answer_count, 1)
