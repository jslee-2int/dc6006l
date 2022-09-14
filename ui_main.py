# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 557)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow, QWidget{\n"
"    font-family: \"맑은 고딕\";\n"
"    \n"
"    background-color: rgb(27, 28, 34);\n"
"}\n"
"QLabel{\n"
"    color: rgb(225, 225, 225);\n"
"}\n"
"QListWidget{\n"
"    color: rgb(140, 140, 140);\n"
"}\n"
"QComboBox{\n"
"    color: rgb(140, 140, 140);\n"
"    border: 1px solid rgb(78, 78, 83);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(61, 59, 64);\n"
"    padding: 3px;\n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"    width: 20px;\n"
"    border: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(200, 0))
        self.frame.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame#frame{\n"
"    background-color: rgb(25, 26, 31);\n"
"    border-right: 1px solid #404146;\n"
"}\n"
"QLabel{\n"
"    background-color: rgb(25, 26, 31);\n"
"    color: rgb(94, 95, 98);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        self.label_8.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(0, 20))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(80, 118, 205);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 70);\n"
"border-radius: 2px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:2px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setStyleSheet("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 27))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_7.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.listWidget = QtWidgets.QListWidget(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.listWidget.setStyleSheet("QScrollBar:vertical {\n"
"    border: 0px solid #000000;\n"
"    margin: 0px 0px 0px 0px;\n"
"                width: 10px; /*스크롤바의 너비*/\n"
"                background:black;\n"
"            }\n"
" \n"
"QScrollBar::handle:vertical {\n"
"                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));\n"
"                min-height: 0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));\n"
"    height: 0 px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_8.addWidget(self.listWidget)
        self.gridLayout.addWidget(self.frame_7, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_10.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"border: 1px solid rgb(80, 118, 205);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 70);\n"
"border-radius: 2px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:2px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_4.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_11.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"border: 1px solid rgb(80, 118, 205);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 70);\n"
"border-radius: 2px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:2px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_4.addWidget(self.pushButton_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_volt = QtWidgets.QLabel(self.frame_2)
        self.label_volt.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        self.label_volt.setFont(font)
        self.label_volt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_volt.setObjectName("label_volt")
        self.verticalLayout_3.addWidget(self.label_volt)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.label_curr = QtWidgets.QLabel(self.frame_3)
        self.label_curr.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        self.label_curr.setFont(font)
        self.label_curr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_curr.setObjectName("label_curr")
        self.verticalLayout_4.addWidget(self.label_curr)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_pow = QtWidgets.QLabel(self.frame_4)
        self.label_pow.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        self.label_pow.setFont(font)
        self.label_pow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pow.setObjectName("label_pow")
        self.verticalLayout_5.addWidget(self.label_pow)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.label_temp = QtWidgets.QLabel(self.frame_5)
        self.label_temp.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        self.label_temp.setFont(font)
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.verticalLayout_6.addWidget(self.label_temp)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMinimumSize(QtCore.QSize(0, 20))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(80, 118, 205);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 70);\n"
"border-radius: 2px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:2px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.frame_8)
        self.label_14.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 0, 1, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        self.frame_11.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(80, 118, 205);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 70);\n"
