from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    l10n_ir_national_code = fields.Char(
        string="Natinal Code", size=11, help="National code used for iran."
    )
