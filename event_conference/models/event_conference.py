from odoo import models, fields, api


class EventConference(models.Model):
    _name = 'event.conference'
    _description = 'Conference'
    _order = 'date_begin'

    name = fields.Char(string='Conference Name', required=True)
    organizer_id = fields.Many2one('res.partner', string='Organizer')
    date_begin = fields.Datetime(string='Start Date', required=True)
    date_end = fields.Datetime(string='End Date')
    location = fields.Char(string='Location')
    capacity = fields.Integer(string='Capacity')
    seats_taken = fields.Integer(string='Seats Taken', compute='_compute_seats_taken', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='State', default='draft', tracking=True)
    session_ids = fields.One2many('event.session', 'conference_id', string='Sessions')
    active = fields.Boolean(string='Active', default=True)
    color = fields.Integer(string='Color Index')

    @api.depends('session_ids', 'session_ids.seats_taken')
    def _compute_seats_taken(self):
        for conf in self:
            conf.seats_taken = sum(conf.session_ids.mapped('seats_taken'))

    def action_confirm(self):
        for conf in self:
            conf.state = 'confirmed'

    def action_done(self):
        for conf in self:
            conf.state = 'done'

    def action_draft(self):
        for conf in self:
            conf.state = 'draft'
