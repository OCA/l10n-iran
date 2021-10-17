import random
from datetime import timedelta

import jdatetime as jd
from babel.dates import format_datetime

from odoo import _, fields, models
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from odoo.tools.misc import get_lang


class AccountJournal(models.Model):
    _inherit = "account.journal"

    def get_bar_graph_datas(self):
        if self.env.user.calendar == "gregorian":
            return super(AccountJournal, self).get_bar_graph_datas()
        data = []
        today = fields.Datetime.now(self)
        data.append({"label": _("Due"), "value": 0.0, "type": "past"})
        day_of_week = int(format_datetime(today, "e", locale=get_lang(self.env).code))
        first_day_of_week = today + timedelta(days=-day_of_week + 1)
        for i in range(-1, 4):
            if i == 0:
                label = _("This Week")
            elif i == 3:
                label = _("Not Due")
            else:
                start_week = first_day_of_week + timedelta(days=i * 7)
                end_week = start_week + timedelta(days=6)
                if start_week.month == end_week.month:
                    start_week = jd.date.fromgregorian(
                        day=start_week.day,
                        month=start_week.month,
                        year=start_week.year,
                        locale="fa_IR",
                    )
                    end_week = jd.date.fromgregorian(
                        day=end_week.day,
                        month=end_week.month,
                        year=end_week.year,
                        locale="fa_IR",
                    )
                    label = (
                        str(start_week.day)
                        + "-"
                        + str(end_week.day)
                        + " "
                        + end_week.strftime("%b")
                    )
                else:
                    label = (
                        jd.date.fromgregorian(
                            day=start_week.day,
                            month=start_week.month,
                            year=start_week.year,
                            locale="fa_IR",
                        ).strftime("%d %b")
                        + "-"
                        + jd.date.fromgregorian(
                            day=end_week.day,
                            month=end_week.month,
                            year=end_week.year,
                            locale="fa_IR",
                        ).strftime("%d %b")
                    )
            data.append(
                {"label": label, "value": 0.0, "type": "past" if i < 0 else "future"}
            )

        # Build SQL query to find amount aggregated by week
        (select_sql_clause, query_args) = self._get_bar_graph_select_query()
        query = ""
        start_date = first_day_of_week + timedelta(days=-7)
        for i in range(0, 6):
            if i == 0:
                query += (
                    "("
                    + select_sql_clause
                    + " and invoice_date_due < '"
                    + start_date.strftime(DF)
                    + "')"
                )
            elif i == 5:
                query += (
                    " UNION ALL ("
                    + select_sql_clause
                    + " and invoice_date_due >= '"
                    + start_date.strftime(DF)
                    + "')"
                )
            else:
                next_date = start_date + timedelta(days=7)
                query += (
                    " UNION ALL ("
                    + select_sql_clause
                    + " and invoice_date_due >= '"
                    + start_date.strftime(DF)
                    + "' and invoice_date_due < '"
                    + next_date.strftime(DF)
                    + "')"
                )
                start_date = next_date

        self.env.cr.execute(query, query_args)
        query_results = self.env.cr.dictfetchall()
        is_sample_data = True
        for index in range(0, len(query_results)):
            if query_results[index].get("aggr_date") is not None:
                is_sample_data = False
                data[index]["value"] = query_results[index].get("total")

        [graph_title, graph_key] = self._graph_title_and_key()

        if is_sample_data:
            for index in range(0, len(query_results)):
                data[index]["type"] = "o_sample_data"
                # we use unrealistic values for the sample data
                data[index]["value"] = random.randint(0, 20)
                graph_key = _("Sample data")

        return [
            {
                "values": data,
                "title": graph_title,
                "key": graph_key,
                "is_sample_data": is_sample_data,
            }
        ]
