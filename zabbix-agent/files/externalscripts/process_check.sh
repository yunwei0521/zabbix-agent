#!/bin/bash
case $# in
3)
	num=`ps -ef |egrep -v "$0|grep"|grep -w "$2"|grep -w "$1"|wc -l`
        if [ $num == $3 ]
        then
                echo $num
        else
                echo 0
        fi
        ;;
2)
	ps -ef |egrep -v "$0|grep"|grep -w "$2"|grep -w "$1"|wc -l
	;;
1)
	ps -ef |egrep -v "$0|grep"|grep -w "$1"|wc -l
	;;
*)
	exit 1
esac	
