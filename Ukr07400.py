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

    for i in range(42):
        days.append(0)

    days[today_weekday] = today_num.day

    for i in range(today_weekday, len(days)):
        if days[i] == 0 and i < 42:
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

    days_str = ' '.join(days_char)

    week_01 = days_char[:7]
    week_02 = days_char[7:14]
    week_03 = days_char[14:21]
    week_04 = days_char[21:28]
    week_05 = days_char[28:35]
    week_06 = days_char[35:]

    weeks = (str(week_01) + "\n" + str(week_02) + "\n" + str(week_03) + "\n" + str(week_04) + "\n" + str(week_05) + "\n" + str(week_06))

    print weeks

    row = (20 * "-" + "\nMO TU WE TH FR SA SU\n" + 20 * "-" + "\n")

    print row

    return today_str


print create_calendar_page(6, 2018)
