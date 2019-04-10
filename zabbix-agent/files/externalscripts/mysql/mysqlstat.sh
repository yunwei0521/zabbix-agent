#!/bin/bash
#####################################################################
#grant select on mysql.* to zabbix@localhost identified by '123456';#
#####################################################################
user=zabbix
password=123456
command="select * from mysql.user;"
mysql -u "$user" -p"$password" -e "$command" &> /dev/null
result=$?
if [ $result -eq 0 ] 2> /dev/null ;then
	echo "up"
	exit 0
else
	echo "down"
	exit 1
fi
