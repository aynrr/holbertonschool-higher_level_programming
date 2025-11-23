#!/usr/bin/python3
def multiple_returns(sentence):
#Creating a function that returns a tuple with the length of a string and its first character.
    length = len(sentence)
    if ((length == 0)):
#If the sentence is empty, the first characte is equal to None
        first = None
    else:
        first = sentence[0]
        return(length, first)
