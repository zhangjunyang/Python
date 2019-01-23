# PyQt+OpenCV 录制保存、播放视频
#! /usr/bin/env python
#coding=utf-8
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import opencv
from PIL import Image
#this is important for capturing/displaying images
from opencv import highgui 
from opencv import cv
import time

MPEG1VIDEO = 0x314D4950
camera = highgui.cvCreateCameraCapture(0)#找摄像头，一般填0-99都可以


class MainWindow(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self)
        self.resize(550, 550)
        self.setWindowTitle('vedio control')
        self.status = 0 #0 is init status;1 is play video; 2 is capture video
        self.image = QImage()
        
        #录制的视频保存位置、格式等参数设定
        self.videowriter =  highgui.cvCreateVideoWriter("test.mpg", highgui.CV_FOURCC('m','p','g','1'), 25, cv.cvSize(200,200), 1)
        #播放的视频位置
        self.playcapture = highgui.cvCreateFileCapture("test.avi")
        
        #初始化按钮
        self.capturebtn = QPushButton('capture')
        self.playbtn = QPushButton('play')
        exitbtn = QPushButton('exit')
        
        # 界面布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.capturebtn)
        vbox.addWidget(self.playbtn)
        vbox.addWidget(exitbtn)
        
        self.piclabel = QLabel('pic')
        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        hbox.addWidget(self.piclabel)
        
        self.setLayout(hbox)
        
        #加载初始页面
        if self.image.load("1.jpg"):  
            self.piclabel.setPixmap(QPixmap.fromImage(self.image))  
        
        #设定定时器
        self.timer = Timer() #录制视频
        self.playtimer = Timer("updatePlay()")#播放视频
        
        #信号--槽
        self.connect(self.timer, SIGNAL("updateTime()"),
                                                    self.CaptureVGA)
        self.connect(self.capturebtn, SIGNAL("clicked()"), 
                                                    self.PauseBegin)  
        self.connect(self.playtimer, SIGNAL("updatePlay()"), 
                                                    self.PlayVideo)  
        self.connect(self.playbtn, SIGNAL("clicked()"),
                                                    self.VideoPlayPause)
        self.connect(exitbtn, SIGNAL("clicked()"), 
                                              app, SLOT("quit()"))


        
    def PlayVideo(self):
        im = highgui.cvQueryFrame(self.playcapture)
        im = opencv.adaptors.Ipl2PIL(im) 
        im = im.convert('RGB').tostring('jpeg', 'RGB')
        self.image.loadFromData(QByteArray(im))
        self.piclabel.setPixmap(QPixmap.fromImage(self.image))  
    
    def VideoPlayPause(self):
        self.status, playstr, capturestr = ((1, 'pause', 'capture'), (0, 'play', 'capture'), (1, 'pause', 'capture'))[self.status]#三种状态分别对应的显示、处理
        self.playbtn.setText(playstr)
        self.capturebtn.setText(capturestr)
        if self.status is 1:#状态1，播放视频
            self.timer.stop()
            self.playtimer.start()
        else:
            self.playtimer.stop()    
    
    def PauseBegin(self):
        self.status, playstr, capturestr = ((2, 'play', 'pause'), (2, 'play', 'pause'), (0, 'play', 'capture'))[self.status]
        self.capturebtn.setText(capturestr)
        self.playbtn.setText(playstr)
        print  self.status, playstr, capturestr
        if self.status is 2:#状态2，录制并显示视频
            self.timer.start()
            self.playtimer.stop()
        else:
            self.timer.stop()
        
        
    def CaptureVGA(self):
        im = highgui.cvQueryFrame(camera)
        highgui.cvWriteFrame(self.videowriter, im)#录制视频，写入文件
        #convert Ipl image to PIL image
        im = opencv.adaptors.Ipl2PIL(im) 
        im = im.convert('RGB').tostring('jpeg', 'RGB')# 转换格式，jpeg
        self.image.loadFromData(QByteArray(im))#格式支持QT，直接加载
        #im.save('3.jpg')#opencv 返回的是Ipl 格式，QT无法直接显示。不知道如何转换格式，采用保存、读取的方式。
        #pic.load('3.jpg')
        self.piclabel.setPixmap(QPixmap.fromImage(self.image))  #一帧一帧的显示
            
    
class Timer(QThread):
    
    def __init__(self, signal = "updateTime()", parent=None):
        super(Timer, self).__init__(parent)
        self.stoped = False
        self.signal = signal
        self.mutex = QMutex()


    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        while True:
            if self.stoped:
                return


            self.emit(SIGNAL(self.signal))
            time.sleep(0.04) #40毫秒发送一次信号，每秒25帧
    
    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True
        
    def isStoped(self):    
        with QMutexLocker(self.mutex):
            return self.stoped
 
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())