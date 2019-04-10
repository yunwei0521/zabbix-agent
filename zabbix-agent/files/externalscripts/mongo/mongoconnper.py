#!/bin/env python
import mongostatmod
import sys
def calc(a,b) :
	return "%.2f" % (a/b*100)
try:
  port = sys.argv[1]
except Exception:
  print "Pls give me a port"
else:
  try:
    currentconn = mongostatmod.mongoconn(port,"current")
    availableconn = mongostatmod.mongoconn(port,"available")
    percent = calc(float(currentconn),float(availableconn))
    print percent
  except Exception:
    #print "unkown error occur"
    pass
