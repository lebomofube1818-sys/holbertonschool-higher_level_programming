#!/usr/bin/python3
"""
Module for converting CSV data into JSON format.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV file data to JSON format and save it to data.json.

    Args:
        filename (str): The CSV file name.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        data_list = []

        with open(filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data_list.append(row)

        with open("data.json", 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file)

        return True

    except Exception:
        return False
