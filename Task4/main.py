from PyQt5 import QtWidgets,QtGui
from Gui import Ui_MainWindow
import sys
import matplotlib.pyplot as plt

from scipy import signal
import scipy
import scipy.io.wavfile as wav
from scipy.io import wavfile
import os
import wave
import pylab
import hashlib
import numpy as np
from numpy.lib import stride_tricks
import pandas as pd
from glob import glob
from scipy.io import wavfile
from PIL import Image
import imagehash
from os.path import relpath
import difflib
from scipy.io.wavfile import write
from matplotlib.mlab import specgram
from skimage.feature import peak_local_max
import math
# 

#1. Spectral Centroid
#The spectral centroid indicates at which frequency the energy of a spectrum is centered upon or in other words 
# It indicates where the ” center of mass” for a sound is located. This is like a weighted mean:


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
     
        self.signal=[] 
        self.data= []
        self.songs=[]
        self.ui.BrowseS1.clicked.connect(lambda: self.browse(1))
        self.ui.BrowseS2.clicked.connect(lambda: self.browse(2))
        self.ui.Mixer.clicked.connect(self.Mixing)

        self.data_dir='./Songs/'
        self.SpectroGram=glob(self.data_dir+'*.wav')  #to add . use * and glob which takes file path
        for i in range(len(self.SpectroGram)):  #loop on the songs
            self.songs.append(relpath(self.SpectroGram[i], './Songs\\')) #put songs on spectrogram array
        self.spectral_Centroid=[]
        
        for i in range(len(self.SpectroGram)):
            self.SpectroCreator(self.SpectroGram[i],i) #run only in first time to go to spectrogram func 
       
    
    
    def SpectroCreator(self,file,i):
            FS, data = wavfile.read(file)  # read wav file
            data=data[0:60*FS]
            plt.specgram(data[:,0], Fs=FS,  NFFT=128, noverlap=0)   
            ax = plt.axes()
            ax.set_axis_off()
            plt.savefig('./Spectrograms/sp_Song' + str(i)+'.png')






    def browse(self,n):
            
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self)

        FS, data = wavfile.read(fileName)  # read wav file
        data=data[0:60*FS]
        if n==1:
            self.data1=data
            self.fs1=FS
            
        elif n==2:
            
            self.data2=data
            self.fs2=FS 

    def Mixing(self):
        self.MixerValue=self.ui.MixSlider.value()/100
        output=np.add(self.data1[0:2646000,0:2]*self.MixerValue,self.data2[0:2646000,0:2]*(1-self.MixerValue))
        data=np.array(output,dtype=np.float64)
        output=data.astype(np.int16)
        write("Mixed.wav", 44100, output)
        plt.specgram(output[:,0], Fs=self.fs1, NFFT=128, noverlap=0)
        ax = plt.axes()
        ax.set_axis_off()
        plt.savefig('Mixed.png')




def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()