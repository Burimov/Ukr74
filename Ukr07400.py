# -*- coding: utf-8 -*-

def create_calendar_page(month, year, day = 1):
    # -*- coding: utf-8 -*-
    import datetime
    today_num = datetime.date(year, month, day)
    today_str = today_num.strftime("%A, %B, %d, %Y")

    return today_str


print create_calendar_page(1, 2018)

