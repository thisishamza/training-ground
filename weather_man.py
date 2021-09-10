import os
import glob
import csv
import argparse
from calculations import do_calculations
from reports import report_generator

readings_data_structure = {}
path_to_files = os.getcwd() + '/weatherfiles'


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


def populate_readings_data_structure(single_day_reading):
    """receives a single line from reading file and generates a dictionary of values

    Args:
        split_line ([String]): [A single line read from file]

    Returns:
        [Dictionary]: [A dictionary containing datapoints for a tuple]
    """
    single_day_reading['Max TemperatureC'] = to_correct_type(
        single_day_reading['Max TemperatureC'])
    single_day_reading['Mean TemperatureC'] = to_correct_type(
        single_day_reading['Mean TemperatureC'])
    single_day_reading['Min TemperatureC'] = to_correct_type(
        single_day_reading['Min TemperatureC'])
    single_day_reading['Dew PointC'] = to_correct_type(
        single_day_reading['Dew PointC'])
    single_day_reading['MeanDew PointC'] = to_correct_type(
        single_day_reading['MeanDew PointC'])
    single_day_reading['Min DewpointC'] = to_correct_type(
        single_day_reading['Min DewpointC'])
    single_day_reading['Max Humidity'] = to_correct_type(
        single_day_reading['Max Humidity'])
    single_day_reading['Mean Humidity'] = to_correct_type(
        single_day_reading[' Mean Humidity'])
    single_day_reading['Min Humidity'] = to_correct_type(
        single_day_reading[' Min Humidity'])
    single_day_reading['CloudCover'] = to_correct_type(
        single_day_reading[' CloudCover'])
    single_day_reading['WindDirDegrees'] = to_correct_type(
        single_day_reading['WindDirDegrees'])
    single_day_reading['Max VisibilityKm'] = to_correct_type(
        single_day_reading[' Max VisibilityKm'])
    single_day_reading['Mean VisibilityKm'] = to_correct_type(
        single_day_reading[' Mean VisibilityKm'])
    single_day_reading['Min VisibilitykM'] = to_correct_type(
        single_day_reading[' Min VisibilitykM'])
    single_day_reading['Max Wind SpeedKm/h'] = to_correct_type(
        single_day_reading[' Max Wind SpeedKm/h'])
    single_day_reading['Mean Wind SpeedKm/h'] = to_correct_type(
        single_day_reading[' Mean Wind SpeedKm/h'])
    single_day_reading['Max Gust SpeedKm/h'] = to_correct_type(
        single_day_reading[' Max Gust SpeedKm/h'])
    single_day_reading['Precipitationmm'] = to_correct_type(
        single_day_reading['Precipitationmm'])
    single_day_reading['Max Sea Level PressurehPa'] = to_correct_type(
        single_day_reading[' Max Sea Level PressurehPa'])
    single_day_reading['Mean Sea Level PressurehPa'] = to_correct_type(
        single_day_reading[' Mean Sea Level PressurehPa'])
    single_day_reading['Min Sea Level PressurehPa'] = to_correct_type(
        single_day_reading[' Min Sea Level PressurehPa'])
    return single_day_reading


def read_data(path_to_files):
    """Reads data files and populates a nested dictionary to store data

    Args:
        path_to_files ([String]): [path to directory containing data files]
    """
    for file_name in glob.glob(os.path.join(path_to_files, '*.txt')):
        with open(file_name, mode='r') as csv_file:
            single_file_table = csv.DictReader(csv_file)
            for single_day_reading in single_file_table:
                if single_day_reading:
                    single_day_reading = populate_readings_data_structure(
                        single_day_reading)
                    try:
                        date = single_day_reading['PKT']
                    except KeyError:
                        date = single_day_reading['PKST']
                    readings_data_structure[date] = single_day_reading


def valid_directory_path(directory_path):
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
    read_data(path_to_files=arguments['path'])
    if arguments['e']:
        do_calculations.highest_lowest_temperature(
            readings_data_structure, arguments['e'])
    if arguments['a']:
        do_calculations.average_highest_lowest_temperature(
            readings_data_structure, arguments['a'])
    if arguments['c']:
        report_generator.bar_charts_for_temperature(
            readings_data_structure, arguments['c'])
        report_generator.single_bar_chart_temperature(
            readings_data_structure, arguments['c'])


if __name__ == "__main__":
    main()
