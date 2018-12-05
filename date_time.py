# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:13:57 2018

@author: sebastian
"""

from datetime import datetime
now = datetime.now()

print('%02d-%02d-%04d' % (now.month, now.day, now.year))
print('%02d:%02d:%03d' % (now.hour, now.minute, now.second))