#!/usr/bin/env python
# encoding: utf-8
import urllib2,json
def etcd_mi(host,port):
  url = 'http://{host}:{port}/v3alpha/maintenance/status'.format(host=host,port=port)
  values = {"type":"nothing"}
  headers = { 'cache-control':'no-store','content-type':'application/json'}
  data = json.dumps(values)
  req = urllib2.Request(url, data, headers)
  try:
    response = urllib2.urlopen(req,timeout=5)
  except Exception as e:
    raise e
  else:
    return json.loads(response.read())


if __name__ == "__main__":
  import sys
  data = etcd_mi(sys.argv[1],sys.argv[2])
  print (data.get('dbSize'))
