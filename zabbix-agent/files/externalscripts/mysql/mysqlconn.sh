#!/bin/bash
#####################################################################
#grant select on mysql.* to zabbix@localhost identified by '123456';#
#####################################################################
user=zabbix
password=123456
command="show status like '%connect%';"
SCPATH="/etc/zabbix/externalscripts/mysql"

function query(){
result=`mysql -u $user -p"$password" -e "$command" 2> /dev/null | grep -w $1 | awk '{print $2}'`
if [ $result -gt 0 ] 2> /dev/null ;then
	echo $result
else
	echo "connect to mysql server confused"
	exit 1
fi
}

function maxconn(){
	command="show variables like 'max_connections';"
	result=`mysql -u $user -p"$password" -e "$command" 2> /dev/null | tail -n 1 | awk '{print $2}'`
	if [ $result -gt 0 ] 2> /dev/null ;then
        	echo $result
	else
        	echo "connect to mysql server confused"
        	exit 1
	fi

}

function connpercent(){
	max=`maxconn`
	now=`query Threads_connected`
	echo `$SCPATH/calc.py $now $max`
}

case $1 in
	error)
	query Aborted_connects
	;;
	count)
	query Connections
	;;
	max)
	query Max_used_connections
	;;
	now)
	query Threads_connected
	;;
	per)
	connpercent
	;;
	*)
	echo "Usage: $0 error|count|max|now|per"
	exit 1
	;;
esac	
