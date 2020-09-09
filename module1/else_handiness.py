#!/usr/bin/python3

import sys

count = int(sys.argv[1])

while count < 9:
    print (count)
    count += 1
    if count == 7:
        break

else:
    print("Finished the while loop")
