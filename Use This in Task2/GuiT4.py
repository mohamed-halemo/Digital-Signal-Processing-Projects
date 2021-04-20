import sys
from PyQt5 import QtCore, QtWidgets
from GuiT5 import *
from PyQt5.QtWidgets import QApplication, QMainWindow

def adjust(x):

    x.setRange(0,5)
    x.setValue(1)
       
def adjustSpectroGram(x):

    x.setRange(0,5)
    x.setValue(0)
