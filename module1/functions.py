#!/usr/bin/python3

import sys

def print5times(line_to_print):
    for count in range(0,5):
        print(line_to_print)

# command line argument is inside of argv[1]
print5times(sys.argv[1])
