# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Multi_Band_Resistor_Color_Code_Calculator import *
from Splash_python_code import *
from Experiment_1_Wired import *
class MyMainWindow(object):

   def setupUi(self, MainWindow):


        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1560, 720)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1501, 771))
        self.label_3.setStyleSheet("QLabel{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 331, 591))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    background-color: rgb(240, 240, 240);\n"
"border: 5px solid;\n"
" \n"
"    border-top-color: rgb(240, 240, 240);\n"
"    border-bottom-color: rgb(255, 255, 255);\n"
"    border-left-color: rgb(255, 255, 255);\n"
"    border-right-color: rgb(79, 58, 80);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.checkBox_Fundamental_Circuit = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Fundamental_Circuit.setGeometry(QtCore.QRect(20, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Fundamental_Circuit.setFont(font)
        self.checkBox_Fundamental_Circuit.setObjectName("checkBox_Fundamental_Circuit")
        self.checkBox_Resistor_Color_Code = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Resistor_Color_Code.setGeometry(QtCore.QRect(50, 70, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Resistor_Color_Code.setFont(font)
        self.checkBox_Resistor_Color_Code.setObjectName("checkBox_Resistor_Color_Code")
        self.checkBox_Experiment_1 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Experiment_1.setGeometry(QtCore.QRect(50, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Experiment_1.setFont(font)
        self.checkBox_Experiment_1.setObjectName("checkBox_Experiment_1")
        self.checkBox_Experiment_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Experiment_2.setGeometry(QtCore.QRect(50, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_Experiment_2.setFont(font)
        self.checkBox_Experiment_2.setObjectName("checkBox_Experiment_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(50, 200, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 90, 911, 461))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"border:none;\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 55, 191, 258))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"border-radius: 15px;\n"
"    border-color: rgb(79, 58, 80);\n"
"}")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 175, 4))
        self.label_4.setStyleSheet("QLabel{\n"
"    background-color: rgb(79, 58, 80);\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_Resistor_Color_code = QtWidgets.QLabel(self.groupBox_2)
        self.label_Resistor_Color_code.setGeometry(QtCore.QRect(10, 140, 191, 171))
        self.label_Resistor_Color_code.setStyleSheet("QLabel{\n"
"border-radius:15px 15px 15px 15px;\n"
"}\n"
"")
        self.label_Resistor_Color_code.setText("")
        self.label_Resistor_Color_code.setPixmap(QtGui.QPixmap("resistor-res5.gif"))
        self.label_Resistor_Color_code.setScaledContents(True)
        self.label_Resistor_Color_code.setObjectName("label_Resistor_Color_code")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(230, 55, 191, 258))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"border-radius: 15px;\n"
"    border-color: rgb(79, 58, 80);\n"
"}")
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(240, 120, 175, 4))
        self.label_17.setStyleSheet("QLabel{\n"
"    background-color: rgb(79, 58, 80);\n"
"}")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(240, 145, 171, 151))
        self.label_6.setStyleSheet("QLabel{\n"
"border-radius:15px 15px 15px 15px;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: rgb(132, 97, 85);\n"
"}\n"
"")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("multimeter_current.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(450, 140, 191, 171))
        self.label_8.setStyleSheet("QLabel{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QLabel:hover{\n"
"    background-color: rgba(51, 51, 51,0.5);\n"
"border-radius: 15px;\n"
"}")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(450, 55, 191, 258))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"border-radius: 15px;\n"
"    border-color: rgb(79, 58, 80);\n"
"}")
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(460, 120, 175, 4))
        self.label_18.setStyleSheet("QLabel{\n"
"    background-color: rgb(79, 58, 80);\n"
"}")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(460, 150, 171, 151))
        self.label_9.setStyleSheet("QLabel{\n"
"border-radius:15px 15px 15px 15px;\n"
"}\n"
"QLabel:hover{\n"
"    background-color: rgb(132, 97, 85);\n"
"}\n"
"")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("KCL KVL 1.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(670, 55, 191, 258))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("QLabel{\n"
"border:1px solid black;\n"
"border-radius: 15px;\n"
"    border-color: rgb(79, 58, 80);\n"
"}")
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(680, 120, 175, 4))
        self.label_19.setStyleSheet("QLabel{\n"
"    background-color: rgb(79, 58, 80);\n"
"}")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(675, 145, 181, 161))
        self.label_11.setStyleSheet("QLabel{\n"
"border-radius:25px;\n"
"}")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("lissajous.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.pushButton_Experiment_1 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_Experiment_1.setGeometry(QtCore.QRect(230, 140, 191, 171))
        self.pushButton_Experiment_1.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(51, 51, 51,0.5);\n"
"border-radius: 15px;\n"
"}")
        self.pushButton_Experiment_1.setText("")
        self.pushButton_Experiment_1.setObjectName("pushButton_Experiment_1")
        self.pushButton_Experiment_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_Experiment_2.setGeometry(QtCore.QRect(450, 140, 191, 171))
        self.pushButton_Experiment_2.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(51, 51, 51,0.5);\n"
