#!/usr/bin/env python3

# Creates a simple httpserver and test page
from http.server import BaseHTTPRequestHandler

class GetHandler(BaseHTTPRequestHandler):

     def do_GET(self):
        DUMMY_RESPONSE =  b"""<html>
        
        <head>
        <title>Title goes here!</title>
        </head>
        
       
        <body>
        <p>This is a test.</p>
        </body>
        
        </html>"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(DUMMY_RESPONSE))
        self.end_headers()
        self.wfile.write(DUMMY_RESPONSE)

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 777), GetHandler)
    print('Starting server, use <Ctrl + F2> to stop')
    server.serve_forever()