#!/usr/bin/python

import os


for dirpath,dirnames,filenames in os.walk("/home/"):
    print "directory path is"+dirpath
    for directory in dirnames:
        print "dir:"+os.path.join(dirpath,directory)
    for filename in filenames:
        print "file:"+os.path.join(dirpath,filename)
