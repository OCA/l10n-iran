from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    default_l10n_ir_grocery_allowance = fields.Float(
        default_model="hr.contract",
        string="Grocery Allowance",
        store=True,
        default=0.0,
        help="Monthly food allowance.",
    )

    default_l10n_ir_house_allowance = fields.Float(
        default_model="hr.contract",
        string="House Allowance",
        store=True,
        default=0.0,
        help="Monthly housing allowance.",
    )

    default_wage = fields.Float(
        default_model="hr.contract",
        string="Wage",
        default=0.0,
        store=True,
        help="Employee's monthly gross wage.",
    )

    default_l10n_ir_daily_wages = fields.Float(
        default_model="hr.contract",
        string="Daily Wage",
        default=0.0,
        store=True,
        help="Employee's monthly gross wage.",
    )

    default_l10n_ir_child_allowance = fields.Float(
        default_model="hr.contract",
        string="Child Allowance",
        default=0.0,
        store=True,
        help="Employee's monthly gross wage.",
    )
