# -*- coding: utf-8 -*-

def create_calendar_page(month, year, day=1):
    # -*- coding: utf-8 -*-
    import datetime
    today_num = datetime.date(year, month, day)
    today_str = today_num.strftime("%A, %B, %d, %Y")
    day_name_01 = today_num.strftime("%A")
    dt_28 = datetime.timedelta(28)
    dt_29 = datetime.timedelta(29)
    dt_30 = datetime.timedelta(30)


    print today_num + dt_28
    print today_num + dt_29
    print today_num + dt_30

    row_01 = '-' * 20
    row_02 = "MO TU WE TH FR SA SU"
    row_03 = '-' * 20

    week_01_list = []
    week_02_list = []
    week_03_list = []
    week_04_list = []
    week_05_list = []

    for i in range(7):
        week_01_list.append(0)
        week_02_list.append(0)
        week_03_list.append(0)
        week_04_list.append(0)
        week_05_list.append(0)

    if day_name_01 == 'Monday':
        week_01_list[0] = 1
    else:
        week_01_list[0] = 0

    if day_name_01 == 'Tuesday':
        week_01_list[1] = 1
    else:
        week_01_list[1] = 0

    if day_name_01 == 'Wednesday':
        week_01_list[2] = 1
    else:
        week_01_list[2] = 0

    if day_name_01 == 'Thursday':
        week_01_list[3] = 1
    else:
        week_01_list[3] = 0

    if day_name_01 == 'Friday':
        week_01_list[4] = 1
    else:
        week_01_list[4] = 0

    if day_name_01 == 'Saturday':
        week_01_list[5] = 1
    else:
        week_01_list[5] = 0

    if day_name_01 == 'Sunday':
        week_01_list[6] = 1
    else:
        week_01_list[6] = 0


    for i in range(len(week_01_list)):
        if week_01_list[i] > 0 and i < 6:
            week_01_list[i + 1] = week_01_list[i] + 1

    week_02_list[0] = week_01_list[i] + 1
    for i in range(1, len(week_02_list)):
        week_02_list[i] = week_02_list[i - 1] + 1

    week_03_list[0] = week_02_list[i] + 1
    for i in range(1, len(week_03_list)):
        week_03_list[i] = week_03_list[i - 1] + 1

    week_04_list[0] = week_03_list[i] + 1
    for i in range(1, len(week_04_list)):
        week_04_list[i] = week_04_list[i - 1] + 1

    week_05_list[0] = week_04_list[i] + 1
    for i in range(1, len(week_05_list)):
        week_05_list[i] = week_05_list[i - 1] + 1



    print week_01_list
    print week_02_list
    print week_03_list
    print week_04_list
    print week_05_list


    print row_01
    print row_02
    print row_03
    print day_name_01


    return today_str


print create_calendar_page(1, 2018)
