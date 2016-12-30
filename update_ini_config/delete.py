#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser

config = configparser.ConfigParser()

config.read('config_file.ini')
#config.remove_option("ematter", "ges")
#第一个是中括号里面的，第二个是key，第三个是需要修改的新值

config.remove_section("ematter")

config.write(open('config_file.ini', "w"))