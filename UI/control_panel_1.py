# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_waiter_bot(object):
    def setupUi(self, waiter_bot):
        waiter_bot.setObjectName("waiter_bot")
        waiter_bot.resize(669, 808)
        self.label = QtWidgets.QLabel(waiter_bot)
        self.label.setGeometry(QtCore.QRect(0, 10, 651, 41))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(waiter_bot)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 171, 181))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setMinimumSize(QtCore.QSize(0, 29))
        self.label_2.setMaximumSize(QtCore.QSize(157, 23))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setMinimumSize(QtCore.QSize(0, 74))
        self.label_12.setMaximumSize(QtCore.QSize(164, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.battery_low = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.battery_low.setMinimumSize(QtCore.QSize(0, 0))
        self.battery_low.setMaximumSize(QtCore.QSize(165, 37))
        self.battery_low.setObjectName("battery_low")
        self.verticalLayout_3.addWidget(self.battery_low)
        self.tabWidget = QtWidgets.QTabWidget(waiter_bot)
        self.tabWidget.setGeometry(QtCore.QRect(190, 60, 471, 741))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.table_navigation = QtWidgets.QWidget()
        self.table_navigation.setObjectName("table_navigation")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.table_navigation)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 461, 690))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table6.setMinimumSize(QtCore.QSize(0, 88))
        self.table6.setMaximumSize(QtCore.QSize(101, 92))
        self.table6.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.table6.setIcon(icon)
        self.table6.setIconSize(QtCore.QSize(60, 60))
        self.table6.setObjectName("table6")
        self.gridLayout_2.addWidget(self.table6, 3, 2, 1, 1)
        self.table7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table7.setMinimumSize(QtCore.QSize(0, 88))
        self.table7.setMaximumSize(QtCore.QSize(101, 92))
        self.table7.setText("")
        self.table7.setIcon(icon)
        self.table7.setIconSize(QtCore.QSize(60, 60))
        self.table7.setObjectName("table7")
        self.gridLayout_2.addWidget(self.table7, 6, 0, 1, 1)
        self.table1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table1.setMinimumSize(QtCore.QSize(0, 88))
        self.table1.setMaximumSize(QtCore.QSize(101, 92))
        self.table1.setText("")
        self.table1.setIcon(icon)
        self.table1.setIconSize(QtCore.QSize(60, 60))
        self.table1.setObjectName("table1")
        self.gridLayout_2.addWidget(self.table1, 0, 0, 1, 1)
        self.go_table = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.go_table.setMinimumSize(QtCore.QSize(0, 88))
        self.go_table.setMaximumSize(QtCore.QSize(101, 71))
        self.go_table.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_table.setIcon(icon1)
        self.go_table.setIconSize(QtCore.QSize(70, 70))
        self.go_table.setObjectName("go_table")
        self.gridLayout_2.addWidget(self.go_table, 9, 2, 1, 1)
        self.table4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table4.setMinimumSize(QtCore.QSize(0, 88))
        self.table4.setMaximumSize(QtCore.QSize(101, 92))
        self.table4.setText("")
        self.table4.setIcon(icon)
        self.table4.setIconSize(QtCore.QSize(60, 60))
        self.table4.setObjectName("table4")
        self.gridLayout_2.addWidget(self.table4, 3, 0, 1, 1)
        self.return_kitchen = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.return_kitchen.setMinimumSize(QtCore.QSize(0, 88))
        self.return_kitchen.setMaximumSize(QtCore.QSize(101, 71))
        self.return_kitchen.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.return_kitchen.setIcon(icon2)
        self.return_kitchen.setIconSize(QtCore.QSize(60, 60))
        self.return_kitchen.setObjectName("return_kitchen")
        self.gridLayout_2.addWidget(self.return_kitchen, 9, 0, 1, 1)
        self.table9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table9.setMinimumSize(QtCore.QSize(0, 88))
        self.table9.setMaximumSize(QtCore.QSize(101, 92))
        self.table9.setText("")
        self.table9.setIcon(icon)
        self.table9.setIconSize(QtCore.QSize(60, 60))
        self.table9.setObjectName("table9")
        self.gridLayout_2.addWidget(self.table9, 6, 2, 1, 1)
        self.table3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table3.setMinimumSize(QtCore.QSize(0, 88))
        self.table3.setMaximumSize(QtCore.QSize(101, 92))
        self.table3.setText("")
        self.table3.setIcon(icon)
        self.table3.setIconSize(QtCore.QSize(60, 60))
        self.table3.setObjectName("table3")
        self.gridLayout_2.addWidget(self.table3, 0, 2, 1, 1)
        self.table8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table8.setMinimumSize(QtCore.QSize(0, 88))
        self.table8.setMaximumSize(QtCore.QSize(101, 92))
        self.table8.setText("")
        self.table8.setIcon(icon)
        self.table8.setIconSize(QtCore.QSize(60, 60))
        self.table8.setObjectName("table8")
        self.gridLayout_2.addWidget(self.table8, 6, 1, 1, 1)
        self.table2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table2.setMinimumSize(QtCore.QSize(0, 88))
        self.table2.setMaximumSize(QtCore.QSize(101, 92))
        self.table2.setText("")
        self.table2.setIcon(icon)
        self.table2.setIconSize(QtCore.QSize(60, 60))
        self.table2.setObjectName("table2")
        self.gridLayout_2.addWidget(self.table2, 0, 1, 1, 1)
        self.table5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.table5.setMinimumSize(QtCore.QSize(0, 88))
        self.table5.setMaximumSize(QtCore.QSize(101, 92))
        self.table5.setText("")
        self.table5.setIcon(icon)
        self.table5.setIconSize(QtCore.QSize(60, 60))
        self.table5.setObjectName("table5")
        self.gridLayout_2.addWidget(self.table5, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 23))
        self.label_3.setMaximumSize(QtCore.QSize(96, 12))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setMinimumSize(QtCore.QSize(0, 23))
        self.label_6.setMaximumSize(QtCore.QSize(96, 12))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setMinimumSize(QtCore.QSize(0, 23))
        self.label_8.setMaximumSize(QtCore.QSize(96, 12))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 23))
        self.label_5.setMaximumSize(QtCore.QSize(96, 12))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 23))
        self.label_4.setMaximumSize(QtCore.QSize(96, 12))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setMinimumSize(QtCore.QSize(0, 23))
        self.label_7.setMaximumSize(QtCore.QSize(96, 12))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setMinimumSize(QtCore.QSize(0, 23))
        self.label_9.setMaximumSize(QtCore.QSize(96, 12))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setMinimumSize(QtCore.QSize(0, 23))
        self.label_10.setMaximumSize(QtCore.QSize(96, 12))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 8, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setMinimumSize(QtCore.QSize(0, 23))
        self.label_11.setMaximumSize(QtCore.QSize(96, 12))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 8, 2, 1, 1)
        self.start_auto_nav = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.start_auto_nav.setObjectName("start_auto_nav")
        self.gridLayout_2.addWidget(self.start_auto_nav, 9, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_5.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_5.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_5, 4, 1, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_6.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_6.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_6, 4, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_4.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_4, 4, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_7.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_7.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_7, 7, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_8.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_8.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_8, 7, 1, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_9.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_9.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_9, 7, 2, 1, 1)
        self.tabWidget.addTab(self.table_navigation, "")
        self.manual_control = QtWidgets.QWidget()
        self.manual_control.setObjectName("manual_control")
        self.gridLayoutWidget = QtWidgets.QWidget(self.manual_control)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 70, 461, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.F = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.F.setMinimumSize(QtCore.QSize(0, 100))
        self.F.setMaximumSize(QtCore.QSize(102, 100))
        self.F.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("up arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.F.setIcon(icon3)
        self.F.setIconSize(QtCore.QSize(60, 60))
        self.F.setObjectName("F")
        self.gridLayout.addWidget(self.F, 0, 1, 1, 1)
        self.stop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.stop.setMinimumSize(QtCore.QSize(0, 100))
        self.stop.setMaximumSize(QtCore.QSize(102, 100))
        self.stop.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon4)
        self.stop.setIconSize(QtCore.QSize(60, 60))
        self.stop.setObjectName("stop")
        self.gridLayout.addWidget(self.stop, 1, 1, 1, 1)
        self.LF = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.LF.setMinimumSize(QtCore.QSize(0, 100))
        self.LF.setMaximumSize(QtCore.QSize(102, 100))
        self.LF.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("left up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LF.setIcon(icon5)
        self.LF.setIconSize(QtCore.QSize(60, 60))
        self.LF.setAutoDefault(False)
        self.LF.setDefault(False)
        self.LF.setFlat(False)
        self.LF.setObjectName("LF")
        self.gridLayout.addWidget(self.LF, 0, 0, 1, 1)
        self.B = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B.setMinimumSize(QtCore.QSize(0, 100))
        self.B.setMaximumSize(QtCore.QSize(102, 100))
        self.B.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("down arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.B.setIcon(icon6)
        self.B.setIconSize(QtCore.QSize(60, 60))
        self.B.setObjectName("B")
        self.gridLayout.addWidget(self.B, 2, 1, 1, 1)
        self.RF = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RF.setMinimumSize(QtCore.QSize(0, 100))
        self.RF.setMaximumSize(QtCore.QSize(102, 100))
        self.RF.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("right up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RF.setIcon(icon7)
        self.RF.setIconSize(QtCore.QSize(60, 60))
        self.RF.setObjectName("RF")
        self.gridLayout.addWidget(self.RF, 0, 2, 1, 1)
        self.LB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.LB.setMinimumSize(QtCore.QSize(0, 100))
        self.LB.setMaximumSize(QtCore.QSize(102, 100))
        self.LB.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("right down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LB.setIcon(icon8)
        self.LB.setIconSize(QtCore.QSize(60, 60))
        self.LB.setObjectName("LB")
        self.gridLayout.addWidget(self.LB, 2, 0, 1, 1)
        self.RB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.RB.setMinimumSize(QtCore.QSize(0, 100))
        self.RB.setMaximumSize(QtCore.QSize(102, 100))
        self.RB.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("left down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RB.setIcon(icon9)
        self.RB.setIconSize(QtCore.QSize(60, 60))
        self.RB.setObjectName("RB")
        self.gridLayout.addWidget(self.RB, 2, 2, 1, 1)
        self.L = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.L.setMinimumSize(QtCore.QSize(0, 100))
        self.L.setMaximumSize(QtCore.QSize(102, 100))
        self.L.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("left arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.L.setIcon(icon10)
        self.L.setIconSize(QtCore.QSize(60, 60))
        self.L.setObjectName("L")
        self.gridLayout.addWidget(self.L, 1, 0, 1, 1)
        self.R = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.R.setMinimumSize(QtCore.QSize(0, 100))
        self.R.setMaximumSize(QtCore.QSize(102, 100))
        self.R.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("right arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.R.setIcon(icon11)
        self.R.setIconSize(QtCore.QSize(60, 60))
        self.R.setObjectName("R")
        self.gridLayout.addWidget(self.R, 1, 2, 1, 1)
        self.tabWidget.addTab(self.manual_control, "")
        self.mapping = QtWidgets.QWidget()
        self.mapping.setObjectName("mapping")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.mapping)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(100, 50, 291, 381))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.manual_map = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.manual_map.setMinimumSize(QtCore.QSize(0, 100))
        self.manual_map.setObjectName("manual_map")
        self.verticalLayout_2.addWidget(self.manual_map)
        self.autonomous_map = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.autonomous_map.setMinimumSize(QtCore.QSize(0, 100))
        self.autonomous_map.setObjectName("autonomous_map")
        self.verticalLayout_2.addWidget(self.autonomous_map)
        self.map_view = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.map_view.setMinimumSize(QtCore.QSize(0, 100))
        self.map_view.setObjectName("map_view")
        self.verticalLayout_2.addWidget(self.map_view)
        self.tabWidget.addTab(self.mapping, "")
        self.emergency_stop = QtWidgets.QPushButton(waiter_bot)
        self.emergency_stop.setGeometry(QtCore.QRect(20, 300, 141, 100))
        self.emergency_stop.setMinimumSize(QtCore.QSize(0, 100))
        self.emergency_stop.setText("")
        self.emergency_stop.setIcon(icon4)
        self.emergency_stop.setIconSize(QtCore.QSize(65, 65))
        self.emergency_stop.setObjectName("emergency_stop")
        self.verticalLayoutWidget = QtWidgets.QWidget(waiter_bot)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 450, 160, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setMinimumSize(QtCore.QSize(0, 50))
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.bottom_front_cam = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bottom_front_cam.setMinimumSize(QtCore.QSize(0, 62))
        self.bottom_front_cam.setMaximumSize(QtCore.QSize(16777215, 61))
        self.bottom_front_cam.setObjectName("bottom_front_cam")
        self.verticalLayout.addWidget(self.bottom_front_cam)
        self.up_front_cam = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.up_front_cam.setMinimumSize(QtCore.QSize(0, 62))
        self.up_front_cam.setMaximumSize(QtCore.QSize(16777215, 61))
        self.up_front_cam.setObjectName("up_front_cam")
        self.verticalLayout.addWidget(self.up_front_cam)

        self.retranslateUi(waiter_bot)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(waiter_bot)

    def retranslateUi(self, waiter_bot):
        _translate = QtCore.QCoreApplication.translate
        waiter_bot.setWindowTitle(_translate("waiter_bot", "Control Pannel"))
        self.label.setText(_translate("waiter_bot", "RMP Waiter Bot Control"))
        self.label_2.setText(_translate("waiter_bot", "Battery Level"))
        self.label_12.setText(_translate("waiter_bot", "0%"))
        self.battery_low.setText(_translate("waiter_bot", "Battery Low"))
        self.label_3.setText(_translate("waiter_bot", "Table 1"))
        self.label_6.setText(_translate("waiter_bot", "Table 4"))
        self.label_8.setText(_translate("waiter_bot", "Table 6"))
        self.label_5.setText(_translate("waiter_bot", "Table 3"))
        self.label_4.setText(_translate("waiter_bot", "Table 2"))
        self.label_7.setText(_translate("waiter_bot", "Table 5"))
        self.label_9.setText(_translate("waiter_bot", "Table 7"))
        self.label_10.setText(_translate("waiter_bot", "Table 8"))
        self.label_11.setText(_translate("waiter_bot", "Table 9"))
        self.start_auto_nav.setText(_translate("waiter_bot", "Start"))
        self.comboBox_5.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox_5.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox_5.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox_5.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox_5.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox_5.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.comboBox_6.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox_6.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox_6.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox_6.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox_6.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox_6.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.comboBox_3.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox_3.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox_3.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox_3.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox_3.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox_3.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.comboBox_4.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox_4.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox_4.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox_4.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox_4.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox_4.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.comboBox_2.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox_2.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox_2.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox_2.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox_2.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox_2.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.comboBox.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.comboBox_7.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox_7.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox_7.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox_7.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox_7.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox_7.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.comboBox_8.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox_8.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox_8.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox_8.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox_8.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox_8.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.comboBox_9.setItemText(0, _translate("waiter_bot", "Select"))
        self.comboBox_9.setItemText(1, _translate("waiter_bot", "Tray 1"))
        self.comboBox_9.setItemText(2, _translate("waiter_bot", "Tray 2"))
        self.comboBox_9.setItemText(3, _translate("waiter_bot", "Tray 3"))
        self.comboBox_9.setItemText(4, _translate("waiter_bot", "Tray 4"))
        self.comboBox_9.setItemText(5, _translate("waiter_bot", "Tray 5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.table_navigation), _translate("waiter_bot", "Table Navigation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manual_control), _translate("waiter_bot", "Manual Control"))
        self.manual_map.setText(_translate("waiter_bot", "Manual"))
        self.autonomous_map.setText(_translate("waiter_bot", "Autonomous"))
        self.map_view.setText(_translate("waiter_bot", "Map View / Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapping), _translate("waiter_bot", "Mapping"))
        self.label_13.setText(_translate("waiter_bot", "Camera View"))
        self.bottom_front_cam.setText(_translate("waiter_bot", "Bottom Front"))
        self.up_front_cam.setText(_translate("waiter_bot", "Top Front"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    waiter_bot = QtWidgets.QWidget()
    ui = Ui_waiter_bot()
    ui.setupUi(waiter_bot)
    waiter_bot.show()
    sys.exit(app.exec_())
