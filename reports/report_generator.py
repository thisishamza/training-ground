def bar_charts_for_temperature(weather_readings):
    """generates a bar chart of maximum and minimum temperature on each day of a month

    Args:
        weather_readings ([List]): [Nested list of given month data]
    """
    CRED = '\33[31m'
    CBLUE = '\33[34m'
    CWHITE = '\33[37m'
    min_temperature = weather_readings[1]
    max_temperature = weather_readings[0]
    for day, weather_reading in enumerate(weather_readings[0]):
        print(f"{day+1} {CRED}", '+' * int(max_temperature[day]), f"{CWHITE} {max_temperature[day]}C")
        print(f"{day+1} {CBLUE}", '+' * int(min_temperature[day]), f"{CWHITE} {min_temperature[day]}C")


def single_bar_chart_temperature(weather_readings):
    """generates a bar chart of maximum and minimum temperature on each day of a month

    Args:
        weather_readings ([List]): [Nested list of given month data]
    """
    CRED = '\33[31m'
    CBLUE = '\33[34m'
    CWHITE = '\33[37m'
    min_temperature = weather_readings[1]
    max_temperature = weather_readings[0]
    for day, weather_reading in enumerate(weather_readings[0]):
        print(day+1, CBLUE + "+"*int(min_temperature[day]) + CRED + "+"*int(max_temperature[day]) + CWHITE, 
              min_temperature[day], "-", max_temperature[day])