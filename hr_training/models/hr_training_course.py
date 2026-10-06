from odoo import models, fields


class HrTrainingCourse(models.Model):
    _name = 'hr.training.course'
    _description = 'Training Course'
    _order = 'name'

    name = fields.Char(string='Course Title', required=True)
    code = fields.Char(string='Code')
    description = fields.Html(string='Description')
    duration_hours = fields.Float(string='Duration (hours)')
    level = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ], string='Level', default='beginner')
    trainer_id = fields.Many2one('res.partner', string='Trainer')
    enrollment_ids = fields.One2many('hr.training.enrollment', 'course_id', string='Enrollments')
    active = fields.Boolean(string='Active', default=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    color = fields.Integer(string='Color Index')
