#!/usr/bin/python

import socket
import sys
import signal

def handler(signum,frm):
    sock.close()
    print sock
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address=('localhost',10000)

print 'started server on port %s on ip %s'%server_address

sock.bind(server_address)

signal.signal(signal.SIGALRM,handler)
signal.alarm(50)
try:
    sock.listen(1)
    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()

except:
    print "hello"



