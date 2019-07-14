#!/usr/bin/python

import signal

def ctrlc_handler(signum,frm):
    print "haha`you cant kill me~"

print"installing signal handler"

signal.signal(signal.SIGINT,ctrlc_handler)

print "DOne"

while True:
    pass