"border-radius: 15px;\n"
"}")
        self.pushButton_Experiment_2.setText("")
        self.pushButton_Experiment_2.setObjectName("pushButton_Experiment_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 140, 191, 171))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(51, 51, 51,0.5);\n"
"border-radius: 15px;\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_Resistor__Color_Code = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_Resistor__Color_Code.setGeometry(QtCore.QRect(10, 140, 191, 171))
        self.pushButton_Resistor__Color_Code.setStyleSheet("QPushButton{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(51, 51, 51,0.5);\n"
"border-radius: 15px;\n"
"pushbutton.setToolTip( \"Click this button to open file\"  );\n"
"}")
        self.pushButton_Resistor__Color_Code.setText("")
        self.pushButton_Resistor__Color_Code.setObjectName("pushButton_Resistor__Color_Code")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 36, 1325, 5))
        self.label.setStyleSheet("QLabel{\n"
"    background-color: rgb(79, 58, 80);\n"
"}")
        self.pushButton_Resistor__Color_Code.setToolTip("Click here to open the simulation");
        self.pushButton_Experiment_1.setToolTip("Click here to open the simulation");
        self.pushButton_Experiment_2.setToolTip("Click here to open the simulation");
        self.pushButton_3.setToolTip("Click here to open the simulation");
        self.pushButton_Resistor__Color_Code.clicked.connect(self.dis_colorcodemainwindow)
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_Experiment_1.clicked.connect(self.experiment)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
   def experiment(self):
           self.window = QtWidgets.QMainWindow()
           self.ui = Experiment_one_MainWindow()
           self.ui.setupUi(self.window)
           self.window.show()

   def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab Experiments"))
        self.groupBox.setTitle(_translate("MainWindow", "Courses"))
        self.checkBox_Fundamental_Circuit.setText(_translate("MainWindow", "Fundamental of Circuit"))
        self.checkBox_Resistor_Color_Code.setText(_translate("MainWindow", "Resistor Color Code Calculator"))
        self.checkBox_Experiment_1.setText(_translate("MainWindow", "Experiment-1"))
        self.checkBox_Experiment_2.setText(_translate("MainWindow", "Experiment-2"))
        self.checkBox_5.setText(_translate("MainWindow", "Experiment-3"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Fundamentals of Circuit Lab Experiments"))
        self.label_2.setText(_translate("MainWindow", "Resistor Color Code\n"
"Calculator"))
        self.label_15.setText(_translate("MainWindow", "Experiment 1: Measurem-\n"
"ent of D.C. Currents,\n"
"Voltage, Resistances"))
        self.label_16.setText(_translate("MainWindow", "Experiment 2: KVL, KCL,\n"
"Thevenin\'s Theorem\n"
"and Norton\'s Theorem"))
        self.label_20.setText(_translate("MainWindow", "Experiment 3: The Cathode\n"
"ray oscilloscope"))

   def dis_colorcodemainwindow(self):
        self.colorcode_window = QtWidgets.QMainWindow()
        self.Resis_ui = Resistor_MainWindow()
        self.Resis_ui.setupUi(self.colorcode_window)
        self.colorcode_window.show()
        # Ui_Dialog.dis_player()




# if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # My_AllMainWindow = QtWidgets.QMainWindow()
    # ui = MyMainWindow()
    # ui.setupUi(My_AllMainWindow)
    # My_AllMainWindow.show()
    # sys.exit(app.exec_())
