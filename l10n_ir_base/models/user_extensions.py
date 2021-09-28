from odoo import fields, models


class UsersExtensions(models.Model):
    _inherit = "res.users"

    calendar = fields.Selection(
        [("gregorian", "Gregorian Calendar"), ("jalali", "Jalali (Persian) Calendar")],
        default="gregorian",
    )
    date_format = fields.Selection(
        [("YYYY/MM/DD", "1399/01/01"), ("YYYY/M/D", "1399/1/1")], default="YYYY/MM/DD"
    )
