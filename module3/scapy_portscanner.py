#!/usr/bin/env python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys
from scapy.all import *

if len(sys.argv) != 4:
    print("Usage: %s target startport endport" %(sys.argv[0]))
    sys.exit(0)

target = str(sys.argv[1])
startport = int(sys.argv[2])
endport = int(sys.argv[3])

print('Scanning '+target+' for open TCP ports\n')


