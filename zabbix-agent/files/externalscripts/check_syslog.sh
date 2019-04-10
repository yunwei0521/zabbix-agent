#!/bin/bash
cat $1|grep "`date '+%b %e'`"|grep -Ei 'error|fail' |grep -v "peer died" |grep -v "importing name"|grep -v "Invalid user"|grep -v "Failed password"|grep -v "Authentication failed" > /tmp/syslog_check.tmp
if [ $? != 0 ]
then
	echo "ok"
	rm -f /tmp/syslog_check.tmp
else
	cat /tmp/syslog_check.tmp
fi
