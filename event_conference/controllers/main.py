from odoo import http
from odoo.http import request


class EventController(http.Controller):
    @http.route('/events/upcoming', type='json', auth='public')
    def upcoming_events(self):
        conferences = request.env['event.conference'].sudo().search([
            ('state', '=', 'confirmed'),
        ], order='date_begin asc', limit=20)
        return [{
            'id': c.id,
            'name': c.name,
            'date_begin': c.date_begin.isoformat() if c.date_begin else None,
            'location': c.location,
        } for c in conferences]
