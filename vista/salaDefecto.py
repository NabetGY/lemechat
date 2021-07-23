# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'salaDefecto.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_salaDefecto(object):
    def setupUi(self, salaDefecto):
        salaDefecto.setObjectName("salaDefecto")
        salaDefecto.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(salaDefecto)
        self.centralwidget.setObjectName("centralwidget")
        self.btnEnviar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnviar.setGeometry(QtCore.QRect(500, 340, 101, 41))
        self.btnEnviar.setObjectName("btnEnviar")
        self.campoTexto = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.campoTexto.setGeometry(QtCore.QRect(160, 340, 331, 41))
        self.campoTexto.setObjectName("campoTexto")
        self.chat = QtWidgets.QTextEdit(self.centralwidget)
        self.chat.setGeometry(QtCore.QRect(160, 50, 441, 271))
        self.chat.setReadOnly(True)
        self.chat.setObjectName("chat")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 141, 19))
        self.label.setObjectName("label")
        self.salaActual = QtWidgets.QLabel(self.centralwidget)
        self.salaActual.setGeometry(QtCore.QRect(300, 20, 67, 19))
        self.salaActual.setObjectName("salaActual")
        salaDefecto.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(salaDefecto)
        self.statusbar.setObjectName("statusbar")
        salaDefecto.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(salaDefecto)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        self.menuinicio = QtWidgets.QMenu(self.menubar)
        self.menuinicio.setObjectName("menuinicio")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        salaDefecto.setMenuBar(self.menubar)
        self.actionCrear_Sala = QtWidgets.QAction(salaDefecto)
        self.actionCrear_Sala.setObjectName("actionCrear_Sala")
        self.actionDesconectar = QtWidgets.QAction(salaDefecto)
        self.actionDesconectar.setObjectName("actionDesconectar")
        self.actionCambiar_de_Sala = QtWidgets.QAction(salaDefecto)
        self.actionCambiar_de_Sala.setObjectName("actionCambiar_de_Sala")
        self.actionSalir_de_la_Sala = QtWidgets.QAction(salaDefecto)
        self.actionSalir_de_la_Sala.setObjectName("actionSalir_de_la_Sala")
        self.actionListar_Salas = QtWidgets.QAction(salaDefecto)
        self.actionListar_Salas.setObjectName("actionListar_Salas")
        self.actionUsuarios_conectados = QtWidgets.QAction(salaDefecto)
        self.actionUsuarios_conectados.setObjectName("actionUsuarios_conectados")
        self.actionMensaje_Privado = QtWidgets.QAction(salaDefecto)
        self.actionMensaje_Privado.setObjectName("actionMensaje_Privado")
        self.menuOpciones.addAction(self.actionCrear_Sala)
        self.menuOpciones.addAction(self.actionCambiar_de_Sala)
        self.menuOpciones.addAction(self.actionSalir_de_la_Sala)
        self.menuOpciones.addAction(self.actionDesconectar)
        self.menuOpciones.addAction(self.actionListar_Salas)
        self.menuOpciones.addAction(self.actionUsuarios_conectados)
        self.menuOpciones.addAction(self.actionMensaje_Privado)
        self.menubar.addAction(self.menuinicio.menuAction())
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(salaDefecto)
        QtCore.QMetaObject.connectSlotsByName(salaDefecto)

    def retranslateUi(self, salaDefecto):
        _translate = QtCore.QCoreApplication.translate
        salaDefecto.setWindowTitle(_translate("salaDefecto", "MainWindow"))
        self.btnEnviar.setText(_translate("salaDefecto", "Enviar"))
        self.label.setText(_translate("salaDefecto", "Bienvenido a la sala:"))
        self.salaActual.setText(_translate("salaDefecto", "TextLabel"))
        self.menuinicio.setTitle(_translate("salaDefecto", "inicio"))
        self.menuOpciones.setTitle(_translate("salaDefecto", "Opciones"))
        self.actionCrear_Sala.setText(_translate("salaDefecto", "Crear Sala"))
        self.actionDesconectar.setText(_translate("salaDefecto", "Desconectar"))
        self.actionCambiar_de_Sala.setText(_translate("salaDefecto", "Cambiar de Sala"))
        self.actionSalir_de_la_Sala.setText(_translate("salaDefecto", "Salir de la Sala actual"))
        self.actionSalir_de_la_Sala.setIconText(_translate("salaDefecto", "Salir de la sala actual"))
        self.actionSalir_de_la_Sala.setToolTip(_translate("salaDefecto", "Salir de la sala actual"))
        self.actionListar_Salas.setText(_translate("salaDefecto", "Listar Salas"))
        self.actionUsuarios_conectados.setText(_translate("salaDefecto", "Usuarios conectados"))
        self.actionMensaje_Privado.setText(_translate("salaDefecto", "Mensaje Privado"))
