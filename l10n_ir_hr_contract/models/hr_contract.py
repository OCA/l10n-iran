# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class HrContract(models.Model):
    _inherit = "hr.contract"

    l10n_ir_daily_wages = fields.Monetary(
        string="Daily wages",
        help="Daily wages",
    )
    l10n_ir_child_allowance = fields.Monetary(
        string="Child Allowance",
        help=(
            "Monthly child allowance based on"
            " (daily wage x 3 x children counts)."
        ),
    )
    l10n_ir_grocery_allowance = fields.Monetary(
        string="Grocery Allowance",
        help="Monthly food allowance.",
    )
    l10n_ir_hiring_bonus = fields.Monetary(
        string="Hiring Bonus",
        help="Monthly rewardable extra hiring bonus.",
    )
    l10n_ir_house_allowance = fields.Monetary(
        string="House Allowance",
        help="Monthly housing allowance.",
    )
    l10n_ir_life_insurance = fields.Monetary(
        string="Life Insurance",
        help="Monthly life insurance amount.",
    )
    l10n_ir_responsibility_bonus = fields.Monetary(
        string="Responsibility Bonus",
        help="Monthly liability bonus.",
    )
    l10n_ir_seniority_benefits = fields.Monetary(
        string="Seniority Benefits",
        help="Monthly seniority benefits by each year of the contract.",
    )
    l10n_ir_supplement_insurance = fields.Monetary(
        string="Supplement Insurance",
        help="Monthly supplementary insurance amount.",
    )
    l10n_ir_technical_bonus = fields.Monetary(
        string="Technical Bonus",
        help="Monthly technical bonus.",
    )
