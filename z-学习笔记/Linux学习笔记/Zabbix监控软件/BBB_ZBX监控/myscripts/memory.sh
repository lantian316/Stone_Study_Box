#/bin/bash
function total {
	/usr/bin/free |grep 'Mem'|awk '{print $2}'
}
function used {
	/usr/bin/free |grep 'Mem'|awk '{print $3}'
}
function free {
	/usr/bin/free |grep 'Mem'|awk '{print $4}'
}
function buff {
        /usr/bin/free |grep 'Mem'|awk '{print $6}'
}
function swap
{	
	/usr/bin/free | awk /^Swap/'{print $2}'
}
function shared
{
	/usr/bin/free | awk /^Mem/'{print $5}'
}
$1
