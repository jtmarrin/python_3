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

if startport == endport:
    endport += 1

try:
    for x in range(startport, endport):
        packet = IP(dst=target)/TCP(dport=x,flags='S')
        response = sr1(packet,timeout=0.5,verbose=0)
        if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12: #SYN/ACK flag
            print('Port '+ str(x) + ' is open!')
            sr(IP(dst=target)/TCP(dport=response.sport,flags='R'),timeout=0.5,verbose=0)  # reset packet
except:
    print('You may be scanning a closed host!\n')
print('Scan is complete!\n')

