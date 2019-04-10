#!/usr/bin/env python
#encoding: utf-8
#!/bin/env python
import sys
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError,ConnectionFailure
import socket
Hostname = socket.gethostname()
try:
 mongoport = int(sys.argv[1])
except (IndexError,NameError):
  print "You need specify a port"
else:
  try:
    conn = MongoClient(Hostname,mongoport)
    data = conn.admin.command('serverStatus')
  except ConnectionFailure:
    print "mongoprot %s can't be connection" %(mongoport)
  except ServerSelectionTimeoutError:
    print "mongo exec command fail"
  else:
    print data['mem']['resident']
    conn.close()
