#!/bin/bash
su grid -c "cat ~grid/.bash_profile |grep ^export >/tmp/.grid_env_$$;source /tmp/.grid_env_$$;rm -f /tmp/.grid_env_$$;asmcmd ls -ls"|egrep -v "(^#|^$|^State)"|awk '{print $7,$8}' >/tmp/asm_disk.tmp
asm_total=0
asm_free=0
while read total free
do
        if [ x$asm_total != x ] && [ x$asm_free != x ]
        then
                asm_total=$[$asm_total+$total]
                asm_free=$[$asm_free+$free]
        fi
done </tmp/asm_disk.tmp
rm -f /tmp/asm_disk.tmp

case $1 in
total)
        echo "$asm_total*1024*1024"|bc
        ;;
use)
        echo "($asm_total-$asm_free)*1024*1024"|bc
        ;;
free)
        echo "$asm_free*1024*1024"|bc
        ;;
used)
        echo "scale=2
        ($asm_total-$asm_free)*100/$asm_total"|bc
        ;;
*)
        echo "usage: $0 [total|use|free|used]"
        ;;
esac
