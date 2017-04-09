#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import platform

system_type=platform.system()
if system_type=="Windows":
    print("The current system is Windows...      System version is Windows",platform.release())
elif system_type=="Linux":
    print("The current system is Linux...      System version is",platform.release())
else:
    print('I don\'t know this system...')