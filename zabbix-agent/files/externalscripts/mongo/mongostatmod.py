#!/usr/bin/env python
#test
import sys
import json
import os
import commands
import socket
mongobin = "/home/mongo/bin/mongo"
mongoscript="/etc/zabbix/externalscripts/mongo/connection.js"
mongoip = socket.gethostname()
def mongostat(port):
	(status, output) = commands.getstatusoutput('%s %s:%s %s| grep ^{'%(mongobin,mongoip,port,mongoscript))
	if status == 0:
		flag = "up"
	else:
		flag = "down"
	return flag
def mongoconn(port,mode):
	result = os.popen('%s %s:%s %s| grep ^{'%(mongobin,mongoip,port,mongoscript)).read()
	jsonformat = json.loads(result)
	return jsonformat[mode]
