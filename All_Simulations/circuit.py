# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testing.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtWidgets import QListWidgetItem,QAbstractItemView
from Experiments_Lab_Manual import *
import numpy as np
from RVI_Measurment import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1371, 705)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(234, 234, 234);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-90, -10, 1500, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: rgb(50, 75, 97);\n"
"    color: White;\n"
"}")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1141, 120, 181, 241))
        self.label_4.setStyleSheet("QLabel{\n"
"    \n"
"    \n"
"    background-color: rgb(62, 62, 62);\n"
"border-radius:40px;\n"
"border: 10px solid;\n"
"    \n"
"    border-color: rgb(255, 170, 0);\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(20, 140, 151, 371))
        self.label_31.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: white;\n"
"border-radius:40px;\n"
"border: 2px solid;\n"
"    border-color: rgb(127, 110, 87);\n"
"}")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.pushButton_Home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Home.setGeometry(QtCore.QRect(690, 650, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Home.setFont(font)
        self.pushButton_Home.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(51, 51, 51, 0);\n"
"color:white;\n"
"border:none;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-color: rgb(51, 51, 51, 0.3);\n"
"}\n"
"\n"
"")
        self.pushButton_Home.setText("")
        self.pushButton_Home.setObjectName("pushButton_Home")
        self.pushButton_Lab_Manual = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Lab_Manual.setGeometry(QtCore.QRect(1230, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Lab_Manual.setFont(font)
        self.pushButton_Lab_Manual.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Lab_Manual.setStyleSheet("QPushButton\n"
"{\n"
"border:none;\n"
"color:white;\n"
"    background-color: rgb(127, 110, 87);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-color: rgb(51, 51, 51, 0.5);\n"
"}")
        self.pushButton_Lab_Manual.setObjectName("pushButton_Lab_Manual")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(695, 655, 31, 31))
        self.label_22.setStyleSheet("QLabel\n"
"{\n"
"border:none;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"")
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("../../.designer/backup/Home_Icon.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 5, 31, 31))
        self.label_2.setStyleSheet("background-color: rgb(50, 75, 97);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../.designer/backup/run_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_Run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Run.setGeometry(QtCore.QRect(1010, 0, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Run.setFont(font)
        self.pushButton_Run.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_Run.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(51, 51, 51, 0);\n"
"color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-color: rgb(51, 51, 51, 0.5);\n"
"}")
        self.pushButton_Run.setText("")
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1150, 10, 31, 21))
        self.label_5.setStyleSheet("background-color: rgb(50, 75, 97);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../.designer/backup/Stop-icon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(1070, 0, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_stop.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(51, 51, 51, 0);\n"
"color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-color: rgb(51, 51, 51, 0.5);\n"
"}")
        self.pushButton_stop.setText("")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.Multimeter_value_displayer = QtWidgets.QLabel(self.centralwidget)
        self.Multimeter_value_displayer.setGeometry(QtCore.QRect(1161, 140, 141, 91))
        self.Multimeter_value_displayer.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: white;\n"
"border-radius:20px;\n"
"border: 2px solid;\n"
"    border-color: rgb(127, 110, 87);\n"
"}")
        self.Multimeter_value_displayer.setText("")
        self.Multimeter_value_displayer.setObjectName("Multimeter_value_displayer")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1155, 290, 30, 30))
        self.label_11.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: black;\n"
"border-radius:15px;\n"
"border: 4px solid;\n"
"    border-color: rgb(127, 110, 87);\n"
"}")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1195, 290, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: black;\n"
"border-radius:15px;\n"
"border: 4px solid;\n"
"    border-color: rgb(127, 110, 87);\n"
"}")
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1235, 290, 30, 30))
        self.label_13.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: black;\n"
"border-radius:15px;\n"
"border: 4px solid;\n"
"    border-color: rgb(127, 110, 87);\n"
"}")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1275, 290, 30, 30))
        self.label_14.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: black;\n"
"border-radius:15px;\n"
"border: 4px solid;\n"
"    border-color: rgb(127, 110, 87);\n"
"}")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1154, 260, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(62, 62, 62);")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1234, 260, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(62, 62, 62);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1194, 260, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(62, 62, 62);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.Voltage_Measurement_port = QtWidgets.QLabel(self.centralwidget)
        self.Voltage_Measurement_port.setGeometry(QtCore.QRect(1162, 297, 16, 16))
        self.Voltage_Measurement_port.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: black;\n"
"border-radius:8px;\n"
"border: 4px solid;\n"
"    \n"
"    border-color: rgb(85, 0, 0);\n"
"}")
        self.Voltage_Measurement_port.setText("")
        self.Voltage_Measurement_port.setObjectName("Voltage_Measurement_port")
        self.current_measurement_port = QtWidgets.QLabel(self.centralwidget)
        self.current_measurement_port.setGeometry(QtCore.QRect(1202, 297, 16, 16))
        self.current_measurement_port.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: black;\n"
"border-radius:8px;\n"
"border: 4px solid;\n"
"    \n"
"    border-color: rgb(85, 0, 0);\n"
"}")
        self.current_measurement_port.setText("")
        self.current_measurement_port.setObjectName("current_measurement_port")
        self.resistance_measurement_port = QtWidgets.QLabel(self.centralwidget)
        self.resistance_measurement_port.setGeometry(QtCore.QRect(1242, 297, 16, 16))
        self.resistance_measurement_port.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: black;\n"
