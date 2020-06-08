#!/usr/bin/python

import cgi
import pymongo

rsvpclient = pymongo.MongoClient('ds121665.mlab.com', 21665)
rsvpclient.admin.authenticate('nodejs','G8bYFxjx5d6iB7Y', mechanism = 'SCRAM-SHA-1', source='users')
rsvp = rsvpclient["users"]
guest = rsvp["guest"]
form = cgi.FieldStorage(environ={'REQUEST_METHOD':'POST'})
json_data = { "name": form.getvalue("name") }
guest.insert_one(json_data)
