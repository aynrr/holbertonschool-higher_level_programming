#!/usr/bin/python3
def max_integer(my_list=[]):
    if ((len(my_list) == 0)):
        return None
    else:
        max = -1
        for num in my_list:
            if num > max:
                max = num
        return max
