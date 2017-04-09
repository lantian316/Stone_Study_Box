#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser

configfile="Config_file.ini"
config = configparser.ConfigParser()
config.readfp(open(configfile))
a = config.get("ZIP","Checksum")
b = config.get("MYSQLD","Database")
print(a)
print(b)

print(config.sections())
print(config.options("MYSQLD"))
print(config.items("MYSQLD"))