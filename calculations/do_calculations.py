def temp_given_month(data):
    """looks for highest temperature/humidity in a given year and month

    Args:
        data ([type]): [description]
    """
    year = input("Enter Year for Avg temperature and humidity as YYYY ")
    month = input("Enter Month for Avg temperature and humidity as MM ")
    if int(month) < 10:
        month = month[1]
    count = 0
    avg_highest_temperature = 0
    avg_lowest_temperature = 0
    avg_mean_humidity = 0
    for date_key in data.keys():
        if date_key.split('-')[0] == year and date_key.split('-')[1] == month:
            count += 1
            avg_highest_temperature += data[date_key]['Max TemperatureC']
            avg_lowest_temperature += data[date_key]['Min TemperatureC']
            avg_mean_humidity += data[date_key]['Mean Humidity']
            
    print(f"Avg Highest: {avg_highest_temperature//count}C\n")
    print(f"Avg Lowest: {avg_lowest_temperature//count}C\n")
    print(f"Avg Humidity: {avg_mean_humidity//count}%\n\n")
    
    
    
     
def temp_given_year(data):
    """looks for highest temperature/humidity and lowest temperature given a particular year

    Args:
        data ([Dictionary]): [A nested dictionary containing all data]
    """
    year = input("Enter Year for highest temperature/humidity as YYYY ")
    highest_temperature = 0
    highest_temperature_day = ""
    lowest_temperature = 1000
    lowest_temperature_day = ""
    highest_humidity = 0
    highest_humidity_day = ""
    
    for date_key in data.keys():
        if date_key.split('-')[0] == year:
            if highest_temperature < data[date_key]['Max TemperatureC']:
                highest_temperature = data[date_key]['Max TemperatureC']
                highest_temperature_day = date_key   
            if lowest_temperature > data[date_key]['Min TemperatureC']:
                lowest_temperature = data[date_key]['Min TemperatureC']
                lowest_temperature_day = date_key
            if highest_humidity < data[date_key]['Max Humidity']:
                highest_humidity = data[date_key]['Max Humidity']
                highest_humidity_day = date_key
                
    print(f"Highest: {highest_temperature}C on {highest_temperature_day}\n")
    print(f"Lowest: {lowest_temperature}C on {lowest_temperature_day}\n")
    print(f"Humidity: {highest_humidity}% on {highest_humidity_day}\n\n")