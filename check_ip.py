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

#if the ip address is in the tcpicli output and MongoDB, then do nothing
#if the ip address is in the tcpicli output and not in MongoDB, add to DB
for ip in middle_source_list[:]:
	if db.ip.find({'ip':ip}).count() > 0:
		print "Exist in  MongoDB:"+str(ip)
	else:
		print "Doesn't exist in MongoDB:"+str(ip)
		print "Adding to MongoDB"
		ip_record = {"ip":ip}
		record_id = collection.insert_one(ip_record)

#if the MongoDB has ip address not in middle_source_list, then remove ip
#if MongoDB has ip address and middle_source_list has ip, don't do anything
cursor = db.ip.find({})
for document in cursor:
	ip1 = document['ip']
	if ip1 in middle_source_list:
		print str(ip1)+" is in middle source list"
	else:
		print "removing ip from MongoDB"
		db.ip.remove({'ip':ip1})
