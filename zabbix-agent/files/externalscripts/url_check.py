#!/usr/bin/env python
#coding:utf-8
import httplib
from sys import argv
def usage():
	print 'usage:%s <reason|status> <ipaddr> <port> <url>'%(argv[0])
def get_url(ipaddr,port,url):
	httpClient = httplib.HTTPConnection(ipaddr,port,timeout=10)
	httpClient.request('GET',url)
	response = httpClient.getresponse()
	return response
def url_true(url):
	url_n = url.replace('%3F','?')
	return url_n
if __name__ == '__main__':
	try:
		if len(argv) != 5:
			usage()
		else:
			action = argv[1]
			ipaddr = argv[2]
			port = argv[3]
			url = url_true(argv[4])
			if action not in ['reason','status']:
				usage()
			else:
				result = get_url(ipaddr,port,url)
				if action == 'reason':
					print result.reason
				else:
					print result.status
	except Exception,msg:
		print msg
