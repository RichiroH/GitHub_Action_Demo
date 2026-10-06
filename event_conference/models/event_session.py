from odoo import models, fields, api


class EventSession(models.Model):
    _name = 'event.session'
    _description = 'Conference Session'
    _order = 'start_datetime'

    name = fields.Char(string='Session Title', required=True)
    conference_id = fields.Many2one('event.conference', string='Conference', required=True, ondelete='cascade')
    speaker_id = fields.Many2one('res.partner', string='Speaker')
    start_datetime = fields.Datetime(string='Start', required=True)
    end_datetime = fields.Datetime(string='End')
    duration = fields.Float(string='Duration (hours)', compute='_compute_duration', store=True)
    seats_max = fields.Integer(string='Maximum Seats')
    seats_taken = fields.Integer(string='Seats Taken', default=0)
    seats_available = fields.Integer(string='Available Seats', compute='_compute_seats_available', store=True)
    tag_ids = fields.Many2many('res.partner.category', string='Tags')

    @api.depends('start_datetime', 'end_datetime')
    def _compute_duration(self):
        for s in self:
            if s.start_datetime and s.end_datetime:
                s.duration = (s.end_datetime - s.start_datetime).total_seconds() / 3600.0
            else:
                s.duration = 0.0

    @api.depends('seats_max', 'seats_taken')
    def _compute_seats_available(self):
        for s in self:
            s.seats_available = (s.seats_max - s.seats_taken) if s.seats_max else 0
