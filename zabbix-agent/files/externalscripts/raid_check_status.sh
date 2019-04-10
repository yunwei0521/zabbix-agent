#!/bin/bash
function error_message(){
	printf "Usage: $0 temp|online pdN \n"
	exit 1
}
[ $# -ne  3 ] && {
	error_message
}
EnclosureDevID=$3
MegaPATH=/opt/MegaRAID/MegaCli/MegaCli64
SoltNU=$(printf $2 | cut -c 3-)

#module for temperate
function temp_status() {
if [ -z $SoltNU ] || [ -z $EnclosureDevID ]
then
	error_message
fi
ru=$($MegaPATH -pdInfo -PhysDrv[$EnclosureDevID:$SoltNU] -aALL | grep -i Temp | awk -F ":" '{print  $2}' | awk -F "C" '{print $1}')
[ -z $ru ] && {
	error_message
}
echo $ru
}


#module for online
function online_status() {
if [ -z $SoltNU ] || [ -z $EnclosureDevID ]
then
	error_message
fi
ru=$(/opt/MegaRAID/MegaCli/MegaCli64 -pdInfo -PhysDrv[$EnclosureDevID:$SoltNU] -aALL | grep '^Firmware state' | awk -F ":" '{print $2}' | awk -F "," '{print $1}' | sed 's/ //g')
[ -z $ru ] && {
	error_message
}
echo $ru
}




case $1 in
	temp)
	temp_status
	;;
	online)
	online_status
	;;
	*)
	error_message
	;;
esac
