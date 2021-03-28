from mainWindow import Ui_MainWindow
import ntpath
import os
import sys
from PyQt5 import QtGui, QtWidgets ,QtCore , QtSerialPort
from PyQt5.QtCore import Qt
from scipy.fftpack import fft
from tkinter import *
from PyQt5.QtGui import * 

from reportlab.pdfgen import canvas 
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

#imports


class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()
       
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.image = QImage(self.size(), QImage.Format_RGB32)
  
        # setting canvas color to white
        self.image.fill(Qt.white)
        
        
      
        
        self.browse=self.ui.pushButton
        self.browse.clicked.connect(self.Browse_Handler2)
        self.PDF=self.ui.pushButton_3
        self.PDF.clicked.connect(self.save)
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
               


                                       
        while self.drawbool==1 and self.counter <= len(self.xGraph2):
            self.graph.clear()
            self.graph.plot(self.xGraph2[self.lastidx:self.PlotValue],self.yGraph2[self.lastidx:self.PlotValue],pen=(75))
            QtCore.QCoreApplication.processEvents()
            self.counter=self.counter+1
            self.PlotValue+=self.IncreaseValue
            ts = X[1]-X[0]
            sig_f= fft(Y)
            sig_f= np.abs(sig_f[0:np.size(sig_f)//2])
    
            fs= 1/ts
            freq_axis= np.linspace(0, np.max(fs), np.size(X)//2,dtype=np.float32)
            self.graph2.plot(freq_axis,sig_f)
            if(self.xGraph2[self.counter]>=self.c):
                print(self.counter)
                self.lastidx=self.lastidx+650
                self.PlotValue+=self.IncreaseValue
                self.graph.plot(self.xGraph2[self.lastidx:self.PlotValue],self.yGraph2[self.lastidx:self.PlotValue],pen=(75))
                self.c=self.c+0.025


            time.sleep(0.01)    

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image,
                                      self.image.rect())

        
       

    def save(self):
       w = QtWidgets.QWidget()
       screen = QtWidgets.QApplication.primaryScreen()
       screenshot=screen.grabWindow(QApplication.desktop().winId())
       screenshot.save('shot.jpg', 'jpg')
       image='shot.jpg'
       w.close()
       pdf = canvas.Canvas("Report.pdf")
       pdf.drawInlineImage(image, 10 ,-60,550,1120)
       
       pdf.save()
        
        
   

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
