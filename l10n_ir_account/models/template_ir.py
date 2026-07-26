# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import models

from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template("ir")
    def _get_ir_template_data(self):
        """Return the data necessary for the chart template.

        :return: all the values that are not stored but are used to instantiate
                 the chart of accounts. Common keys are:
                 * property_*
                 * code_digits
        :rtype: dict
        """
        return {
            "property_account_receivable_id": "l10n_ir_chart_111301",
            "property_account_payable_id": "l10n_ir_chart_211001",
            "property_account_expense_categ_id": "l10n_ir_chart_511000",
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
                "bank_account_code_prefix": "1110",
                "cash_account_code_prefix": "1110",
                "transfer_account_code_prefix": "1110",
                "account_default_pos_receivable_account_id": "l10n_ir_chart_111411",
                "income_currency_exchange_account_id": "l10n_ir_chart_621508",
                "expense_currency_exchange_account_id": "l10n_ir_chart_621511",
                "account_sale_tax_id": "ir_sale_tax_10",
                "account_purchase_tax_id": "ir_purchase_tax_10",
            }
        }
