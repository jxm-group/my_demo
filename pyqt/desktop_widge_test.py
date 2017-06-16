#!/usr/bin/env python
# encoding: utf-8

"""
@version : 
@author  : 
@license : 
@contact : ****@massclouds.com
@site    : http://blog.csdn.net/***
@software: PyCharm
@time    : 16-11-10 下午11:26
"""
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QPushButton
from PyQt4.QtCore import SIGNAL

class PushButton(QPushButton):
    def __init__(self,parent=None):
        super(PushButton, self).__init__(None)

        self.__desktop = QApplication.desktop()
        self.__reset_size()
        self.connect( self.__desktop,SIGNAL("resized(int)"),self.desktop_resize_test)

    def __reset_size(self):
        qRect = self.__desktop.screenGeometry()        #设备屏幕尺寸
        self.resize(qRect.width()/3, qRect.height()/3)
        self.move(qRect.width()/3, qRect.height()/3)
        print "reset size  : ", self.size()

    def desktop_resize_test(self,screen):
        print  "------- desktop_resize_test -------"
        print "screen : ", screen
        desktopRect =  self.__desktop.availableGeometry() #获取可用桌面大小:
        print "可用桌面大小:", desktopRect

        screenRect =  self.__desktop.screenGeometry()   #获取设备屏幕大小
        print "设备屏幕大小:" ,screenRect
        self.__reset_size()
        print  "------------------------------"

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    button = PushButton()
    button.show()
    app.exec_()
