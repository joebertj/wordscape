#!/usr/bin/python

import cgi
import pymongo
import sys
import json

rsvpclient = pymongo.MongoClient('ds121665.mlab.com', 21665)
rsvpclient.admin.authenticate('nodejs','G8bYFxjx5d6iB7Y', mechanism = 'SCRAM-SHA-1', source='users')
rsvp = rsvpclient["users"]
guest = rsvp["guest"]
data = sys.stdin.read()
person = json.loads(data)
guest.insert_one({"id": person["id"], "name": person["name"]})
