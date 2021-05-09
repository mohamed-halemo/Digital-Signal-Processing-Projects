from PyQt5 import QtWidgets, QtGui
from MainWindow import Ui_MainWindow
from modesEnum import Modes
import sys , os
from PyQt5 import QtCore, QtGui, QtWidgets
_translate = QtCore.QCoreApplication.translate
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog, QMessageBox
import matplotlib.pyplot 
from matplotlib.animation import FuncAnimation
import pyqtgraph as pg
import time
from PIL import Image
from PyQt5 import QtCore
import numpy as np
import matplotlib as plt
from PyQt5.QtGui import QPixmap
from tkinter import ttk
import tkinter.filedialog
from tkinter.filedialog import askopenfilename # Open dialog box
import cv2
import logging
from scipy.fftpack import fft2,ifft2

import enum
from pyqtgraph import  ImageItem
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from modesEnum import Modes
from PyQt5 import QtWidgets, QtGui
from scipy.fftpack import fft2,ifft2
from PIL import Image #IMAGES library
from tkinter import ttk
from tkinter import Tk
import numpy as np
from modesEnum import Modes 
from tkinter import messagebox
import pyqtgraph as pg
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog, QMessageBox
import logging






logging.basicConfig(filename='log.txt', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')





class ImageModel():

    def __init__(self,MessaAge,IMAGEPLOT,EDIT,BOX):
    
        ###
        # important intializations and will get  their values when given image
        ###
        self.ui =Ui_MainWindow()
        self.MessaAge=MessaAge
        self.imgByte = None
        self.dft = None
        self.real = None
        self.imaginary = None
        self.magnitude = None
        self.phase = None
        self.IMAGEPLOTTER=IMAGEPLOT
        self.EDIT=EDIT
        self.BOX=BOX
        
        self.BOX.currentTextChanged.connect(self.ComboBox)


    def IMPORT(self,n):
        self.IMAGEPLOTTER.clear() #clearing when importing
        self.EDIT.clear()    #clearing when importing
        fname, _ =QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '/PC', "Image Files (*.jpg *.png *.jpeg)")
        img = Image.open(fname).convert("RGB") #using image from PLI library to display the image and make it in RGB format

        if ((n!= 0 ) & (img.size != n)): #so if n=0 no images and if img.size!=1 or 0 then we won't be able to add more
            print('Not Same Size')
            main=Tk() #use external GUI to pop a message
            main.withdraw()#to hide window of the TK GUI that appears
            messagebox.showinfo("Error", "IMAGE 1 is not shown or IMAGE 2 Has Different Size than IMAGE 1")#pop message
            main.destroy()#closing that GUI as we donot need it
            return

        self.imgByte = img.size #setting image size
        self.dft=fft2(np.asarray(img))#2D fourier transform for the image
        self.real=self.dft.real ##getting real values
        self.imaginary=self.dft.imag  ##getting imaginary
        self.magnitude=np.abs(self.dft) ##magnitude
        self.phase=np.angle(self.dft)  ## phase
        self.Draw(np.asarray(img),self.IMAGEPLOTTER,1) #sending image to function Draw,asarray converts image to array
        logging.info('CREATED {} WITH SIZE: {} '.format(self.MessaAge, self.imgByte))#message is the number of image 
        logging.info('{} DATA HAS BEEN SET '.format(self.MessaAge))
        logging.info('{} HAS BEEN IMPORTED '.format(self.MessaAge))
        logging.info('ORIGINAL {} HAS BEEN DRAWN '.format(self.MessaAge))



    
   
  

    def ComboBox(self): #choosing what to Draw from combo box
        if self.BOX.currentIndex()==0:
            self.EDIT.clear()
        elif self.BOX.currentIndex()==1:
            self.Draw(self.magnitude,self.EDIT,2)
            logging.info('MAGNITUDE {} HAS BEEN DRAWN '.format(self.MessaAge))
        elif self.BOX.currentIndex()==2:
            self.Draw(self.phase,self.EDIT,2)
            logging.info('PHASE {} HAS BEEN DRAWN '.format(self.MessaAge))
        elif self.BOX.currentIndex()==3:
            self.Draw(self.real,self.EDIT,2)
            logging.info('REAL {} HAS BEEN DRAWN '.format(self.MessaAge))
        elif self.BOX.currentIndex()==4:
            self.Draw(self.imaginary,self.EDIT,2)
            logging.info('IMAGINARY {} HAS BEEN DRAWN '.format(self.MessaAge))


    def Draw(self,TODRAW,selfarea,n):
        if n==1:
            selfarea.addItem(pg.ImageItem(np.rot90(TODRAW ,3)))#rotate the image 3 times until it gets right
        elif n==2:
            selfarea.addItem(pg.ImageItem(np.rot90(TODRAW ,3))) #the second widget after each image >>


        
