import sys 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QInputDialog, QListWidget, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import socket 
import threading
import pickle
import json

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

firebaseConfig ={
	'apiKey': "AIzaSyCRUbKV40x0WxXtcirgw7DbLdOP6hPWO74",
	'authDomain': "lemechat-bd.firebaseapp.com",
	'databaseURL' : "",
	'projectId': "lemechat-bd",
	'storageBucket': "lemechat-bd.appspot.com",
	'messagingSenderId': "708805251431",
	'appId': "1:708805251431:web:36c4633fd84795988e9fc2"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

class Login(QMainWindow):
	"""docstring for Login"""
	def __init__(self):
		super(Login, self).__init__()
		loadUi("login.ui", self)
		self.btnEntrar.clicked.connect(self.loginFuncion)
		self.contrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
		self.btnRegistrate.clicked.connect(self.registrate)
		self.labelError.setVisible(False)


	def registrate(self): 
		registrate = Registro()
		widget.addWidget(registrate)
		widget.setCurrentIndex(widget.currentIndex()+1)

	def loginFuncion(self):
		email = self.email.text()
		password = self.contrasenia.text()
		try:
			usuario = auth.sign_in_with_email_and_password(email, password)
			print(usuario)
			print(type(usuario))
			salaDefecto = SalaDefecto()
			salaDefecto.usuario = usuario
			widget.addWidget(salaDefecto)
			widget.setCurrentIndex(widget.currentIndex()+1)
		except Exception as e:
			self.labelError.setVisible(True)
			raise e


class Registro(QMainWindow):
	"""docstring for Registro"""
	def __init__(self):
		super(Registro, self).__init__()
		loadUi("registro.ui", self)
		self.contrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
		self.contrasenia_2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.btnRegistrate.clicked.connect(self.registroFuncion)
		self.labelError.setVisible(False)
		
	def registroFuncion(self):
		email = self.email.text()
		password = self.contrasenia.text()
		password_2 = self.contrasenia_2.text()
		username = self.username.text()
		nombres = self.nombres.text()
		apellidos = self.apellidos.text()
		edad = self.edad.text()
		genero = self.genero.text()

		if password == password_2:
			try:
				auth.create_user_with_email_and_password(email, password)
				db = firestore.client()
				perfil = {'username': username, 'email': email, 'nombres': nombres, 'apellidos': apellidos, 'edad': edad, 'genero': genero}
				db.collection('perfiles').add(perfil)
				login = Login()
				widget.addWidget(login)
				widget.setCurrentIndex(widget.currentIndex()+1)
			except Exception as e:
				self.labelError.setVisible(True)
				raise e

class Comunicate(QtCore.QObject):
	senial = QtCore.pyqtSignal(bytes)

def miHilo(callbackFunc):
	# Setup the signal-slot mechanism.
	miOrigen = Comunicate()
	miOrigen.senial.connect(callbackFunc) 
	while(True):
		try:
			msgParaSala = cliente.recv(1024)
			miOrigen.senial.emit(msgParaSala)
		except:
			cliente.close()
			break

class SalaDefecto(QMainWindow):
	"""docstring for SalaDefecto"""
	def __init__(self):
		super(SalaDefecto, self).__init__()
		loadUi("salaDefecto.ui", self)
		self.btnEnviar.clicked.connect(self.enviar)
		self.actionCrear_Sala.triggered.connect(self.crearSala)
		self.actionCambiar_de_Sala.triggered.connect(self.cambiarSala)
		self.actionSalir_de_la_Sala.triggered.connect(self.salirSala)
		self.actionDesconectar.triggered.connect(self.desconectar)
		self.actionListar_Salas.triggered.connect(self.listarSalas)
		self.usuario = {}
		self.db=firestore.client()


		self.conexion()
		self.iniciarHilo()
		
	def conexion(self):
		'''print(self.usuario)
		usuario = auth.get_account_info(self.usuario['idToken'])
		print(usuario)
		db.firestore.client()
		perfil = self.db.collection('perfiles').where('email', '==', usuario.email)
		print(perfil)
		print(usuario.email)'''
		cliente.connect(('localhost', 8003))
		self.salaActual.setText('Principal')

	def desconectar(self):
		cliente.sendall('#exit'.encode('utf-8'))
		cliente.close()
		login = Login()
		widget.addWidget(login)
		widget.setCurrentIndex(widget.currentIndex()+1)
		print('cliente desconectado...')
		

	def iniciarHilo(self):
		hilo = threading.Thread(target=miHilo, args=(self.recibir,))
		hilo.daemon = True
		hilo.start()

	def recibir(self, mensaje):
		datos = mensaje.decode('utf-8')
		opcion = datos[:10].strip()
		print(opcion)
		if opcion == '#lR':
			self.listarSalasRecv(datos[10:])
		else:
			self.chat.append(mensaje.decode('utf-8'))
			self.chat.setAlignment(Qt.AlignLeft)

	def enviar(self):
		try:
			mensaje = self.campoTexto.toPlainText()
			self.campoTexto.clear()
			self.chat.append(mensaje)
			self.chat.setAlignment(Qt.AlignRight)			
			cliente.sendall(mensaje.encode('utf-8'))
		except:
			cliente.close()

	def crearSala(self):
		nombreSala, ok = QInputDialog.getText(self, 'Crear Sala', 'Nombre de la Sala: ')
		if ok:
			cliente.sendall('#cR'.encode('utf-8'))
			cliente.sendall(nombreSala.encode('utf-8'))
			self.salaActual.setText(nombreSala)
			self.chat.clear()

	def cambiarSala(self):
		nombreSala, ok = QInputDialog.getText(self, 'Cambiar de Sala', 'Nombre de la Sala: ')
		if ok:
			cliente.sendall('#gR'.encode('utf-8'))
			cliente.sendall(nombreSala.encode('utf-8'))
			self.salaActual.setText(nombreSala)
			self.chat.clear()

	def salirSala(self):
		if self.salaActual.text() != 'DEFECTO':
			cliente.sendall('#eR'.encode('utf-8'))
			self.salaActual.setText('DEFECTO')
			self.chat.clear()

	def listarSalas(self):
		cliente.sendall('#lR'.encode('utf-8'))

	def listarSalasRecv(self, mensaje):
		salasDisponibles = json.loads(mensaje)
		vistaListar = Dialog(self)
		vistaListar.listar(salasDisponibles)
		vistaListar.show()
		

class Dialog(QDialog):
	def __init__(self, *args, **kwargs):
		super(Dialog, self).__init__(*args, **kwargs)
		self.setWindowTitle("Salas Disponibles")
		self.setFixedSize(300, 400)
		self.listaSalas = QListWidget()
		

	def listar(self, salas):
		layout = QVBoxLayout()
		for sala, num in salas.items():
			mensaje = 'Sala: {} : Usuarios conectatos({})'.format(sala, num)
			self.listaSalas.addItem(mensaje)
		layout.addWidget(self.listaSalas)
		self.setLayout(layout)



cliente = socket.socket() 
app = QApplication(sys.argv)
mainWindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(640)
widget.setFixedHeight(456)
widget.show()
app.exec()
