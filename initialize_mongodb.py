#!/usr/bin/python

import subprocess
import json
import pymongo
from pymongo import MongoClient


# run the tcpicli tool to get the middle source list
result = subprocess.check_output(["/home/apps/bin/tcpicli_linux", "cdn", "GetCdnMiddleSourceList", "format=ip_block"])
json_data = json.loads(result)

#convert the middle_source to a list
middle_source_list = json_data['data']['middle_source_list']

#setup the Mongo DB connection
client = MongoClient()

#setting to the middle_source_list database
db = client.middle_source_list

#set up the collection
collection = db['ip']

for ip in middle_source_list[:]:
	ip_record = {"ip":ip}
	record_id = collection.insert_one(ip_record)
