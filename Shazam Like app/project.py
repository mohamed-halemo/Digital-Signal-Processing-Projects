from PyQt5 import QtWidgets,QtGui
from Gui2 import Ui_MainWindow
import sys
import matplotlib.pyplot as plt
import librosa
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
from tempfile import mktemp
import librosa.display
import soundfile as sf

import sklearn

class Operations():
    def __init__(self,data1,data2,value): #data1,2 ,slider value
        self.data1=data1
        self.data2=data2
        self.similarityFeature=[]
        self.sumf=[]
        self.sumHashAndFeature=[]
        self.songs=[]
        self.similarityFeature2=[]
        self.similarityFeature4=[]

        self.similarityFeature5=[]

        self.MixerValue=value
        self.data_dir='./Songs/'
        self.SpectroGram=glob(self.data_dir+'*.wav')  #to add . use * and glob which takes file path
        for i in range(len(self.SpectroGram)):  #loop on the songs
            self.songs.append(relpath(self.SpectroGram[i], './Songs\\')) #put songs on spectrogram array
      

        # for i in range(len(self.SpectroGram)):
        #     self.CromaFeatuer(self.SpectroGram[i],i) #run only in first time then comment
            # self.Mfcc(self.SpectroGram[i],i) #run only in first time then comment
            # self.tepofeature(self.SpectroGram[i],i) #run only in first time then comment
            # self.cemel(self.SpectroGram[i],i) #run only in first time then comment

        self.arrayofHashFeature=self.Hash('./SpectroFeatuers/')
        self.arrayofHashFeature2=self.Hash('./SpectroFeatuer2/')
        self.arrayofHashFeature4=self.Hash('./SpectroFeatuer4/')



    
    def Hash(self,folder):
        arrayofHash=[]
        self.data_dir_SG=folder
        self.files=glob(self.data_dir_SG+'/*.png')
        for i in range(len(self.files)): 
            file=self.files[i]
            img = Image.open(file)
            hashedVersion = imagehash.phash(img)
            if len(arrayofHash)>69:
                print("N")
            else:    
                arrayofHash.append(hashedVersion)
        return arrayofHash


    def Mfcc(self,file,i):
        y, sr = librosa.load(str(file),duration=60.0)
        librosa.feature.mfcc(y=y, sr=sr)   
        librosa.feature.mfcc(y=y, sr=sr, hop_length=1024, htk=True)    
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128,
                                   fmax=8000)

        librosa.feature.mfcc(S=librosa.power_to_db(S))
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        fig, ax = plt.subplots()
        librosa.display.specshow(mfccs, x_axis='time', ax=ax)
        # Compute the auto-correlation tempogram, unnormalized to make comparison easier
       
       
      
        if i==88888:
            plt.savefig('SPF_Song Mfcc' + '.png')
        else:
            plt.savefig('./SpectroFeatuer4/SPF_Song' + str(i).zfill(3)+'.png')



    def tepofeature(self,file,i):
        y, sr = librosa.load(str(file),duration=60.0)
        hop_length = 1024 #number of audio samples between successive onset measurements
        oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
        tempogram = librosa.feature.fourier_tempogram(onset_envelope=oenv, sr=sr,
                                                        hop_length=hop_length)
        # Compute the auto-correlation tempogram, unnormalized to make comparison easier
        ac_tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=sr,
                                         hop_length=hop_length, norm=None)
        librosa.display.specshow(np.abs(tempogram), sr=sr, hop_length=hop_length,
                         x_axis='time', y_axis='fourier_tempo', cmap='plasma'
                         )
       
      
        if i=="tepo":
            plt.savefig('SPF_Song ' + str(i)+'.png')
        else:
            plt.savefig('./SpectroFeatuer3/SPF_Song' + str(i).zfill(3)+'.png')
       



    



    def CromaFeatuer(self,file,i):
        
        samples, sample_rate = librosa.load(str(file),duration=60.0)     
        chroma = librosa.feature.chroma_cqt(samples, sr=sample_rate)
        librosa.display.specshow(chroma)
        plt.tight_layout()
        if i==18888:
            plt.savefig('SPF_Song croma' + str(i)+'.png', bbox_inches='tight',  transparent=True,pad_inches=0)
        else:
            plt.savefig('./SpectroFeatuers/SPF_Song' + str(i).zfill(3)+'.png', bbox_inches='tight',  transparent=True,pad_inches=0, frameon='false')

    def cemel(self,file,i):
        y, sr = librosa.load(str(file),duration=60.0)
        onset_env = librosa.onset.onset_strength(y, sr=sr,

                                                aggregate=np.median)
        tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,

                                            sr=sr)
        hop_length = 1024

        # fig, ax = plt.subplots(nrows=2, sharex=True)

        times = librosa.times_like(onset_env, sr=sr, hop_length=hop_length)

        M = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=hop_length)
        
        librosa.display.specshow(librosa.power_to_db(M, ref=np.max),

                                y_axis='mel', x_axis='time', hop_length=hop_length,

                                )
        if i==28888:
            plt.savefig('SPF_Song cmel' + str(i)+'.png', bbox_inches='tight',  transparent=True,pad_inches=0)
        else:
            plt.savefig('./SpectroFeatuer2/SPF_Song' + str(i).zfill(3)+'.png', bbox_inches='tight',  transparent=True,pad_inches=0, frameon='false')
        
    def Mixing(self):
        # # self.MixerValue=self.ui.MixSlider.value()/100
        # if self.data1.ndim==1:
        output=np.add(self.data1[0:2646000,0:2]*self.MixerValue,self.data2[0:2646000,0:2]*(1-self.MixerValue))
        # else :
        # output=np.add(self.data1*self.MixerValue,self.data2*(1-self.MixerValue))
       
        data=np.array(output,dtype=np.float64)
        output=data.astype(np.int16)
        write("Mixed.wav", 44100, output)
        # plt.specgram(output, Fs=self.fs2, NFFT=128, noverlap=0)
        ax = plt.axes()
        ax.set_axis_off()
        plt.savefig('Mixed.png', bbox_inches='tight',  transparent=True,pad_inches=0)
        file='Mixed.png'
        self.CromaFeatuer("Mixed.wav",18888)
        img = Image.open(file)
        self.hashedVersion = imagehash.phash(img)
        fileFeature='SPF_Song croma18888.png'
        imgFeature = Image.open(fileFeature)
        self.FeatureHash = imagehash.phash(imgFeature)

        self.cemel("Mixed.wav",28888)
        fileFeaturemel='SPF_Song cmel28888.png'
        imgFeaturemel = Image.open(fileFeaturemel)
        self.FeatureHashmel = imagehash.phash(imgFeaturemel)

        self.Mfcc("Mixed.wav",88888)
        fileFeatureMfcc='SPF_Song Mfcc.png'
        imgFeatureMfcc = Image.open(fileFeatureMfcc)
        self.FeatureHashMfcc = imagehash.phash(imgFeatureMfcc)

        self.tepofeature("Mixed.wav","tepo")
        fileFeatureTepo='SPF_Song tepo.png'
        imgFeatureTepo = Image.open(fileFeatureTepo)
        self.FeatureHashTepo = imagehash.phash(imgFeatureTepo)




        for c in range(len(self.arrayofHashFeature4)):
            diffFeature4=self.arrayofHashFeature4[c]-self.FeatureHashMfcc 
            simFeature4=diffFeature4/256
            simFeature4=1-simFeature4
            self.similarityFeature4.append(simFeature4)
        print("Similarity Feature Mfcc")
        print(self.similarityFeature)
        print('\n')

        for c in range(len(self.arrayofHashFeature)):
            diffFeature=self.arrayofHashFeature[c]-self.FeatureHash  
            simFeature=diffFeature/256
            simFeature=1-simFeature
            self.similarityFeature.append(simFeature)
        print("Similarity Feature Croma")
        print(self.similarityFeature)
        print('\n')
