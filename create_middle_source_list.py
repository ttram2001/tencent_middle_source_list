#!/usr/bin/python

import datetime
import json
import subprocess
import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client.middle_source_list
collection = db['ip']

cursor = db.ip.find().sort('ip')
counter = 1
currentDT = datetime.datetime.now()
print '<html> <title> Tencent Middle Source List </title>'
print '<body>'
print '<h1> Tencent Middle Source List as of ' + str(currentDT) + '</h1>'
print '<table border=1>'
print '<th> Count </th><th> IP Address </th><th> Datetime </th>'
for document in cursor:
	print '<tr>'
	print '<td>' + str(counter) + '</td><td>' + document['ip'] + '</td><td> ' + str(currentDT) + '</td>'
	print '</tr>'
	counter = counter + 1

print '</table>'
print '</body>'
print '</html>'
