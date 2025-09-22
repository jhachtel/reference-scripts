#!/usr/bin/env python3

import json

from datetime import datetime as date_time
from os.path import basename as get_filename
from sys import argv as get_arg

DEFAULT_SEPARATOR = ','
TIMESTAMP_FORMAT = "%Y%m%d_%H%M%S"
SAMPLE_DATA_DIRECTORY = '/Users/jhachtel/Projects/reference-scripts/sample_data'
TESTING_DATA_CSV_FILE = '/Users/jhachtel/Projects/reference-scripts/reference_test_data/cities.csv'


def get_headers_from_file(file, separator=DEFAULT_SEPARATOR):
    return file.readline().strip().split(separator)


def get_objects_from_file(file, headers, separator=DEFAULT_SEPARATOR):
    sample_objects = []
    for line in file:
        sample_object = dict.fromkeys(headers)
        values = line.strip().split(separator)
        if values == header:
            continue
        else:
            for count, value in enumerate(values):
                key = headers[count]
                sample_object[key] = value.strip()
            sample_objects.append(sample_object)
    return sample_objects


def export_sample_objects(object_list):
    now = date_time.now()
    timestamp = now.strftime(TIMESTAMP_FORMAT)
    for count, sample_object in enumerate(object_list):
        new_filename = f"{SAMPLE_DATA_DIRECTORY}/{JSON_OBJECT_NAME}_{timestamp}_{count}.json"
        with open(new_filename, 'w') as new_file:
            json.dump(sample_object, new_file, indent=4)


def get_filepath_from_command():
    try:
        filepath = get_arg[1]
        print(f'Creating JSON sample data from: {filepath}')
        return filepath
    except IndexError:
        print("No path to a file provided.")
        print(f"Creating JSON sample data from the default testing data file: {TESTING_DATA_CSV_FILE}")
        return TESTING_DATA_CSV_FILE


if __name__ == '__main__':

    filepath = get_filepath_from_command()
    filename = get_filename(filepath).split('.')[0]

    JSON_OBJECT_NAME = f'{filename}_sample_object'

    with open(filepath, 'r') as sample_data:
        header = get_headers_from_file(sample_data)
        sample_objects = get_objects_from_file(sample_data, header)
        export_sample_objects(sample_objects)

