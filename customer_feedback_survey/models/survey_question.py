from odoo import models, fields


class SurveyQuestion(models.Model):
    _name = 'feedback.question'
    _description = 'Survey Question'
    _order = 'sequence, id'

    survey_id = fields.Many2one('feedback.survey', string='Survey', required=True, ondelete='cascade')
    sequence = fields.Integer(string='Sequence', default=10)
    name = fields.Char(string='Question', required=True)
    question_type = fields.Selection([
        ('text', 'Text'),
        ('stars', 'Star Rating'),
        ('yesno', 'Yes/No'),
    ], string='Type', default='text', required=True)
    required = fields.Boolean(string='Required', default=True)
