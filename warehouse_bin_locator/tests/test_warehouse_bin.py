from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestWarehouseBin(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.zone = cls.env['warehouse.zone'].create({'name': 'Z', 'code': 'Z'})
        cls.bin = cls.env['warehouse.bin'].create({
            'code': 'Z-01',
            'zone_id': cls.zone.id,
            'capacity': 50,
            'occupied': 10,
        })

    def test_free_space(self):
        self.assertEqual(self.bin.free_space, 40)

    def test_is_empty_flag(self):
        self.assertFalse(self.bin.is_empty)
        self.bin.occupied = 0
        self.assertTrue(self.bin.is_empty)

    def test_barcode_validation(self):
        with self.assertRaises(ValidationError):
            self.env['warehouse.bin'].create({
                'code': 'Z-02',
                'zone_id': self.zone.id,
                'barcode': 'ABC-not-digits',
            })
