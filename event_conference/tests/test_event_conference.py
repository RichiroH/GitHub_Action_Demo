from odoo.tests.common import TransactionCase


class TestEventConference(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.conference = cls.env['event.conference'].create({
            'name': 'Test Conf',
            'capacity': 100,
        })

    def test_confirm_done_flow(self):
        self.conference.action_confirm()
        self.assertEqual(self.conference.state, 'confirmed')
        self.conference.action_done()
        self.assertEqual(self.conference.state, 'done')

    def test_seats_taken_aggregation(self):
        self.env['event.session'].create({
            'name': 'S1',
            'conference_id': self.conference.id,
            'seats_taken': 30,
        })
        self.assertEqual(self.conference.seats_taken, 30)
