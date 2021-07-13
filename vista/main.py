import sys 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QInputDialog, QListWidget, QVBoxLayout, QtWidget
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
				db.collection('perfiles').document(email).set(perfil)
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
		self.actionUsuarios_conectados.triggered.connect(self.showUsers)
		self.usuario = {}
		self.db=firestore.client()


		self.conexion()
		self.iniciarHilo()
		
	def conexion(self):
		db = firestore.client()
		perfil = db.collection('perfiles').where("email","==",auth.current_user['email']).get()
		per = perfil[0].to_dict()
		print(per['username'])
		un=per['username']### user name
		cliente.connect(('localhost', 8004))
		self.salaActual.setText('Principal')
		datos = '#nM<{}>'.format(un)
		cliente.sendall(datos.encode('utf-8'))

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
		elif opcion == '#sU':
			self.listarUsuariosRecv(datos[10:])
		else:
			mensajeun = json.loads(datos)
			self.chat.setAlignment(Qt.AlignLeft)
			self.chat.append('{}: {}'.format(mensajeun['username'],mensajeun['mensaje']))

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
			datos = '#cR<{}>'.format(nombreSala)
			print(datos)
			cliente.sendall(datos.encode('utf-8'))
			self.salaActual.setText(nombreSala)
			self.chat.clear()

	def cambiarSala(self):
		nombreSala, ok = QInputDialog.getText(self, 'Cambiar de Sala', 'Nombre de la Sala: ')
		if ok:
			datos = '#gR<{}>'.format(nombreSala)
			cliente.sendall(datos.encode('utf-8'))
			self.salaActual.setText(nombreSala)
			self.chat.clear()

	def salirSala(self):
		if self.salaActual.text() != 'DEFECTO':
			cliente.sendall('#eR'.encode('utf-8'))
			self.salaActual.setText('DEFECTO')
			self.chat.clear()

	def listarSalas(self):
		cliente.sendall('#lR'.encode('utf-8'))
		#db = firestore.client()
		# print('##############')
		# print(auth.current_user['email'])
		# print('****************')
		# consulta = db.collection(u'perfiles')
		# perfiles =  consulta.stream()
		# for perfil in perfiles:
		# 	print('{} => {} '.format(perfil.id, perfil.to_dict()))
		# print('***************************************')
		# consulta2 = db.collection(u'perfiles').where('email','==','zel2@mail.com').stream()
		# for item in consulta2:
		# 	print('{} => {} '.format(item.id, item.to_dict()))

	def listarSalasRecv(self, mensaje):
		salasDisponibles = json.loads(mensaje)
		vistaListar = Dialog(self)
		vistaListar.listarSalas(salasDisponibles)
		vistaListar.show()

	def showUsers(self):
		cliente.sendall('#showUsers'.encode('utf-8'))

	def listarUsuariosRecv(self, mensaje):
		usuariosDisponibles = json.loads(mensaje)
		vistaListar = Dialog(self)
		vistaListar.listarUsuarios(usuariosDisponibles)
		vistaListar.show()

	def chatPrivado(self):
		usuario, ok = QInputDialog.getText(self, 'Buscar usuario', 'digita el nombre del usuario: ')
		if ok:
			datos = '#private<{}>'.format(usuario)
			cliente.sendall(datos.encode('utf-8'))
			self.salaActual.setText(usuario)
			self.chat.clear()


class Dialog(QDialog):
	def __init__(self, *args, **kwargs):
		super(Dialog, self).__init__(*args, **kwargs)
		self.setWindowTitle("Salas Disponibles")
		self.setFixedSize(300, 400)
		self.listaDeDatos = QListWidget()
		self.listaDeDatos.clicked.connect(self.opcionesDeUsuario)
		

	def listarSalas(self, salas):
		layout = QVBoxLayout()
		for sala, num in salas.items():
			mensaje = 'Sala: {} : Usuarios conectatos({})'.format(sala, num)
			self.listaDeDatos.addItem(mensaje)
		layout.addWidget(self.listaDeDatos)
		self.setLayout(layout)

	def listarUsuarios(self, usuarios):
		layout = QVBoxLayout()
		for usuario in usuarios:
			self.listaDeDatos.addItem(usuario)
		layout.addWidget(self.listaDeDatos)
		self.setLayout(layout)

	def opcionesDeUsuario(self):
		item = self.listaDeDatos.currentItem()
		print(item.text())





cliente = socket.socket() 
app = QApplication(sys.argv)
mainWindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(640)
widget.setFixedHeight(456)
widget.show()
app.exec()
