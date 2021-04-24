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
class lists ():
    def list(self):
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
        self.values=[self.value_1,self.value_2,self.value_3,self.value_4,self.value_5,self.value_6,self.value_7,self.value_8,self.value_9,self.value_10]



    
    
