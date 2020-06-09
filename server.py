#!/usr/bin/env python3

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

relay_host = os.getenv('RELAY_HOST')
relay_user = os.getenv('RELAY_USER')
relay_pass = os.getenv('RELAY_PASS')
smarthost = 'sed -i "s/^dc_smarthost=.\+/dc_smarthost=\'' + relay_host + '::587\'/" /etc/exim4/update-exim4.conf.conf'
credential = 'echo -n "' + relay_host + ':' + relay_user + ':' + relay_pass + '" > /etc/exim4/passwd.client'
commit = 'update-exim4.conf'
os.system(smarthost)
os.system(credential)
os.system(commit)
webdir = "html"
port = int(os.getenv('PORT')) or 8082
os.chdir(webdir)
srvaddr = ('', port)
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
CGIHTTPRequestHandler.have_fork = False
srvobj.serve_forever()
