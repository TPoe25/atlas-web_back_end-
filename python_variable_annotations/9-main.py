#!/usr/bin/env python3

def element_length(lst):
    return [(i, len(i)) for i in lst]

element_length =  __import__('9-element_length').element_length

print(element_length.__annotations__)
