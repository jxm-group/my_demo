#!/usr/bin/env python
# encoding: utf-8


"""
@version : v4.5
@author  : jiangxmin
@license : 
@contact : jiang_xmin@massclouds.com
@site    : http://blog.csdn.net/jxm_csdn
@software: PyCharm
@file    : mydlg.py.py
@time    : 16-7-3 下午4:17
"""

import sys
from PyQt4.QtGui import QApplication,QDialog, QPixmap, QPalette, QBrush
from PyQt4 import uic
import res                                     # 导入资源文件 *****

class MyDlg(QDialog):
    def __init__(self):
        super(MyDlg, self).__init__()
        uic.loadUi("./mydlg.ui", self)            #  加载ui文件  *****

        self.setGeometry(50,50,800,600)
        self.setAutoFillBackground(True)

        # 设置窗口背景
        pixmap = QPixmap(":/images/onepiece.jpg").scaled(self.size()) # 适应窗口大小
        palette = QPalette()
        palette.setBrush(QPalette.Window,QBrush(pixmap))
        self.setPalette(palette)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    dlg = MyDlg()
    dlg.show()
    app.exec_()