#setting image 1,2 and output widget,choosing mode,setting both comboboxes for output and images choosing and setting Sliders
    def mix(self, Image2, OUTPUT,MODE,ComboOUT1,ComboOUT2,ComboImageo1,ComboImageo2,Slider1,Slider2):

 ############################################ NEEDED  ATTRIBUTES ASSIGN ###############################################
        self.MODE=MODE#magn&phase , real&imag
        self.ComboOUT1=ComboOUT1 #ComboBox out 1
        self.ComboOUT2=ComboOUT2 #ComboBox out 2
        self.ComboImageo1=ComboImageo1 #ComboBox of choosing which image first
        self.ComboImageo2=ComboImageo2 #ComboBox of choosing which image
        self.Image1=self    #image 1
        self.Image2=Image2  #image 2 
        self.OUTPUT=OUTPUT  #out put plot widget
        self.Slider1=Slider1
        self.Slider2=Slider2

        logging.info('Mix Function Has Started '.format())



########################################## COMPONENT IMAGE ASSIGN ############################################################ 
        def SetChosenComp(n): ##choosing which image first
            if n.currentIndex()==0:
                return self.Image1,self.Image2 #if chosen first then put second 2nd
            else:
                return self.Image2,self.Image1
########################################## COMPONENT IMAGE ASSIGN ############################################################  
#  
########################################### SLIDER ############################################################    
#to show both comp effect we do that
        def Sliders(Component11,Component12,Component21,Component22):
            RESULT1=np.add(Component11*(self.Slider1.value()/100),Component12*((100-self.Slider1.value())/100))#for first image(wa7da fehom hatkon sefr kol mara bas 3awez atl3hom f one var)
            # logging.info('SLIDER 1 VALUE APPLIED TO CHOSSEN COMPONENT 1 '.format())
            RESULT2=np.add(Component21*(self.Slider2.value()/100),Component22*((100-self.Slider2.value())/100))#for 2nd image
            # logging.info('SLIDER 2 VALUE APPLIED TO CHOSSEN COMPONENT 2 '.format())
            return RESULT1,RESULT2
########################################## SLIDER ############################################################    
########################################## UNIFORM CALCULATING FUNCTIONS ######################################################
        def UnitMagnitude(n):
            return np.divide(n,n)#all magnitude values are set to 1
        def UnitPhase(n):
            return np.multiply(n,0) #all phase values are set to 0
