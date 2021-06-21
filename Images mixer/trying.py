from PyQt5 import  QtWidgets
from MainWindow import *

from PIL import Image
from scipy.fftpack import fft2,ifft2
import numpy as np

def DrawComp(self):

    if self.PickedImage2.currentIndex()==0 :
        self.Edited2.clear()

    elif self.PickedImage2.currentIndex()==1:
        self.Draw(self.magnitude2,self.Edited2,2)
    
    elif self.PickedImage2.currentIndex()==2:
        self.Draw(self.phase2,self.Edited2,2)
    
    elif self.PickedImage2.currentIndex()==3:
        self.Draw(self.real2,self.Edited2,2)
    
    elif self.PickedImage2.currentIndex()==4:
        self.Draw(self.imaginary2,self.Edited2,2)




def ImageDataToMixx(self,n):
    # self.IMAGEPLOTTER.clear() #clearing when importing
    # self.EDIT.clear()    #clearing when importing
    fname, _ =QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', '/PC', "Image Files (*.jpg *.png *.jpeg)")
    print (fname)
    return fname