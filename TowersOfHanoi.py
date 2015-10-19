# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 16:17:43 2015

@author: svalluru
"""

import sys

def move(src, dst, tmp, num):
    if num == 1: print 'Move from', src, 'to', dst
    else:
        move(src, tmp, dst, num-1)
        move(src, dst, tmp, 1)
        move(tmp, dst, src, num-1)

move('left', 'right', 'middle', int(sys.argv[1]))