#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = []
    for num in my_list:
        if ((uniq_list.count(num) == 0)):
            uniq_list.append(num)
    result = sum(uniq_list)
    return result
