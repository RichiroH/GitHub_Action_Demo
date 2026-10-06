from odoo import models, fields, _


class SurveySummaryWizard(models.TransientModel):
    _name = 'survey.summary.wizard'
    _description = 'Survey Summary Wizard'

    survey_id = fields.Many2one('feedback.survey', string='Survey', required=True, readonly=True)
    summary = fields.Text(string='Summary', readonly=True)

    def action_generate(self):
        self.ensure_one()
        survey = self.survey_id
        lines = [_('Survey: %s') % survey.name, _('Answers: %d') % survey.answer_count]
        for question in survey.question_ids:
            answers = survey.answer_ids.filtered(lambda a: a.question_id == question)
            lines.append(_('Q: %s (%d answers)') % (question.name, len(answers)))
        self.summary = '\n'.join(lines)
        return {
            'type': 'ir.actions.act_window',
            'name': _('Survey Summary'),
            'res_model': 'survey.summary.wizard',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
