#!/usr/bin/env python3

import socket

target_host = "127.0.0.1"
target_port = 9999

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))

# receive some data
# use netcat to see the data sent: nc -luvw 1 9999
data, addr = client.recvfrom(4096)

print(data)