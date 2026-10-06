from odoo import models, fields, _
from odoo.exceptions import UserError


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'
    _order = 'id desc'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Available From')
    expected_price = fields.Float(string='Expected Price', required=True)
    selling_price = fields.Float(string='Selling Price', readonly=True, copy=False)
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area (sqm)')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], string='Garden Orientation')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    seller_id = fields.Many2one('res.partner', string='Seller', required=True)
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False, readonly=True)
    offer_ids = fields.One2many('estate.offer', 'property_id', string='Offers')
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ], string='State', default='new', required=True, copy=False, tracking=True)
    active = fields.Boolean(string='Active', default=True)

    def action_cancel(self):
        for prop in self:
            if prop.state == 'sold':
                raise UserError(_('Sold properties cannot be cancelled.'))
            prop.state = 'cancelled'

    def action_sold(self):
        for prop in self:
            if prop.state == 'cancelled':
                raise UserError(_('Cancelled properties cannot be sold.'))
            prop.state = 'sold'
