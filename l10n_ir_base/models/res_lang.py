from odoo import fields, models


class UsersExtensions(models.Model):
    _inherit = "res.lang"


    calendar = fields.Selection(
        [("gregorian", "Gregorian Calendar"), ("jalali", "Jalali (Persian) Calendar")],
        default="jalali",
    )

    