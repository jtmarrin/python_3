#!/usr/bin/env python3

# Creates simple http Server
# can use this to server whatever you want server exploits or send fuzzed output

import socketserver
import http.server

PORT = 10000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()