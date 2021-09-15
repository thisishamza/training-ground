class TemperatureCalculator:
    def get_maximum_humidity_yearly(self, maximum_humidity_every_month):
        yearly_values = {}
        for key_date, monthwise_readings in maximum_humidity_every_month.items():
            yearly_values[key_date] = max(
                monthwise_readings, key=lambda x: x['Max Humidity'])
        return yearly_values


    def get_maximum_temperature_yearly(self, maximum_temperature_every_month):
        yearly_values = {}
        for key_date, monthwise_readings in maximum_temperature_every_month.items():
            yearly_values[key_date] = max(
                monthwise_readings, key=lambda x: x['Max TemperatureC'])
        return yearly_values


    def get_minimum_temperature_yearly(self, minimum_temperature_every_month):
        yearly_values = {}
        for key_date, monthwise_readings in minimum_temperature_every_month.items():
            yearly_values[key_date] = min(
                monthwise_readings, key=lambda x: x['Min TemperatureC'])
        return yearly_values


    def highest_lowest_temperature(self, yearly_weather_readings, year):
        """looks for highest temperature/humidity in a given year and month

        Args:
            weather_readings ([Dictionary]): [A nested dictionary containing all data]
            year ([String]): [Year given by user]
        """
        minimum_temperature_yearly = self.get_minimum_temperature_yearly(
            yearly_weather_readings[0])[int(year)]
        minimum_temperature_date = minimum_temperature_yearly['date'].strftime(
            "%d %b")
        maximum_temperature_yearly = self.get_maximum_temperature_yearly(
            yearly_weather_readings[1])[int(year)]
        maximum_temperature_date = maximum_temperature_yearly['date'].strftime(
            "%d %b")
        maximum_humidity_yearly = self.get_maximum_humidity_yearly(
            yearly_weather_readings[2])[int(year)]
        maximum_humidity_date = maximum_humidity_yearly['date'].strftime("%d %b")
        print(
            f"Max Temperature {maximum_temperature_yearly['Max TemperatureC']} on {maximum_temperature_date}")
        print(
            f"Min Temperature {minimum_temperature_yearly['Min TemperatureC']} on {minimum_temperature_date}")
        print(
            f"Max Humidity {maximum_humidity_yearly['Max Humidity']} on {maximum_humidity_date}")


    def average_highest_lowest_temperature(self, monthly_weather_readings, date):
        """looks for highest temperature/humidity and lowest temperature given a particular year

        Args:
            weather_readings ([Dictionary]): [A nested dictionary containing all data]
            date ([Dictionary]): [A dictionary of given year, month and day]
        """
        year = int(date.split('/')[0])
        month = int(date.split('/')[1])
        print(f"Avg Max Temperature {monthly_weather_readings[0][year][month]}")
        print(f"Avg Min Temperature {monthly_weather_readings[1][year][month]}")
        print(f"Avg Mean Humidity {monthly_weather_readings[2][year][month]}")
