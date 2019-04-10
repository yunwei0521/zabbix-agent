#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import subprocess
import socket
json_data = {"data":[]}
net_cmd = '''sudo netstat -nlpt|awk '/mongo/{print $4}'
'''
myname = socket.getfqdn(socket.gethostname(  ))
myaddr = socket.gethostbyname(myname)
p = subprocess.Popen(net_cmd, shell=True, stdout=subprocess.PIPE)
net_result = p.stdout.readlines()
for server in net_result:
  dic_content = {
   "{#MONGO_PORT}" : server.split(':')[1].strip(),
   }
  json_data['data'].append(dic_content)
result = json.dumps(json_data,sort_keys=True,indent=4)
print result
