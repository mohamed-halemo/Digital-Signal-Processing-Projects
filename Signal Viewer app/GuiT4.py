import sys
from PyQt5 import QtCore, QtWidgets
from GuiT5 import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import pandas as pd
from reportlab.pdfgen import canvas
from PIL import Image
def adjust(x):

    x.setRange(0,5)
    x.setValue(1)
       
def adjustSpectroGram(x):

    x.setRange(0,5)
    x.setValue(0)

def PDF(x,y):
    pdf=canvas.Canvas("Report.pdf")
    for i in range(3) :
       pdf.drawInlineImage(x[0],10, 600)
       pdf.drawInlineImage(y[0],300, 600)
       pdf.drawInlineImage(x[1],10, 300)
       pdf.drawInlineImage(y[1],300, 300)
       pdf.drawInlineImage(x[2],10, 0)
       pdf.drawInlineImage(y[2],300, 0)
    pdf.save()


def ConvertToPdf(a,b,c,d):
       w = QtWidgets.QWidget()
       screen = QtWidgets.QApplication.primaryScreen()
       screenshot=screen.grabWindow(a)
       screenshot2=screen.grabWindow(b)
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
       c.append(image1)
       d.append(image3)
 
