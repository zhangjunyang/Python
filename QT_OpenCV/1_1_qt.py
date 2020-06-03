import os,sys,time
from PyQt5 import QtCore,QtWidgets,QtGui

class test(QtWidgets.QWidget):
    def setUI(self):
        #设置工具窗口的大小
        self.setGeometry(400,400,400,200)
        #设置工具窗口的标题
        self.setWindowTitle("Test")
        #设置窗口的图标
        self.setWindowIcon(QtGui.QIcon('xxx.jpg'))
        self.show()

if __name__=='__main__':
    #创建应用程序和对象
    app = QtWidgets.QApplication(sys.argv)
    ui = test()
    ui.setUI()
    sys.exit(app.exec_())