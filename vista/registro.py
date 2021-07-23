# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro.ui'
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
        self.label.setGeometry(QtCore.QRect(220, 10, 191, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255); font-size: 28pt;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 161, 21))
        self.label_2.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 14pt;")
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(250, 90, 211, 31))
        self.email.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"background-color: rgb(46, 52, 54);")
        self.email.setObjectName("email")
        self.contrasenia = QtWidgets.QLineEdit(self.centralwidget)
        self.contrasenia.setGeometry(QtCore.QRect(250, 140, 211, 31))
        self.contrasenia.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);\n"
"border-color:rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"")
        self.contrasenia.setObjectName("contrasenia")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 14pt;")
        self.label_3.setObjectName("label_3")
        self.btnRegistrate = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrate.setGeometry(QtCore.QRect(260, 390, 111, 41))
        self.btnRegistrate.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.btnRegistrate.setObjectName("btnRegistrate")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 181, 21))
        self.label_4.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 14pt;")
        self.label_4.setObjectName("label_4")
        self.contrasenia_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.contrasenia_2.setGeometry(QtCore.QRect(250, 190, 211, 31))
        self.contrasenia_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);\n"
"border-color:rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"")
        self.contrasenia_2.setObjectName("contrasenia_2")
        self.labelError = QtWidgets.QLabel(self.centralwidget)
        self.labelError.setGeometry(QtCore.QRect(470, 100, 101, 16))
        self.labelError.setStyleSheet("color: rgb(164, 0, 0);")
        self.labelError.setObjectName("labelError")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 14pt;")
        self.label_5.setObjectName("label_5")
        self.nombres = QtWidgets.QLineEdit(self.centralwidget)
        self.nombres.setGeometry(QtCore.QRect(140, 300, 171, 31))
        self.nombres.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"background-color: rgb(46, 52, 54);")
        self.nombres.setObjectName("nombres")
        self.apellidos = QtWidgets.QLineEdit(self.centralwidget)
        self.apellidos.setGeometry(QtCore.QRect(440, 300, 171, 31))
        self.apellidos.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"background-color: rgb(46, 52, 54);")
        self.apellidos.setObjectName("apellidos")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 14pt;")
        self.label_6.setObjectName("label_6")
        self.edad = QtWidgets.QLineEdit(self.centralwidget)
        self.edad.setGeometry(QtCore.QRect(140, 340, 71, 31))
        self.edad.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"background-color: rgb(46, 52, 54);")
        self.edad.setObjectName("edad")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 14pt;")
        self.label_7.setObjectName("label_7")
        self.genero = QtWidgets.QLineEdit(self.centralwidget)
        self.genero.setGeometry(QtCore.QRect(440, 340, 141, 31))
        self.genero.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"background-color: rgb(46, 52, 54);")
        self.genero.setObjectName("genero")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 340, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 14pt;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 240, 181, 21))
        self.label_9.setStyleSheet("color: rgb(245, 121, 0);\n"
"font-size: 14pt;")
        self.label_9.setObjectName("label_9")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(250, 240, 211, 31))
        self.username.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"font-size:17pt;\n"
"background-color: rgb(46, 52, 54);")
        self.username.setObjectName("username")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Registrate!"))
        self.label_2.setText(_translate("MainWindow", "Correo Electronico:"))
        self.label_3.setText(_translate("MainWindow", "Contraseña:"))
        self.btnRegistrate.setText(_translate("MainWindow", "Registrate"))
        self.label_4.setText(_translate("MainWindow", "Confirme contraseña:"))
        self.labelError.setText(_translate("MainWindow", "Correo invalido"))
        self.label_5.setText(_translate("MainWindow", "Nombres:"))
        self.label_6.setText(_translate("MainWindow", "Apellidos:"))
        self.label_7.setText(_translate("MainWindow", "Edad:"))
        self.label_8.setText(_translate("MainWindow", "Genero:"))
        self.label_9.setText(_translate("MainWindow", "Nombre de Usuario:"))
