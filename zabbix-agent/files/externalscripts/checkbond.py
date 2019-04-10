#!/bin/env python
#!_*_conding:UTF-8_*_
import os
import sys
import json
datalist = {}
if len(sys.argv) != 2:
  print "Pls add a device"
  sys.exit(1)
cmd = 'ethtool %s' %(sys.argv[1])
#init dict
def checkbond():
  try:
    result = os.popen(cmd).readlines()
    #popen return object type is file
  except Exception:
    print "command exce error: %s" %(cmd)
    sys.exit(1)
  else:
    return result
if __name__ == "__main__":
  result = checkbond()
  for line in result:
    line = line.strip('\n').strip('\t').split(':')
    datalist[line[0]] = line[1]
jsonlist = json.dumps(datalist,sort_keys=True,indent=7,separators=(',',':'))
#convert json format
jsonformat = json.loads(jsonlist)
try:
  assert jsonformat["Link detected"].strip() == 'yes'
except Exception:
  print 'down'
else:
  print 'up'
