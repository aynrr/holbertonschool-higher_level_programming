#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if ((idx < 0)) or ((idx >= len(my_list))):
        return my_list
    else:
        new_list = my_list
        id = 0
        for num in my_list:
            if ((id == idx)):
                new_list.remove(num)
            id = id + 1
        return new_list
        return my_list
