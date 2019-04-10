#!/bin/bash
LANG=C;df -P 2>/dev/null|egrep -v "Filesystem|tmpfs|^[1-9]"|awk '{print $2,$3}' >/tmp/disk_used.tmp
disk_total=0
disk_use=0
while read total use
do
	if [ x$disk_total != x ] && [ x$disk_use != x ]
	then
		disk_total=$[$disk_total+$total]
		disk_use=$[$disk_use+$use]
	fi
done </tmp/disk_used.tmp
rm -f /tmp/disk_used.tmp

case $1 in 
total)
	echo "$disk_total*1024"|bc
	;;
use)
	echo "$disk_use*1024"|bc
	;;
free)
        echo "($disk_total-$disk_use)*1024"|bc
        ;;
used)
	echo "scale=2
	$disk_use*100/$disk_total"|bc
	;;
*)
	echo "usage: $0 [total|use|free|used]"
	;;
esac
