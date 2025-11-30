#!/usr/bin/python3
"""Convert CSV data to JSON format"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Reads a CSV file and writes its content as JSON to data.json."""

    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            r = csv.DictReader(csv_file)
            data = list(r)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return True

    except Exception:
        return False

