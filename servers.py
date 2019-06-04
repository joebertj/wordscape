#!/usr/bin/env python3

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler
import ssl

webdir = "html"
ports = 8443
os.chdir(webdir)
srvaddrs = ('', ports)
srvobjs = HTTPServer(srvaddrs, CGIHTTPRequestHandler)
srvobjs.socket = ssl.wrap_socket (srvobjs.socket, keyfile='../privkey.pem', certfile='../fullchain.pem', server_side=True)
CGIHTTPRequestHandler.have_fork = False
srvobjs.serve_forever()
