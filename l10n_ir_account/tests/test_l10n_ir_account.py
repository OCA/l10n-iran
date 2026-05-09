# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.tests import TransactionCase


class TestL10nIrAccount(TransactionCase):
    """Test the Iranian chart of accounts template."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company = cls.env.company
        cls.env["account.chart.template"]._load("ir", cls.company, install_demo=False)

    def test_chart_installation(self):
        """Installing the Iranian chart should create accounts."""
        accounts = self.env["account.account"].search(
            [("company_ids", "=", self.company.id)]
        )
        self.assertTrue(
            len(accounts) > 10,
            f"Expected more than 10 accounts after chart install, got {len(accounts)}",
        )

    def test_vat_taxes_created(self):
        """VAT 10% taxes should be created after chart install."""
        taxes = self.env["account.tax"].search(
            [
                ("company_id", "=", self.company.id),
                ("amount", "=", 10),
            ]
        )
        self.assertTrue(len(taxes) > 0, "VAT 10% taxes must exist")

    def test_tax_groups_created(self):
        """Tax groups should be created."""
        tax_groups = self.env["account.tax.group"].search(
            [("company_id", "=", self.company.id)]
        )
        self.assertTrue(len(tax_groups) >= 3, "At least 3 tax groups exist")

    def test_account_types_fixed(self):
        """Cash accounts should have asset_cash type, not income."""
        cash_account = self.env["account.account"].search(
            [
                ("company_ids", "=", self.company.id),
                ("code", "=", "111001"),
            ],
            limit=1,
        )
        self.assertTrue(cash_account, "Cash account 111001 must exist")
        self.assertEqual(
            cash_account.account_type,
            "asset_cash",
            "Cash account code 111001 must have type asset_cash",
        )

    def test_revenue_accounts_have_income_type(self):
        """Revenue accounts should have income type."""
        revenue_account = self.env["account.account"].search(
            [
                ("company_ids", "=", self.company.id),
                ("code", "=", "411001"),
            ],
            limit=1,
        )
        self.assertTrue(revenue_account, "Revenue account 411001 must exist")
        self.assertEqual(
            revenue_account.account_type,
            "income",
            "Revenue account code 411001 must have type income",
        )

    def test_currency_configured(self):
        """IRR currency should be configured."""
        irr = self.env.ref("base.IRR")
        self.assertTrue(irr.active, "IRR currency must be active")
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