#divide by 256 to get similarty
      
        for j in range(len(self.arrayofHashFeature2)):
            diffFeature2=self.arrayofHashFeature2[j]-self.FeatureHashmel  
            simFeature2=diffFeature2/256
            simFeature2=1-simFeature2
            self.similarityFeature2.append(simFeature2)
        print("Similarity Feature cmel")
        print(self.similarityFeature2)
        print('\n')

        for i in range(len(self.arrayofHashFeature)):

            self.sumf.append((self.similarityFeature4[i]+self.similarityFeature2[i]+self.similarityFeature[i])*100/3)
            
        self.sumHashAndFeature=list(zip(self.sumf,self.songs))
        self.sumHashAndFeature.sort(reverse = True) 
        for i in range (len(self.sumHashAndFeature)):
            print(self.sumHashAndFeature[i])   
            print('\n')

        return self.sumHashAndFeature
        

        
#ah 
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BrowseS1.clicked.connect(lambda: self.browse(1))
        self.ui.BrowseS2.clicked.connect(lambda: self.browse(2))
        self.signal=[] 
        self.data= []
        self.songs=[]
        self.similarity=[]
        self.similarityFeature=[]
        self.similarityFeature2=[]
        self.similarityFeature3=[]
        self.data1=[]
        self.data2=[]
        self.sumf=[]
        self.sumHashAndFeature=[]
        self.ui.MixSlider.setValue(0)
        self.ui.MixSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.ui.MixSlider.sliderReleased.connect(self.Mixing)
        # self.slidervalue=self.ui.MixSlider.value()/100
        # self.ui.Mixer.clicked.connect(self.Mixing)
        self.data_dir='./Songs/'
        self.SpectroGram=glob(self.data_dir+'*.wav')  #to add . use * and glob which takes file path
        for i in range(len(self.SpectroGram)):  #loop on the songs
            self.songs.append(relpath(self.SpectroGram[i], './Songs\\')) #put songs on spectrogram array
      


        # self.arrayofHashFeature=self.Hash('./SpectroFeatuers/')
        # self.arrayofHashFeature2=self.Hash('./SpectroFeatuer2/')
        # self.arrayofHashFeature3=self.Hash('./SpectroFeatuer3/')
       
    def SG_Maker(self,file,i):
            FS, data = wavfile.read(file)  # read wav file
            data=data[0:60*FS]
            if data.ndim==2:   #if the song is stereo 
                plt.specgram(data[:,0], Fs=FS,  NFFT=128, noverlap=0)   
            else:  #if the song is mono
                plt.specgram(data, Fs=FS,  NFFT=128, noverlap=0)               
            ax = plt.axes()
            ax.set_axis_off()
            plt.savefig('./Spectrograms/sp_Song' + str(i)+'.png')


    def browse(self,n):
        
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self)
        if fileName:

            self.FileName=fileName
            FS, data = wavfile.read(fileName)  # read wav file
            print(FS)

            data=data[0:60*FS]
     


            if n==1:
                self.ui.BrowseS1.setText(self.FileName)
                self.path1=self.FileName
                # if data.ndim==2:
                #     self.data1=data[:,0]
                # else: 
                self.data1=data
                self.fs1=FS

        
            if self.fs1>FS :
                data=data[0:60*FS]
                print(self.fs1)
                print("FS A2AL")

            else:
                data=data[0:60*self.fs1]
                print(self.fs1)
                print("kEDA FS akkbar")



            if n==2:
                self.path2=self.FileName

                self.ui.BrowseS2.setText(self.FileName)

                # if data.ndim==2:
                #     self.data2=data[:,0]
                # else:
                self.data2=data
                self.fs2=FS 

                # x1 , sr1 = librosa.load(self., duration=60.0)
        #         x2 , sr2 = librosa.load(path2, duration=60.0)
        #         x1=x1*self.MixerValue
        #         x2=x2*(1-self.MixerValue)
        #         x=x1+x2
        #         temp = mktemp('.wav')
    
        #         sf.write(temp,x ,sr1)
        # # print(temp)
        #         sound = AudioSegment.from_wav(temp)

        #         sound.export('mixed.mp3', format="mp3")
        else :
            return
       



    # def CromaFeatuer(self,file,i):
        
    #     samples, sample_rate = librosa.load(str(file),duration=60.0)     
    #     chroma = librosa.feature.chroma_cqt(samples, sr=sample_rate)
    #     librosa.display.specshow(chroma)
    #     plt.tight_layout()
    #     if i==18888:
    #         plt.savefig('SPF_Song croma' + str(i)+'.png', bbox_inches='tight',  transparent=True,pad_inches=0, frameon='false')
    #     else:
    #         plt.savefig('./SpectroFeatuers/SPF_Song' + str(i).zfill(3)+'.png', bbox_inches='tight',  transparent=True,pad_inches=0, frameon='false')


  


    # def Hash(self,folder):
    #     arrayofHash=[]
    #     self.data_dir_SG=folder
    #     self.files=glob(self.data_dir_SG+'/*.png')
    #     for i in range(len(self.files)): 
    #         file=self.files[i]
    #         img = Image.open(file)
    #         hashedVersion = imagehash.phash(img)
    #         arrayofHash.append(hashedVersion)
    #     return arrayofHash



    def Mixing(self):
        print('\n')
        self.slidervalue=self.ui.MixSlider.value()/100

        print(self.slidervalue)
        Operation=Operations(self.data1,self.data2,self.slidervalue)
        self.values=Operation.Mixing()
        

        # self.MixerValue=self.ui.MixSlider.value()/100
        # output=self.data1*self.MixerValue+self.data2*(1-self.MixerValue)
        # data=np.array(output,dtype=np.float64)
        # output=data.astype(np.int16)
        # write("Mixed.wav", 44100, output)
        # plt.specgram(output, Fs=self.fs2, NFFT=128, noverlap=0)
        # ax = plt.axes()
        # ax.set_axis_off()
        # plt.savefig('Mixed.png', bbox_inches='tight',  transparent=True,pad_inches=0, frameon='false')
        # file='Mixed.png'
        # self.CromaFeatuer("Mixed.wav",18888)
        # img = Image.open(file)
        # self.hashedVersion = imagehash.phash(img)
        # fileFeature='SPF_Song croma18888.png'
        # imgFeature = Image.open(fileFeature)
        # self.FeatureHash = imagehash.phash(imgFeature)

        # self.cemel("Mixed.wav",28888)
        # fileFeaturemel='SPF_Song cmel28888.png'
        # imgFeaturemel = Image.open(fileFeaturemel)
        # self.FeatureHashmel = imagehash.phash(imgFeaturemel)

        # self.tepofeature("Mixed.wav",48888)

        # fileFeature3='SPF_Song48888.png'
        # imgFeature3 = Image.open(fileFeature3)
        # self.FeatureHash3 = imagehash.phash(imgFeature3)




        # for c in range(len(self.arrayofHashFeature)):
        #     diffFeature=self.arrayofHashFeature[c]-self.FeatureHash  
        #     simFeature=diffFeature/64
        #     simFeature=1-simFeature
        #     self.similarityFeature.append(simFeature)
        # print("Similarity Feature Croma")
        # print(self.similarityFeature)
        # print('\n')

      
   
        # for i in range(len(self.arrayofHashFeature2)):
        #     self.sumf.append(self.similarityFeature[i]*100)
        # self.sumHashAndFeature=list(zip(self.sumf,self.songs))
        # self.sumHashAndFeature.sort(reverse = True) 
        self.j=0
        self.i=0
        for i in range (20):
            # if i==9 or i==19:
            #     self.j=self.j+1
            #     self.i=0
            # self.i=self.i+1
            self.ui.Table.setItem(i, 0,QtWidgets.QTableWidgetItem(str(self.values[i])))
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()


if __name__ == "__main__":
    main()