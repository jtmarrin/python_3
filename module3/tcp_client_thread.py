#!/usr/bin/env python3

import socket
import threading
import sys

def EchoClientHandler(clientSocket, addr):
    while 1:
        client_data = clientSocket.recv(2048)
        if client_data:
            clientSocket.send(client_data)
        else:
            clientSocket.close()
            return

echoServer = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
echoServer.bind(("0.0.0.0", int(sys.argv[1])))
echoServer.listen(10)

while 1:
    cSock, addr = echoServer.accept()

    # start a new thread to service
    print("Starting a new thread to service client\n")
    x = threading.Thread(target=EchoClientHandler, args=(cSock,addr))
    x.start()
