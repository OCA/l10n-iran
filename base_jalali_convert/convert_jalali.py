# -*- coding: utf-8 -*-
# © 2015 Elico Corp (https://www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import datetime
import logging
try:
    import jdatetime
except (ImportError, IOError) as err:
    _logger.debug(err)


def convert_jalali(orign_date_str):
    if orign_date_str:
        orign_date_list = orign_date_str.split(' ')
        orign_date = datetime.datetime.strptime(orign_date_list[0],
                                                "%Y-%m-%d")
        jalali_date = jdatetime.date.fromgregorian(day=orign_date.day,
                                                   month=orign_date.month,
                                                   year=orign_date.year)
        return ' '.join((orign_date.strftime("%Y-%m-%d"),
                         jalali_date.strftime('%Y-%m-%d')))
