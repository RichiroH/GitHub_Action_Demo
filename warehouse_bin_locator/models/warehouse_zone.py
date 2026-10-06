from odoo import models, fields


class WarehouseZone(models.Model):
    _name = 'warehouse.zone'
    _description = 'Warehouse Zone'
    _order = 'code'

    name = fields.Char(string='Zone Name', required=True)
    code = fields.Char(string='Code', required=True)
    bin_ids = fields.One2many('warehouse.bin', 'zone_id', string='Bins')
    bin_count = fields.Integer(string='Bin Count', compute='_compute_bin_count', store=True)
    active = fields.Boolean(string='Active', default=True)
    note = fields.Text(string='Notes')

    def _compute_bin_count(self):
        for zone in self:
            zone.bin_count = len(zone.bin_ids)
