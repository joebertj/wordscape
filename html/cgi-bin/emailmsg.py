#!/usr/bin/python3

import cgi
import subprocess
print("Content-Type: text/html\n")
form = cgi.FieldStorage(environ={'REQUEST_METHOD':'POST'})
fname = form.getvalue("fname")
lname = form.getvalue("lname")
email = form.getvalue("email")
subject = form.getvalue("subject")
message = form.getvalue("message")
mail = [ 'mail', '-s', subject, '-r', email, '--', 'joebert@kenchlightyear.com']
body = [ 'printf', 'Message from: ' + fname + ' ' + lname + '\n\n' + message ]
bodyproc = subprocess.Popen(body, stdout=subprocess.PIPE)
mailproc = subprocess.Popen(mail, stdin=bodyproc.stdout)
confirmation = "Thank you for contacting us. We have received your message. We will get back to you soon."
signature = "Regards,\nJoebert Jacaba\nCEO, Kench Lightyear\n+63 919 999 2056"
mail = [ 'mail', '-s', "Confirmation", '-r', 'joebert@kenchlightyear.com', '--', email ]
body = [ 'printf', 'Hello ' + fname + ',\n\n' + confirmation + '\n\n' + signature]
bodyproc = subprocess.Popen(body, stdout=subprocess.PIPE)
mailproc = subprocess.Popen(mail, stdin=bodyproc.stdout)
print(confirmation)
print('<p><a href="javascript:self.close()">Close</a></p>')
