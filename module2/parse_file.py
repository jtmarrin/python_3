#!/usr/bin/env python3

# script to parse syslog for instances of 'localdomain'

with open("/var/log/syslog") as f:
    for num, line in enumerate(f, 1):
        if 'localdomain' in line:
            num = str(num)
            print(line)

