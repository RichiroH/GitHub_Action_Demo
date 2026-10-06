from odoo.tests.common import TransactionCase


class TestEstateProperty(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.prop_type = cls.env['estate.property.type'].create({'name': 'House'})
        cls.seller = cls.env['res.partner'].create({'name': 'Seller'})
        cls.property = cls.env['estate.property'].create({
            'name': 'Test Property',
            'expected_price': 100000,
            'property_type_id': cls.prop_type.id,
            'seller_id': cls.seller.id,
        })

    def test_default_state(self):
        self.assertEqual(self.property.state, 'new')

    def test_sold_cancel_exclusion(self):
        self.property.action_sold()
        self.assertEqual(self.property.state, 'sold')
