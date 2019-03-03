#!/usr/bin/env python3

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
import ssl

webdir = "html"
port = 8443
os.chdir(webdir)
srvaddr = ('', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.socket = ssl.wrap_socket (srvobj.socket, keyfile='../privkey.pem', certfile='../fullchain.pem', server_side=True)
CGIHTTPRequestHandler.have_fork = False
srvobj.serve_forever()
