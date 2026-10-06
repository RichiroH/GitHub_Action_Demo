from odoo import models, fields, api


class SurveySurvey(models.Model):
    _name = 'feedback.survey'
    _description = 'Customer Feedback Survey'
    _order = 'create_date desc'

    name = fields.Char(string='Survey Title', required=True)
    description = fields.Html(string='Description')
    partner_id = fields.Many2one('res.partner', string='Customer')
    question_ids = fields.One2many('feedback.question', 'survey_id', string='Questions')
    answer_ids = fields.One2many('feedback.answer', 'survey_id', string='Answers')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('closed', 'Closed'),
    ], string='State', default='draft', tracking=True)
    date_open = fields.Datetime(string='Opening Date', readonly=True)
    date_closed = fields.Datetime(string='Closing Date', readonly=True)
    answer_count = fields.Integer(string='Answer Count', compute='_compute_answer_count', store=True)
    active = fields.Boolean(string='Active', default=True)

    @api.depends('answer_ids')
    def _compute_answer_count(self):
        for s in self:
            s.answer_count = len(s.answer_ids)

    def action_open(self):
        for s in self:
            s.state = 'open'
            s.date_open = fields.Datetime.now()

    def action_close(self):
        for s in self:
            s.state = 'closed'
            s.date_closed = fields.Datetime.now()

    def action_open_summary_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Survey Summary',
            'res_model': 'survey.summary.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_survey_id': self.id},
        }
