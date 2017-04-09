#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os

system_type=os.name

if system_type=="nt":
    print("The current system is Windows...")
elif system_type=="posix":
    print("The current system is Linux  OR MAC OS...")
else:
    print('I don\'t know this system...')