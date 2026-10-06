from odoo.tests.common import TransactionCase


class TestHrTraining(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.course = cls.env['hr.training.course'].create({
            'name': 'Test Course',
            'duration_hours': 4.0,
        })
        cls.attendee = cls.env['res.partner'].create({'name': 'Jane Trainee'})
        cls.enrollment = cls.env['hr.training.enrollment'].create({
            'course_id': cls.course.id,
            'attendee_id': cls.attendee.id,
            'score': 80,
        })

    def test_completion_pass(self):
        self.enrollment.action_enroll()
        self.enrollment.action_complete()
        self.assertEqual(self.enrollment.state, 'completed')

    def test_completion_fail(self):
        self.enrollment.score = 40
        self.enrollment.action_enroll()
        self.enrollment.action_complete()
        self.assertEqual(self.enrollment.state, 'failed')
