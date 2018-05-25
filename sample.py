#!/usr/bin/python

import json
import subprocess
import pymongo
from pymongo import MongoClient

client = MongoClient()

db = client.middle_source_list
collection = db['ip']

cursor = db.ip.find({})
for document in cursor:
	print document['ip']
