#!/usr/bin/env python3

# TCP server that takes a command line -s for seconds then will shutdown after elapsing

import socket
import threading
import argparse
import signal

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--seconds', help='Description', required=False)
args = parser.parse_args()
seconds = int(args.seconds)

def expired_handler(signum, frm):
    print ("The listeners seconds have elapsed")

signal.signal(signal.SIGALRM, expired_handler)
signal.alarm(seconds)
bind_ip = "0.0.0.0"
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))

# Max backlog of connections set to 5
server.listen(5)
print ("[*] Listening on %s:%d" % (bind_ip,bind_port))

# This is our client-handling thread
def handle_client(client_socket):
    # print what client sends
    request = client_socket.recv(1024)
    print ("[*] Recieved %s" %request)
    # send back a packet
    client_socket.send(b'ACK')
    client_socket.close()

while True:
    client,addr = server.accept()
    print ("[*] Accepted connection from %s:%d" %(addr[0],addr[1]))

    # spin up client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
