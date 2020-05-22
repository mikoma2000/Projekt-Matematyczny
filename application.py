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

from machine import Machine


class Application(QtWidgets.QMainWindow):

    def __init__(self):
        super(Application, self).__init__() 
        self.setWindowTitle("Cyclotrone info log")
        self.setGeometry(100,100, 500, 300)

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textEdit.setText("Add your notes")

        menuClose = QtWidgets.QAction("Exit", self) 
        menuClose.setShortcut("Ctrl+Q")
        menuClose.setStatusTip("It closes the app")
        menuClose.triggered.connect(self.closeApp)
        
        menuSave = QtWidgets.QAction("Save your notes", self)
        menuSave.setShortcut("Crtl+S")
        menuSave.setStatusTip("Saves your notes to a file")
        menuSave.triggered.connect(self.fileSave)

        menuCompile = QtWidgets.QAction("Turn on cyclotrone", self)
        menuCompile.setStatusTip("Opens info log to compute data")
        menuCompile.triggered.connect(self.compileFunc)

        menuCompare = QtWidgets.QAction("Compare with other particles", self)
        menuCompare.setStatusTip("Compares with alfa particle and proton")
        menuCompare.triggered.connect(self.compareFunc)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        fileMenu.addAction(menuSave)
        fileMenu.addAction(menuClose)

        compMenu = mainMenu.addMenu("Compile")
        compMenu.addAction(menuCompile)
        compMenu.addAction(menuCompare)

        self.statusBar()
        self.show()

        # nowa wersja byt Dariusz Marek
        self.machine = Machine()

    def compileFunc(self):
        # nowa wersja byt Dariusz Marek
        self.machine.show()


    def compareFunc(self):
        style.use('seaborn')
        fig = plt.figure()

        xV = [1,2,3]
        yV = [2.6e11, 7.5e7*1000, 1.44e8*1000]

        xEk = [1,2,3]
        yEk = [3.16e-8, 1.9e-11*1000, 1.7e-11*1000]

        plot1 = plt.subplot2grid((1,2), (0,0), colspan = 1, rowspan = 1)
        plot2 = plt.subplot2grid((1,2), (0,1), colspan = 1, rowspan = 1)

        plot1.bar(xEk,yEk, label = 'Kinetic energy', color = 'orange')
        plot1.set_xlabel("Electrone/Alfa*10e3/Protone*10e3")
        plot1.set_ylabel("value in Joules")

        plot2.bar(xV,yV, label = 'velocity')
        plot2.set_xlabel('Electrone/Aflfa*10e3/Protone*10e3')
        plot2.set_ylabel("Value in meters per seconds ")
        plot1.legend()
        plot2.legend()
        plt.show()

        
    def fileSave(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Zapisz plik tekstowy", "", "Pliki tesktowy (*txt *hmtl *doc)", options=options)
        fileName = open(fileName, 'w')
        plik = self.textEdit.toPlainText()
        fileName.write(plik)
        sys.exit()
        self.show()   

    def closeApp(self): 
        choice = QtWidgets.QMessageBox.question(self, "Exit window", 
        "Are you sure?",
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass
