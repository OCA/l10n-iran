# -*- coding: utf-8 -*-
# © 2015 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.addons.base_jalali_convert.convert_jalali import convert_jalali
from openerp import models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def convert_jalali(self, obj):
        self.ensure_one()
        date_iran = convert_jalali(obj.date_order)
        return date_iran


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.multi
    def convert_jalali(self, obj):
        self.ensure_one()
        date_iran = convert_jalali(obj.date_planned)
        return date_iran
