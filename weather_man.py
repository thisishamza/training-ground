import argparse
import re
import os

from sys import displayhook

from calculations.temperature_calculations import TemperatureCalculator
from files_reader.read_files import Reader
from reports.report_generator import ReportGenerator

weather_readings = {}


def valid_year(year):
    valid_year = re.compile(r'\b(200[4-9]|201[0-6])\b')
    if valid_year.search(year):
        return year
    else:
        raise argparse.ArgumentTypeError(f"Invalid year {year} should be between 2004-2016")
    
    
def valid_month(month):
    if 1 <= int(month) <= 12:
        return month
    else:
        raise argparse.ArgumentTypeError(f"Invalid month {month}")
        
def valid_date(date):
    year = date.split('/')[0]
    month = date.split('/')[1]
    valid_year(year)
    valid_month(month)
    return date
        


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
    parser.add_argument('-a', help='Year and month as yyyy/m', type=valid_date)
    parser.add_argument('-c', help='Year and month as yyyy/mm', type=valid_date)
    parser.add_argument('-e', help='Year as yyyy', type=valid_year)
    return parser.parse_args()


def main():
    parsed_arguments = parse_arguments()
    arguments = vars(parsed_arguments)
    files_reader = Reader()
    generate_report = ReportGenerator()
    calculate_temperature = TemperatureCalculator()
    
    if arguments['e']:
        files_reader.compile_list_of_files(arguments['e'], arguments['path'])
        files_reader.read_data(arguments['path'])
        yearly_weather_readings = files_reader.compile_data_for_yearly_calculations()
        calculate_temperature.highest_lowest_temperature(yearly_weather_readings, arguments['e'])
        
    if arguments['a']:
        files_reader.compile_list_of_files(arguments['a'], arguments['path'])
        files_reader.read_data(arguments['path'])
        monthly_weather_readings = files_reader.compile_data_for_monthly_calculations()
        calculate_temperature.average_highest_lowest_temperature(
            monthly_weather_readings, arguments['a'])
        
    if arguments['c']:
        files_reader.compile_list_of_files(arguments['c'], arguments['path'])
        files_reader.read_data(arguments['path'])
        monthly_report_readings = files_reader.compile_data_for_monthly_reports(arguments['c'])
        generate_report.bar_charts_for_temperature(monthly_report_readings)
        generate_report.single_bar_chart_temperature(monthly_report_readings)


if __name__ == "__main__":
    main()
