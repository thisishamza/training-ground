import argparse
import csv
import glob
import os

from datetime import datetime

from calculations import temperature_calculations
from reports import report_generator


complete_weather_readings = {}


def to_correct_type(value):
    """converts values from files to appropriate datatype

    Args:
        value ([String]): [A single data string from reading file]

    Returns:
        [0]: [returns 0 if data is missing]
        [float]: [if we get numeric data]
        [string]: [if we get string data]
    """
    if value == "":
        return 0
    else:
        try:
            return float(value)
        except ValueError as ve:
            return value


def convert_date_to_year_month_day(date):
    date = date.split('/')
    if len(date) > 0:
        year = date[0]
    else:
        year = ""
    if len(date) > 1:
        month = date[1]
        if int(month) < 10:
            try:
                month = month[1]
            except IndexError:
                month = month[0]
    else:
        month = ""
    if len(date) > 2:
        day = date[-1]
    else:
        day = " "
    return {
        'year': year,
        'month': month,
        'day': day
    }


def get_date_from_daily_weather_reading(daily_weather_reading):
    try:
        return datetime.strptime(str(daily_weather_reading['PKT']), "%Y-%m-%d")
    except KeyError:
        return datetime.strptime(str(daily_weather_reading['PKST']), "%Y-%m-%d")


def populate_weather_readings(single_day_reading, date):
    """receives a single line from reading file and generates a dictionary of values

    Args:
        single_day_reading ([Dictionary]): [A dictionary having single day weather reading]
        date ([datetime]): [A datetime object containing date of every single row]

    Returns:
        [Dictionary]: [A dictionary containing datapoints required by the task]
    """
    day_reading = {}
    day_reading['date'] = date
    day_reading['Max TemperatureC'] = to_correct_type(
        single_day_reading['Max TemperatureC'])
    day_reading['Mean TemperatureC'] = to_correct_type(
        single_day_reading['Mean TemperatureC'])
    day_reading['Min TemperatureC'] = to_correct_type(
        single_day_reading['Min TemperatureC'])
    day_reading['Max Humidity'] = to_correct_type(
        single_day_reading['Max Humidity'])
    day_reading['Mean Humidity'] = to_correct_type(
        single_day_reading[' Mean Humidity'])
    day_reading['Min Humidity'] = to_correct_type(
        single_day_reading[' Min Humidity'])
    return day_reading


def compile_data_for_monthly_reports(date):
    maximum_temperature = {}
    minimum_temperature = {}
    for key_year, year in complete_weather_readings.items():
        for key_month, month in year.items():
            maximum_temperature.setdefault(
                key_year, {}).setdefault(
                    key_month, [daily_readings['Max TemperatureC'] for daily_readings in month])
            minimum_temperature.setdefault(
                key_year, {}).setdefault(
                    key_month, [daily_readings['Min TemperatureC'] for daily_readings in month])
    year = int(date['year'])
    month = int(date['month'])
    yearly_maximum_reading = maximum_temperature[year]
    yearly_minimum_reading = minimum_temperature[year]
    return [yearly_maximum_reading[month], yearly_minimum_reading[month]]


def compile_data_for_monthly_calculations():
    avg_minimum_temperature_every_month = {}
    avg_maximum_temperature_every_month = {}
    avg_mean_humidity_every_month = {}
    for key_year, year in complete_weather_readings.items():
        for key_month, month in year.items():
            avg_maximum_temperature_every_month.setdefault(
                key_year, {}).setdefault(key_month, float(
                    sum(daily_readings['Max TemperatureC'] for daily_readings in month)) / len(month))
            avg_minimum_temperature_every_month.setdefault(
                key_year, {}).setdefault(key_month, float(
                    sum(d['Min TemperatureC'] for d in month)) / len(month))
            avg_mean_humidity_every_month.setdefault(
                key_year, {}).setdefault(key_month, float(
                    sum(d['Mean Humidity'] for d in month)) / len(month))
    return [avg_maximum_temperature_every_month, 
            avg_minimum_temperature_every_month, 
            avg_mean_humidity_every_month]


def compile_data_for_yearly_calculations():
    minimum_temperature_every_month = {}
    maximum_temperature_every_month = {}
    maximum_humidity_every_month = {}
    for key_year, year in complete_weather_readings.items():
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
                max(month, key=lambda x: x['Mean Humidity']))
            maximum_humidity_every_month[key_year] = maximum_humidity
    return [minimum_temperature_every_month, 
            maximum_temperature_every_month, 
            maximum_humidity_every_month]


def read_data(path_to_files):
    """Reads data files and populates a nested dictionary to store data

    Args:
        path_to_files ([String]): [path to directory containing data files]
    """
    for file_name in glob.glob(os.path.join(path_to_files, '*.txt')):
        with open(file_name, mode='r') as csv_file:
            for single_day_weather_reading in csv.DictReader(csv_file):
                if single_day_weather_reading:
                    if single_day_weather_reading.get('PKT'):
                        date = datetime.strptime(
                            str(single_day_weather_reading['PKT']), "%Y-%m-%d")
                    else:
                        date = datetime.strptime(
                            str(single_day_weather_reading['PKST']), "%Y-%m-%d")
                    day_reading = populate_weather_readings(
                        single_day_weather_reading, date)
                    complete_weather_readings.setdefault(date.year, {}).setdefault(
                        date.month, []).append(day_reading)


def valid_directory_path(directory_path):
    """Checks if a path to a directory is valid or not

    Args:
        directory_path ([String]): [Path to directory containing data files]

    Raises:
        argparse.ArgumentTypeError: [TypeError if path to directory is invalid]

    Returns:
        [argparse.Namespace]: [description]
    """
    if os.path.isdir(directory_path):
        return directory_path
    else:
        raise argparse.ArgumentTypeError(
            f"{directory_path} is not a valid path")


def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze weather man data')
    parser.add_argument('-path', help='Path to folder containing data files',
                        type=valid_directory_path, required=True)
    parser.add_argument('-a', help='Year and month as yyyy/m')
    parser.add_argument('-c', help='Year and month as yyyy/mm')
    parser.add_argument('-e', help='Year as yyyy')
    return parser.parse_args()


def main():
    parsed_arguments = parse_arguments()
    arguments = vars(parsed_arguments)
    read_data(arguments['path'])
    if arguments['e']:
        yearly_weather_readings = compile_data_for_yearly_calculations()
        temperature_calculations.highest_lowest_temperature(
            yearly_weather_readings, arguments['e'])
    if arguments['a']:
        monthly_weather_readings = compile_data_for_monthly_calculations()
        temperature_calculations.average_highest_lowest_temperature(
            monthly_weather_readings, convert_date_to_year_month_day(arguments['a']))
    if arguments['c']:
        monthly_report_readings = compile_data_for_monthly_reports(
            convert_date_to_year_month_day(arguments['c']))
        report_generator.bar_charts_for_temperature(monthly_report_readings)
        report_generator.single_bar_chart_temperature(monthly_report_readings)


if __name__ == "__main__":
    main()