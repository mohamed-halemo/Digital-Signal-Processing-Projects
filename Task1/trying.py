from mainWindow import Ui_MainWindow
import ntpath
import os
import sys
from PyQt5 import QtGui, QtWidgets ,QtCore , QtSerialPort
from PyQt5.QtCore import Qt,QTimer
from scipy.fftpack import fft
from tkinter import *
from PyQt5.QtGui import * 
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import sip
import matplotlib.animation as animation
# We require a canvas class
import platform
import time
import numpy as np
import matplotlib.backends.backend_pdf
from reportlab.pdfgen import canvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
#imports
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import time


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
       
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.increment=0
        self.timer=QTimer(self)

        
        self.image = QImage(self.size(), QImage.Format_RGB32)
  
        # setting canvas color to white
        self.image.fill(Qt.white)
       
        self.stop=self.ui.pushButton_5
        self.stop.clicked.connect(self.wa2f)
        self.browse=self.ui.pushButton
        self.browse.clicked.connect(self.Browse_Handler2)
        self.PDF=self.ui.pushButton_3
        self.PDF.clicked.connect(self.click_handler)
        self.btn=self.ui.pushButton_4
        self.btn.clicked.connect(self.Pause)
        self.graph=self.ui.Graph1
        self.graph2=self.ui.Graph1_2
        self.xGraph2=[]
        self.yGraph2=[]
        self.PlotValue=2
        self.counter=0
        self.IncreaseValue=12
        self.drawbool=1
        self.c=0.025
        self.lastidx=0
    def Browse_Handler2(self):
        
        # random data
        filename=QFileDialog.getOpenFileName()
        path=filename[0]
        X, Y = [], []

        with open(path,"r") as f:
            for line in f:
               values = [float(s) for s in line.split()]
               self.xGraph2.append(values[0])
               self.yGraph2.append(values[1])
               X.append(values[0])
               Y.append(values[1])
            ts = X[1]-X[0]
            sig_f= fft(Y)
            sig_f= np.abs(sig_f[0:np.size(sig_f)//2])
    
            fs= 1/ts
            freq_axis= np.linspace(0, np.max(fs), np.size(X)//2,dtype=np.float32)
            self.graph2.plot(freq_axis,sig_f)   
        def paintEvent(self):
            qp=QPainter(self)
            qp.setPen(QPen(Qcolor(Qt.black),5))
            qp.drawRect(500,500,1000,1000)
            
                                       
      
    def Draw(self):
        if self.increment>=1000:
            self.timer.stop()
        else:
            self.increment+=1
                
        while self.drawbool==1 and self.counter <= len(self.xGraph2)  :
            if self.increment>=1000:
               self.timer.stop()
            else:
               self.increment+=1
            self.graph.clear()
            self.graph.plot(self.xGraph2[self.lastidx:self.PlotValue],self.yGraph2[self.lastidx:self.PlotValue],pen=(75))
            QtCore.QCoreApplication.processEvents()
            self.counter=self.counter+1
            self.PlotValue+=self.IncreaseValue
            self.btn.setText("pause")
            
            if(self.xGraph2[self.counter]>=self.c):
                print(self.counter)
                self.lastidx=self.lastidx+65
                self.PlotValue+=self.IncreaseValue
                self.graph.plot(self.xGraph2[self.lastidx:self.PlotValue],self.yGraph2[self.lastidx:self.PlotValue],pen=(75))
                self.c=self.c+0.025
           
        time.sleep(0.01)  
              

    def Pause(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Resume')
            return 0
        else:
            self.timer.timeout.connect(self.Draw)

            
            self.timer.start()
            return 1

    def wa2f(self):
        os.system("pause")
    #    input("Downloading....")

                      
    def save(self):
          
        # selecting file path
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
  
        # if file path is blank return back
        if filePath == "":
            return
          
        # saving canvas at desired path
        self.image.save(filePath)
        
    def click_handler(self):
       w = QtWidgets.QWidget()
       screen = QtWidgets.QApplication.primaryScreen()
       screenshot=screen.grabWindow(QApplication.desktop().winId())
       screenshot.save('shot.jpg', 'jpg')
       image=('shot.jpg')
       screenshot.save('shot2.jpg', 'jpg')

       image2=('shot2.jpg')
       w.close()
       pdf = canvas.Canvas("Report.pdf")
           
       pdf2=canvas.Canvas("Report2.pdf")
           
       pdf2.drawInlineImage(image2,20,-30,255,666)
       
       pdf.drawInlineImage(image, 10 ,-60,550,1120)

       pdf.save()
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
