# -*- coding: utf-8 -*-
# © 2015 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.addons.base_jalali_convert.convert_jalali import convert_jalali
from openerp import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.one
    def convert_jalali(self, obj):
        return convert_jalali(obj.date_order)
