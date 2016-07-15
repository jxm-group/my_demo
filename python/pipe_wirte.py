#!/usr/bin/env python
#coding=utf-8

import os 
from time import sleep

try:
    f = open("/tmp/fifo1",'w')
except Exception as e:
    print e.message

try:
    msg = f.write("em1212312345123:restart----\n")
except Exception as e:
    print e.message

sleep(10)
f.close()
print " -----------"

