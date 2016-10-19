#!/usr/bin/env python

import re

line = "Some line to test"

matchObj = re.match( r".* line .*", line)
if matchObj != None:
    print matchObj.group()
