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



class Machine(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):
      
        lb1 = QLabel("Mass of a particle: [kg]", self)
        lb2 = QLabel("Charge of a particle: [C]", self)
        lb3 = QLabel("Result:", self)


        ukladT = QGridLayout()
        ukladT.addWidget(lb1, 0, 0)
        ukladT.addWidget(lb2, 0, 1)
        ukladT.addWidget(lb3, 0, 2)

       
        self.setLayout(ukladT)
        
                 
        self.massEdt = QLineEdit()
        self.chargeEdt = QLineEdit()
        self.resultEdt = QLineEdit()
        self.resultEdt.setDisabled(True)

        self.resultEdt.readonly = True
        self.resultEdt.setToolTip("It's a final value of physical quantity chosen by you for a particle described by your parameters")
        self.massEdt.setToolTip("Choose value of mass of a particle")
        self.chargeEdt.setToolTip("Choose value of charge of a particle")
        
        
        ukladT.addWidget(self.massEdt, 1, 0)
        ukladT.addWidget(self.chargeEdt, 1, 1)
        ukladT.addWidget(self.resultEdt, 1, 2)
 

        ekBtn = QPushButton("Kinetic Energy [J]", self)
        ekBtn.clicked.connect(self.buttonClicked)
        
        velBtn = QPushButton("Velocity [m/s]", self)
        velBtn.clicked.connect(self.buttonClicked)
        
        endBtn = QPushButton("Cancel", self)
        endBtn.clicked.connect(self.end)

        ukladH = QHBoxLayout()
        ukladH.addWidget(ekBtn)
        ukladH.addWidget(velBtn)
        

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(endBtn, 3, 0, 1, 3)

        self.setGeometry(40, 40, 300, 100)        
        self.setWindowTitle("Maschine")
        # nowa wersja byt Dariusz Marek
        # self.show()
        
    def end(self):
        self.close()

    
    # nowa wersja byt Dariusz Marek
    @staticmethod
    def kineticEnergy(mass, energy):
        return 2.53 * energy ** 2 / mass

    # nowa wersja byt Dariusz Marek
    @staticmethod
    def velocity(mass, energy):
        return 2.25 * energy / mass
        
    def buttonClicked(self):
        if not self.massEdt.text() and not self.chargeEdt.text():
            return

        mass = float(self.massEdt.text())
        energy = float(self.chargeEdt.text())

        if energy == 0:
            self.resultEdt.setText("div by 0")
        else:

            # nowa wersja byt Dariusz Marek
            calculated_velocity_value = Machine.velocity(mass, energy)
            calculated_energy_value = Machine.kineticEnergy(mass, energy)
            
            self.resultEdt.setText( "Velocity : {0:.2f} , Energy: {1:.2f}".format(calculated_velocity_value, calculated_energy_value) )
            
            self.graph(calculated_velocity_value, calculated_energy_value)

    
    def graph(self, velocity, kineticEnergy):
        style.use('seaborn')
        fig = plt.figure()
        x = [1]
        


        # def graphValues():
        #     xs = []
        #     ys = []

        #     for i in range (0,3,1):
        #         x = i
        #         y = value

        #         xs.append(x)
        #         ys.append(y)

        #     return xs, ys
        
        plot1 = plt.subplot2grid((1,2), (0,0), colspan = 1, rowspan = 1)
        plot2 = plt.subplot2grid((1,2), (0,1), colspan = 1, rowspan = 1)

        # x,y = graphValues()
        plot1.bar(x,[kineticEnergy], label = 'Kinetic energy', color = 'orange')
        plot1.set_xlabel("Electrone/Alfa/Protone")
        plot1.set_ylabel("value in Joules")

        # x,y = graphValues()
        plot2.bar(x,[velocity], label = 'velocity')
        plot2.set_xlabel('Electrone/Aflfa/Protone')
        plot2.set_ylabel("Value in meters per seconds ")
        plot1.legend()
        plot2.legend()
        plt.show()