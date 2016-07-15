#!/usr/bin/env python
#coding=utf-8

import os
os.mkfifo("/tmp/fifo1")

try:
    f = open("/tmp/fifo1",'r')
except Exception as e:
    print e.message

while True:
    try:
        f = open("/tmp/fifo1",'r')
        msg = f.readline()
    except Exception as e:
        print e.message
    
    #msg = msg.strip("\n") # 去掉 换行符
    msg,tmp = msg.split("\n")

    if msg == "exit":
        break
    elif msg == "":
        pass
    else:
        print "recv pipe : %s" % msg 

f.close()

#msg=None
#
#while True:
#    try:
#        cmd = "cat /tmp/fifo1"
#        f = os.popen(cmd, "r")
#        msg = f.readline().strip('\n')  # 去掉\n
#        f.close()
#    except Exception as e:
#        print e.message
#
#    msg = msg.strip("\n") # 去掉 换行符
#
#    if msg == "exit":
#        break
#    elif msg == "":
#        pass
#    else:
#        print "recv pipe : %s\n" % msg 
#

os.remove("/tmp/fifo1")
print " ------ exit-----"

