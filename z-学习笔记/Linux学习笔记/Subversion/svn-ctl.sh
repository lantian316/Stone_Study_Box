#!/bin/bash
# Name:redisd
# Version:0.0.1
# Author:Stone
# QQ:283302410
# Email:lantian316@163.com
# Blog:http://blog.linuxnb.com
# Linux Command help:http://man.linuxnb.com
# Datetime:2016-07-26 22:17:28
# svn - Startup script for redis
# chkconfig: - 85 15
# description: svn Server
# Processname: svnd
# Source function library.
. /etc/rc.d/init.d/functions

user=svnuser
RETVAL=0


start() {
    su $user -c "svnserve -d -r /svndata/svn" &>/dev/null
    RETVAL=$?
    return $RETVAL
}
stop() {
    pkill svnserve
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