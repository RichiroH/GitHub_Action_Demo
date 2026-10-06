from odoo.tests.common import TransactionCase


class TestRestaurantMenu(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.dish = cls.env['restaurant.dish'].create({
            'name': 'Salad',
            'category': 'starter',
            'price': 8.0,
        })
        cls.menu = cls.env['restaurant.menu'].create({
            'name': 'Lunch Menu',
        })

    def test_dish_count(self):
        self.menu.dish_ids = [(4, self.dish.id)]
        self.assertEqual(self.menu.dish_count, 1)
        self.assertEqual(self.menu.total_price, 8.0)

    def test_toggle_available(self):
        self.assertTrue(self.dish.available)
        self.dish.toggle_available()
        self.assertFalse(self.dish.available)
