#!/usr/bin/env python
#coding=utf-8

# http://blog.chinaunix.net/uid-20393955-id-345449.html
from ctypes import *

foo = CDLL('./foo.so')
myprint = foo.myprint
myprint.argtypes = [POINTER(c_char)] # 参数类型，为char指针
myprint.restype = c_char_p # 返回类型，同样为char指针

res = myprint("hello world")
print "python res = ",res


add = foo.add
add.argtypes = [c_float, c_float] # 参数类型，两个float（c_float内ctypes类型）
add.restype = c_float
print add(4.31, 4.2)

