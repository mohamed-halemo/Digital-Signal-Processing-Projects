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
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 29, 1251, 798))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Graph1 = PlotWidget(self.layoutWidget)
        self.Graph1.setObjectName("Graph1")
        self.tabs = QtWidgets.QTabWidget()

        