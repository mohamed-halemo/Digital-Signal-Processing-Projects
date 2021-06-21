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
        # self.value_1=1
        # self.value_2=1
        # self.value_3=1
        # self.value_4=1
        # self.value_5=1
        # self.value_6=1
        # self.value_7=1
        # self.value_8=1
        # self.value_9=1
        # self.value_10=1
        self.l = lists()

        self.value_11=0
        self.value_12=0
        # self.values=[self.value_1,self.value_2,self.value_3,self.value_4,self.value_5,self.value_6,self.value_7,self.value_8,self.value_9,self.value_10]
        self.X=[]
        self.Y=[]
        self.sig_f=[]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.signalLIST=[]
        self.spectrogramarray=[]
        # self.slide1=0
        # self.slide2=0
        # self.slide3=0
        # self.slide4=0
        # self.slide5=0
        # self.slide6=0
        # self.slide7=0
        # self.slide8=0
        # self.slide9=0
        # self.slide10=0
        # self.slideres=[self.slide1,self.slide2,self.slide3,self.slide4,self.slide5,self.slide6,self.slide7,self.slide8,self.slide9,self.slide10]
        #fig = Figure(figsize=(8, 8), dpi=100)
        #self.Spec =fig.add_subplot(212)
        #########added for spectrogram
        self.graph3=self.ui.Graph1_3
        self.fig,self.ax1 = plt.subplots()
        self.plotWidget=FigureCanvas(self.fig)
        ####
        self.newvalue=0

        
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
        self.sliderz=self.ui.sliders
        # self.zoombtn=self.ui.pushButton_6
        # self.zoombtn.clicked.connect(self.zooming)
        # self.zoomoutbtn=self.ui.pushButton_5
        # self.zoomoutbtn.clicked.connect(self.zoomingout)
        self.zoombtn=self.ui.pushButton_6
        self.zoombtn.clicked.connect(lambda:self.zooming(2))
        self.zoomoutbtn=self.ui.pushButton_5
        self.zoomoutbtn.clicked.connect(lambda:self.zooming(1/2))
        # for i in range(10):
        #         self.slideres[i]=self.sliderz[i]
        #         self.sliderz[i].valueChanged.connect(self.updateSlider)
        #         adjust(self.sliderz[i])
        #         print(self.sliderz[i].value())
        boolean=0
        while boolean==0:
            for i in range(10):
                self.sliderz[i].valueChanged.connect(self.updateSlider)
                adjust(self.sliderz[i])
                print(self.sliderz[i].value())
                boolean=1
        # self.slider1=self.ui.verticalSlider_11
        # self.slider1.valueChanged.connect(self.updateSlider)
        # adjust(self.slider1)
        # self.slider2=self.ui.verticalSlider
        # self.slider2.valueChanged.connect(self.updateSlider)
        # adjust(self.slider2)
        # self.slider3=self.ui.verticalSlider_2
        # self.slider3.valueChanged.connect(self.updateSlider)
        # adjust(self.slider3)
        # self.slider4=self.ui.verticalSlider_3
        # self.slider4.valueChanged.connect(self.updateSlider)
        # adjust(self.slider4)
        # self.slider5=self.ui.verticalSlider_4
        # self.slider5.valueChanged.connect(self.updateSlider)
        # adjust(self.slider5)
        # self.slider6=self.ui.verticalSlider_5
        # self.slider6.valueChanged.connect(self.updateSlider)
        # adjust(self.slider6)
        # self.slider7=self.ui.verticalSlider_6
        # self.slider7.valueChanged.connect(self.updateSlider)
        # adjust(self.slider7)
        # self.slider8=self.ui.verticalSlider_7
        # self.slider8.valueChanged.connect(self.updateSlider)
        # adjust(self.slider8)
        # self.slider9=self.ui.verticalSlider_8
        # self.slider9.valueChanged.connect(self.updateSlider)
        # adjust(self.slider9)
        # self.slider10=self.ui.verticalSlider_9
        # self.slider10.valueChanged.connect(self.updateSlider)
        # adjust(self.slider10)
        self.slider11=self.ui.verticalSlider_10
        self.slider11.valueChanged.connect(self.updateSlider)
        adjustSpectroGram(self.slider11)
        self.slider12=self.ui.verticalSlider_12
        self.slider12.valueChanged.connect(self.updateSlider)
        adjustSpectroGram(self.slider12)
        
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
        self.inVerse=[]
        self.Xf=[]
        self.ts=0
        self.freq_axis=[]
        # self.Hrange=[]
        # self.H2range=[]
        # self.H3range=[]
        # self.H4range=[]
        # self.H5range=[]
        # self.H6range=[]
        # self.H7range=[]
        # self.H8range=[]
        # self.H9range=[]
        # self.H10range=[]
        # self.H11range=[]
        # self.H12range=[]
        # self.Ranges=[self.Hrange,self.H2range,self.H3range,self.H4range,self.H5range,self.H6range,self.H7range,self.H8range,self.H9range,self.H10range]
        self.inV=[0]*10

        self.inVs=[]   
        # self.inV2=[]    
        # self.inV3=[]
        # self.inV4=[]
        # self.inV5=[]
        # self.inV6=[]
        # self.inV7=[]
        # self.inV8=[]
        # self.inV9=[]
        # self.inV10=[]
        for i in range (10):
            self.inVs.append(self.inV[i])

        self.value=[1]*10
        self.values=[]
        
        for i in range (10):
            self.values.append(self.value[i])    
        self.sig_f2=[]
        # self.sig_f3=[]
        # self.sig_f4=[]
        # self.sig_f5=[]
        # self.sig_f6=[]
        # self.sig_f7=[]
        # self.sig_f8=[]
        # self.sig_f9=[]
        # self.sig_f10=[]
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
        # for i in range(10):
        #     if self.values[i]>1:
        #         print("wrwwwwwwwwwwwwwwwwwwwwwwwwww")

        #         self.DrawSpecOnly()
        self.value_11=self.slider11.value()
        

        
        self.value_12=self.slider12.value()
        
        

       

        if self.value_12==0 and self.value_11==0:
            self.ax1.set_ylim(0,250)

        self.specEqualizer()
    
        
        
        #return self.value_1,self.value_2,self.value_3,self.value_5,self.value_6,self.value_7,self.value_8,self.value_9,self.value_10
            
            
            
            
           
            
       
                                        
        
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

        





        #print(self.graph2.viewRange())

        #self.sig_f= np.abs(self.sig_f[0:np.size(self.sig_f)//2])
        
        inVerse=np.real(np.fft.ifft(sig_f))#0->5900
        
    
        Xf=np.arange(len(inVerse))
        self.graph2.plot(Xf,inVerse,pen=(75))


    def specEqualizer(self):
        # self.sig_f2=fft(self.Y)
        # self.sig_f2= np.abs(self.sig_f2[0:np.size(self.sig_f2)//2])
        # for i in range(len(self.sig_f2)):
        #     for j in range(10):
            
        #         if 100*0.1*j<self.sig_f2[i]<100*0.1*(j+1) :
        #             self.sig_f2[i]= self.sig_f2[i]*self.values[j]

        #             break
        #         self.Ranges[j]=np.real(np.fft.ifft(self.sig_f2))
        fs= 1/self.ts

        self.sig_f2=fft(self.Y)
        self.sig_f2= np.abs(self.sig_f2[0:np.size(self.sig_f2)])
        for i in range(len(self.sig_f2)):
            for j in range(10):

                if  self.sig_f2[i]<=fs*0.1*(j+1)*0.5:
                    self.sig_f2[i]=self.sig_f2[i]*self.values[j]
        self.inV=   np.real(np.fft.ifft(self.sig_f2))     
        # xm_range=np.size(self.sig_f)//2
        # steps=[0,xm_range//5,3*xm_range//10,4*xm_range//10,xm_range//2,3*xm_range//5,7*xm_range//10,4*xm_range//5,9*xm_range//10,xm_range]

        # step= xm_range//10
        # step2= xm_range//5
        # step3= 3*xm_range//10
        # step4= 4*xm_range//10
        # step5= xm_range//2
        # step6= 3*xm_range//5
        # step7= 7*xm_range//10
        # step8= 4*xm_range//5
        # step9= 9*xm_range//10
        # step10= 10*xm_range//10
        # sig_f= fft(self.Y)
        # sig_f2=fft(self.Y)
        # sig_f3=fft(self.Y)
        # sig_f4=fft(self.Y)
        # sig_f5=fft(self.Y)
        # sig_f6=fft(self.Y)
        # sig_f7=fft(self.Y)
        # sig_f8=fft(self.Y)
        # sig_f9=fft(self.Y)
        # sig_f10=fft(self.Y)
        # self.sig_f= self.sig_f[0:xm_range]
        # self.sig_f2= self.sig_f[0:xm_range]
        # self.sig_f3= self.sig_f[0:xm_range]
        # self.sig_f4= self.sig_f[0:xm_range]
        # self.sig_f5= self.sig_f[0:xm_range]
        # self.sig_f6= self.sig_f[0:xm_range]
        # self.sig_f7= self.sig_f[0:xm_range]
        # self.sig_f8= self.sig_f[0:xm_range]
        # self.sig_f9= self.sig_f[0:xm_range]
        # self.sig_f10= self.sig_f[0:xm_range]
        # self.sig_f[0:step]*=self.values[0]
        # self.sig_f2[step:step2]*=self.values[1]
        # self.sig_f3[step2:step3]*=self.values[2]
        # self.sig_f4[step3:step4]*=self.values[3]
        # self.sig_f5[step4:step5]*=self.values[4]
        # self.sig_f6[step5:step6]*=self.values[5]
        # self.sig_f7[step6:step7]*=self.values[6]
        # self.sig_f8[step7:step8]*=self.values[7]
        # self.sig_f9[step8:step9]*=self.values[8]
        # self.sig_f9[step9:step10]*=self.values[9]
        # inV1=np.real(np.fft.ifft(sig_f))#
        # inV2=np.real(np.fft.ifft(sig_f2))
        # inV3=np.real(np.fft.ifft(sig_f3))#
        # inV4=np.real(np.fft.ifft(sig_f4))#
        # inV5=np.real(np.fft.ifft(sig_f5))#
        # inV6=np.real(np.fft.ifft(sig_f6))#
        # inV7=np.real(np.fft.ifft(sig_f7))#
        # inV8=np.real(np.fft.ifft(sig_f8))#
        # inV9=np.real(np.fft.ifft(sig_f9))#
        # inV10=np.real(np.fft.ifft(sig_f10))#
        # for i in range(len(inV1)):
                
        #     self.Hrange.append(inV1[i])
        # for i in range(len(inV2)):
                
        #     self.H2range.append(inV2[i])
        # for i in range(len(inV3)):
                
        #     self.H3range.append(inV3[i])
        # for i in range(len(inV4)):
                
        #     self.H4range.append(inV4[i])
        # for i in range(len(inV5)):
                
        #     self.H5range.append(inV5[i])
        # for i in range(len(inV6)):
                
        #     self.H6range.append(inV6[i])
        # for i in range(len(inV7)):
                
        #     self.H7range.append(inV7[i])

        # for i in range(len(inV8)):
                
        #     self.H8range.append(inV8[i])
        # for i in range(len(inV9)):
                
        #     self.H9range.append(inV9[i])
        # for i in range(len(inV10)):
                
        #     self.H10range.append(inV10[i])










    def DrawSpecOnly(self):

        self.fig.canvas.draw()
        

        self.fig.canvas.flush_events()
        

        self.specEqualizer()
    

        self.ax1.specgram(self.inV,NFFT=1024,Fs=500,noverlap=10,cmap='jet_r')

        # for i in range(10):
        #     if self.values[i]>1:
        #         self.ax1.specgram(self.inV,NFFT=1024,Fs=500,noverlap=10,cmap='jet_r')
        #         print("in")



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
        
     

    # def zoomingout(self):

    #     x_range,y_range=self.graph.viewRange()
    #     self.graph.setXRange(x_range[0],x_range[0]+x_range[1]/2)
    #     self.graph.setYRange(y_range[0]/2,y_range[1]/2)
    #     xx_range,yy_range=self.graph2.viewRange()
    #     self.graph2.setXRange(xx_range[0],xx_range[0]+xx_range[1]/2)
    #     self.graph2.setYRange(yy_range[0]/2,yy_range[1]/2)
        

        #self.graph.setRange((x_range[0]/2,x_range[1]/2),(y_range[0]/2,y_range[1]/2))
        
        
  

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
          
        
    def scrollit(self):

        QtCore.QCoreApplication.processEvents()
        self.btn.setText("Plotting..")
        x_range,y_range=self.graph.viewRange()
        x_range2=(x_range[1]-x_range[0])/500
        self.graph.setXRange(x_range[0]+x_range2, x_range[1]+x_range2,0)
        xx_range,yy_range=self.graph2.viewRange()
        
        xx_range2=(xx_range[1]-xx_range[0])/500
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
