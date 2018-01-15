# -*- coding: utf-8 -*-

def create_calendar_page(month, year, day=1):
    # -*- coding: utf-8 -*-
    import datetime
    today_num = datetime.date(year, month, day)
    today_str = today_num.strftime("%A, %B, %d, %Y")
    day_name_01 = today_num.strftime("%A")
    today_weekday = today_num.weekday()
    dt_28 = datetime.timedelta(28)
    dt_29 = datetime.timedelta(29)
    dt_30 = datetime.timedelta(30)
    dt_31 = datetime.timedelta(31)
    deltas = [dt_28, dt_29, dt_30, dt_31]

    row_01 = '-' * 20
    row_02 = "MO TU WE TH FR SA SU"
    row_03 = '-' * 20
    days = []

    for i in range(36):
        days.append(0)

    days[today_weekday] = today_num.day

    for i in range(today_weekday, len(days)):
        if days[i] == 0 and i < 36:
            days[i] = days[i - 1] + 1

    for i in range(len(deltas)):
        is_day_next_month = today_num + deltas[i]
        last_day_of_the_month = today_num + deltas[i] - datetime.timedelta(1)
        if is_day_next_month.day == 1:
            break

    for i in range(len(days)):
        if days[i] > last_day_of_the_month.day:
            days[i] = 0

    days_char = []
    for i in days:
        if i < 10:
            days_char_item = '0' + str(i)
            days_char.append(days_char_item)
        else:
            days_char.append(str(i))


    print last_day_of_the_month.day
    print row_01
    print row_02
    print row_03
    print days

    print days_char

    print day_name_01
    print today_weekday

    return today_str


print create_calendar_page(6, 2018)
