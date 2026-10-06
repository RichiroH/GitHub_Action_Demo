from odoo import models, fields


class EstateCloseWizard(models.TransientModel):
    _name = 'estate.close.wizard'
    _description = 'Close Estate Property Wizard'

    property_id = fields.Many2one('estate.property', string='Property', required=True)
    final_note = fields.Text(string='Closing Note')

    def action_confirm_close(self):
        self.ensure_one()
        self.property_id.action_sold()
        return {'type': 'ir.actions.act_window_close'}
