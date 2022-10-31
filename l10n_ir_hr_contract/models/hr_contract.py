from odoo import fields, models


class HrContract(models.Model):
    _inherit = "hr.contract"

    l10n_ir_daily_wages = fields.Monetary(
        string="Daily wages",
        store=True,
        help="Daily wages",
    )
    l10n_ir_child_allowance = fields.Monetary(
        string="Child Allowance",
        store=True,
        help="Monthly child allowance based on (daily wage x 3 x children counts).",
    )
    l10n_ir_grocery_allowance = fields.Monetary(
        string="Grocery Allowance",
        store=True,
        help="Monthly food allowance.",
    )
    l10n_ir_hiring_bonus = fields.Monetary(
        string="Hiring Bonus", store=True, help="Monthly rewardable extra hiring bonus."
    )
    l10n_ir_house_allowance = fields.Monetary(
        string="House Allowance",
        store=True,
        help="Monthly housing allowance.",
    )
    l10n_ir_life_insurance = fields.Monetary(
        string="Life Insurance", store=True, help="Monthly life insurance amount."
    )
    l10n_ir_responsibility_bonus = fields.Monetary(
        string="Responsibility Bonus ", store=True, help="Monthly liability bonus."
    )
    l10n_ir_seniority_benefits = fields.Monetary(
        string="Seniority Benefits",
        store=True,
        help="Monthly seniority benefits by each year of the contract.",
    )
    l10n_ir_supplement_insurance = fields.Monetary(
        string="Supplement Insurance",
        store=True,
        help="Monthly supplementary insurance amount.",
    )
    l10n_ir_technical_bonus = fields.Monetary(
        string="Technical Bonus", store=True, help="Monthly technical bonus."
    )
