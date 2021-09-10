def bar_charts_for_temperature(readings_data_structure, date):
    """generates a bar chart of maximum and minimum temperature on each day of a month

    Args:
        data ([Dictionary]): [Nested dictionary of all data]
    """
    date = date.split('/')
    year = date[0]
    month = date[1]
    if int(month) < 10:
        month = month[1]
    CRED = '\33[31m'
    CBLUE = '\33[34m'
    CWHITE = '\33[37m'
    for date_key in readings_data_structure.keys():
        if date_key.split('-')[0] == year and date_key.split('-')[1] == month:
            max_temp = int(readings_data_structure[date_key]['Max TemperatureC'])
            min_temp = int(readings_data_structure[date_key]['Min TemperatureC'])
            print(f"{date_key.split('-')[-1]} {CRED}",
                  '+'*max_temp, f"{CWHITE} {max_temp} C")
            print(f"{date_key.split('-')[-1]} {CBLUE}",
                  '+'*min_temp, f"{CWHITE} {min_temp} C")


def single_bar_chart_temperature(readings_data_structure, date):
    date = date.split('/')
    year = date[0]
    month = date[1]
    if int(month) < 10:
        month = month[1]
    CRED = '\33[31m'
    CBLUE = '\33[34m'
    CWHITE = '\33[37m'
    for date_key in readings_data_structure.keys():
        if date_key.split('-')[0] == year and date_key.split('-')[1] == month:
            max_temp = int(readings_data_structure[date_key]['Max TemperatureC'])
            min_temp = int(readings_data_structure[date_key]['Min TemperatureC'])
            print(date_key.split('-')[-1], CBLUE + "+"*min_temp +
                  CRED + "+"*max_temp + CWHITE, min_temp, "-", max_temp)