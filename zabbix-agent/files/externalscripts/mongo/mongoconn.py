#!/usr/bin/env python
#test
import sys
import json
import os
import socket
mongobin = "/home/mongo/bin/mongo"
mongoip = socket.gethostname()
mongoscript="/etc/zabbix/externalscripts/mongo/connection.js"
port = sys.argv[1]
mode = sys.argv[2]
result = os.popen('%s %s:%s %s| grep ^{'%(mongobin,mongoip,port,mongoscript)).read()
jsonformat = json.loads(result)
print jsonformat[mode]
