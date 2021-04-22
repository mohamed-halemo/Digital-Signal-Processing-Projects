from GuiT5 import Ui_MainWindow
import ntpath
import os
import sys
from GuiT4 import * #functions el repeated 
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
        self.xx_range=[]
        self.value_1=1
        self.value_2=1
        self.value_3=1
        self.value_4=1
        self.value_5=1
        self.value_6=1
        self.value_7=1
        self.value_8=1
        self.value_9=1
        self.value_10=1
        self.X=[]
        self.Y=[]
        self.sig_f=[]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.signalLIST=[]
        self.spectrogramarray=[]
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
        self.zoombtn=self.ui.pushButton_6
        self.zoombtn.clicked.connect(self.zooming)
        self.zoomoutbtn=self.ui.pushButton_5
        self.zoomoutbtn.clicked.connect(self.zoomingout)
        self.slider1=self.ui.verticalSlider_11
        self.slider1.valueChanged.connect(self.updateSlider)
        adjust(self.slider1)
        self.slider2=self.ui.verticalSlider
        self.slider2.valueChanged.connect(self.updateSlider)
        adjust(self.slider2)
        self.slider3=self.ui.verticalSlider_2
        self.slider3.valueChanged.connect(self.updateSlider)
        adjust(self.slider3)
        self.slider4=self.ui.verticalSlider_3
        self.slider4.valueChanged.connect(self.updateSlider)
        adjust(self.slider4)
        self.slider5=self.ui.verticalSlider_4
        self.slider5.valueChanged.connect(self.updateSlider)
        adjust(self.slider5)
        self.slider6=self.ui.verticalSlider_5
        self.slider6.valueChanged.connect(self.updateSlider)
        adjust(self.slider6)
        self.slider7=self.ui.verticalSlider_6
        self.slider7.valueChanged.connect(self.updateSlider)
        adjust(self.slider7)
        self.slider8=self.ui.verticalSlider_7
        self.slider8.valueChanged.connect(self.updateSlider)
        adjust(self.slider8)
        self.slider9=self.ui.verticalSlider_8
        self.slider9.valueChanged.connect(self.updateSlider)
        adjust(self.slider9)
        self.slider10=self.ui.verticalSlider_9
        self.slider10.valueChanged.connect(self.updateSlider)
        adjust(self.slider10)
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
        self.Hrange=[]
        self.H2range=[]
        self.H3range=[]
        self.H4range=[]
        self.H5range=[]
        self.H6range=[]
        self.H7range=[]
        self.H8range=[]
        self.H9range=[]
        self.H10range=[]
        self.H11range=[]
        self.H12range=[]

        self.inV=[]
        self.inV2=[]
        self.inV3=[]
        self.inV4=[]
        self.inV5=[]
        self.inV6=[]
        self.inV7=[]
        self.inV8=[]
        self.inV9=[]
        self.inV10=[]
        self.sig_f2=[]
        self.sig_f3=[]
        self.sig_f4=[]
        self.sig_f5=[]
        self.sig_f6=[]
        self.sig_f7=[]
        self.sig_f8=[]
        self.sig_f9=[]
        self.sig_f10=[]
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
            

            self.Draw()


         

        def paintEvent(self):
            qp=QPainter(self)
            qp.setPen(QPen(Qcolor(Qt.black),5))
            qp.drawRect(500,500,1000,1000)

        

        
        

    def updateSlider(self):
        
        self.value_1=self.slider1.value()
       
    
        self.value_2=self.slider2.value()
       
        self.value_3=self.slider3.value()
      


        self.value_4=self.slider4.value()
       
        self.value_5=self.slider5.value()
       
        self.value_6=self.slider6.value()
        
        self.value_7=self.slider7.value()
        
        self.value_8=self.slider8.value()
       
        self.value_9=self.slider9.value()
        
        self.value_10=self.slider10.value()
       
        self.value_11=self.slider11.value()
        

        
        self.value_12=self.slider12.value()
       
        self.Equalizer()

        if self.value_1>1 or self.value_2>1 or self.value_3>1 or self.value_4>1 or self.value_5>1 or self.value_6>1 or self.value_7>1 or self.value_8>1 or self.value_9>1 or self.value_10>1 or  self.value_12>=0 or self.value_11>=0 :

            self.DrawSpecOnly()


        if self.value_12==0 and self.value_11==0:
            self.ax1.set_ylim(0,250)

        self.specEqualizer()
    
        
        
        #return self.value_1,self.value_2,self.value_3,self.value_5,self.value_6,self.value_7,self.value_8,self.value_9,self.value_10
            
            
            
            
           
            
       
                                        
        
    def Draw(self):
        
        
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

            

                
    def Equalizer(self): #yeghyaaar awel 10% fe el graph
        
        self.graph2.clear()
        for i in range(len(self.xx_range)):
            
            
            if self.xx_range[i] < 5900 : #4500
                sig_f= fft(self.Y)*self.value_1
                
            elif 5901<self.xx_range[i]<11800 : #10500
                sig_f= fft(self.Y)*self.value_2
               
            elif 11801<self.xx_range[i]<17700 :
                sig_f=fft(self.Y)*self.value_3
              
            elif 17701<self.xx_range[i]<23600 :
                sig_f=fft(self.Y)*self.value_4
             
            elif 23601<self.xx_range[i]<29500 :
                sig_f=fft(self.Y)*self.value_5
               
            elif 29501<self.xx_range[i]<35400 :
                sig_f=fft(self.Y)*self.value_6
             

            elif 35401<self.xx_range[i]<41300 :
                sig_f=fft(self.Y)*self.value_7
               
            elif 41300<self.xx_range[i]<47200 :
                sig_f=fft(self.Y)*self.value_8
                
            elif 47201<self.xx_range[i]<53100 :
                sig_f=fft(self.Y)*self.value_9
               
            else:
                sig_f=fft(self.Y)*self.value_10
                

        





        #print(self.graph2.viewRange())

        #self.sig_f= np.abs(self.sig_f[0:np.size(self.sig_f)//2])
        
        inVerse=np.real(np.fft.ifft(sig_f))#0->5900
        
    
        Xf=np.arange(len(inVerse))
        self.graph2.plot(Xf,inVerse,pen=(75))

    def specEqualizer(self):

        xm_range=np.size(self.sig_f)//2
        step= xm_range//10
        step2= xm_range//5
        step3= 3*xm_range//10
        step4= 4*xm_range//10
        step5= xm_range//2
        step6= 3*xm_range//5
        step7= 7*xm_range//10
        step8= 4*xm_range//5
        step9= 9*xm_range//10
        step10= 10*xm_range//10
        sig_f= fft(self.Y)
        sig_f2=fft(self.Y)
        sig_f3=fft(self.Y)
        sig_f4=fft(self.Y)
        sig_f5=fft(self.Y)
        sig_f6=fft(self.Y)
        sig_f7=fft(self.Y)
        sig_f8=fft(self.Y)
        sig_f9=fft(self.Y)
        sig_f10=fft(self.Y)
        self.sig_f= self.sig_f[0:xm_range]
        self.sig_f2= self.sig_f[0:xm_range]
        self.sig_f3= self.sig_f[0:xm_range]
        self.sig_f4= self.sig_f[0:xm_range]
        self.sig_f5= self.sig_f[0:xm_range]
        self.sig_f6= self.sig_f[0:xm_range]
        self.sig_f7= self.sig_f[0:xm_range]
        self.sig_f8= self.sig_f[0:xm_range]
        self.sig_f9= self.sig_f[0:xm_range]
        self.sig_f10= self.sig_f[0:xm_range]
        self.sig_f[0:step]*=self.value_1
        self.sig_f2[step:step2]*=self.value_2
        self.sig_f3[step2:step3]*=self.value_3
        self.sig_f4[step3:step4]*=self.value_4
        self.sig_f5[step4:step5]*=self.value_5
        self.sig_f6[step5:step6]*=self.value_6
        self.sig_f7[step6:step7]*=self.value_7
        self.sig_f8[step7:step8]*=self.value_8
        self.sig_f9[step8:step9]*=self.value_9
        self.sig_f9[step9:step10]*=self.value_9
        inV1=np.real(np.fft.ifft(sig_f))#
        inV2=np.real(np.fft.ifft(sig_f2))
        inV3=np.real(np.fft.ifft(sig_f3))#
        inV4=np.real(np.fft.ifft(sig_f4))#
        inV5=np.real(np.fft.ifft(sig_f5))#
        inV6=np.real(np.fft.ifft(sig_f6))#
        inV7=np.real(np.fft.ifft(sig_f7))#
        inV8=np.real(np.fft.ifft(sig_f8))#
        inV9=np.real(np.fft.ifft(sig_f9))#
        inV10=np.real(np.fft.ifft(sig_f10))#
        for i in range(len(inV1)):
                
            self.Hrange.append(inV1[i])
        for i in range(len(inV2)):
                
            self.H2range.append(inV2[i])
        for i in range(len(inV3)):
                
            self.H3range.append(inV3[i])
        for i in range(len(inV4)):
                
            self.H4range.append(inV4[i])
        for i in range(len(inV5)):
                
            self.H5range.append(inV5[i])
        for i in range(len(inV6)):
                
            self.H6range.append(inV6[i])
        for i in range(len(inV7)):
                
            self.H7range.append(inV7[i])

        for i in range(len(inV8)):
                
            self.H8range.append(inV8[i])
        for i in range(len(inV9)):
                
            self.H9range.append(inV9[i])
        for i in range(len(inV10)):
                
            self.H10range.append(inV10[i])










    def DrawSpecOnly(self):

        self.fig.canvas.draw()
        

        self.fig.canvas.flush_events()
        if self.value_1==0 and not self.value_2==0:
            self.ax1.clear()
        if self.value_1>1 :


            self.ax1.specgram(self.Hrange,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_2>1:
            self.ax1.specgram(self.H2range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_3>1:
            self.ax1.specgram(self.H3range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_4>1:
            self.ax1.specgram(self.H4range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_5>1:
            self.ax1.specgram(self.H5range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_6>1:
            self.ax1.specgram(self.H6range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_7>1:
            self.ax1.specgram(self.H7range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_8>1:
            self.ax1.specgram(self.H8range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_9>1:
            self.ax1.specgram(self.H9range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        if self.value_10>1:
            self.ax1.specgram(self.H10range,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')




        if self.value_11>=0:

            self.ax1.specgram(self.yGraph2,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')
        
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
            self.ax1.specgram(self.yGraph2,NFFT=1024,Fs=500,noverlap=900,cmap='jet_r')

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
            
         
            

        if self.value_1==0 and self.value_2==0 and self.value_3==0 and self.value_4==0 and self.value_5==0 and self.value_6==0 and self.value_7==0 and self.value_8==0 and self.value_9==0 and self.value_10==0  :
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
        
        #self.bgraab7aga()
        
    #    input("Downloading....")

    def zoomingout(self):

        x_range,y_range=self.graph.viewRange()
        self.graph.setXRange(x_range[0],x_range[0]+x_range[1]/2)
        self.graph.setYRange(y_range[0]/2,y_range[1]/2)
        xx_range,yy_range=self.graph2.viewRange()
        self.graph2.setXRange(xx_range[0],xx_range[0]+xx_range[1]/2)
        self.graph2.setYRange(yy_range[0]/2,yy_range[1]/2)
        

        #self.graph.setRange((x_range[0]/2,x_range[1]/2),(y_range[0]/2,y_range[1]/2))
        
        
  

    def zooming(self):
        x_range,y_range=self.graph.viewRange()
        self.graph.setXRange(x_range[0],x_range[0]+x_range[1]*2)
        self.graph.setYRange(y_range[0]*2,y_range[1]*2)
        xx_range,yy_range=self.graph2.viewRange()
        self.graph2.setXRange(xx_range[0],xx_range[0]+xx_range[1]*2)
        self.graph2.setYRange(yy_range[0]*2,yy_range[1]*2)
        
        

                        
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
       screenshot2=screen.grabWindow(self.graph3.winId())
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
