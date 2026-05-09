# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.tests import TransactionCase


class TestL10nIrStates(TransactionCase):
    """Test the Iranian states and cities data."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.iran = cls.env.ref("base.ir")
        cls.states = cls.env["res.country.state"].search(
            [("country_id", "=", cls.iran.id)]
        )

    def test_states_loaded(self):
        """Iranian provinces should be loaded."""
        self.assertTrue(
            len(self.states) >= 31,
            f"Expected at least 31 states, got {len(self.states)}",
        )
        tehran = self.states.filtered(lambda s: s.name == "استان تهران")
        self.assertTrue(tehran, "Tehran province should exist")

    def test_cities_loaded(self):
        """Iranian cities should be loaded."""
        cities = self.env["res.city"].search([("country_id", "=", self.iran.id)])
        self.assertTrue(
            len(cities) >= 1000,
            f"Expected at least 1000 cities, got {len(cities)}",
        )

    def test_country_enforces_cities(self):
        """Iran should enforce cities and state required."""
        self.assertTrue(self.iran.enforce_cities)
        self.assertTrue(self.iran.state_required)

    def test_state_has_iran_code(self):
        """Each state should have an Iranian province code."""
        for state in self.states:
            self.assertTrue(
                state.code,
                f"State {state.name} should have a code",
            )
