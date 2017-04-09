#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser
config = configparser.ConfigParser()
# set a number of parameters
config.read('config_file.ini')
#有没有这一句很关键，如果有这句是追加，没有这句会替换原有内容

config.add_section("book")
config.set("book", "title", "the python standard library")
config.set("book", "author", "fredrik lundh")
config.add_section("ematter")
config.set("ematter", "pages", "250")
# write to file
config.write(open('config_file.ini', "w"))
