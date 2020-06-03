# 创建一个人脸图像检测处理的QT界面系统

from PyQt5 import QtCore,QtWidgets,QtGui
import sys
import cv2
import numpy as np
cascade_fn = 'C:/Users/zhangjunyang/model/haarcascades/haarcascade_frontalface_alt.xml' #训练好的xml数据
# cascade_fn = 'C:/Users/zhangjunyang/model/haarcascades/haarcascade_frontalface_alt2.xml' #训练好的xml数据
# cascade_fn = 'C:/Users/zhangjunyang/model/haarcascades/haarcascade_frontalface_default.xml' #训练好的xml数据
save_video = False
snap_flag = False
open_face = True
preprocessing = True

def Face_detect(img, cascade):  #人脸检测函数
#     rects = cascade.detectMultiScale(img, scaleFactor=1.3,minNeighbors=5, minSize=(20, 20), flags=cv2.CV_HAAR_DO_CANNY_PRUNING)
    rects = cascade.detectMultiScale(img, scaleFactor=1.3,minNeighbors=5, minSize=(20, 20), flags=0)
    if len(rects) == 0:
            return []
    print(rects)
    rects[:,2:] += rects[:,:2]  # 设置矩形框的大小
    print(rects)
    return rects

def draw_rects(img, rects, color): # 在img上绘制矩形
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

def laplaceTransform(img):    # Laplace滤波
    gray_laplace = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)
    dst = cv2.convertScaleAbs(gray_laplace)
    return dst

def SobelFilter(img):        # Sobel滤波
    x = cv2.Sobel(img,cv2.CV_16S,1,0)
    y = cv2.Sobel(img,cv2.CV_16S,0,1)
    absX = cv2.convertScaleAbs(x)
    absY = cv2.convertScaleAbs(y)
    gray_sobel = cv2.addWeighted(absX,0.5,absY,0.5,0)
    return gray_sobel

# def EqualizeHist(img):      # 直方图均衡化
#     equalize = cv2.equalizeHist(img)
#     return equalize
    
