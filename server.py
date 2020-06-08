#!/usr/bin/env python3

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = "html"
port = os.getenv('PORT') or 8082
os.chdir(webdir)
srvaddr = ('', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
CGIHTTPRequestHandler.have_fork = False
srvobj.serve_forever()
