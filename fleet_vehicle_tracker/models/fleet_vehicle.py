from odoo import models, fields


class FleetVehicle(models.Model):
    _name = 'fleet.vehicle.tracker'
    _description = 'Fleet Vehicle'
    _order = 'license_plate'

    name = fields.Char(string='Vehicle Name', required=True)
    license_plate = fields.Char(string='License Plate')
    driver_id = fields.Many2one('res.partner', string='Driver')
    model = fields.Char(string='Model')
    brand = fields.Char(string='Brand')
    year = fields.Integer(string='Year')
    color = fields.Char(string='Color')
    fuel_type = fields.Selection([
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ], string='Fuel Type', default='gasoline')
    acquisition_date = fields.Date(string='Acquisition Date')
    odometer = fields.Integer(string='Odometer (km)')
    status = fields.Selection([
        ('active', 'Active'),
        ('maintenance', 'In Maintenance'),
        ('retired', 'Retired'),
    ], string='Status', default='active', tracking=True)
    mileage_log_ids = fields.One2many('fleet.mileage.log', 'vehicle_id', string='Mileage Logs')
    active = fields.Boolean(string='Active', default=True)
    note = fields.Text(string='Notes')

    def action_set_maintenance(self):
        for vehicle in self:
            vehicle.status = 'maintenance'

    def action_set_active(self):
        for vehicle in self:
            vehicle.status = 'active'