########################################## UNIT CALCULATING FUNCTIONS ######################################################



 #################################### START OF MIXING WITH SOME CHECKS FIRST ############################################
       
        if self.Image1.imgByte==None or self.Image2.imgByte==None:
            main=Tk()
            main.withdraw()
            messagebox.showinfo("Error", "Plz Insert IMAGE 1 and IMAGE 2 to MIX ")                    #ERROR MESSAGE 
            logging.info('ERROR MESSAGE ACTION: The User Tried To Mix Without Inserting Images '.format())
            main.destroy()
        elif self.OUTPUT==None:
            main=Tk()
            main.withdraw()
            messagebox.showinfo("Error", "Plz CHoose OUTPUT ")                    #ERROR MESSAGE 
            logging.info('ERROR MESSAGE ACTION: The User Tried to Mix Without Choosing Output'.format())
            main.destroy()
        else:

            Component11,Component12=SetChosenComp(self.ComboImageo1) #compnent 1 and 2 gets applied on 1st pic
            Component21,Component22=SetChosenComp(self.ComboImageo2)  #component 1 and 2 gets applied on 2nd pic


            if self.MODE==Modes.realAndImaginary:
                if self.ComboOUT1.currentText()=='REAL':
                    REAL,IMAG=Sliders(Component11.real,Component12.real,Component21.imaginary,Component22.imaginary)#set real first
                else: 
                    IMAG,REAL=Sliders(Component11.imaginary,Component12.imaginary,Component21.real,Component22.real) #set image first
                data=ifft2(np.add(REAL,(1J*IMAG))) #INVERSE Fourier transofrm for 2D for reald and imag to Draw it after adding them

            if self.MODE==Modes.magnitudeAndPhase:
                if self.ComboOUT1.currentText()=='MAGNITUDE':
                    if self.ComboOUT2.currentText()=='PHASE':
                        MAGNITUDE,PHASE=Sliders(Component11.magnitude,Component12.magnitude,Component21.phase,Component22.phase)#mag 1st
                    else:
                        MAGNITUDE,PHASE=Sliders(Component11.magnitude,Component12.magnitude,UnitPhase(Component21.phase),UnitPhase(Component22.phase)) 
                elif self.ComboOUT1.currentText()=="PHASE":
                    if self.ComboOUT2.currentText()=="MAGNITUDE":
                        PHASE,MAGNITUDE=Sliders(Component11.phase,Component12.phase,Component21.magnitude,Component22.magnitude) 
                    else:
                        PHASE,MAGNITUDE=Sliders(Component11.phase,Component12.phase,UnitMagnitude(Component21.magnitude),UnitMagnitude(Component22.magnitude)) 
                elif self.ComboOUT1.currentText()=="UNIT MAGNITUDE":
                    if self.ComboOUT2.currentText()=="PHASE":
                        MAGNITUDE,PHASE=Sliders(UnitMagnitude(Component11.magnitude),UnitMagnitude(Component12.magnitude),Component21.phase,Component22.phase) 
                    else:
                        MAGNITUDE,PHASE=Sliders(UnitMagnitude(Component11.magnitude),UnitMagnitude(Component12.magnitude),UnitPhase(Component21.phase),UnitPhase(Component22.phase)) 
                elif self.ComboOUT1.currentText()=="UNIT PHASE":
                    if self.ComboOUT2.currentText()=="MAGNITUDE":
                        PHASE,MAGNITUDE=Sliders(UnitPhase(Component11.phase),UnitPhase(Component12.phase),Component21.magnitude,Component22.magnitude) 
                    else:
                        PHASE,MAGNITUDE=Sliders(UnitPhase(Component11.phase),UnitPhase(Component12.phase),UnitMagnitude(Component21.magnitude),UnitMagnitude(Component22.magnitude)) 
                data=ifft2(np.multiply(MAGNITUDE,np.exp(1j*PHASE)))  
                 
            item=ImageItem(np.rot90(data,3))##updating image with data from above after mixing
            self.OUTPUT.addItem(item)
            logging.info('MIX Has BEEN DRAWN WITH MODE {}  '.format(self.MODE))
            logging.info('  MIXING HAS ENDED  '.format())

























class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.img1=ImageModel("IMAGE 1",self.ui.Image1,self.ui.Image2,self.ui.IMAGECOMB1)#assigning name and widgets and comboboxes
        self.img2=ImageModel("IMAGE 2",self.ui.Image3,self.ui.Image4,self.ui.IMAGECOMB2)

        self.ui.actionImport_Image_1.triggered.connect(self.img1.IMPORT)#import function from imagemodel class
        self.ui.actionImport_Image_2.triggered.connect(lambda: self.img2.IMPORT(self.img1.imgByte))#giving img size to have both of same size
        self.ui.COMB1.currentTextChanged.connect(self.RestrictingComboBox)

############################################ Sending All neded data to Mix function in ImageCLass ###########################################################

        self.ui.horizontalSlider.valueChanged.connect(lambda: self.img1.mix(self.img2,self.GetOutPutMix(),self.GetModeAndAssign(),self.ui.COMB1
        ,self.ui.Comb22,self.ui.Comb11,self.ui.Comb21,self.ui.horizontalSlider,self.ui.horizontalSlider_2))
