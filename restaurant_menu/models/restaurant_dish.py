from odoo import models, fields


class RestaurantDish(models.Model):
    _name = 'restaurant.dish'
    _description = 'Dish'
    _order = 'sequence, name'

    name = fields.Char(string='Dish Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    category = fields.Selection([
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
    ], string='Category', default='main')
    price = fields.Monetary(string='Price', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')
    description = fields.Text(string='Description')
    allergens = fields.Char(string='Allergens')
    vegetarian = fields.Boolean(string='Vegetarian')
    spicy = fields.Boolean(string='Spicy')
    available = fields.Boolean(string='Available', default=True)
    image = fields.Image(string='Photo')
    menu_ids = fields.Many2many('restaurant.menu', string='Menus')
    active = fields.Boolean(string='Active', default=True)

    def toggle_available(self):
        for dish in self:
            dish.available = not dish.available
