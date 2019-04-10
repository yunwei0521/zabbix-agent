#!/usr/bin/env python
#coding:utf8
import os,json
def discovery_disk():
	disk_list=[]
	FSNAME=os.popen(r"df -hP|egrep -v 'overlay|shm|tmpfs|devicemapper|Filesystem' |awk '{print $NF}'").readlines()
	for d in FSNAME:
		disk_dict={}
		disk_dict['{#FSNAME}'] = d.strip()
		disk_list.append(disk_dict)
	print json.dumps({'data':disk_list},sort_keys=True)
discovery_disk()
