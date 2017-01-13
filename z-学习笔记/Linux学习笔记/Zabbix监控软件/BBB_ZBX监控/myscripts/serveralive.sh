#!/bin/bash
#

serverip=$1
if /usr/bin/ping -c 1 -W 1 $serverip &>/dev/null;then
	#if [ $serverip == "123.59.56.188" ];then
		echo 10
	#elif [ $serverip == "106.75.148.159" ];then
	#	echo 9
	#elif [ $serverip == "120.132.49.163" ];then
	#	echo 8
	#elif [ $serverip == "180.150.179.130" ];then
	#	echo 7
	#else
	#	echo 1
	#fi
else
	echo 0
fi
