# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.tests import TransactionCase


class TestL10nIrHrContract(TransactionCase):
    """Test the Iranian HR contract localization."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.employee = cls.env["hr.employee"].create(
            {"name": "Test Employee"}
        )
        cls.contract = cls.env["hr.contract"].create(
            {
                "name": "Test Contract",
                "employee_id": cls.employee.id,
                "wage": 50000000,
                "state": "open",
            }
        )

    def test_contract_fields_exist(self):
        """All Iranian contract fields should be available."""
        fields_to_check = [
            "l10n_ir_daily_wages",
            "l10n_ir_child_allowance",
            "l10n_ir_grocery_allowance",
            "l10n_ir_hiring_bonus",
            "l10n_ir_house_allowance",
            "l10n_ir_life_insurance",
            "l10n_ir_responsibility_bonus",
            "l10n_ir_seniority_benefits",
            "l10n_ir_supplement_insurance",
            "l10n_ir_technical_bonus",
        ]
        for field_name in fields_to_check:
            self.assertIn(
                field_name,
                self.contract._fields,
                f"Field {field_name} should exist on hr.contract",
            )

    def test_contract_fields_set_and_read(self):
        """Iranian contract fields should store and return values."""
        self.contract.l10n_ir_daily_wages = 1500000
        self.contract.l10n_ir_house_allowance = 5000000
        self.contract.l10n_ir_child_allowance = 3000000
        self.assertEqual(self.contract.l10n_ir_daily_wages, 1500000)
        self.assertEqual(self.contract.l10n_ir_house_allowance, 5000000)
        self.assertEqual(self.contract.l10n_ir_child_allowance, 3000000)

    def test_config_settings_defaults(self):
        """ResConfigSettings should have Iranian default fields."""
        config = self.env["res.config.settings"].create({})
        self.assertIn(
            "default_l10n_ir_daily_wages", config._fields,
        )
        self.assertIn(
            "default_l10n_ir_house_allowance", config._fields,
        )
        self.assertIn(
            "default_l10n_ir_grocery_allowance", config._fields,
        )
        self.assertIn(
            "default_l10n_ir_child_allowance", config._fields,
        )
