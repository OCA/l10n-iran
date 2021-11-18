from odoo import _, api, fields, models


class ResUser(models.Model):
    _inherit = "res.users"

    calendar = fields.Char(
        string="Calendar",
        size=10,
        help="user current calendar",
        readonly=True,
        translate=True,
        compute="_compute_calendar",
    )

    @api.depends("user_id")
    def _compute_calendar(self):
        self.calendar = _(self.env["res.lang"]._lang_get(self.env.user.lang).calendar)