"border-radius:8px;\n"
"border: 4px solid;\n"
"    \n"
"    border-color: rgb(85, 0, 0);\n"
"}")
        self.resistance_measurement_port.setText("")
        self.resistance_measurement_port.setObjectName("resistance_measurement_port")
        self.Common_port = QtWidgets.QLabel(self.centralwidget)
        self.Common_port.setGeometry(QtCore.QRect(1282, 297, 16, 16))
        self.Common_port.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: black;\n"
"border-radius:8px;\n"
"border: 4px solid;\n"
"    \n"
"    border-color: rgb(170, 113, 0);\n"
"}")
        self.Common_port.setText("")
        self.Common_port.setObjectName("Common_port")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1267, 260, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(62, 62, 62);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.listWidget_Drag_R1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Drag_R1.setGeometry(QtCore.QRect(45, 155, 101, 51))
        self.listWidget_Drag_R1.setStyleSheet("QListWidget{\n"
"border: 1px solid;\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"background-color: white;\n"
"}")
        self.listWidget_Drag_R1.setObjectName("listWidget_Drag_R1")
        self.listWidget_Drag_R3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Drag_R3.setGeometry(QtCore.QRect(70, 240, 61, 101))
        self.listWidget_Drag_R3.setStyleSheet("QListWidget{\n"
"border: 1px solid;\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"background-color: white;\n"
"}")
        self.listWidget_Drag_R3.setObjectName("listWidget_Drag_R3")
        self.listWidget_Drag_V1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Drag_V1.setGeometry(QtCore.QRect(70, 380, 61, 101))
        self.listWidget_Drag_V1.setStyleSheet("QListWidget{\n"
"border: 1px solid;\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"background-color: white;\n"
"}")
        self.listWidget_Drag_V1.setObjectName("listWidget_Drag_V1")
        self.Circuit_board = QtWidgets.QListWidget(self.centralwidget)
        self.Circuit_board.setGeometry(QtCore.QRect(270, 160, 571, 361))
        self.Circuit_board.setStyleSheet("background-color: rgb(62, 159, 200);\n"
"border-radius:20px;")
        self.Circuit_board.setObjectName("Circuit_board")
        self.label.raise_()
        self.label_4.raise_()
        self.label_31.raise_()
        self.pushButton_Lab_Manual.raise_()
        self.label_22.raise_()
        self.pushButton_Home.raise_()
        self.label_2.raise_()
        self.pushButton_Run.raise_()
        self.label_5.raise_()
        self.pushButton_stop.raise_()
        self.Multimeter_value_displayer.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.Voltage_Measurement_port.raise_()
        self.current_measurement_port.raise_()
        self.resistance_measurement_port.raise_()
        self.Common_port.raise_()
        self.label_19.raise_()
        self.listWidget_Drag_R1.raise_()
        self.listWidget_Drag_R3.raise_()
        self.listWidget_Drag_V1.raise_()
        self.Circuit_board.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.listWidget_Drag_R1.setDragEnabled(True)
        # self.listWidget_Drag_R2.setDragEnabled(True)
        self.listWidget_Drag_R3.setDragEnabled(True)
        self.listWidget_Drag_V1.setDragEnabled(True)
        self.Circuit_board.setAcceptDrops(True)

        # self.listWidget_Drag_V2.setDragEnabled(True)
        R1 = QListWidgetItem(QIcon("Resistor_icon.png"), "")
        R2 = QListWidgetItem(QIcon("Resistor_icon.png"), "")
        R3 = QListWidgetItem(QIcon("Resistor_icon2.png"), "")
        V1 = QListWidgetItem(QIcon("Battery_icon.png"), "")
        V2 = QListWidgetItem(QIcon("Battery_icon.png"), "")
        self.listWidget_Drag_R1.insertItem(1, R1)
        print(self.Circuit_board.count())
        # self.listWidget_Drag_R2.insertItem(1, R2)
        self.listWidget_Drag_R3.insertItem(1, R3)
        self.listWidget_Drag_V1.insertItem(1, V1)
        # self.listWidget_Drag_V2.insertItem(1, V2)
        self.listWidget_Drag_R1.setIconSize(QSize(85, 100))
        # self.listWidget_Drag_R2.setIconSize(QSize(85, 100))
        self.listWidget_Drag_R3.setIconSize(QSize(40, 90))
        self.listWidget_Drag_V1.setIconSize(QSize(50, 70))
        # self.listWidget_Drag_V2.setIconSize(QSize(50, 70))
        self.retranslateUi(MainWindow)
        self.Circuit_board.setIconSize(QSize(100,100))
        self.Circuit_board.itemAlignment()
        self.Circuit_board.setSpacing(20)
        self.Circuit_board.setItemAlignment(Qt.AlignRight)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Experiment One"))
        self.label.setText(_translate("MainWindow", "                          Measurement of D.C. Currents, Voltage and Resistances"))
        self.pushButton_Lab_Manual.setText(_translate("MainWindow", "Lab Manual"))
        self.label_15.setText(_translate("MainWindow", "V"))
        self.label_17.setText(_translate("MainWindow", "R"))
        self.label_18.setText(_translate("MainWindow", "A"))
        self.label_19.setText(_translate("MainWindow", "COM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
