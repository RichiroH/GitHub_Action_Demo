from odoo import models, fields, api


class RestaurantMenu(models.Model):
    _name = 'restaurant.menu'
    _description = 'Menu'
    _order = 'date_validity desc'

    name = fields.Char(string='Menu Name', required=True)
    code = fields.Char(string='Reference')
    date_validity = fields.Date(string='Valid From')
    is_active = fields.Boolean(string='Currently Active', default=True)
    dish_ids = fields.Many2many('restaurant.dish', string='Dishes')
    dish_count = fields.Integer(string='Dish Count', compute='_compute_dish_count', store=True)
    total_price = fields.Monetary(string='Total Price', compute='_compute_total_price', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')

    @api.depends('dish_ids')
    def _compute_dish_count(self):
        for menu in self:
            menu.dish_count = len(menu.dish_ids)

    @api.depends('dish_ids', 'dish_ids.price')
    def _compute_total_price(self):
        for menu in self:
            menu.total_price = sum(menu.dish_ids.mapped('price'))
