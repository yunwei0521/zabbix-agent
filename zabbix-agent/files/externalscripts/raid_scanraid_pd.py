#!/usr/bin/python
#!_*_conding:UTF-8_*_
import os
import json

r=os.popen('/opt/MegaRAID/MegaCli/MegaCli64 -PDList -a0 -NoLog | grep "Enclosure Device ID" | awk -F ":" \'{print $2}\' | sed \'s/ //g\'').read().split()
devices=[]
EID=[]
a=0
for device in r:
		SID='pd'+str(a)+''
		devices += [{'{#EDID}':device,'{#SID}':SID}]
		a+=1
print json.dumps({'data':devices},sort_keys=True,indent=7,separators=(',',':'))

