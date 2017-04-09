#!/bin/bash

# Author:Stone
# QQ:283302410
# Email:lantian316@163.com
# Blog:http://blog.linuxnb.com
# Linux Command help:http://man.linuxnb.com
# Datetime:2017-03-31 15:17:28


BASE_PATH=/home/beibeibao-online/wwwdata/
SHELL_WORK_PATH=`pwd`
WAR_FILE_NAME=$1
PROJECT_NAME=$2
USER=tomcat

date1=$(date +\%Y\%m\%d-\%H\%M\%S)
#date2=$(date +\%Y\%m\%d)



check() {
	echo "开始检查$1参数文件是否存在 ..."
	cat /etc/passwd | grep $USER >>/dev/null 2>&1
	make_sure_user=$?
	if [ ! -f "./$WAR_FILE_NAME" ]; then
		echo $WAR_FILE_NAME 参数文件不存在...
		exit 2
	elif [ ! -d "$BASE_PATH$PROJECT_NAME" ]; then
		echo $BASE_PATH$PROJECT_NAME 原始代码目录不存在...
		echo 操作中断，请手动确认....
		exit 2
    elif [ $make_sure_user -ne 0 ];then
        echo "$USER    用户不存在..."
	else
		echo 检测成功...
		sleep 3
		backup
	fi
}



backup() {
	echo "开始备份原始代码目录   $BASE_PATH$PROJECT_NAME   ..."
	sleep 2
	mv $BASE_PATH$PROJECT_NAME $BASE_PATH$PROJECT_NAME$date1
	if [ $? = 0 ];then
		echo "备份成功,,原始代码目录备份到   $BASE_PATH$PROJECT_NAME$date1 ..."
		bushu
	else
		echo "........................备份失败.操作中断..."
		exit 1
	fi
}

bushu() {
	mkdir $BASE_PATH$PROJECT_NAME
	echo "创建目录  $BASE_PATH$PROJECT_NAME     成功...."
	cp $WAR_FILE_NAME $BASE_PATH$PROJECT_NAME
	echo "复制$WAR_FILE_NAME到$BASE_PATH$PROJECT_NAME     成功...."
	cd $BASE_PATH$PROJECT_NAME
	echo "开始解压新的war包......"
	sleep 3
	if jar -xf $WAR_FILE_NAME;then
		echo "新war包解压成功......"
		rm -f $BASE_PATH$PROJECT_NAME/$WAR_FILE_NAME
		update_quanxian
	else
		echo "........................解压失败.操作中断..."
		exit 1
	fi
}

update_quanxian() {
	cd $SHELL_WORK_PATH
	echo "开始修改新的代码目录为合适的所有者和权限...."
	chown -R $USER.$USER $BASE_PATH$PROJECT_NAME
	echo "新代码目录所有者和权限....修改成功......"
	echo
	echo "请检查$PROJECT_NAME项目的配置文件...应用代码级别de配置文件"
	echo "确保配置没有问题后，切换到tomcat的bin目录执行su $USER -c ./startup.sh"
	exit 0
}

start() {
	check
}

usage() {
	echo "请必须输入两个参数,第一个参数为war包名，第二个为项目名"
	echo $"Usage: $0 WAR_FILE_NAME {mpayweb|mpayadmin}"
}

if [ $# != 2 ] ; then
	usage
	exit 1
else
	start
fi
