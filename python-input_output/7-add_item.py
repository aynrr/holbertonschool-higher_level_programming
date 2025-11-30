#!/usr/bin/python3
"""adding arguments"""
import sys


from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
file = "add_item.json"
try:
    a = load_from_json_file(file)
except:
    a = []
a.extend(sys.argv(1:)
save_to_json_file(a, file)
