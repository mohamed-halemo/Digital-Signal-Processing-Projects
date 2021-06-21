from GuiT5 import Ui_MainWindow
import ntpath
import os
import sys
from app import lists
from GuiT4 import *  
from PyQt5 import QtGui, QtWidgets ,QtCore , QtSerialPort
from PyQt5.QtCore import Qt,QTimer
from scipy.fftpack import fft
from tkinter import *
from PyQt5.QtGui import * 
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
from scipy.fft import fft, fftfreq,irfft

class ApplicationWindow(QtWidgets.QMainWindow):
            

    def __init__(self,parent=None):
        super(ApplicationWindow, self).__init__()
        self.RangeVal=59000
        self.xx_range=[]
    
        self.l = lists()

        self.value_11=0
        self.value_12=0
        self.X=[]
        self.Y=[]
        self.sig_f=[]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.signalLIST=[]
        self.spectrogramarray=[]
        self.graph3=self.ui.Graph1_3
        self.fig,self.ax1 = plt.subplots()
        self.plotWidget=FigureCanvas(self.fig)
        ####
        self.newvalue=0

        
        self.increment=0
        self.timer=QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.Draw)
        self.tab=self.ui.tabWidget
        self.newtab=self.ui.Newtabbtn
        self.newtab.clicked.connect(self.NewTabCreation)
        self.removetab=self.ui.Removetabbtn
        self.removetab.clicked.connect(self.RemovingTab)

      
        self.sliderz=self.ui.sliders
        self.scrollbackbtn=self.ui.CompareButton
        self.scrollbackbtn.clicked.connect(lambda:self.scrollback(1,-1))
        self.zoombtn=self.ui.pushButton_6
        self.zoombtn.clicked.connect(lambda:self.zooming(2))
        self.zoomoutbtn=self.ui.pushButton_5
        self.zoomoutbtn.clicked.connect(lambda:self.zooming(1/2))
      
        boolean=0
        while boolean==0:
            for i in range(10):
                self.sliderz[i].valueChanged.connect(self.updateSlider)
                adjust(self.sliderz[i])
                print(self.sliderz[i].value())
                boolean=1
      
        self.slider11=self.ui.verticalSlider_10
        self.slider11.valueChanged.connect(self.updateSlider)
        adjustSpectroGram(self.slider11)
        self.slider12=self.ui.verticalSlider_12
        self.slider12.valueChanged.connect(self.updateSlider)
        adjustSpectroGram(self.slider12)
        
        self.scrollbtn=self.ui.pushButton_8
        self.scrollbtn.clicked.connect(lambda:self.scrollback(-1,1))
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
        self.inVerse=[]
        self.Xf=[]
        self.ts=0
        self.freq_axis=[]
        self.inV=[0]*10

        self.inVs=[]   
      
        for i in range (10):
            self.inVs.append(self.inV[i])

        self.value=[1]*10
        self.values=[]
        
        for i in range (10):
            self.values.append(self.value[i])    
        self.sig_f2=[]
        self.increase=25
    def Browse_Handler2(self):
        self.graph.clear()      
        self.xGraph2=[]
        self.yGraph2=[]
        self.plotvalue=2
        self.graph2.clear()
        
        
        filename=QFileDialog.getOpenFileName()
        path=filename[0]

        with open(path,"r") as f:
            for line in f:
                values = [float(s) for s in line.split()]
                self.xGraph2.append(values[0])
                self.yGraph2.append(values[1])
                self.X.append(values[0])
                self.Y.append(values[1])
            self.ts = self.X[1]-self.X[0]
            
            self.sig_f= fft(self.Y)
            self.inVerse=np.real(np.fft.ifft(self.sig_f))
            self.Xf=np.arange(len(self.inVerse))
            self.graph2.plot(self.Xf,self.inVerse,pen=(75))
        
            
         
            fs= 1/self.ts
            self.freq_axis= np.linspace(0, np.max(fs), np.size(X)//2,dtype=np.float32)
            self.graph.clear()
            
            self.graph.plot(self.xGraph2,self.yGraph2,pen=(75))
            x_range,y_range=self.graph.viewRange()

            self.graph.setXRange(0,x_range[0]+x_range[1]/20)
          
            self.xx_range,yy_range=self.graph2.viewRange()
            self.graph2.setXRange(0,self.xx_range[0]+self.xx_range[1]/20)
            self.graph2.setYRange(-100,300)
            
            self.lay = QtWidgets.QVBoxLayout(self.graph3)  
            self.lay.setContentsMargins(0, 0, 0, 0)      
            self.lay.addWidget(self.plotWidget)
            print(self.xx_range)

            self.Draw()


        def paintEvent(self):
            qp=QPainter(self)
            qp.setPen(QPen(Qcolor(Qt.black),5))
            qp.drawRect(500,500,1000,1000)
     
        

    def updateSlider(self):
        if self.value_11>0 or self.value_12>0:
            self.MinMax()
        for i in range(10):

            self.values[i]=self.sliderz[i].value()
            if self.values[i]>1:
                print("wrwwwwwwwwwwwwwwwwwwwwwwwwww")

                self.DrawSpecOnly()
         
        self.Equalizer()
       
        self.value_11=self.slider11.value()
        

        
        self.value_12=self.slider12.value()
        
        
        if self.value_12==0 and self.value_11==0:
            self.ax1.set_ylim(0,250)

        self.specEqualizer()
    
        
        
                
                                          
    def Draw(self):
        
        # RangesVal=xx_Range
        while self.drawbool==1:
            QtCore.QCoreApplication.processEvents()
            self.btn.setText("Plotting..")
            x_range,y_range=self.graph.viewRange()
            x_range2=(x_range[1]-x_range[0])/500  #3shan ymshy 7eta 7eta
            self.graph.setXRange(x_range[0]+x_range2, x_range[1]+x_range2,0)
            #self.Equalizer()
            
            self.xx_range,yy_range=self.graph2.viewRange()
            xx_range2=(self.xx_range[1]-self.xx_range[0])/500
            self.graph2.setXRange(self.xx_range[0]+xx_range2,self.xx_range[1]+xx_range2,0)

            

                
    def Equalizer(self): 
        
        self.graph2.clear()
        for i in range(len(self.xx_range)):
            for j in range(10):
            
                if self.RangeVal*0.1*j<self.xx_range[i]<self.RangeVal*0.1*(j+1) :
                     #10500
                    sig_f= fft(self.Y)*self.values[j]
                    break

        
        
        inVerse=np.real(np.fft.ifft(sig_f))#0->5900
        
    
        Xf=np.arange(len(inVerse))
        self.graph2.plot(Xf,inVerse,pen=(75))


    def specEqualizer(self):
       
        fs= 1/self.ts

        self.sig_f2=fft(self.Y)
        self.sig_f2= np.abs(self.sig_f2[0:np.size(self.sig_f2)])
        for i in range(len(self.sig_f2)):
            for j in range(10):

                if  self.sig_f2[i]<=fs*0.1*(j+1)*0.5:
                    self.sig_f2[i]=self.sig_f2[i]*self.values[j]
        self.inV=   np.real(np.fft.ifft(self.sig_f2))     
       





    def DrawSpecOnly(self):

        self.fig.canvas.draw()
        

        self.fig.canvas.flush_events()
        

        self.specEqualizer()
    

        self.ax1.specgram(self.inV,NFFT=1024,Fs=500,noverlap=10,cmap='jet_r')

      


    def MinMax(self):
        self.fig.canvas.draw()
        

        self.fig.canvas.flush_events()
        if self.value_11>=0:

            self.ax1.specgram(self.inVerse,NFFT=1024,Fs=500,noverlap=10,cmap='jet_r')
        
            if self.value_12 and self.value_11==0:
                self.ax1.set_ylim(0,250)
            elif self.value_12==1:
                self.ax1.set_ylim(25,250-self.value_11*25)
            elif self.value_12==2:
                self.ax1.set_ylim(50,250-self.value_11*25)
            elif self.value_12==3:
                self.ax1.set_ylim(75,250-self.value_11*25)
            elif self.value_12==4:
                self.ax1.set_ylim(100,250-self.value_11*25)
            elif self.value_12==5:
                self.ax1.set_ylim(125,250-self.value_11*25)
        
        if self.value_12>=0:
            self.ax1.specgram(self.yGraph2,NFFT=1024,Fs=500,noverlap=10,cmap='jet_r')

        # self.ax.set_ylim([0,200])
       
            if self.value_11==1:
                self.ax1.set_ylim(0+self.value_12*25,225)
            elif self.value_11==2:
                self.ax1.set_ylim(0+self.value_12*25,200)
            elif self.value_11==3:
                self.ax1.set_ylim(0+self.value_12*25,175)
            elif self.value_11==4:
                self.ax1.set_ylim(0+self.value_12*25,150)
            elif self.value_11==5:
                self.ax1.set_ylim(0+self.value_12*25,125)

        self.show()    
            
         
            
        if not any(self.values):
            self.ax1.clear()


                 

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
              
  

    def zooming(self, zoomfactorr ):
        x_range,y_range=self.graph.viewRange()
        self.graph.setXRange(x_range[0],x_range[0]+x_range[1]*zoomfactorr)
        self.graph.setYRange(y_range[0]*zoomfactorr,y_range[1]*zoomfactorr)
        xx_range,yy_range=self.graph2.viewRange()
        self.graph2.setXRange(xx_range[0],xx_range[0]+xx_range[1]*zoomfactorr)
        self.graph2.setYRange(yy_range[0]*zoomfactorr,yy_range[1]*zoomfactorr)
        
        

                        
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
       
        ConvertToPdf(self.graph.winId(),self.graph3.winId(),self.signalLIST,self.spectrogramarray)
       

    def PrintPDF(self):
       
       
       PDF(self.signalLIST,self.spectrogramarray)
          
        
    # 
    def scrollback(self, A , B):

        QtCore.QCoreApplication.processEvents()
        x_range,y_range=self.graph.viewRange()
        x_range2=(A*x_range[0]+B*x_range[1])/5
        if A==1 and B==-1 and x_range[0]>=0.2:

            self.graph.setXRange(x_range[0]+x_range2, x_range[1]+x_range2,0)
        elif A==-1 and B==1 :
            self.graph.setXRange(x_range[0]+x_range2, x_range[1]+x_range2,0)

        xx_range,yy_range=self.graph2.viewRange()
        xx_range2=(A*xx_range[0]+B*xx_range[1])/5
        if A==1 and B==-1 and x_range[0]>=0.2:
            self.graph2.setXRange(xx_range[0]+xx_range2, xx_range[1]+xx_range2,0)
        elif A==-1 and B==1 :    
            self.graph2.setXRange(xx_range[0]+xx_range2, xx_range[1]+xx_range2,0)

                
    def NewTabCreation(self):
        text = 'Tab %d' % (self.tab.count() + 1)
        self.tab.addTab(ApplicationWindow(self.tab), text)
   
    def RemovingTab(self):
        self.tab.removeTab(1)

    

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()
