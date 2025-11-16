#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase using only string format"""
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += "{}".format(chr(ord(c) - 32))
        else:
            result += "{}".format(c)
    print("{}".format(result))
