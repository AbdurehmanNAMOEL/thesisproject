# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Experiment_3_PART_B1_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidgetItem

class thevenin_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1382, 639)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(234, 234, 234);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-90, -10, 1721, 51))
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
        self.label_4.setGeometry(QtCore.QRect(1119, 53, 181, 241))
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
        self.label_31.setGeometry(QtCore.QRect(20, 140, 151, 401))
        self.label_31.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: white;\n"
"border-radius:40px;\n"
"border: 2px solid;\n"
"    border-color: rgb(127, 110, 87);\n"
"}")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.pushButton_Lab_Manual = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Lab_Manual.setGeometry(QtCore.QRect(1240, 0, 141, 41))
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 5, 31, 31))
        self.label_2.setStyleSheet("background-color: rgb(50, 75, 97);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../.designer/backup/run_icon.png"))
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
        self.label_5.setGeometry(QtCore.QRect(1090, 10, 31, 21))
        self.label_5.setStyleSheet("background-color: rgb(50, 75, 97);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../../.designer/backup/Stop-icon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(1080, 0, 51, 41))
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
        self.Multimeter_value_displayer.setGeometry(QtCore.QRect(1139, 73, 141, 91))
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
        self.label_11.setGeometry(QtCore.QRect(1133, 223, 30, 30))
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
        self.label_12.setGeometry(QtCore.QRect(1173, 223, 30, 30))
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
        self.label_13.setGeometry(QtCore.QRect(1213, 223, 30, 30))
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
        self.label_14.setGeometry(QtCore.QRect(1253, 223, 30, 30))
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
        self.label_15.setGeometry(QtCore.QRect(1132, 193, 31, 21))
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
        self.label_17.setGeometry(QtCore.QRect(1212, 193, 31, 21))
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
        self.label_18.setGeometry(QtCore.QRect(1172, 193, 31, 21))
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
        self.Voltage_Measurement_port.setGeometry(QtCore.QRect(1140, 230, 16, 16))
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
        self.current_measurement_port.setGeometry(QtCore.QRect(1180, 230, 16, 16))
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
        self.resistance_measurement_port.setGeometry(QtCore.QRect(1220, 230, 16, 16))
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
        self.Common_port.setGeometry(QtCore.QRect(1260, 230, 16, 16))
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
        self.label_19.setGeometry(QtCore.QRect(1245, 193, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(62, 62, 62);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.pushButton_partA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_partA.setGeometry(QtCore.QRect(40, 60, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_partA.setFont(font)
        self.pushButton_partA.setStyleSheet("QPushButton{\n"
"border: 2px solid;\n"
"border-top-color: rgb(234, 234, 234);\n"
"border-left-color: rgb(234, 234, 234);\n"
"border-bottom-color: rgb(234, 234, 234);\n"
"color: rgb(71, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(223, 74, 0);\n"
"}\n"
"")
        self.pushButton_partA.setObjectName("pushButton_partA")
        self.listWidget_Drag_C1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Drag_C1.setGeometry(QtCore.QRect(45, 155, 101, 51))
        self.listWidget_Drag_C1.setStyleSheet("QListWidget{\n"
"border: 1px solid;\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"background-color: white;\n"
"}")
        self.listWidget_Drag_C1.setObjectName("listWidget_Drag_C1")
        self.listWidget_Drag_R1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Drag_R1.setGeometry(QtCore.QRect(70, 240, 61, 101))
        self.listWidget_Drag_R1.setStyleSheet("QListWidget{\n"
"border: 1px solid;\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"background-color: white;\n"
"}")
        self.listWidget_Drag_R1.setObjectName("listWidget_Drag_R1")
        self.listWidget_Drag_L1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Drag_L1.setGeometry(QtCore.QRect(70, 380, 61, 101))
        self.listWidget_Drag_L1.setStyleSheet("QListWidget{\n"
"border: 1px solid;\n"
"border-right-color: rgb(255, 255, 255);\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"border-left-color: rgb(255, 255, 255);\n"
"background-color: white;\n"
"}")
        self.listWidget_Drag_L1.setObjectName("listWidget_Drag_L1")
        self.partB_R1_right_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.partB_R1_right_label_2.setGeometry(QtCore.QRect(570, 155, 80, 7))
        self.partB_R1_right_label_2.setStyleSheet("background-color: rgb(200, 136, 91);\n"
"border-radius:3px;")
        self.partB_R1_right_label_2.setText("")
        self.partB_R1_right_label_2.setObjectName("partB_R1_right_label_2")
        self.partB_R1_value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.partB_R1_value_2.setGeometry(QtCore.QRect(660, 440, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.partB_R1_value_2.setFont(font)
        self.partB_R1_value_2.setStyleSheet("QLineEdit{\n"
"border:none;\n"
"border-radius: 15px;\n"
"}")
        self.partB_R1_value_2.setText("")
        self.partB_R1_value_2.setObjectName("partB_R1_value_2")
        self.listWidget_Drop_partB_1_R1_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Drop_partB_1_R1_2.setGeometry(QtCore.QRect(590, 143, 141, 41))
        self.listWidget_Drop_partB_1_R1_2.setStyleSheet("QListWidget{\n"
"border-radius: 20px;\n"
"border: 2px dashed;\n"
"border-color: rgb(170, 125, 111, 0.2);\n"
"background-color: rgb(198, 237, 207);\n"
"}")
        self.listWidget_Drop_partB_1_R1_2.setObjectName("listWidget_Drop_partB_1_R1_2")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(460, 440, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("background-color: rgb(198, 237, 207);\n"
"color: rgb(71, 0, 0);")
        self.label_50.setObjectName("label_50")
        self.partB_1_v1_Top_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.partB_1_v1_Top_label_2.setGeometry(QtCore.QRect(380, 160, 7, 80))
        self.partB_1_v1_Top_label_2.setStyleSheet("background-color: rgb(200, 136, 91);\n"
"border-radius:3px;")
        self.partB_1_v1_Top_label_2.setText("")
        self.partB_1_v1_Top_label_2.setObjectName("partB_1_v1_Top_label_2")
        self.partB_R1_name_2 = QtWidgets.QLabel(self.centralwidget)
        self.partB_R1_name_2.setGeometry(QtCore.QRect(650, 115, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.partB_R1_name_2.setFont(font)
        self.partB_R1_name_2.setStyleSheet("background-color: rgb(198, 237, 207);\n"
"color: rgb(71, 0, 0);")
        self.partB_R1_name_2.setObjectName("partB_R1_name_2")
        self.PartA_window_3 = QtWidgets.QLabel(self.centralwidget)
        self.PartA_window_3.setGeometry(QtCore.QRect(210, 60, 861, 471))
        self.PartA_window_3.setStyleSheet("QLabel{    \n"
"    background-color: rgb(54, 248, 100, 0.2);\n"
"border-radius:40px;\n"
"}")
        self.PartA_window_3.setText("")
        self.PartA_window_3.setObjectName("PartA_window_3")
        self.partB_1_v1_name_2 = QtWidgets.QLabel(self.centralwidget)
        self.partB_1_v1_name_2.setGeometry(QtCore.QRect(320, 275, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.partB_1_v1_name_2.setFont(font)
        self.partB_1_v1_name_2.setStyleSheet("QLabel{\n"
"    background-color: rgb(198, 237, 207);\n"
"    color: rgb(71, 0, 0);\n"
"}")
        self.partB_1_v1_name_2.setObjectName("partB_1_v1_name_2")
        self.partB_1_v1_value_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.partB_1_v1_value_2.setGeometry(QtCore.QRect(660, 440, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.partB_1_v1_value_2.setFont(font)
        self.partB_1_v1_value_2.setStyleSheet("QLineEdit{\n"
"border:none;\n"
"border-radius: 15px;\n"
"}")
        self.partB_1_v1_value_2.setText("")
        self.partB_1_v1_value_2.setObjectName("partB_1_v1_value_2")
        self.partB_1_submit_pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.partB_1_submit_pushButton_2.setGeometry(QtCore.QRect(810, 440, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.partB_1_submit_pushButton_2.setFont(font)
        self.partB_1_submit_pushButton_2.setStyleSheet("QPushButton{\n"
"border:none;\n"
"border-radius:10px;\n"
"}")
        self.partB_1_submit_pushButton_2.setObjectName("partB_1_submit_pushButton_2")
        self.partB_1_v1_bottom2_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.partB_1_v1_bottom2_label_2.setGeometry(QtCore.QRect(380, 322, 7, 65))
        self.partB_1_v1_bottom2_label_2.setStyleSheet("background-color: rgb(200, 136, 91);\n"
"border-radius:3px;")
        self.partB_1_v1_bottom2_label_2.setText("")
        self.partB_1_v1_bottom2_label_2.setObjectName("partB_1_v1_bottom2_label_2")
        self.partB_1_R1_left_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.partB_1_R1_left_label_2.setGeometry(QtCore.QRect(382, 160, 220, 7))
        self.partB_1_R1_left_label_2.setStyleSheet("background-color: rgb(200, 136, 91);\n"
"border-radius:3px;")
        self.partB_1_R1_left_label_2.setText("")
        self.partB_1_R1_left_label_2.setObjectName("partB_1_R1_left_label_2")
        self.partB_1_v1_bottom_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.partB_1_v1_bottom_label_3.setGeometry(QtCore.QRect(380, 380, 500, 7))
        self.partB_1_v1_bottom_label_3.setStyleSheet("background-color: rgb(200, 136, 91);\n"
"border-radius:3px;")
        self.partB_1_v1_bottom_label_3.setText("")
        self.partB_1_v1_bottom_label_3.setObjectName("partB_1_v1_bottom_label_3")
        self.partB_1_R1_right_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.partB_1_R1_right_label_2.setGeometry(QtCore.QRect(715, 160, 160, 7))
        self.partB_1_R1_right_label_2.setStyleSheet("background-color: rgb(200, 136, 91);\n"
"border-radius:3px;")
        self.partB_1_R1_right_label_2.setText("")
        self.partB_1_R1_right_label_2.setObjectName("partB_1_R1_right_label_2")
        self.listWidget_Drop_partB_1_V1_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_Drop_partB_1_V1_2.setGeometry(QtCore.QRect(355, 235, 61, 100))
        self.listWidget_Drop_partB_1_V1_2.setStyleSheet("QListWidget{\n"
"border-radius: 20px;\n"
"border: 2px dashed;\n"
"border-color: rgb(170, 125, 111, 0.2);\n"
"background-color: rgb(198, 237, 207);\n"
"}")
        self.listWidget_Drop_partB_1_V1_2.setObjectName("listWidget_Drop_partB_1_V1_2")
        self.partB_R1_name_3 = QtWidgets.QLabel(self.centralwidget)
        self.partB_R1_name_3.setGeometry(QtCore.QRect(230, 70, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.partB_R1_name_3.setFont(font)
        self.partB_R1_name_3.setStyleSheet("background-color: rgb(198, 237, 207);\n"
"color: rgb(71, 0, 0);")
        self.partB_R1_name_3.setObjectName("partB_R1_name_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 550, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"  border:none;\n"
" background-color: rgb(167, 195, 200);\n"
" border-radius:8px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  border:2px solid white;\n"
"  \n"
"    background-color: rgb(120, 192, 200);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 550, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"  border:none;\n"
" background-color: rgb(167, 195, 200);\n"
" border-radius:8px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"  border:2px solid white;\n"
"  \n"
"    background-color: rgb(120, 192, 200);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.partB_1_V1_bottom_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.partB_1_V1_bottom_button_2.setGeometry(QtCore.QRect(365, 333, 36, 36))
        self.partB_1_V1_bottom_button_2.setStyleSheet("QPushButton{\n"
"border-radius: 18px;\n"
"border: 2px dashed;\n"
"border-color: rgb(170, 125, 111, 0.2);\n"
"background-color: rgb(198, 237, 207);\n"
"}")
        self.partB_1_V1_bottom_button_2.setText("")
        self.partB_1_V1_bottom_button_2.setObjectName("partB_1_V1_bottom_button_2")
        self.partB_1_v1Top_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.partB_1_v1Top_button_2.setGeometry(QtCore.QRect(365, 205, 36, 36))
        self.partB_1_v1Top_button_2.setStyleSheet("QPushButton{\n"
"border-radius: 18px;\n"
"border: 2px dashed;\n"
"border-color: rgb(170, 125, 111, 0.2);\n"
"background-color: rgb(198, 237, 207);\n"
"}")
        self.partB_1_v1Top_button_2.setText("")
        self.partB_1_v1Top_button_2.setObjectName("partB_1_v1Top_button_2")
        self.partB_1_V1_bottom_button_22 = QtWidgets.QPushButton(self.centralwidget)
        self.partB_1_V1_bottom_button_22.setGeometry(QtCore.QRect(860, 365, 36, 36))
        self.partB_1_V1_bottom_button_22.setStyleSheet("QPushButton{\n"
"border-radius: 18px;\n"
"border: 2px dashed;\n"
"border-color: rgb(170, 125, 111, 0.2);\n"
"background-color: rgb(198, 237, 207);\n"
"}")
        self.partB_1_V1_bottom_button_22.setText("")
        self.partB_1_V1_bottom_button_22.setObjectName("partB_1_V1_bottom_button_22")
        self.partB_1_R1_right_button_22 = QtWidgets.QPushButton(self.centralwidget)
        self.partB_1_R1_right_button_22.setGeometry(QtCore.QRect(860, 145, 36, 36))
        self.partB_1_R1_right_button_22.setStyleSheet("QPushButton{\n"
"border-radius: 18px;\n"
"border: 2px dashed;\n"
"border-color: rgb(170, 125, 111, 0.2);\n"
"background-color: rgb(198, 237, 207);\n"
"}")
        self.partB_1_R1_right_button_22.setText("")
        self.partB_1_R1_right_button_22.setObjectName("partB_1_R1_right_button_22")
        self.partB_1_R1_left_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.partB_1_R1_left_button_2.setGeometry(QtCore.QRect(560, 145, 36, 36))
        self.partB_1_R1_left_button_2.setStyleSheet("QPushButton{\n"
"border-radius: 18px;\n"
"border: 2px dashed;\n"
"border-color: rgb(170, 125, 111, 0.2);\n"
"background-color: rgb(198, 237, 207);\n"
"}")
        self.partB_1_R1_left_button_2.setText("")
        self.partB_1_R1_left_button_2.setObjectName("partB_1_R1_left_button_2")
        self.partB_1_R1_right_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.partB_1_R1_right_button_2.setGeometry(QtCore.QRect(720, 145, 36, 36))
        self.partB_1_R1_right_button_2.setStyleSheet("QPushButton{\n"
"border-radius: 18px;\n"
"border: 2px dashed;\n"
"border-color: rgb(170, 125, 111, 0.2);\n"
"background-color: rgb(198, 237, 207);\n"
"}")
        self.partB_1_R1_right_button_2.setText("")
        self.partB_1_R1_right_button_2.setObjectName("partB_1_R1_right_button_2")
        self.partB_R1_right_label_2.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_31.raise_()
        self.pushButton_Lab_Manual.raise_()
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
        self.pushButton_partA.raise_()
        self.listWidget_Drag_C1.raise_()
        self.listWidget_Drag_R1.raise_()
        self.listWidget_Drag_L1.raise_()
        self.PartA_window_3.raise_()
        self.label_50.raise_()
        self.partB_R1_value_2.raise_()
        self.partB_1_submit_pushButton_2.raise_()
        self.listWidget_Drop_partB_1_V1_2.raise_()
        self.listWidget_Drop_partB_1_R1_2.raise_()
        self.partB_R1_name_2.raise_()
        self.partB_1_v1_value_2.raise_()
        self.partB_R1_name_3.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.partB_1_V1_bottom_button_2.raise_()
        self.partB_1_v1Top_button_2.raise_()
        self.partB_1_V1_bottom_button_22.raise_()
        self.partB_1_R1_right_button_22.raise_()
        self.partB_1_R1_left_button_2.raise_()
        self.partB_1_R1_right_button_2.raise_()
        self.partB_1_v1_bottom_label_3.raise_()
        self.partB_1_v1_bottom2_label_2.raise_()
        self.partB_1_R1_right_label_2.raise_()
        self.partB_1_R1_left_label_2.raise_()
        self.partB_1_v1_Top_label_2.raise_()
        self.partB_1_v1_name_2.raise_()

        R3 = QListWidgetItem(QIcon("Resistor_icon2.png"), "")
        self.listWidget_Drag_R1.insertItem(1, R3)
        self.listWidget_Drag_R1.setIconSize(QSize(60, 110))
        C1 = QListWidgetItem(QIcon("Resistor_icon.png"), "")
        self.listWidget_Drag_C1.insertItem(1, C1)
        self.listWidget_Drag_C1.setIconSize(QSize(85, 35))
        self.L1 = QListWidgetItem(QIcon("Battery_icon.png"), "")
        self.listWidget_Drag_L1.insertItem(1, self.L1)
        self.listWidget_Drag_L1.setIconSize(QSize(35, 80))
        self.listWidget_Drag_C1.setDragEnabled(True)
        self.listWidget_Drag_R1.setDragEnabled(True)
        self.listWidget_Drag_L1.setDragEnabled(True)

        self.listWidget_Drop_partB_1_R1_2.setAcceptDrops(True)
        self.listWidget_Drop_partB_1_V1_2.setAcceptDrops(True)

        self.listWidget_Drop_partB_1_R1_2.setIconSize(QSize(125, 220))
        self.listWidget_Drop_partB_1_V1_2.setIconSize(QSize(195, 85))
        self.listWidget_Drop_partB_1_R1_2.doubleClicked.connect(self.display_value)
        self.listWidget_Drop_partB_1_R1_2.clicked.connect(self.set_theve_R1_value)
        self.listWidget_Drop_partB_1_V1_2.clicked.connect(self.set_theve_V1_value)
        self.partB_1_submit_pushButton_2.clicked.connect(self.assign_value)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def set_theve_R1_value(self):
            self.partB_R1_value_2.show(), self.partB_1_v1_value_2.hide()

    def set_theve_V1_value(self):
            self.partB_R1_value_2.hide(), self.partB_1_v1_value_2.show()


    def assign_value(self):
            self.rr =self.partB_R1_value_2.text()
            self.vv = self.partB_1_v1_value_2.text()
            print(self.vv)
    def display_value(self):
            R = float(self.rr)
            V = float(self.vv)
            I = V/R
            self.Multimeter_value_displayer.setText(" R1 = {0}Ω \n V1 = {1}V \n I1 = {2}A".format(self.rr, self.vv, I))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Experiment One"))
        self.label.setText(_translate("MainWindow", "                               KVL,KCL,Thevenin\'s Theorem and Norton\'s Theorem"))
        self.pushButton_Lab_Manual.setText(_translate("MainWindow", "Lab Manual"))
        self.label_15.setText(_translate("MainWindow", "V"))
        self.label_17.setText(_translate("MainWindow", "R"))
        self.label_18.setText(_translate("MainWindow", "A"))
        self.label_19.setText(_translate("MainWindow", "COM"))
        self.pushButton_partA.setText(_translate("MainWindow", "PART B-1"))
        self.partB_R1_value_2.setPlaceholderText(_translate("MainWindow", "  Enter R1 Value"))
        self.label_50.setText(_translate("MainWindow", "Click a component to \n"
"change its value"))
        self.partB_R1_name_2.setText(_translate("MainWindow", "R1"))
        self.partB_1_v1_name_2.setText(_translate("MainWindow", "V1"))
        self.partB_1_v1_value_2.setPlaceholderText(_translate("MainWindow", "  Enter V1 Value"))
        self.partB_1_submit_pushButton_2.setText(_translate("MainWindow", "Ok"))
        self.partB_R1_name_3.setText(_translate("MainWindow", "Thevenin Equivalent Circuit"))
        self.pushButton.setText(_translate("MainWindow", "Original Circuit"))
        self.pushButton_3.setText(_translate("MainWindow", "Norton Equivalent"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = thevenin_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())