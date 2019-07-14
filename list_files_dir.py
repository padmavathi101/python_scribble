#!/usr/bin/python
import os
import glob

path="."
for items in os.listdir(path):
    if os.path.isfile(items):
        print "file:"+str(os.stat(items))
    elif os.path.isdir(path+items):
        print "dir:"+items
    elif os.path.islink(path+items):
        print "link:"+items
    else:
        print "unknown"
        print items
