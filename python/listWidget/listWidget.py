#coding:utf-8
from PyQt4.QtGui import QMainWindow, QListWidget, QAbstractItemView, QListView,\
    QListWidgetItem, QIcon, QApplication, QVBoxLayout, QMenu, QCursor, QAction
from PyQt4.QtCore import QSize, SIGNAL, pyqtSignature, Qt
# from PyQt4.Qt import Qt
import sys
# from PyQt4 import QtCore
class ItemWidget(QListWidgetItem):
    def __init__(self,iconPath,name, parent=None):
        super(ItemWidget, self).__init__(parent)
        self.setIcon(QIcon(iconPath))
        self.setText(name)
        
class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)
#         self.setFixedSize(QSize(600,400))
#         self.setWindowTitle("test")
#         self.listWidget = QListWidget(self)
        self.setStyleSheet("QListWidget{margin:0px;padding:0px;border:0px;outline:0px;}"
                          "QListWidget:item{outline:0px; margin-left:25px;margin-bottom:5px;}"
#                           "QListWidget:item:selected { background-color:#EDEDEF;color:balck }"
#                         "QListWidget:item:text{background-color:#EDEDEF}"
                          )
        self.verticalScrollBar().setStyleSheet("QScrollBar:vertical{"
                                                                "width:6px;"
                                                                "background-color:rgba(180,180,180,180);"
                                                                "margin:0px,0px,0px,0px;"
                                                                "padding-top:0px;"
                                                                "padding-bottom:0px;}"
                                                        "QScrollBar:handle:vertical{"
                                                                       " width:6px;"
                                                                        " background:rgba(80,80,80,50%);"
                                                                        "border-radius:3px; "  # 滚动条两端变成椭圆
                                                                       " min-height:80;}"
                                                        "QScrollBar:handle:vertical:hover {"
                                                            "width:6px;"
                                                            "background:rgba(0,0,0,50%); "  # 鼠标放到滚动条上的时候，颜色变深
                                                            "border-radius:3px;"
                                                            "min-height:20;}"
                                                        "QScrollBar:add-line:vertical{"   # 这个应该是设置下箭头的，3.png就是箭头
                                                                "height:0px;width:6px;"
                                                                #"border-image:url(:/images/a/3.png);"
                                                                "subcontrol-position:bottom;}"
                                                                
                                                        "QScrollBar:sub-line:vertical{"   # 设置上箭头
                                                                
                                                                "height:0px;width:6px;"
                                                                #"border-image:url(:/images/a/1.png);"
                                                                "subcontrol-position:top;}"
                                                                )
#         self.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal{"
#                                                                 "height:0px;"
#                                                                 "background:rgba(0,0,0,0);"
#                                                                 "margin:0px,0px,0px,0px;"
#                                                                 "padding-top:0px;"
#                                                                 "padding-bottom:0px;}"
#                                                                  
#                                                         "QScrollBar:add-line:vertical{"   # 这个应该是设置下箭头的，3.png就是箭头
#                                                                 "height:0px;width:0px;"
#                                                                 #"border-image:url(:/images/a/3.png);"
#                                                                 "subcontrol-position:bottom;}"
#                                                                
#                                                         "QScrollBar:sub-line:vertical{"   # 设置上箭头
#                                                                
#                                                                 "height:0px;width:0px;"
#                                                                 #"border-image:url(:/images/a/1.png);"
#                                                                 "subcontrol-position:top;}"
#                                                                 )
#         self.setFixedSize(QSize(500,300))
        self.setIconSize(QSize(110,85))
        self.setViewMode(QListView.IconMode)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
#         self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setDragEnabled(False)
        self.connect(self, SIGNAL("itemDoubleClicked(QListWidgetItem*)"),self.itemDoubleClicked)
#         self.connect(self, SIGNAL("itemActivated(QListWidgetItem*)"),self.itemActivated)
    def itemDoubleClicked(self, item):
        self.emit(SIGNAL("takeStuComputer"), item.text())
#     def mouseReleaseEvent(self, event):
# 
#         self.emit(SIGNAL("mouseRelase"))
    def contextMenuEvent (self, event):
        if self.itemAt(event.pos()):
            contextMenu = QMenu(self) 
            rightAction = QAction(self.tr(u'Screen Sharing'), self, triggered=self.slotActionHandler)
            contextMenu.addAction(rightAction)
    #         self.actionStuComputerBroadCast.connect(self.slotActionHandler)
            
            contextMenu.exec_(QCursor.pos())
#         self.customContextMenuRequested[QtCore.QPoint].connect( self.slotActionHandler)
#         self.actionStuComputerBroadCast = self.contextMenu.addAction(self.tr(u'Screen Sharing'))
    def slotActionHandler(self):  
        
        self.emit(SIGNAL("stuComputerBroadCast"), self.currentItem().text())
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    test = ListWidget()
    test.resize(QSize(600,555))
    test.show()
    test.test()
    app.exec_()