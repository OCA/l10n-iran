# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.tests import TransactionCase


class TestL10nIrAccount(TransactionCase):
    """Test the Iranian chart of accounts template."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.chart_template = cls.env["account.chart.template"]._get_chart_template(
            "ir"
        )

    def test_chart_template_exists(self):
        """The IR chart template should be available."""
        self.assertIsNotNone(
            self.chart_template,
            "Iranian chart template should exist",
        )

    def test_chart_template_data(self):
        """Chart template should return proper configuration."""
        data = self.env["account.chart.template"]._get_ir_template_data()
        self.assertIn("property_account_receivable_id", data)
        self.assertIn("property_account_payable_id", data)
        self.assertIn("property_account_expense_categ_id", data)
        self.assertIn("property_account_income_categ_id", data)

    def test_company_defaults(self):
        """Company defaults should be properly set."""
        defaults = self.env["account.chart.template"]._get_ir_res_company()
        company_id = self.env.company.id
        self.assertIn(company_id, defaults)
        company_defaults = defaults[company_id]
        self.assertFalse(company_defaults["anglo_saxon_accounting"])
        self.assertEqual(
            company_defaults["account_fiscal_country_id"], "base.ir"
        )
        self.assertEqual(
            company_defaults["bank_account_code_prefix"], "1111"
        )
        self.assertEqual(
            company_defaults["cash_account_code_prefix"], "1113"
        )
        self.assertEqual(
            company_defaults["transfer_account_code_prefix"], "1114"
        )

    def test_account_templates_loaded(self):
        """CSV templates should contain valid account data."""
        accounts = self.env["account.chart.template"]._get_chart_template_data(
            "ir"
        )
        self.assertTrue(
            accounts.get("account.account"), "Account data should be loaded"
        )
        self.assertTrue(
            accounts.get("account.tax"), "Tax data should be loaded"
        )
        self.assertTrue(
            accounts.get("account.fiscal.position"),
            "Fiscal position data should be loaded",
        )

    def test_chart_installation(self):
        """Installing the Iranian chart should create accounts."""
        company = self.env.company
        chart_template = self.env["account.chart.template"]._get_chart_template(
            "ir"
        )
        self.assertIsNotNone(
            chart_template, "Chart template should be returned"
        )
        # Load the chart for the current company
        self.env["account.chart.template"]._load(
            "ir", company
        )
        # Check that accounts were created
        accounts = self.env["account.account"].search(
            [("company_id", "=", company.id)]
        )
        self.assertTrue(
            len(accounts) > 10,
            f"Expected more than 10 accounts after chart install, got {len(accounts)}",
        )

    def test_vat_taxes_created(self):
        """VAT 10% taxes should be created after chart install."""
        company = self.env.company
        self.env["account.chart.template"]._load("ir", company)
        taxes = self.env["account.tax"].search(
            [
                ("company_id", "=", company.id),
                ("amount", "=", 10),
            ]
        )
        self.assertTrue(len(taxes) > 0, "VAT 10% taxes should exist")

    def test_tax_groups_created(self):
        """Tax groups should be created."""
        company = self.env.company
        self.env["account.chart.template"]._load("ir", company)
        tax_groups = self.env["account.tax.group"].search(
            [("company_id", "=", company.id)]
        )
        self.assertTrue(len(tax_groups) >= 3, "At least 3 tax groups should exist")

    def test_account_types_fixed(self):
        """Cash accounts should have asset_cash type, not income."""
        company = self.env.company
        self.env["account.chart.template"]._load("ir", company)
        cash_account = self.env["account.account"].search(
            [
                ("company_id", "=", company.id),
                ("code", "=", "111001"),
            ],
            limit=1,
        )
        if cash_account:
            self.assertEqual(
                cash_account.account_type, "asset_cash",
                "Cash account code 111001 should have type asset_cash",
            )

    def test_revenue_accounts_have_income_type(self):
        """Revenue accounts should have income type."""
        company = self.env.company
        self.env["account.chart.template"]._load("ir", company)
        revenue_account = self.env["account.account"].search(
            [
                ("company_id", "=", company.id),
                ("code", "=", "411001"),
            ],
            limit=1,
        )
        if revenue_account:
            self.assertEqual(
                revenue_account.account_type, "income",
                "Revenue account code 411001 should have type income",
            )

    def test_currency_configured(self):
        """IRR currency should be configured."""
        irr = self.env.ref("base.IRR")
        self.assertTrue(irr.active, "IRR currency should be active")
        self.assertEqual(irr.name, "IRR")
        self.assertEqual(irr.symbol, "ریال")

    def test_banks_loaded(self):
        """Iranian banks should be available."""
        banks = self.env["res.bank"].search(
            [("country", "=", self.env.ref("base.ir").id)]
        )
        self.assertTrue(
            len(banks) >= 20,
            f"Expected at least 20 Iranian banks, got {len(banks)}",
        )
