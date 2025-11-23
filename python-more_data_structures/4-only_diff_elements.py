#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    only_1 = (set_1 - set_2)
    only_2 = (set_2 - set_1)
    diff_elements = (only_1 | only_2)
    return diff_elements
