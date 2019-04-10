#!/bin/bash
if [ $# != 1 ];then
echo "error ! please check your item:custom.ora.chkdf <system_username>"
exit 1
fi

echo "set heading on
set verify off
set feedback off
set linesize 200
col tablespace_name for a15
col file_name for a45
col online_status for a15
select tablespace_name,file_name,online_status from dba_data_files where online_status='OFFLINE';
exit;
" >/tmp/oradf.sql
if ! id $1 >/dev/null 2>&1
then
        echo $1 user not exists
        exit 1
else
	su $1 -c "cat ~$1/.bash_profile |grep ^export >/tmp/.oracle_env_$$;source /tmp/.oracle_env_$$;rm -f /tmp/.oracle_env_$$;sqlplus -s / as sysdba @/tmp/oradf.sql|sed  '/^$/d'" > /tmp/oradf.tmp
fi
if egrep -qi 'error' /tmp/oradf.tmp;then
	cat /tmp/oradf.tmp
	rm -f /tmp/oradf.tmp /tmp/oradf.sql
	exit 1
fi
if grep -qi offline /tmp/oradf.tmp
then
	cat /tmp/oradf.tmp
else
	echo "ok"
fi
rm -f /tmp/oradf.tmp /tmp/oradf.sql
