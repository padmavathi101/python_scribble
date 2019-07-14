#!/usr/bin/python

import thread
import time

def worker_thread(id):
    print "Thread id %d is now alive"%id
    count=1
    while True:
        print "Thread with Id %d has counter value %d"%(id,count)
        time.sleep(2)
        count=count+1


for i in range(5):
    thread.start_new_thread(worker_thread,(i,))

while True:
    pass

