#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    '''Creating a function that replaces an element in a list at a specific position without modifying the original list.'''
    new_list = my_list[:]
    if ((idx < 0)):
    #If idx is negative, the function returns a copy of the original list
        return new_list
    elif ((idx >= len(my_list))):
    #If idx is out of range (> of number of element in my_list), the function returns a copy of the original list
        return new_list
    else:
    #Replacing the element
        new_list[idx] = element
        return new_list
        return my_list
