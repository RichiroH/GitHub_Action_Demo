from odoo import models, fields, _
from odoo.exceptions import UserError


class EstateOffer(models.Model):
    _name = 'estate.offer'
    _description = 'Estate Offer'
    _order = 'price desc'

    price = fields.Float(string='Price', required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
    ], string='Status', copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline', store=True)

    def _compute_date_deadline(self):
        for offer in self:
            offer.date_deadline = fields.Date.add(offer.create_date or fields.Date.today(), days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            if offer.date_deadline:
                offer.validity = (offer.date_deadline - (offer.create_date.date() if offer.create_date else fields.Date.today())).days

    def action_accept(self):
        for offer in self:
            if any(o.status == 'accepted' for o in offer.property_id.offer_ids if o.id != offer.id):
                raise UserError(_('An offer is already accepted.'))
            offer.status = 'accepted'
            offer.property_id.buyer_id = offer.partner_id
            offer.property_id.selling_price = offer.price
            offer.property_id.state = 'offer_accepted'

    def action_refuse(self):
        for offer in self:
            offer.status = 'refused'
