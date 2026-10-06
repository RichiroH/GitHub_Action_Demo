from odoo import models, fields, _
from odoo.exceptions import UserError


class HrTrainingEnrollment(models.Model):
    _name = 'hr.training.enrollment'
    _description = 'Training Enrollment'
    _order = 'date_start desc'

    course_id = fields.Many2one('hr.training.course', string='Course', required=True, ondelete='cascade')
    attendee_id = fields.Many2one('res.partner', string='Attendee', required=True)
    date_start = fields.Datetime(string='Start Date', required=True)
    date_end = fields.Datetime(string='End Date')
    score = fields.Float(string='Score (%)')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], string='State', default='draft', tracking=True)
    certificate_report = fields.Char(string='Certificate')

    def action_enroll(self):
        for enr in self:
            enr.state = 'enrolled'

    def action_complete(self):
        for enr in self:
            if enr.score >= 60:
                enr.state = 'completed'
            else:
                enr.state = 'failed'

    def action_print_certificate(self):
        self.ensure_one()
        if self.state != 'completed':
            raise UserError(_('Certificate is only available for completed enrollments.'))
        return self.env.ref('hr_training.action_report_training_certificate').report_action(self)
