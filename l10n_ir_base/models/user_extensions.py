from odoo import fields, models


class UsersExtensions(models.Model):
    _inherit = "res.users"

    l10n_ir_national_code = fields.Char(
        string="Natinal Code", size=11, help="National code used for iran."
    )

    calendar = fields.Selection(
        [("gregorian", "Gregorian Calendar"), ("jalali", "Jalali (Persian) Calendar")],
        default="gregorian",
    )


class ResPartner(models.Model):
    _inherit = "res.partner"

    l10n_ir_national_code = fields.Char(
        string="National Code", size=11, help="National code used for iran."
    )
