from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class WarehouseBin(models.Model):
    _name = 'warehouse.bin'
    _description = 'Warehouse Bin'
    _order = 'zone_id, code'
    _rec_names_search = ['code', 'barcode']

    code = fields.Char(string='Bin Code', required=True)
    barcode = fields.Char(string='Barcode')
    zone_id = fields.Many2one('warehouse.zone', string='Zone', required=True)
    capacity = fields.Integer(string='Capacity (units)', default=100)
    occupied = fields.Integer(string='Occupied', default=0)
    free_space = fields.Integer(string='Free Space', compute='_compute_free_space', store=True)
    is_empty = fields.Boolean(string='Empty', compute='_compute_is_empty', store=True)
    product_tmpl_id = fields.Many2one('product.template', string='Product (example)')
    state = fields.Selection([
        ('active', 'Active'),
        ('locked', 'Locked'),
        ('maintenance', 'Maintenance'),
    ], string='State', default='active', tracking=True)
    active = fields.Boolean(string='Active', default=True)

    _unique_bin_code = models.Constraint(
        'UNIQUE(code)',
        'Bin code must be unique.',
    )

    _check_occupied_capacity = models.Constraint(
        'CHECK(occupied <= capacity)',
        'Occupied cannot exceed capacity.',
    )

    @api.depends('capacity', 'occupied')
    def _compute_free_space(self):
        for b in self:
            b.free_space = max(b.capacity - b.occupied, 0)

    @api.depends('occupied')
    def _compute_is_empty(self):
        for b in self:
            b.is_empty = b.occupied == 0

    @api.constrains('barcode')
    def _check_barcode(self):
        for b in self:
            if b.barcode and not b.barcode.isdigit():
                raise ValidationError(_('Barcode must contain digits only.'))

    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            args = ['|', ('code', operator, name), ('barcode', operator, name)] + args
        return super().name_search(name, args, operator, limit)

    def action_lock(self):
        for b in self:
            b.state = 'locked'

    def action_unlock(self):
        for b in self:
            b.state = 'active'

    @classmethod
    def _mark_empty_bins(cls):
        """Scheduled action target: flag empty bins to maintenance."""
        bins = cls.search([('is_empty', '=', True), ('state', '=', 'active')])
        bins.write({'state': 'maintenance'})
        return True
