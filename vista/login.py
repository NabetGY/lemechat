# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 40, 221, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255); font-size: 28pt;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 211, 41))
        self.label_2.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 17pt;")
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(312, 116, 251, 51))
        self.email.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"background-color: rgb(46, 52, 54);")
        self.email.setObjectName("email")
        self.contrasenia = QtWidgets.QLineEdit(self.centralwidget)
        self.contrasenia.setGeometry(QtCore.QRect(312, 206, 251, 51))
        self.contrasenia.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);\n"
"border-color:rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"")
        self.contrasenia.setObjectName("contrasenia")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 210, 211, 41))
        self.label_3.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 17pt;")
        self.label_3.setObjectName("label_3")
        self.btnEntrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEntrar.setGeometry(QtCore.QRect(260, 310, 111, 31))
        self.btnEntrar.setStyleSheet("font-size:17pt;\n"
"background-color: rgb(206, 92, 0);")
        self.btnEntrar.setObjectName("btnEntrar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 380, 141, 21))
        self.label_4.setStyleSheet("color: rgb(164, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.btnRegistrate = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrate.setGeometry(QtCore.QRect(340, 370, 111, 41))
        self.btnRegistrate.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.btnRegistrate.setObjectName("btnRegistrate")
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(210, 270, 221, 21))
        self.labelError.setStyleSheet("color: rgb(164, 0, 0);")
        self.labelError.setObjectName("labelError")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Iniciar Sesion"))
        self.label_2.setText(_translate("MainWindow", "Correo Electronico:"))
        self.label_3.setText(_translate("MainWindow", "Contraseña:"))
        self.btnEntrar.setText(_translate("MainWindow", "Entrar"))
        self.label_4.setText(_translate("MainWindow", "No tienes cuenta?..."))
        self.btnRegistrate.setText(_translate("MainWindow", "Registrate"))
        self.labelError.setText(_translate("MainWindow", "Correo o contraseña invalido..."))
