#!/usr/bin/python

import os
def child_proc():
    print"I am the child and my pid is%d"%os.getpid()
    print"child is exiting"
def parent_proc():
    print"I am the parent and my pid is%d"%os.getpid()
    childid=os.fork()
    if(childid==0):
        #we are inside child
        child_proc()
    else:
        print"pid of child is%d"%childid
    while True:
        pass

parent_proc()

