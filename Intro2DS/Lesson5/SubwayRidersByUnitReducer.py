# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:20:10 2015

@author: svalluru
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:36:41 2015

@author: svalluru
"""

import sys

def reducer():
    
    #Also make sure to fill out the mapper code before clicking "Test Run" or "Submit".

    #Each line will be a key-value pair separated by a tab character.
    #Print out each key once, along with the total number of Aadhaar 
    #generated, separated by a tab. Make sure each key-value pair is 
    #formatted correctly! Here's a sample final key-value pair: 'Gujarat\t5.0'

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
        
    aadhaar_generated = 0
    old_key = None
    
    lines = sys.stdin.readlines()           
    lines.sort()  
    for line in lines:
        data = line.strip().split("\t")
        if len(data) !=2:
            continue
        this_key, count = data
        
        if old_key and old_key != this_key:
            print "{0}\t{1}".format(old_key,aadhaar_generated)
            aadhaar_generated = 0
        old_key = this_key
        aadhaar_generated += float(count)
    if old_key !=None:
        print "{0}\t{1}".format(old_key,aadhaar_generated)
            
            
            
            
        # your code here

reducer()
