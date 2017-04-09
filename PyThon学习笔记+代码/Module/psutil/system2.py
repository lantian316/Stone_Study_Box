#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import psutil

if psutil.WINDOWS:
    print("The current system is Windows...")
else:
    print('The current system is Linux  OR MAC OS...')