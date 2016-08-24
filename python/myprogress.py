#!/usr/bin/env python
# -*- coding: utf-8 -*-  


# 参考:
#  http://blog.csdn.net/a379840689/article/details/41088735

from PyQt4.QtCore import Qt,  QString
from PyQt4.QtGui  import  QLabel, QWidget,QHBoxLayout, QFontMetrics


class WidgetProgress(QWidget):
    def __init__(self,parent = None):
        super(WidgetProgress,self).__init__(parent)

        #self.setFixedWidth(300)
        self.setFixedSize(500,300)
        self.tipLabel = QLabel(self.tr("downloading..."))

        self.setStyleSheet("background-color:rgba(5,5,255,0);") 

        self.tipLabel.setStyleSheet(
            "background-color:rgba(5,5,255,255);"
            "QToolTip{"
                 "background-color:rgba(5,255,55,255)"
             "};"
            ) 
    

        labelLayout = QHBoxLayout(self)
        labelLayout.addStretch()
        labelLayout.addWidget(self.tipLabel)
        labelLayout.addStretch()

        self.test()
         
                

    def test(self):
        s = "win7_32 test1 test2 test3 test4"
        text = self.tr("course ") + s + u" downloading..."

        text_2 = self.__getElidedText(self.tipLabel.font(),text, 150)
        self.tipLabel.setText(text_2)
        #text = "<html style=\"background:rgb(255,255,255);" \
        #        "border:0px\"" \
        #        ">" \
        #        "<font color=red>%s</font>" \
        #        "</html>" % text
        self.setToolTip(text)

    def __getElidedText(self,font,s,maxWidth):
        '''
        '''
        fontWidth = QFontMetrics(font)
        width = fontWidth.width(s)
        if width >= maxWidth:
            s = fontWidth.elidedText(s,Qt.ElideRight,maxWidth)
        return s

class Widget(QWidget):
    def __init__(self,parent=None):
        super(Widget,self).__init__(parent)
        self.dlg = WidgetProgress(self)
        self.setStyleSheet("background-color:rgba(155,5,255,255);"
            "QToolTip{"
                 "background-color:rgba(5,255,55,255)"
             "};"
        ) 

if __name__ == "__main__":
    from PyQt4.QtGui import  QApplication
    import sys
    app = QApplication(sys.argv)
    #dlg =  WidgetProgress()
    dlg =  Widget()
    dlg.show()
    app.exec_()




