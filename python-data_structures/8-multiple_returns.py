#!/usr/bin/python3

def multiple_returns(sentence):
    tupla = ()
    if len(sentence) == 0:
        tupla = (0, "None")
        return tupla
    else:
        tupla = (len(sentence), sentence[0])
        return tupla
