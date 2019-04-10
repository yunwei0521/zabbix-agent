#!/usr/bin/python
#!_*_conding:UTF-8_*_
import os
import json

r=os.popen('cat /proc/net/dev | grep bond | awk -F ":" \'{print $1}\' | sed \'s/ //g\'').read().split()
devices=[]
for device in r:
	devices += [{'{#BOND}':device}]
print json.dumps({'data':devices},sort_keys=True,indent=7,separators=(',',':'))
