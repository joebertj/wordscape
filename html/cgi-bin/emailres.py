#!/usr/bin/python3

import cgi
import subprocess
print("Content-Type: text/html\n")
form = cgi.FieldStorage(environ={'REQUEST_METHOD':'POST'})
email = form.getvalue("email")
mail = [ 'mail', '-s', 'Resume of Joebert Jacaba', '-r', 'joebert@kenchlightyear.com', '--', email ]
body = [ 'cat', '/app/html/bodyattach' ]
bodyproc = subprocess.Popen(body, stdout=subprocess.PIPE)
mailproc = subprocess.Popen(mail, stdin=bodyproc.stdout)
print("Your email has been delivered. It should arrive shortly.")
print('<p><a href="javascript:self.close()">Close</a></p>')
