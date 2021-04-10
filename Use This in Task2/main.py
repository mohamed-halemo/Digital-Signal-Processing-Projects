    
from GuiT5 import Ui_MainWindow
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
from PyQt5.QtWidgets import QFileDialog,QScrollArea
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
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
        self.signalLIST=[]
        self.spectrogramarray=[]

        self.increment=0
        self.timer=QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.Draw)
        #self.setFixedSize(1300,1040)
        self.tab=self.ui.tabWidget
        self.newtab=self.ui.Newtabbtn
        self.newtab.clicked.connect(self.NewTabCreation)
        self.removetab=self.ui.Removetabbtn
        self.removetab.clicked.connect(self.RemovingTab)

        #ctrl H
        #self.scroll_bar = QScrollBar(self)
        #alt page ,ctrl shift K,enter
        # setting style sheet to the scroll bar
        #shift alt up or down 
        #self.scroll_bar.setStyleSheet("background : lightgreen;")
        self.zoombtn=self.ui.pushButton_6
        self.zoombtn.clicked.connect(self.zooming)
        self.zoomoutbtn=self.ui.pushButton_5
        self.zoomoutbtn.clicked.connect(self.zoomingout)
        self.scrollbtn=self.ui.pushButton_8
        self.scrollbtn.clicked.connect(self.scrollit)
        self.AddToPdf=self.ui.pushButton_7
        self.AddToPdf.clicked.connect(self.PrintPDF)

        self.image = QImage(self.size(), QImage.Format_RGB32)
    
        # setting canvas color to white
        self.image.fill(Qt.white)
        
        self.stop=self.ui.pushButton_2
        self.stop.clicked.connect(self.stopit)
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
        self.IncreaseValue=3
        self.drawbool=1
        self.c=0.025
        self.lastidx=0
    def Browse_Handler2(self):
        self.graph.clear()      
        self.xGraph2=[]
        self.yGraph2=[]
        self.plotvalue=2
                    

        
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
            self.graph.clear()
            self.graph.plot(self.xGraph2,self.yGraph2,pen=(75))
            x_range,y_range=self.graph.viewRange()
            #print(self.xGraph2[:20])                

            self.graph.setXRange(0,x_range[0]+x_range[1]/20)
            print(x_range[0])
            print(x_range[1])
            self.graph2.plot(freq_axis,sig_f)
            self.Draw()   
        def paintEvent(self):
            qp=QPainter(self)
            qp.setPen(QPen(Qcolor(Qt.black),5))
            qp.drawRect(500,500,1000,1000)
            
                                        
        
    def Draw(self):
        # if self.increment>=1000:
        #     self.timer.stop()
        # else:
        #     self.increment+=1
                
        while self.drawbool==1:
            QtCore.QCoreApplication.processEvents()
            self.btn.setText("Plotting..")
            x_range,y_range=self.graph.viewRange()
            x_range2=(x_range[1]-x_range[0])/500  #3shan ymshy 7eta 7eta
            self.graph.setXRange(x_range[0]+x_range2, x_range[1]+x_range2,0)
             
                
                
                
                
            
        
                

    def Pause(self):
        self.drawbool=1

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Resume')
            return 0
        else:
            self.timer.start()
            return 1

    def stopit(self):
        self.drawbool=0
    #    input("Downloading....")

    def zooming(self):

        x_range,y_range=self.graph.viewRange()
        self.graph.setXRange(x_range[0],x_range[0]+x_range[1]/2)
        self.graph.setYRange(y_range[0]/2,y_range[1]/2)
        #self.graph.setRange((x_range[0]/2,x_range[1]/2),(y_range[0]/2,y_range[1]/2))
        
        
  

    def zoomingout(self):
        x_range,y_range=self.graph.viewRange()
        self.graph.setXRange(x_range[0],x_range[0]+x_range[1]*2)
        self.graph.setYRange(y_range[0]*2,y_range[1]*2)
    #    self.graph.setXRange(0,50)
    #    self.graph.setYRange(-1,1)
        

                        
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
       screenshot=screen.grabWindow(self.graph.winId())
       screenshot2=screen.grabWindow(self.graph2.winId())
       screenshot.save('shot.jpg', 'jpg')
       screenshot2.save('shot2.jpg', 'jpg')
       image=('shot.jpg')
       image2=('shot2.jpg')
       image=Image.open('shot.jpg')
       image2=Image.open('shot2.jpg')
       width , height = image.size
       width , height = image2.size
       leftOfImage = 20
       topOfImage = height / 3.5
       rightOfImage = 600
       bottomOfImage = 3.75 * height / 4
       image1=image.crop((leftOfImage,topOfImage,rightOfImage,bottomOfImage))
       image3=image2.crop((leftOfImage,topOfImage,rightOfImage,bottomOfImage))
       NewSize=(250,250)
       image1 = image1 . resize(NewSize)
       image3 = image3 . resize(NewSize)
       w.close()
       self.signalLIST.append(image1)
       self.spectrogramarray.append(image3)


    def PrintPDF(self):
       
       pdf=canvas.Canvas("Report.pdf")
       
       pdf.drawInlineImage(self.signalLIST[0],10, 600)
       pdf.drawInlineImage(self.spectrogramarray[0],300, 600)
       pdf.drawInlineImage(self.signalLIST[1],10, 300)
       pdf.drawInlineImage(self.spectrogramarray[1],300, 300)
       pdf.drawInlineImage(self.signalLIST[2],10, 0)
       pdf.drawInlineImage(self.spectrogramarray[2],300, 0)
       
       pdf.save()   
        
    def scrollit(self):

        QtCore.QCoreApplication.processEvents()
        self.btn.setText("Plotting..")
        x_range,y_range=self.graph.viewRange()
        x_range2=(x_range[1]-x_range[0])/500
        self.graph.setXRange(x_range[0]+x_range2, x_range[1]+x_range2,0)
                
    def NewTabCreation(self):
        self.tab.addTab(QWidget(), "New Tab")
        self.QtWidgets.QWidget(self.tab)

    def RemovingTab(self):
        self.tab.removeTab(1)



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
