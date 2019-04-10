#!/bin/env python
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import socket
Hostname = socket.gethostname()
try:
 mongoport = int(sys.argv[1])
except (IndexError,NameError):
  print "You need specify a port"
else:
  try:
    conn = MongoClient(Hostname,mongoport,connectTimeoutMS=2)
  except ConnectionFailure:
    print "mongoprot %s can't be connection" %(mongoport)
  else:
    print "up"
    conn.close()