#setting image 1,2 and output widget,choosing mode,setting both comboboxes for output and images choosing and setting Sliders

        self.ui.horizontalSlider_2.valueChanged.connect(lambda: self.img1.mix(self.img2,self.GetOutPutMix(),self.GetModeAndAssign(),self.ui.COMB1
        ,self.ui.Comb22,self.ui.Comb11,self.ui.Comb21,self.ui.horizontalSlider,self.ui.horizontalSlider_2))
####################################################################################################################################
################################# GETTER FUNCTIONS FOR OUTPUT AND MODE ####################################################
    def GetOutPutMix(self):
        if self.ui.OUTOPTION.currentIndex()==0:#on choosing nothing keep it cleared
            self.ui.Output1.clear()
            self.ui.OutPut2.clear()
            return
        elif self.ui.OUTOPTION.currentIndex()==1:#choosed output 1
            self.ui.Output1.clear()
            out=self.ui.Output1
            logging.info('OUTPUT 1 has been chosen by user'.format())
            return out
        elif self.ui.OUTOPTION.currentIndex()==2:#choosed output 2
            self.ui.OutPut2.clear()
            out=self.ui.OutPut2
            logging.info('OUTPUT 2 has been chosen by user'.format())
            return out

    def GetModeAndAssign(self):
        if ((self.ui.COMB1.currentIndex() == 3) or (self.ui.COMB1.currentIndex() == 4)):         # REAL OR IMAGINARY IN COMBOX
            logging.info('Real and Imaginary Mode Assigned'.format())
            return Modes.realAndImaginary
        else:
            logging.info('Magnitude and Phase Mode Assigned'.format())  #choosing magnitude cor phase in ComboBox
            return Modes.magnitudeAndPhase
################################# GETTER FUNCTIONS FOR OUTPUT AND MODE ####################################################
################################### REINITIALZING COMBOBOXES FUNCTION ############################################################
    def RestrictingComboBox(self):
            if (self.ui.COMB1.currentIndex()==3):                                                   #check if it Real
                self.ui.Comb22.clear()                                                             #clear the ComboBox 
                self.ui.Comb22.addItem("")                                                         #additems for user                         
                self.ui.Comb22.setItemText(0, _translate("MainWindow", "IMAGINARY"))  #imaginary restricted
                logging.info('Options Restricted for user'.format())
            elif (self.ui.COMB1.currentIndex()==4):                                                                          #Imaginary
                self.ui.Comb22.clear()
                self.ui.Comb22.addItem("")
                self.ui.Comb22.setItemText(0, _translate("MainWindow", "REAL"))
                logging.info('Options Restricted for user'.format())
            elif ((self.ui.COMB1.currentIndex()==1) or (self.ui.COMB1.currentIndex()==6)):          #magnitude or unit magnitude
                self.ui.Comb22.clear()
                self.ui.Comb22.addItem("")
                self.ui.Comb22.addItem("")                                                         #add phase and unit phase 
                self.ui.Comb22.setItemText(0, _translate("MainWindow", "PHASE"))
                self.ui.Comb22.setItemText(1, _translate("MainWindow", "UNIT PHASE"))
                logging.info('Options Restricted for user'.format())      
            elif ((self.ui.COMB1.currentIndex()==2) or (self.ui.COMB1.currentIndex()==5)):                                                                                # phase or unit phase 
                self.ui.Comb22.clear()
                self.ui.Comb22.addItem("")
                self.ui.Comb22.addItem("")                                                         #add Magnitude and unit Magnitude 
                self.ui.Comb22.setItemText(0, _translate("MainWindow", "MAGNITUDE"))
                self.ui.Comb22.setItemText(1, _translate("MainWindow", "UNIT MAGNITUDE")) 
                logging.info('Options Restricted for user'.format())
            else:
                return      
##################################### REINITIALZING COMBOBOXES FUNCTION ##################################################################









def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()