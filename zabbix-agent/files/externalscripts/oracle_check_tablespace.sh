#!/bin/bash
if [ $# != 1 ];then
echo "error ! please check your item:custom.ora.chkts [<system_username>]"
exit 1
fi

echo "set heading on
set verify off
set feedback off
set linesize 200
col tablespace_name for a15
select TABLESPACE_NAME,STATUS from dba_tablespaces where STATUS= 'OFFLINE';
exit;
" >/tmp/orats.sql
if ! id $1 >/dev/null 2>&1
then
	echo $1 user not exists
	exit 1
else
	su $1 -c "cat ~$1/.bash_profile |grep ^export >/tmp/.oracle_env_$$;source /tmp/.oracle_env_$$;rm -f /tmp/.oracle_env_$$;sqlplus -s / as sysdba @/tmp/orats.sql|sed  '/^$/d'" > /tmp/orats.tmp
fi
if egrep -qi 'error' /tmp/orats.tmp;then
	cat /tmp/orats.tmp
	rm -f /tmp/orats.tmp /tmp/orats.sql
	exit 1
fi
if grep -qi offline /tmp/orats.tmp
then
	cat /tmp/orats.tmp
else
	echo "ok"
fi
rm -f /tmp/orats.tmp /tmp/orats.sql
