#!/bin/bash
export ORACLE_HOME=/app/product/11.2.0/client_1
export LD_LIBRARY_PATH=$ORACLE_HOME/lib
export ORA_NLS33=$ORACLE_HOME/ocommon/nls/admin/data
export NLS_LANG=AMERICAN_AMERICA.ZHS16GBK
export CLASSPATH=$ORACLE_HOME/jdbc/lib:$ORACLE_HOME/jlib:$ORACLE_HOME/network/jlib:$ORACLE_HOME/JRE
export PATH=$ORACLE_HOME/bin:$PATH
if [ $# != 4 ];then
echo "error ! please check your item:custom.ora.used[<username>,<password>,<tnsname>,<num>]"
exit 1
fi
echo "set heading off
set verify off
set feedback off
set linesize 200
select tablespace_name,
trunc((sum(A.USER_BYTES)/1024/1024-sum(nvl(free_m,0))/1024/1024)/(sum(A.USER_BYTES)/1024/1024),4)*100
from dba_data_files A,
(select sum(BYTES)as free_m,file_id from dba_free_space group by file_id) B
where A.file_id=B.file_id(+)
group by tablespace_name;
"|sqlplus -s $1/$2@$3 > /tmp/oraused_$3.tmp
if egrep -qi '(error|ora)' /tmp/oraused_$3.tmp;then
echo "error ! please check your item:custom.ora.used[<username>,<password>,<tnsname>,<num>]"
rm -f /tmp/oraused_$3.tmp
exit 1
fi
sed -i /^$/d /tmp/oraused_$3.tmp
while read tablespace used
do
        chk=`echo "$used > $4"|bc`
	if [ $chk == 1 ]
	then
		echo "$tablespace used is $used% will full !" >> /tmp/oraused_$3.txt
	fi
done < /tmp/oraused_$3.tmp
if [ -f /tmp/oraused_$3.txt ]
then 
	cat /tmp/oraused_$3.txt
else
	echo "ok"
fi
rm -f /tmp/oraused_$3.txt /tmp/oraused_$3.tmp
