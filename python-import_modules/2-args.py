#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    argcount = len(argv) - 1
    if argcount == 0:
        print("0 arguments.")
    elif argcount == 1:
        print("1 argument:")
    else:
        print(f"{argcount} arguments:")
    for a in range (1, len(argv)):
        print(f"{a}: {argv[a]}")