"border-radius: 2px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:2px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}\n"
"QLineEdit{\n"
"    color: rgb(140, 140, 140);\n"
"    border: 1px solid rgb(78, 78, 83);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(61, 59, 64);\n"
"    padding: 3px;\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.frame_11)
        self.label_17.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_13.addWidget(self.label_17)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_11)
        self.label_19.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame_11)
        self.label_20.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 0, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.verticalLayout_13.addLayout(self.gridLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.centralwidget)
        self.frame_12.setStyleSheet("QFrame{\n"
"border-radius: 8px;\n"
"background-color: rgb(35, 36, 42);\n"
"}\n"
"QPushButton{\n"
"border: 1px solid rgb(80, 118, 205);\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background:rgba(80, 118, 205, 70);\n"
"border-radius: 2px;\n"
"color: rgba(255, 255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgba(80, 118, 205, 200);\n"
"  color:rgba(255, 255, 255, 210);\n"
"  border-radius:2px;\n"
"}\n"
"QPushButton:pressed{\n"
"  background:rgba(80, 118, 205, 100);\n"
"}\n"
"QPushButton:disabled{\n"
"  background:rgba(100, 100, 100, 100);\n"
"  color:rgba(255, 255, 255, 100);\n"
"}\n"
"QLineEdit{\n"
"    color: rgb(140, 140, 140);\n"
"    border: 1px solid rgb(78, 78, 83);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(61, 59, 64);\n"
"    padding: 3px;\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_18 = QtWidgets.QLabel(self.frame_12)
        self.label_18.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(140, 140, 140);")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_14.addWidget(self.label_18)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_21 = QtWidgets.QLabel(self.frame_12)
        self.label_21.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_12)
        self.label_22.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 1, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_8.setMinimumSize(QtCore.QSize(50, 27))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_5.addWidget(self.pushButton_8, 1, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 27))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_5.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_12)
        self.label_23.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 2, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_5.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 27))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 2, 2, 1, 1)
        self.verticalLayout_14.addLayout(self.gridLayout_5)
        self.horizontalLayout_3.addWidget(self.frame_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.listWidget)
        MainWindow.setTabOrder(self.listWidget, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.pushButton_9)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DC-6006L Gui"))
        self.label.setText(_translate("MainWindow", "DC-6006L GUI"))
        self.label_2.setText(_translate("MainWindow", "Contact : https://2int.me/"))
        self.label_8.setText(_translate("MainWindow", "Port Setting"))
        self.label_9.setText(_translate("MainWindow", "Message Window"))
        self.label_10.setText(_translate("MainWindow", "Port"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "115200"))
        self.label_11.setText(_translate("MainWindow", "Baudrate"))
        self.comboBox.setItemText(0, _translate("MainWindow", "COM4"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.label_3.setText(_translate("MainWindow", "Status"))
        self.pushButton_10.setText(_translate("MainWindow", "Send to Msg Windows"))
        self.pushButton_11.setText(_translate("MainWindow", "Stop"))
        self.label_4.setText(_translate("MainWindow", "Voltage"))
        self.label_volt.setText(_translate("MainWindow", "0.00 [V]"))
        self.label_5.setText(_translate("MainWindow", "Current"))
        self.label_curr.setText(_translate("MainWindow", "0.00 [A]"))
        self.label_6.setText(_translate("MainWindow", "Power"))
        self.label_pow.setText(_translate("MainWindow", "0.00 [W]"))
        self.label_7.setText(_translate("MainWindow", "Temperature"))
        self.label_temp.setText(_translate("MainWindow", "0.00 [°C]"))
        self.label_12.setText(_translate("MainWindow", "Setting"))
        self.label_14.setText(_translate("MainWindow", "Power ON/OFF"))
        self.pushButton_3.setText(_translate("MainWindow", "ON"))
        self.pushButton_4.setText(_translate("MainWindow", "OFF"))
        self.label_17.setText(_translate("MainWindow", "Output Setting"))
        self.lineEdit_2.setText(_translate("MainWindow", "1.0"))
        self.label_19.setText(_translate("MainWindow", "Voltage [V]"))
        self.label_20.setText(_translate("MainWindow", "Current [A]"))
        self.lineEdit.setText(_translate("MainWindow", "5.0"))
        self.pushButton_5.setText(_translate("MainWindow", "Set"))
        self.pushButton_6.setText(_translate("MainWindow", "Set"))
        self.label_18.setText(_translate("MainWindow", "Protection Setting"))
        self.label_21.setText(_translate("MainWindow", "Voltage [V]"))
        self.lineEdit_3.setText(_translate("MainWindow", "0.00"))
        self.label_22.setText(_translate("MainWindow", "Current [A]"))
        self.pushButton_8.setText(_translate("MainWindow", "Set"))
        self.pushButton_7.setText(_translate("MainWindow", "Set"))
        self.lineEdit_4.setText(_translate("MainWindow", "0.00"))
        self.label_23.setText(_translate("MainWindow", "Power [W]"))
        self.lineEdit_5.setText(_translate("MainWindow", "0.00"))
        self.pushButton_9.setText(_translate("MainWindow", "Set"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
