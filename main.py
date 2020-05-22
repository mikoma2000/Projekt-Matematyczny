from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QCoreApplication
import sys
import matplotlib.pyplot as plt
from matplotlib import style
import random
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from application import Application

# nowa wersja byt Dariusz Marek
app = QtWidgets.QApplication([]) 
Open = Application()
app.exec_()

