#!/bin/bash
# QQ:s283302410
length=$#


export ORACLE_SID=RTS
if [ $length -eq 1 ] ;then
	export ORACLE_SID=$1
elif [ $length -gt 1 ];then
	echo exit
	exit
fi

archiv_log_path=/u01/app/oracle/flash_recovery_area/$ORACLE_SID/archivelog/

#echo $length
value_list=(`sqlplus -S /nolog <<EOF
connect / as sysdba
set echo off feedback off heading off underline off;
select PERCENT_SPACE_USED from V\\$FLASH_RECOVERY_AREA_USAGE;
exit;
EOF`)
echo ${value_list[2]}

cd $archiv_log_path
number=(`ls /u01/app/oracle/flash_recovery_area/$ORACLE_SID/archivelog/`)
for((i=16;i>0;i--))
do
	
done
