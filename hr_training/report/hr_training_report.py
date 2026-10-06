from odoo import models


class HrTrainingReport(models.AbstractModel):
    _name = 'report.hr_training.report_training_certificate'
    _description = 'Training Certificate Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['hr.training.enrollment'].browse(docids)
        return {
            'docs': docs,
            'doc_model': 'hr.training.enrollment',
        }
