#!/usr/bin/python
# coding=utf-8

from PyQt4.QtGui import QDialog, QVBoxLayout, QPushButton, QApplication,\
    QScrollArea, QWidget, QListWidgetItem, QIcon, QListWidget, QAbstractItemView
import sys
from PyQt4.QtCore import QSize, QPoint, Qt
from PyQt4.Qt import QListView

class ItemWidget(QListWidgetItem):
    def __init__(self,iconPath,name, parent=None):
        super(ItemWidget, self).__init__(parent)
        self.setIcon(QIcon(iconPath))
        self.setText(name)

    def changeIcon(self,iconPath):
        self.setIcon(QIcon(iconPath))

class CourselibsListWidget(QListWidget):
    def __init__(self, parent=None):
        super(CourselibsListWidget,self).__init__(parent)
        #self.resize(QSize(500,250))
        self.setIconSize(QSize(300,300))
#         item = ItemWidget("image\win","Win xp", self)
        self.setViewMode(QListView.IconMode)

        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
#         self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setDragEnabled(False)
        
    def test(self):
        ItemWidget("image/login_pre.png","login.png", self)
        ItemWidget("image/login_pre.png","login.png", self)
        ItemWidget("image/login_pre.png","login.png", self)
        ItemWidget("image/login_pre.png","login.png", self)
        ItemWidget("image/login_pre.png","login.png", self)
	
#        btn = QPushButton("button1",self)
#        self.vLayout.addWidget(btn)

########################################
# 单元测试
#######################################        
if __name__=="__main__":
    app = QApplication(sys.argv)
    mainwindow = CourselibsListWidget()
    mainwindow.test()
    mainwindow.show()
    app.exec_()    
