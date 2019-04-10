#!/usr/bin/env python
#coding:utf8
import os,json
def discovery_disk():
	disk_list=[]
	DKNAME=os.popen(r"cat /proc/diskstats |egrep '\bsd[a-z]\b|\bxvd[a-z]\b|\bvd[a-z]\b'|awk '{print $3}'").readlines()
	for d in DKNAME:
		disk_dict={}
		disk_dict['{#DKNAME}'] = d.strip()
		disk_list.append(disk_dict)
	print json.dumps({'data':disk_list},sort_keys=True)
#	print json.loads(disk_list)
#a=[{'{#FSNAME}':'/','{#FSTYPE}':'ext4'},{'b':2},{'c':3},{'d':4}]
discovery_disk()
#print json.dumps({'data':a},sort_keys=True,indent=4,separators=(',',':'))
#print json.dumps({'data':a},sort_keys=True)
