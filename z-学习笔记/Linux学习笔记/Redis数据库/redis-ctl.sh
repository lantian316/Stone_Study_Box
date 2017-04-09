#!/bin/bash
# Name:redisd
# Version:0.0.1
# Author:Stone
# QQ:283302410
# Email:lantian316@163.com
# Blog:http://blog.linuxnb.com
# Linux Command help:http://man.linuxnb.com
# Datetime:2016-07-26 22:17:28
# Redis - Startup script for redis
# chkconfig: - 85 15
# description: Redis Server
# Processname: redisd
# Source function library.
# 1、此脚本请放在redis根目录
# 2、使用此脚本启动的时候请确保切换到redis_home目录
. /etc/rc.d/init.d/functions

user=redis
redisip=`ps -ef | grep redis-server | grep -v grep | awk '{print $NF}' | cut -d: -f1`
redisport=`ps -ef | grep redis-server | grep -v grep | awk '{print $NF}' | cut -d: -f2`
REDIS_HOME=`pwd`
binfile=$REDIS_HOME/bin/redis-server
config=$REDIS_HOME/etc/redis.conf
RETVAL=0


start() {
    su $user -c "$binfile $config" &>/dev/null
    RETVAL=$?
    return $RETVAL
}
stop() {
    $REDIS_HOME/bin/redis-cli -h $redisip -p $redisport shutdown
    RETVAL=$?
    return $RETAVAL
}
case "$1" in
start)
    start
    ;;
stop)
    stop
    ;;
restart)
    stop
    sleep 3
    start
    ;;
*)
    echo $"Usage: $0 {start|stop|restart}"
    RETVAL=1
esac
exit $RETVAL