import sys
from PyQt5 import QtCore, QtWidgets
from GuiT5 import *
from PyQt5.QtWidgets import QApplication, QMainWindow

class TabPage(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        group = QtWidgets.QGroupBox('')
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(group)
        grid = QtWidgets.QGridLayout(group)
        