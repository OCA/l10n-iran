from odoo import models

from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template("ir")
    def _get_ir_template_data(self):
        """Return the data necessary for the chart template.

        :return: all the values that are not stored but are used to instancieate
                 the chart of accounts. Common keys are:
                 * property_*
                 * code_digits
        :rtype: dict
        """
        return {
            "property_account_receivable_id": "l10n_ir_chart_111411",
            "property_account_payable_id": "l10n_ir_chart_211009",
            "property_account_expense_categ_id": "l10n_ir_chart_621309",
            "property_account_income_categ_id": "l10n_ir_chart_411003",
        }

    @template("ir", "res.company")
    def _get_ir_res_company(self):
        """Return the data to be written on the company.

        The data is a mapping the XMLID to the create/write values of a record.

        :rtype: dict[(str, int), dict]
        """
        return {
            self.env.company.id: {
                "anglo_saxon_accounting": False,
                "account_fiscal_country_id": "base.ir",
                "bank_account_code_prefix": "1014",
                "cash_account_code_prefix": "1015",
                "transfer_account_code_prefix": "1017",
                "account_default_pos_receivable_account_id": "l10n_ir_chart_111411",
            }
        }
