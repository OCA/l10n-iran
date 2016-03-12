# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2010-2013 OpenERP s.a. (<http://openerp.com>).
# Copyright (C) 2016 Farid Shahy (<fshahy@gmail.com>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Iran Country States',
    'category': 'Localization',
    'version': '9.0.1.0.0',
    'author': 'Farid Shahy, Odoo Community Association (OCA)' ,
    'website': 'http://fshahy.github.io',
    'license': 'AGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'data/res_country_states.xml',
    ],
    'images': [],
    'installable': True,
    'auto_install': False,
}