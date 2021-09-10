def average_highest_lowest_temperature(readings_data_structure, date):
    """looks for highest temperature/humidity in a given year and month

    Args:
        data ([type]): [description]
    """
    date = date.split('/')
    year = date[0]
    month = date[1]
    count = 0
    avg_highest_temperature = 0
    avg_lowest_temperature = 0
    avg_mean_humidity = 0
    for date_key in readings_data_structure.keys():
        if date_key.split('-')[0] == year and date_key.split('-')[1] == month:
            count += 1
            avg_highest_temperature += readings_data_structure[date_key]['Max TemperatureC']
            avg_lowest_temperature += readings_data_structure[date_key]['Min TemperatureC']
            avg_mean_humidity += readings_data_structure[date_key]['Mean Humidity']

    print(f"Avg Highest: {avg_highest_temperature//count}C")
    print(f"Avg Lowest: {avg_lowest_temperature//count}C")
    print(f"Avg Humidity: {avg_mean_humidity//count}%")


def highest_lowest_temperature(readings_data_structure, date):
    """looks for highest temperature/humidity and lowest temperature given a particular year

    Args:
        data ([Dictionary]): [A nested dictionary containing all data]
    """
    year = date
    highest_temperature = 0
    highest_temperature_day = ""
    lowest_temperature = 1000
    lowest_temperature_day = ""
    highest_humidity = 0
    highest_humidity_day = ""

    for date_key in readings_data_structure.keys():
        if date_key.split('-')[0] == year:
            if highest_temperature < readings_data_structure[date_key]['Max TemperatureC']:
                highest_temperature = readings_data_structure[date_key]['Max TemperatureC']
                highest_temperature_day = date_key
            if lowest_temperature > readings_data_structure[date_key]['Min TemperatureC']:
                lowest_temperature = readings_data_structure[date_key]['Min TemperatureC']
                lowest_temperature_day = date_key
            if highest_humidity < readings_data_structure[date_key]['Max Humidity']:
                highest_humidity = readings_data_structure[date_key]['Max Humidity']
                highest_humidity_day = date_key

    print(f"Highest: {highest_temperature}C on {highest_temperature_day}")
    print(f"Lowest: {lowest_temperature}C on {lowest_temperature_day}")
    print(f"Humidity: {highest_humidity}% on {highest_humidity_day}")
