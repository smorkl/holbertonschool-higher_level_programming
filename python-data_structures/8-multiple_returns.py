#!/usr/bin/python3

def multiple_returns(sentence):
    tupla = ()
    if len(sentence) < 0:
        tupla = ("None",)
        return tupla
    
    tupla = (len(sentence), sentence[0])
    return tupla