#########################################################################
##视频监控界面原型 功能说明：
##（1）按下ESC或者q键，退出视频监控界面【已实现】
##（2）按下空格键，保存当前视频图像到本地（摄像头拍照功能）【已实现】
##（3）选择是否人脸检测和将视频保存到本地（本地录像功能）【已实现】
##（4）增加功能：多路实时监控，调节亮度和对比度功能，调节画质功能，网络视频监控，循环录像功能
##（5）GUI界面封装：将视频监控功能封装成界面，实现监控产品的基本功能。
#########################################################################

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Video Surveilliance Interface"))
        MainWindow.resize(688, 427)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.Btn_VideoWriter = QtWidgets.QPushButton(self.centralWidget)
        self.Btn_VideoWriter.setGeometry(QtCore.QRect(20, 40, 191, 80))
        self.Btn_VideoWriter.setObjectName(_fromUtf8("Btn_VideoWriter"))
        self.Btn_VideoWriter.clicked.connect(self.Btn_VideoWriter_Clicked)

        self.Btn_VideoWarning = QtWidgets.QPushButton(self.centralWidget)
        self.Btn_VideoWarning.setGeometry(QtCore.QRect(20, 110, 191, 80))
        self.Btn_VideoWarning.setObjectName(_fromUtf8("Btn_VideoWarning"))

        self.Btn_VideoSnap = QtWidgets.QPushButton(self.centralWidget)
        self.Btn_VideoSnap.setGeometry(QtCore.QRect(20, 180, 191, 80))
        self.Btn_VideoSnap.setObjectName(_fromUtf8("Btn_VideoSnap"))
        self.Btn_VideoSnap.clicked.connect(self.Btn_VideoSnap_Clicked)

        self.Btn_FaceDetection = QtWidgets.QPushButton(self.centralWidget)
        self.Btn_FaceDetection.setGeometry(QtCore.QRect(20, 250, 191, 80))
        self.Btn_FaceDetection.setObjectName(_fromUtf8("Btn_FaceDetection"))
        self.Btn_FaceDetection.clicked.connect(self.Btn_FaceDetection_Clicked)

        self.Btn_Preprocessing = QtWidgets.QPushButton(self.centralWidget)
        self.Btn_Preprocessing.setGeometry(QtCore.QRect(20, 320, 191, 80))
        self.Btn_Preprocessing.setObjectName(_fromUtf8("Btn_Preprocessing"))
        self.Btn_Preprocessing.clicked.connect(self.Btn_Preprocessing_Clicked)

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName(_fromUtf8("label"))
        #self.label.setGeometry(QtCore.QRect(20, 320, 91, 41))

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 688, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Btn_VideoWriter_Clicked(self):
        save_video =True
    def Btn_VideoSnap_Clicked(self):
        snap_flag = True
    def Btn_FaceDetection_Clicked(self):
        open_face = True
    def Btn_Preprocessing_Clicked(self):
        preprocessing = True
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle( "MainWindow")

        self.Btn_VideoWriter.setText(_fromUtf8("Recoding"))
        self.Btn_VideoWarning.setText(_translate("MainWindow","Video Warning",None))
        self.Btn_VideoSnap.setText(_translate("MainWindow","Snap",None))
        self.Btn_FaceDetection.setText(_translate("MainWindow","Face Detection",None))
        self.Btn_Preprocessing.setText(_translate("MainWindow","Preprocessing",None))
        self.label.setText("Image")
    def camera_cap(self,MainWindow):
        capture1=cv2.VideoCapture(0) #获取摄像头数据
      #将capture保存为motion-jpeg,cv_fourcc为保存格式
        size = (int(capture1.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture1.get(cv2.CAP_PROP_FRAME_HEIGHT)))

      #isopened可以查看摄像头是否开启
        print(capture1.isOpened(),r"摄像头已开启！")
        num=0
        if save_video:
            flag = True
#             fourcc = cv2.VideoWriter_fourcc(*'XVID')
            fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
            video=cv2.VideoWriter("VideoTest.avi", fourcc,30, size)
        else:
            flag = None
          #要不断读取image需要设置一个循环
        while True:
            if capture1.isOpened():
                ret1,img1=capture1.read()
           #视频中的图片一张张写入
            if flag:
                video.write(img1)
            cv2.imshow('image_origin',img1)
            cv2.waitKey(1)
            #cv2.imwrite('%s.jpg'%(str(num)),img)
            gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
            cascade = cv2.CascadeClassifier(cascade_fn) #加载分类器
            if not cascade:
                print(stderr,"ERROR:Could not load classifier cascade!")
            else:
                pass
            rects1 = Face_detect(gray, cascade) #进行人脸检测
            vis1= img1.copy()
            if open_face:
                draw_rects(vis1, rects1, (0, 255, 0))
                cv2.imshow('image_Face_detect', vis1)
            if preprocessing:
                laplace=laplaceTransform(vis1)
                cv2.imshow('image_laplaceTransform',laplace)

                sobel =SobelFilter(vis1)
                cv2.imshow('image_SobelFilter',sobel)

                equalize1 = cv2.equalizeHist(gray)
                draw_rects(equalize1, rects1, (0, 255, 0))
                cv2.imshow('image_equalizeHist1',equalize1)

            key=cv2.waitKey(2)#里面数字为delay时间，如果大于0为刷新时间，
                #超过指定时间则返回-1，等于0没有返回值，但也可以读取键盘数值。此处设置刷新时间为2ms
            num = num+1
            if key == ord('q'):
                break
            if key == 27: #27表示ESC的ASCII码值
                break
            if snap_flag:
                cv2.imwrite(r'通道1_保存的图片'+str(num)+'.jpg',img1)
        capture1.release()#关闭摄像头
        cv2.destroyAllWindows()#关闭所有窗口


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    ui.camera_cap(window)
    sys.exit(app.exec_())