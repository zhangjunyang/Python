# 创建一个输入姓名、提交、显示输入内容的QT界面

import os,sys
from PyQt5 import QtCore,QtWidgets,QtGui

class test():
    def setUI(self,w):
        #设置工具窗口的大小
        w.setGeometry(400,400,400,200)
        #设置工具窗口的标题
        w.setWindowTitle("Test")
        #设置窗口的图标
        w.setWindowIcon(QtGui.QIcon('icon.png'))
        QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        w.setToolTip('这是Window小工具')

        self.label = QtWidgets.QLabel(w)
        self.label.setGeometry(QtCore.QRect(60, 20, 120, 45))
        self.label.setFont(QtGui.QFont("Roman times",20))
        self.label.setText("Name:")
        #添加设置一个文本框
        self.text = QtWidgets.QLineEdit(w)
        #调整文本框的位置大小
        self.text.setGeometry(QtCore.QRect(150,30,160,30))
        #添加提交按钮和单击事件
        self.btn = QtWidgets.QPushButton(w)
        #设置按钮的位置大小
        #self.btn.setGeometry(QtCore.QRect(150,100,70,30))
        #设置按钮的位置，x坐标,y坐标
        self.btn.move(150,100)
        self.btn.setText("提交")
        #为按钮添加单击事件
        self.btn.clicked.connect(self.getText)


        self.label2 = QtWidgets.QLabel(w)
        self.label2.setGeometry(QtCore.QRect(60, 120, 300, 100))
        self.label2.setFont(QtGui.QFont("Roman times",16,QtGui.QFont.Bold))
        self.label2.setText("请输入名字")

        w.show()

    def getText(self):
        name = self.text.text()
        if name:
            try:
                self.label2.setText("你输入的名字是%s" % name)
                self.text.clear()
            except:
                self.label2.setText("请输入名字")

if __name__=='__main__': 
    #创建应用程序和对象
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    ui = test()
    ui.setUI(w)
    sys.exit(app.exec_())