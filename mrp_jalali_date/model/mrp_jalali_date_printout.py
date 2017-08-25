# -*- coding: utf-8 -*-
# © 2015 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.addons.base_jalali_convert.convert_jalali import convert_jalali
from openerp import models, api
import time


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.one
    def convert_jalali(self, obj):
        date_iran = convert_jalali(obj.date_planned)
        return date_iran

    def get_print_jalali_date(self):
        date_iran = convert_jalali(time.strftime('%Y-%m-%d'))
        return date_iran
