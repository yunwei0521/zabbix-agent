#!/bin/env python
import mongostatmod
import sys
def calc(a,b) :
	return "%.2f%%" % (a/b*100)

port = sys.argv[1]
currentconn = mongostatmod.mongoconn(port,"current")
availableconn = mongostatmod.mongoconn(port,"available")
percent = calc(float(currentconn),float(availableconn))
print "now current connection: %s"%(currentconn)
print "now available connection: %s"%(availableconn)
print "percent: %s"%(percent)
