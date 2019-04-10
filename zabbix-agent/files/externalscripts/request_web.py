#!/usr/bin/env python
#encoding: utf-8
import argparse
import urllib2

parser = argparse.ArgumentParser(description="request app api to check health")
parser.add_argument('-H','--host',type=str,required=True,help='specify remote bind address')
parser.add_argument('-p','--port',type=int,required=True,help='specify a web port')
args = parser.parse_args()
port = args.port
host = args.host
result = None
req = "http://%s:%s"%(host,port)
try:
  response = urllib2.urlopen(req,timeout=5)
  result = 'up' if response.code == 200 else 'down'
except Exception:
  result = 'down'
  raise
finally:
  print result

