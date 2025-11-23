#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    id=0
    for num in new_list:
        if ((num == search)):
            new_list[id] = replace
        id = id + 1
    return new_list
    return my_list
