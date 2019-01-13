# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(212, 182)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(212, 182))
        MainWindow.setMaximumSize(QtCore.QSize(212, 182))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 191, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.stateLabel.setObjectName("stateLabel")
        self.verticalLayout.addWidget(self.stateLabel)
        self.stateComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.stateComboBox.setObjectName("stateComboBox")
        self.verticalLayout.addWidget(self.stateComboBox)
        self.favLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.favLabel.setObjectName("favLabel")
        self.verticalLayout.addWidget(self.favLabel)
        self.favSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.favSlider.setMinimum(1)
        self.favSlider.setMaximum(16)
        self.favSlider.setOrientation(QtCore.Qt.Horizontal)
        self.favSlider.setObjectName("favSlider")
        self.verticalLayout.addWidget(self.favSlider)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 212, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Air Purifier 2 CTRL"))
        self.stateLabel.setText(_translate("MainWindow", "State"))
        self.favLabel.setText(_translate("MainWindow", "Favorite FAN Level"))

