#!/usr/bin/python3
import sys
if __name__ == "__main__":
    new_list = []
    s = 0
    argv = sys.argv[1:]
    for args in (argv):
        num = int(args)
        new_list.append(num)
    for a in (new_list):
        s = s + a
    print(s)
