from odoo import models, fields


class SurveyAnswer(models.Model):
    _name = 'feedback.answer'
    _description = 'Survey Answer'
    _order = 'create_date desc'

    survey_id = fields.Many2one('feedback.survey', string='Survey', required=True, ondelete='cascade')
    question_id = fields.Many2one('feedback.question', string='Question', required=True)
    partner_id = fields.Many2one('res.partner', string='Respondent')
    text_value = fields.Text(string='Text Answer')
    star_value = fields.Integer(string='Stars (1-5)')
    boolean_value = fields.Boolean(string='Yes/No')
    create_date = fields.Datetime(string='Submitted On', readonly=True)
