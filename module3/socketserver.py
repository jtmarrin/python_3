#!/usr/bin/env python3

import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    Request handler class for the server.
    Instatiated once per conn to the server
    and must ovveride the handle() method to implement
    comms to the client
    """

    def handle(self):
        # self.request is the TCP socket conn to client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, Uppercased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # create the server, bind to local 9999
    server = socketserver.TCPServer((HOST,PORT), MyTCPHandler)

    # activate the server, runs until interrupt with Ctrl-C
    server.serve_forever()

    