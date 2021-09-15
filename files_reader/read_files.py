import csv
import glob
import os

from datetime import datetime

class Reader:
    
    list_of_files = []
    weather_readings = {}
                        
                        
    def read_data(self, path_to_files):
        """Reads data files and populates a nested dictionary to store data

        Args:
            path_to_files ([String]): [path to directory containing data files]
        """
        required_keys = ['Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 'Max Humidity', ' Mean Humidity', ' Min Humidity']
        for file_name in self.list_of_files:
            with open(file_name, mode='r') as csv_file:
                for single_day_weather_reading in csv.DictReader(csv_file):
                    if single_day_weather_reading:
                        if single_day_weather_reading.get('PKT'):
                            date = datetime.strptime(str(single_day_weather_reading['PKT']), "%Y-%m-%d")
                        else:
                            date = datetime.strptime(str(single_day_weather_reading['PKST']), "%Y-%m-%d")
                            
                        day_reading = {required_key:single_day_weather_reading[required_key]
                                    for required_key in required_keys if required_key in single_day_weather_reading}
                        
                        day_reading['date'] = date
                        self.weather_readings.setdefault(date.year, {}).setdefault(date.month, []).append(day_reading)


    def compile_data_for_yearly_calculations(self):
        minimum_temperature_every_month = {}
        maximum_temperature_every_month = {}
        maximum_humidity_every_month = {}
        
        for key_year, year in self.weather_readings.items():
            minimum_temperature = []
            maximum_temperature = []
            maximum_humidity = []
            for key_month, month in year.items():
                minimum_temperature.append(
                    min(month, key=lambda x: x['Min TemperatureC']))
                minimum_temperature_every_month[key_year] = minimum_temperature
                maximum_temperature.append(
                    max(month, key=lambda x: x['Max TemperatureC']))
                maximum_temperature_every_month[key_year] = maximum_temperature
                maximum_humidity.append(
                    max(month, key=lambda x: x[' Mean Humidity']))
                maximum_humidity_every_month[key_year] = maximum_humidity
                
        return [minimum_temperature_every_month, 
                maximum_temperature_every_month, 
                maximum_humidity_every_month]


    def compile_data_for_monthly_calculations(self):
        avg_minimum_temperature_every_month = {}
        avg_maximum_temperature_every_month = {}
        avg_mean_humidity_every_month = {}
        for key_year, year in self.weather_readings.items():
            for key_month, month in year.items():
                avg_maximum_temperature_every_month.setdefault(
                    key_year, {}).setdefault(key_month, float(
                        sum(map(int, (daily_readings['Max TemperatureC'] for daily_readings in month if daily_readings['Max TemperatureC'] != '')))) / len(month))
                avg_minimum_temperature_every_month.setdefault(
                    key_year, {}).setdefault(key_month, float(
                        sum(map(int, (daily_readings['Min TemperatureC'] for daily_readings in month if daily_readings['Min TemperatureC'] != '')))) / len(month))
                avg_mean_humidity_every_month.setdefault(
                    key_year, {}).setdefault(key_month, float(
                        sum(map(int, (daily_readings[' Mean Humidity'] for daily_readings in month if daily_readings[' Mean Humidity'] != '')))) / len(month))
        return [avg_maximum_temperature_every_month, 
                avg_minimum_temperature_every_month, 
                avg_mean_humidity_every_month]


    def compile_data_for_monthly_reports(self, date):
        maximum_temperature = {}
        minimum_temperature = {}
        for key_year, year in self.weather_readings.items():
            for key_month, month in year.items():
                maximum_temperature.setdefault(
                    key_year, {}).setdefault(
                        key_month, [daily_readings['Max TemperatureC'] for daily_readings in month])
                minimum_temperature.setdefault(
                    key_year, {}).setdefault(
                        key_month, [daily_readings['Min TemperatureC'] for daily_readings in month])
        date = date.split('/')
        year = int(date[0])
        month = int(date[1])
        print(year,month)
        yearly_maximum_reading = maximum_temperature[year]
        yearly_minimum_reading = minimum_temperature[year]
        return [yearly_maximum_reading[month], yearly_minimum_reading[month]]


    def compile_list_of_files(self, date, path_to_files):
        print(type(date))
        self.list_of_files = []
        date = date.split('/')
        if len(date) == 1:
            year = date[0]
            month = ""
        else:
            year = date[0]
            month = datetime.strptime(date[1],"%m").strftime("%b")
        print(year,month)
        for file_name in glob.glob(os.path.join(path_to_files, '*.txt')):
            if year in file_name and month in file_name:
                self.list_of_files.append(file_name)
