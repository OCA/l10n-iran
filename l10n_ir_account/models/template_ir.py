# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models

from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template("ir")
    def _get_ir_template_data(self):
        """Return the Iranian chart of accounts template configuration."""
        return {
            "property_account_receivable_id": "l10n_ir_chart_111411",
            "property_account_payable_id": "l10n_ir_chart_211009",
            "property_account_expense_categ_id": "l10n_ir_chart_621309",
            "property_account_income_categ_id": "l10n_ir_chart_411003",
        }

    @template("ir", "res.company")
    def _get_ir_res_company(self):
        """Set Iranian company defaults."""
        return {
            self.env.company.id: {
                "anglo_saxon_accounting": False,
                "account_fiscal_country_id": "base.ir",
                "bank_account_code_prefix": "1111",
                "cash_account_code_prefix": "1113",
                "transfer_account_code_prefix": "1114",
                "account_default_pos_receivable_account_id": ("l10n_ir_chart_111411"),
            }
        }
