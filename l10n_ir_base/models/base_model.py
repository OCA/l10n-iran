import logging

import babel.dates
import jdatetime as jd
import pytz

from odoo import api, models
from odoo.osv import expression
from odoo.tools.misc import (
    DEFAULT_SERVER_DATE_FORMAT,
    DEFAULT_SERVER_DATETIME_FORMAT,
    get_lang,
)

_logger = logging.getLogger(__name__)


def display_format_changer(df):
    return {
        "hh:00 dd MMM": "%d %b %H",
        "dd MMM yyyy": "%d %b %Y",
        "'W'w YYYY": "%A %Y",
        "MMMM yyyy": "%b %Y",
        "QQQ yyyy": "%b %Y",
        "yyyy": "%Y",
    }.get(df, "%d %b %Y")


class BaseModelExtend(models.AbstractModel):
    _inherit = "base"

    @api.model
    def _read_group_format_result(self, data, annotated_groupbys, groupby, domain):
        if self.env.user.calendar == "gregorian":
            return super(BaseModelExtend, self)._read_group_format_result(
                data, annotated_groupbys, groupby, domain
            )
        sections = []
        for gb in annotated_groupbys:
            ftype = gb["type"]
            value = data[gb["groupby"]]

            # full domain for this groupby spec
            d = None
            if value:
                if ftype == "many2one":
                    value = value[0]
                elif ftype in ("date", "datetime"):
                    locale = get_lang(self.env).code
                    fmt = (
                        DEFAULT_SERVER_DATETIME_FORMAT
                        if ftype == "datetime"
                        else DEFAULT_SERVER_DATE_FORMAT
                    )
                    tzinfo = None
                    range_start = value
                    range_end = value + gb["interval"]
                    # value from postgres is in local tz (so range is
                    # considered in local tz e.g. "day" is [00:00, 00:00[
                    # local rather than UTC which could be [11:00, 11:00]
                    # local) but domain and raw value should be in UTC
                    if gb["tz_convert"]:
                        tzinfo = range_start.tzinfo
                        range_start = range_start.astimezone(pytz.utc)
                        # take into account possible hour change between start and end
                        range_end = tzinfo.localize(range_end.replace(tzinfo=None))
                        range_end = range_end.astimezone(pytz.utc)

                    range_start = range_start.strftime(fmt)
                    range_end = range_end.strftime(fmt)
                    try:
                        if ftype == "datetime":
                            label = jd.date.fromgregorian(
                                day=value.day,
                                month=value.month,
                                year=value.year,
                                locale="fa_IR",
                            ).strftime(display_format_changer(gb["display_format"]))
                        else:
                            label = jd.date.fromgregorian(
                                day=value.day,
                                month=value.month,
                                year=value.year,
                                locale="fa_IR",
                            ).strftime(display_format_changer(gb["display_format"]))
                    except Exception:
                        _logger.warning(
                            "display_format_changer not found %s", gb["display_format"]
                        )
                        if ftype == "datetime":
                            label = babel.dates.format_datetime(
                                value,
                                format=gb["display_format"],
                                tzinfo=tzinfo,
                                locale=locale,
                            )
                        else:
                            label = babel.dates.format_date(
                                value, format=gb["display_format"], locale=locale
                            )
                    data[gb["groupby"]] = ("%s/%s" % (range_start, range_end), label)
                    d = [
                        "&",
                        (gb["field"], ">=", range_start),
                        (gb["field"], "<", range_end),
                    ]

            if d is None:
                d = [(gb["field"], "=", value)]
            sections.append(d)
        sections.append(domain)

        data["__domain"] = expression.AND(sections)
        if len(groupby) - len(annotated_groupbys) >= 1:
            data["__context"] = {"group_by": groupby[len(annotated_groupbys) :]}
        del data["id"]
        return data
