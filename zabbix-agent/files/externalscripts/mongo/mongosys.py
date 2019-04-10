#!/bin/env python
#!_*_conding:UTF-8_*_
import sys,socket,os
import socket
mongobin = "/home/mongo/bin"
def checksys(host,port,mode):
  try:
    cmd = "%s/mongostat -h %s:%s --rowcount=1 --humanReadable=false" %(mongobin,host,port)
    result = os.popen(cmd).read().split()
    datadict = {}
    comp = (len(result)/2)
    for i in xrange(0,comp):
      datadict[result[i]] = result[(comp+i)]
    print datadict[mode]
    #print "you also can use these mode %s" %(result[0:comp])
  except Exception as err:
    print err
if len(sys.argv) == 3:
  mode = sys.argv[2]
  port = sys.argv[1]
  host = socket.gethostname()
  checksys(host,port,mode)
else:
  print "Please tell me what you want to know"
