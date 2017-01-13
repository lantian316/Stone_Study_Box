#  -*- coding:utf-8 -*-
import IPy
import ipaddress
from IPy import IP

print(ipaddress.ip_address("192.168.2.112"))
print(ipaddress.IPV4LENGTH)

ip=IP('127.0.0.0/30')
for x in ip:
    print(x)
    
    
ip2 = IP('0x7f000000/30')
print(ip == ip2)

print(ip.reverseNames())
print(ip.reverseName())


print(ip.iptype())
print(IP('10.0.0.0/8').version())
print("sdfsdfsd",IP('::1').version())

print(IP(0x7f000001))
print(IP('0x7f000001'))
print(IP('127.0.0.1'))
print(IP('10'))