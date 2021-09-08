import os
import glob
from calculations import do_calculations
from reports import report_generator

dictionary_of_data = {}  
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


def convert_line_to_dic(split_line):
    """receives a single line from reading file and generates a dictionary of values

    Args:
        split_line ([String]): [A single line read from file]

    Returns:
        [Dictionary]: [A dictionary containing datapoints for a tuple]
    """
    return {
                "Max TemperatureC": to_correct_type(split_line[1]),
                "Mean TemperatureC": to_correct_type(split_line[2]),
                "Min TemperatureC": to_correct_type(split_line[3]),
                "Dew PointC": to_correct_type(split_line[4]),
                "MeanDew PointC": to_correct_type(split_line[5]),
                "Min DewpointC": to_correct_type(split_line[6]),
                "Max Humidity": to_correct_type(split_line[7]),
                "Mean Humidity": to_correct_type(split_line[8]),
                "Min Humidity": to_correct_type(split_line[9]),
                "Max Sea Level PressurehPa": to_correct_type(split_line[10]),
                "Mean Sea Level PressurehPa": to_correct_type(split_line[11]),
                "Min Sea Level PressurehPa": to_correct_type(split_line[12]),
                "Max VisibilityKm": to_correct_type(split_line[13]),
                "Mean VisibilityKm": to_correct_type(split_line[14]),
                "Min VisibilitykM": to_correct_type(split_line[15]),
                "Max Wind SpeedKm/h": to_correct_type(split_line[16]),
                "Mean Wind SpeedKm/h": to_correct_type(split_line[17]),
                "Max Gust SpeedKm/h": to_correct_type(split_line[18]),
                "Precipitationmm": to_correct_type(split_line[19]),
                "CloudCover": to_correct_type(split_line[20]),
                "Events": to_correct_type(split_line[21]),
                "WindDirDegrees": to_correct_type(split_line[22]),
            }


def read_data(path_to_files):
    """Reads data files and populates a nested dictionary to store data

    Args:
        path_to_files ([String]): [path to directory containing data files]
    """
    for file_name in glob.glob(os.path.join(path_to_files, '*.txt')):
        with open(file_name, 'r') as data_file:
            lines = data_file.read().split('\n')
            for line in lines[1:]:
                split_line = line.split(',')
                if split_line[0] != "":     #check if line is not empty
                    dictionary_of_single_line = convert_line_to_dic(split_line)
                    dictionary_of_data[split_line[0]] = dictionary_of_single_line



def main():
    read_data(path_to_files = path_to_files)
    do_calculations.temp_given_year(dictionary_of_data)
    do_calculations.temp_given_month(dictionary_of_data)
    report_generator.chart_on_month(dictionary_of_data)
    report_generator.chart_on_month_bonus_task(dictionary_of_data)
    
    
if __name__ == "__main__":
    main()
    