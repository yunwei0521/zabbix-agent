#!/usr/bin/env python
#coding:utf8
import os
from sys import argv
def usage():
	print "usage:%s <process_name> <owner_name> <process_min> <process_max>"%(argv[0])
def check_processes(check_command):
	global check_text
	check_text=os.popen('ps -ef|egrep -v "(grep|%s)"|grep -w "%s"'%(filter1,check_command)).readlines()
def filter_user(check_user):
	global check_text
	tmp=[]
	for f in check_text:
		if check_user == f.split()[0]:
			tmp.append(f)
	check_text=tmp
def check_limit(process_min,process_max):
	process_num=len(check_text)
	if process_min <= process_num <= process_max:
		return check_text
	else:
		return []
if __name__ == "__main__":
	filter1=argv[0]
	if len(argv) in [2,3,5]:
		if len(argv) >= 2:
			check_command=argv[1]
			check_processes(check_command)
		if len(argv) >= 3:
			check_user=argv[2]
			filter_user(check_user)
		if len(argv) == 5:
			process_min=int(argv[3])
			process_max=int(argv[4])
			check_text=check_limit(process_min,process_max)
	else:
		usage()
		exit(1)
	print len(check_text)	
