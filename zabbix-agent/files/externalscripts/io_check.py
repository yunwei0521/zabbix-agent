#!/usr/bin/env python
#coding:utf8
import os,re 
from sys import argv
def usage():
#        print "usage:%s <device_name>[sda|vda|xvda]"%(argv[0])
        print "custom.disk.io[<device_name>](sda,vda,xvda...)"
if __name__ == "__main__":
	if len(argv) != 2:
		usage()
		exit(1)
	else:
		device=argv[1]
		if os.system('ls /dev/%s >/dev/null 2>&1'%(device)) != 0:
			print "not found %s device!"%(device)
			usage()
			exit(1)
		disk_util,disk_await=os.popen("iostat -dx 4 2 %s|egrep -vw '^$|Linux|Device'|tail -1|awk '{print $NF,$(NF-2)}'"%(device)).read().split()
		disk_util=int(float(disk_util))
		disk_await=int(float(disk_await))
		if disk_await < 10 and disk_util > 90:
			print disk_util-10
		else:			
			if disk_util > 100:
				disk_util=100
			print disk_util
