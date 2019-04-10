#!/usr/bin/env python
#coding:utf8
import os,psutil,threading
from sys import argv
def usage():
        print "usage:%s [cpu|mem] <process_name> <owner_name>"%(argv[0])
def pid_check(process_name,owner_name,exclude):
	global app_pid
	owner = '|'.join(owner_name.split(','))
	cmd = r'ps  -eo user,pid,command'
	opts = ''' |grep -w "%s"|egrep "%s"|egrep -v "grep|%s"|awk '{print $2}' '''%(process_name,owner,exclude)
	command = cmd + opts
	app_pid = os.popen(command).read().split()
def process_cpu(pid):
	try:
		p = psutil.Process(pid)
		if psutil.version_info[0] == 0:
			cpu_value = p.get_cpu_percent(1)
		else:
			cpu_value = p.cpu_percent(1)
	except Exception:
		cpu_value = 0
	cpu_lock.acquire()
	cpu_list.append(cpu_value)
	cpu_lock.release()
def cpu_used(process_name,owner_name,exclude=argv[0].split('/')[-1]):
	global threads
	threads = []
	pid_check(process_name,owner_name,exclude)
	for u in app_pid:
		t = threading.Thread(target=process_cpu,args=(int(u),))
		threads.append(t)	
def mem_used(process_name,owner_name,exclude=argv[0].split('/')[-1]):
	size = 0
	pid_check(process_name,owner_name,exclude)
	for m in app_pid:
		try:
			p = psutil.Process(int(m))
			if psutil.version_info[0] == 0:
				memory_size = p.get_memory_info()[0]
			else:
				memory_size = p.memory_info()[0]
		except Exception:
			memory_size = 0
		size += memory_size
	return size
if __name__ == "__main__":
	if len(argv) != 4:
		usage()
	else:
		action = argv[1]
		process_name = argv[2]
		owner_name = argv[3]
		if action not in ['cpu','mem']:
			usage()
		else:
			if action == 'cpu':
				cpu_list = []
				cpu_used(process_name,owner_name)
				cpu_lock = threading.Lock()
				for n in range(len(app_pid)):
					threads[n].setDaemon(False)
					threads[n].start()
				for n in range(len(app_pid)):
					threads[n].join()
				cpu = round(sum(cpu_list),2)
				print cpu
			else:
				mem = mem_used(process_name,owner_name)
                                print mem
