#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, (str)): 
        raise TypeError("text must be a string")
    
    listchar =[".", "?", ":"]
    for char in text:
        print(char, end="")
        for i in listchar:
            if char == i:
                print()
