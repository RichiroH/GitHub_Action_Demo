from odoo.tests.common import TransactionCase


class TestFleetVehicle(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.vehicle = cls.env['fleet.vehicle.tracker'].create({
            'name': 'Test Van',
            'license_plate': 'TEST-999',
            'fuel_type': 'diesel',
        })

    def test_status_transitions(self):
        self.vehicle.action_set_maintenance()
        self.assertEqual(self.vehicle.status, 'maintenance')
        self.vehicle.action_set_active()
        self.assertEqual(self.vehicle.status, 'active')

    def test_mileage_distance(self):
        log = self.env['fleet.mileage.log'].create({
            'vehicle_id': self.vehicle.id,
            'start_odometer': 100,
            'end_odometer': 250,
        })
        self.assertEqual(log.distance, 150)
