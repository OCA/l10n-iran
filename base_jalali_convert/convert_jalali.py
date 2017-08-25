import datetime
import jdatetime


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
