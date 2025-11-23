#!/usr/bin/python3
def multiple_returns(sentence):
#Creating a function that returns a tuple with the length of a string and its first character.
    length = len(sentence)
    first = sentence[0]
    if ((length == 0)):
#If the sentence is empty, the first characte is equal to None
        first = None
    else:
        return(length, first)
