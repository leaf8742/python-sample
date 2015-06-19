#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json

jsonString=''
with open('/Users/LEAF/workingcopy/Eading/软件/eabox/02_IOS/代码/trunk/com.eading.amazing/com.eading.wireless.xcodeproj/project.pbxproj', 'r', encoding='utf-8') as f:
    condition = False
    for line in f.readlines():

        if line.find('End PBXProject section') != -1:
            condition = False

        if condition:
            jsonString += line

        if line.find('Begin PBXProject section') != -1:
            condition = True

    print(jsonString)
