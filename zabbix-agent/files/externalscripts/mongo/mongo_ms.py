#!/bin/env python
import sys
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import socket
Host_Name = socket.gethostname()
try:
 mongoport = int(sys.argv[1])
except (IndexError,NameError):
  print "You need specify a port"
else:
  try:
    conn = MongoClient(Host_Name,mongoport,connectTimeoutMS=2)
    print conn['chinadaasA']['PERSON'].find_one()
  except ConnectionFailure:
    print "mongoprot %s can't be connection" %(mongoport)
  else:
    print "up"
    conn.close()
