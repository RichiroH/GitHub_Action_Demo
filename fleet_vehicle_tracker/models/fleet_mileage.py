from odoo import models, fields, _
from odoo.exceptions import UserError


class FleetMileageLog(models.Model):
    _name = 'fleet.mileage.log'
    _description = 'Fleet Mileage Log'
    _order = 'date desc'

    vehicle_id = fields.Many2one('fleet.vehicle.tracker', string='Vehicle', required=True, ondelete='cascade')
    date = fields.Date(string='Date', default=fields.Date.context_today, required=True)
    start_odometer = fields.Integer(string='Start Odometer')
    end_odometer = fields.Integer(string='End Odometer')
    distance = fields.Integer(string='Distance (km)', compute='_compute_distance', store=True)
    purpose = fields.Char(string='Purpose')
    driver_id = fields.Many2one('res.partner', string='Driver', related='vehicle_id.driver_id', store=True)

    def _compute_distance(self):
        for log in self:
            log.distance = (log.end_odometer - log.start_odometer) if log.end_odometer and log.start_odometer else 0

    def write(self, vals):
        res = super().write(vals)
        for log in self:
            if log.start_odometer and log.end_odometer and log.end_odometer < log.start_odometer:
                raise UserError(_('End odometer cannot be lower than start odometer.'))
        return res
