#!/usr/bin/python

import pymongo
import json

print "Content-type: application/json\n\n";
rsvpclient = pymongo.MongoClient('ds121665.mlab.com', 21665)
rsvpclient.admin.authenticate('nodejs','G8bYFxjx5d6iB7Y', mechanism = 'SCRAM-SHA-1', source='users')
rsvp = rsvpclient["users"]
guest = rsvp["guest"]
person = guest.distinct("name")
i = 0
responses = []
for name in person:
    response =  {}
    response["name"] = name
    responses.append(response)
print(json.JSONEncoder().encode(responses))
