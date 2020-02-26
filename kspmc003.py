import krpc
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton, QCheckBox
from PyQt5.QtCore import Qt

conn = krpc.connect()
vessel = conn.space_center.active_vessel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Next stage control
        def nxtstage():
            print ("stage ignition")
            vessel.control.activate_next_stage()
        #Buttons setting throttle limit
        def thrmax():
            print ("Max Throttle")
            vessel.control.throttle = 1
        def thrmin():
            print ("Null Throttle")
            vessel.control.throttle = 0
        def thrmid():
            print ("Mid Throttle")
            vessel.control.throttle = .5
        #Thrust control slider
        def vslider(verticalSlider):
            q1 = self.verticalSlider.value()
            if q1 <= 5:
                vessel.control.throttle = 0
            if q1 >= 6 and q1 <= 15:
                vessel.control.throttle = 0.1
            if q1 >= 16 and q1 <= 25:
                vessel.control.throttle = 0.2
            if q1 >= 26 and q1 <= 35:
                vessel.control.throttle = 0.3
            if q1 >= 36 and q1 <= 45:
                vessel.control.throttle = 0.4
            if q1 >= 46 and q1 <= 55:
                vessel.control.throttle = 0.5
            if q1 >= 56 and q1 <= 65:
                vessel.control.throttle = 0.6
            if q1 >= 66 and q1 <= 75:
                vessel.control.throttle = 0.7
            if q1 >= 76 and q1 <= 85:
                vessel.control.throttle = 0.8
            if q1 >= 86 and q1 <= 95:
                vessel.control.throttle = 0.9
            if q1 >= 96:
                vessel.control.throttle = 1
        #SAS set state
        def sas1(state):
            if state == QtCore.Qt.Checked:
                vessel.control.sas = True
            else:
                vessel.control.sas = False
        #RCS set state
        def rcs1(state):
            if state == QtCore.Qt.Checked:
                vessel.control.rcs = True
            else:
                vessel.control.rcs = False
        #pitch set to 0*
        def pit0(state):
            if state == rb1.isclicked():
                vessel.auto_pilot.engage()
                vessel.control.pitch(0)
            

        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 270, 81, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        #Sliders
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(110, 40, 160, 220))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.setRange(0, 100)
        self.verticalSlider.valueChanged.connect(vslider)
        self.verticalSlider.setTickInterval(10)

        #Buttons for pitch
        
        #self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_5.setGeometry(QtCore.QRect(200, 36, 30, 25))
        #self.pushButton_5.setObjectName("pushButton_5")
        #self.pushButton_5.clicked.connect(pit0)

        #Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 111, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        #Code for buttons
        self.pushButton.clicked.connect(nxtstage)
        self.pushButton_3.clicked.connect(thrmid)
        self.pushButton_4.clicked.connect(thrmin)
        self.pushButton_2.clicked.connect(thrmax)
        #self.pushButton_5.clicked.connect()

        #Check Boxes
        self.checkBox1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox1.move(290, 36)
        self.checkBox1.setObjectName("SAS")
        self.checkBox1.stateChanged.connect(sas1)

        self.checkBox2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox2.move(290, 66)
        self.checkBox2.setObjectName("RCS")
        self.checkBox2.stateChanged.connect(rcs1)
        
        #Line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(270, 10, 20, 280))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KSP MC 0.0.4"))
        self.pushButton.setText(_translate("MainWindow", "Next Stage"))
        self.pushButton_3.setText(_translate("MainWindow", "Mid"))
        self.pushButton_4.setText(_translate("MainWindow", "Null"))
        self.pushButton_2.setText(_translate("MainWindow", "Max"))
        self.label.setText(_translate("MainWindow", "Vessel Speed Controls"))
        self.checkBox1.setText(_translate("MainWindow", "SAS"))
        self.checkBox2.setText(_translate("MainWindow", "RCS"))
    




if __name__ == "__main__":
    import sys
    while True:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)


    
        MainWindow.show()
        sys.exit(app.exec_())
