#!/usr/bin/python3
"""my first inheritence example"""


class MyList(list):
    """inherits from the list"""
    def print_sorted(self, list):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
