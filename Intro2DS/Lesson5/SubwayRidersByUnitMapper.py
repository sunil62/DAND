# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:09:33 2015

@author: svalluru
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:17:26 2015

@author: svalluru
"""

import sys
import string

def mapper():
    for line in sys.stdin:
        
        data = line.strip().split(",")
        if len(data)!= 22 or data[1] == 'UNIT':
            continue
        if data[1] == 'R550':
            print "{0}\t{1}".format(data[1],data[6])
        

mapper()