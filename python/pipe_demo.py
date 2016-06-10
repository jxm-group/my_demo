#!/usr/bin/env python
#coding=utf-8

import os
os.mkfifo("./pipe")

f = open("./pipe",'r')

while True:
    msg = f.read()
    msg = msg.strip("\n") # 去掉 换行符
    if msg == "exit":
        break
    elif msg == "":
        pass
    else:
        print "pip recv: %s" % msg 


f.close()
os.remove("./pipe")
print " ------ exit-----"

