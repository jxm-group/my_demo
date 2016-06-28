#!/usr/bin/env python
#coding=utf-8
from PyQt4.QtGui import QDialog,QPushButton
from PyQt4.QtCore import pyqtSlot,QMetaObject

class dialog(QDialog):
    def __init__(self,parent=None):
        super(dialog, self).__init__(parent)

        self.setModal(True)
        self.setGeometry(100,100,600,400)


        self.ok=QPushButton(self)
        self.ok.move(200,350)
        self.ok.setText("ok")
        self.ok.setObjectName("ok_pushbutton")

        self.cancle = QPushButton(self)
        self.cancle.move(400,350)
        self.cancle.setText("cancle")
        self.cancle.setObjectName("cancle_pushbutton")

        QMetaObject.connectSlotsByName(self) #信号和槽 自动连接

    @pyqtSlot()
    def on_ok_pushbutton_clicked(self): # on_{objiectName}_clicked
        print "ok"
        self.accept()

    @pyqtSlot()
    def on_cancle_pushbutton_clicked(self):
        print "cancel"
        self.reject()


if __name__ == "__main__":
    from PyQt4.QtGui import QApplication
    import sys

    app = QApplication(sys.argv)

    dlg = dialog()
    result = dlg.exec_()
    if result == QDialog.Accepted:
        print "accepted"
    elif result == QDialog.Rejected:
        print "rejected"

    else:
        print "other"


    # win.show()
    #app.exec_()
