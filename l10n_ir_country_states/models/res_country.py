# -*- coding: utf-8 -*-
# © 2016 Farid Shahy <fshahy@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class CountryState(models.Model):
    _inherit = 'res.country.state'

    name = fields.Char(translate=True)
