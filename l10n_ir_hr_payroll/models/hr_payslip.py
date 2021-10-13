from odoo import fields, models


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    l10n_ir_paid_days = fields.Float(
        compute="_compute_paid_days", string="Paid days", readonly=True
    )
    l10n_ir_valid_days = fields.Float(
        compute="_compute_valid_days", string="Valid days", readonly=True
    )

    def _compute_valid_days(self):
        # TODO from hr modules
        for record in self:
            record.l10n_ir_valid_days = 10

    def _compute_paid_days(self):
        # TODO from hr_holiday
        for record in self:
            record.l10n_ir_paid_days = 10
