#!/usr/bin/env python3

# script for writing command shells or a proxy

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# so you can reuse if disconnected immediately
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))

# server to listen max backlog 5 connections
server.listen(5)

print("[*] Listening on %s:%d" %(bind_ip,bind_port))

# Client handling thread
def handle_client(client_socket):
    # print what client sends
    request = client_socket.recv(1024)
    print("[*] Received: %s" %request)

    # send back an ACK
    client_socket.send(b"ACK!")
    client_socket.close()

while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d" %(addr[0],addr[1]))

    # spin up out client thread to handle imcoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

