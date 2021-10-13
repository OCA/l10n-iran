from odoo import api, fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    l10n_ir_contract_end_date = fields.Date(
        string="End date of the contract",
        compute="_compute_last_contract_date",
        readonly=True,
    )

    l10n_ir_father_name = fields.Char(string="father name", copy=True)

    l10n_ir_first_name = fields.Char(string="first name", copy=True)

    l10n_ir_last_name = fields.Char(string="last name", copy=True)

    l10n_ir_insurance_id = fields.Char(
        string="Insurance ID",
        copy=True,
        help="The insurance ID that will be on the insurance list.",
    )

    l10n_ir_insured = fields.Boolean(
        string="Insured",
        default=False,
        help="Should the employee receive insurance or not.",
    )

    l10n_ir_national_id = fields.Char(string="National Code", copy=True)

    def _get_last_contracts(self):
        self.ensure_one()
        return self.sudo().contract_ids.filtered(lambda c: c.state != "cancel")

    @api.depends("contract_ids.state", "contract_ids.date_end")
    def _compute_last_contract_date(self):
        for employee in self:
            contracts = employee._get_last_contracts()
            if contracts:
                employee.l10n_ir_contract_end_date = max(
                    contracts.mapped("date_end"), key=lambda e: e is not False
                )
            else:
                employee.l10n_ir_contract_end_date = False
