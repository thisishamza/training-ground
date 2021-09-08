def chart_on_month(data):
    """generates a bar chart of maximum and minimum temperature on each day of a month

    Args:
        data ([Dictionary]): [Nested dictionary of all data]
    """
    year = input("Enter Year for Bar-Chart as YYYY ")
    month = input("Enter Month for Bar-Chart as MM ")
    if int(month) < 10:
        month = month[1]
    CRED = '\33[31m'
    CBLUE = '\33[34m'
    CWHITE = '\33[37m'
    for date_key in data.keys():
        if date_key.split('-')[0] == year and date_key.split('-')[1] == month:
            max_temp = int(data[date_key]['Max TemperatureC'])
            min_temp = int(data[date_key]['Min TemperatureC'])
            print(date_key.split('-')[-1], CRED + "+"*max_temp + CWHITE, max_temp, "C")
            print(date_key.split('-')[-1], CBLUE + "+"*min_temp + CWHITE, min_temp, "C\n")


def chart_on_month_bonus_task(data):
    year = input("Enter Year for Bar-Chart as YYYY ")
    month = input("Enter Month for Bar-Chart as MM ")
    if int(month) < 10:
        month = month[1]
    CRED = '\33[31m'
    CBLUE = '\33[34m'
    CWHITE = '\33[37m'
    for date_key in data.keys():
        if date_key.split('-')[0] == year and date_key.split('-')[1] == month:
            max_temp = int(data[date_key]['Max TemperatureC'])
            min_temp = int(data[date_key]['Min TemperatureC'])
            print(date_key.split('-')[-1], CBLUE + "+"*min_temp + CRED + "+"*max_temp + CWHITE, min_temp, "-", max_temp)