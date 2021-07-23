import sys 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QInputDialog, QListWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from oauth2client.service_account import ServiceAccountCredentials


import socket 
import threading
import pickle
import json

from login import Ui_MainWindow
from registro import Ui_MainWindow as ui_registro
from salaDefecto import Ui_salaDefecto

variables_keys = {
	"type": "service_account",
	"project_id": "lemechat-bd",
	"private_key_id": "d3f776e770a0b306f16d2d0d63a5912d039d780a",
	"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCdybjDTC77uRH3\nc/8zqVZBghwDww9C0mwXbzx5+n3pkYhr9hwahzmYh8A0IfF5ujbylzRyvGYjgJKC\nDUtoDEc59S1JOI34+wEh2bYFILKKj67nlBVveQ4glowKikdMJmlqyl38czl4L9VI\nG3Q09rmOBcr4Sysyw0ncvHsANpxfxIXhlp6K2sf+ggY8BEe+02+P26e8DHdK77mk\nCpuQMtKxq2FYT7nOiijCuWx3mSqv8O+nwfreKAqlJ7orb6L6EuoIrtK1pwj9Ap26\noc2cUyIxyPbgZv79K6TiLXbh9ACrS+Vu1QROIEq0OTojra0ha1kqRfEWkDIPyr82\n20urorA/AgMBAAECggEAQN2yxSbGkdlNV4sqONS+jwOr/Kft2CylHyUtmX+uz5xy\nlt+AQi+hL+Fu1H+3w7EX8bbTau+klae/kxNgEpApn9v5GAbV5qtZlc7ok0cT3v6e\nirlH7qG3exIo1BRwpw+LeslixeugjpYreg8/QJ7FPWuIO3a7dYzvCn25mybYNk3w\nTYvOpwgBO/HZ11E1CKhOkYBTTBMMlE14wsbK5IrKShFe5ixFcc4ZMgyCZBQZnd6u\n9GWIWh5Yab9wtBx3NTfbJx12/fh2fbymQFA3ZWq3FbNVCPVUd3jnOZDYMNlv3jJO\n1Fnr1aUV2TsLzPNIl77NEDLn9Seuk1BzKT9T85tFcQKBgQDbpX+t4F0wqiyMCWmX\nK0A/q6BpUB6mEnG8zu8rJ6i8uLKWO6ydWd6rIj42xjKza3NZRft9NlL+EAbdjR2D\niIB1eUF9ef9NOzlacNxt0/qXNGke2EIGI8UOX2tB6zvlHYgS3OB/K7ylcvdZzFgV\nDNx9VH2noZM3P+Ldql0rhkP9MwKBgQC350FzHnbmNvGYcMsvH7vwRMf6cPYxFPk8\nb44hTUp9w1itZO941Rl0xQwg4NQ8Ei9ItATkZLRIFR7JPSSw9WkGBmdnGhmGEcMk\nzAS8S+h0LmZzQIGVPiVSgsIJxWONj5tL9cZgiYOYgBgnOa2a3TStluFQPaIzgoz2\nYTxEHHvIxQKBgG7R/6uQ6jPliHhXP2lALzhwtYytGemcoLoshkt1xRMC9UgLb7os\nX8ZkjpNASNBxxE8kmhDA2frJx0z9KAj3VCjxNvPCG+exm+xfyTe4nlSv4uHnJtjG\nL2RjDFDECQI+diteOf6v6IxphxdNnJtyU8UAXi23vflASIyiqkONiLw1AoGBALa4\n01LqRgDfPpTUHU2pHjbQYFH5wuNpj2n4/SMhhI4IdidyTm2kbjKTRkW0natB9jEq\njGHRnT6xnXEdi0M30y3lVwAd8pY/N8Fr5JiiY0hsgeaphRcgND0TJnBG629P7GFA\nxeZNO69eNqFisZdZimmfrCbp1iuP3zc9zX9vPZ5xAoGAI7osvnmVvqBYSDRL3bmr\nSK2ryJdyEehgoOrlYUipVLAWaodReDb1gD45flqIk5mbZQu4SsK4xeVQGkw/uPMP\nxt6ZYBGMfRwQXWtCAkmsb9EFjuUHpifuABSNJQfXvhnO55J2NKdsReqKOzUeMwqQ\nJg+g9/cbR4dYmO7uM0mz10k=\n-----END PRIVATE KEY-----\n",
	"client_email": "firebase-adminsdk-6yuq4@lemechat-bd.iam.gserviceaccount.com",
	"client_id": "111582688757611876986",
	"auth_uri": "https://accounts.google.com/o/oauth2/auth",
	"token_uri": "https://oauth2.googleapis.com/token",
	"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
	"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6yuq4%40lemechat-bd.iam.gserviceaccount.com"
}
with open('data.json', 'w') as fp:
    json.dump(variables_keys, fp)

cred = credentials.Certificate('data.json')
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

class Login(QMainWindow, Ui_MainWindow):
	"""docstring for Login"""
	def __init__(self):
		super(Login, self).__init__()
		self.setupUi(self)
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
		except :
			self.labelError.setVisible(True)
			


class Registro(QMainWindow, ui_registro):
	"""docstring for Registro"""
	def __init__(self):
		super(Registro, self).__init__()
		self.setupUi(self)
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

def miHilo(callbackFunc, stop):
	# Setup the signal-slot mechanism.
	miOrigen = Comunicate()
	miOrigen.senial.connect(callbackFunc) 
	while(True):
		try:
			if stop:
				break
			msgParaSala = cliente.recv(1024)
			miOrigen.senial.emit(msgParaSala)
		except:
			cliente.close()
			break

class SalaDefecto(QMainWindow, Ui_salaDefecto):
	"""docstring for SalaDefecto"""
	def __init__(self):
		super(SalaDefecto, self).__init__()
		self.setupUi(self)
		self.btnEnviar.clicked.connect(self.enviar)
		self.actionCrear_Sala.triggered.connect(self.crearSala)
		self.actionCambiar_de_Sala.triggered.connect(self.cambiarSala)
		self.actionSalir_de_la_Sala.triggered.connect(self.salirSala)
		self.actionDesconectar.triggered.connect(self.desconectar)
		self.actionListar_Salas.triggered.connect(self.listarSalas)
		self.actionUsuarios_conectados.triggered.connect(self.showUsers)
		self.actionMensaje_Privado.triggered.connect(self.mensajePrivado)
		self.msjPrivado = DialogMsg(parent=self)
		self.usuario = {}
		self.db=firestore.client()
		self.conexion()
		self.stop_threads = False
		self.hilo = threading.Thread(target=miHilo, args=(self.recibir,self.stop_threads))
		self.hilo.daemon = True
		self.hilo.start()

	def closeEvent(self, event):
		print('entroo')
		self.desconectar()
		event.accept()
		
	def conexion(self):
		db = firestore.client()
		perfil = db.collection('perfiles').where("email","==",auth.current_user['email']).get()
		per = perfil[0].to_dict()
		un=per['username']### user name
		cliente.connect(('localhost', 8005))
		self.salaActual.setText('Principal')
		datos = '#nM<{}>'.format(un)
		cliente.sendall(datos.encode('utf-8'))

	def desconectar(self):
		cliente.sendall('#exit'.encode('utf-8'))
		cliente.close()
		print('cliente desconectado...')
		self.stop_threads = True
		self.hilo.join()
		self.close()
		sys.exit(app.exec_())

	def recibir(self, mensaje):
		datos = mensaje.decode('utf-8')		
		opcion = datos[:10].strip()
		if opcion == '#lR':
			self.listarSalasRecv(datos[10:])
		elif opcion == '#sU':
			self.listarUsuariosRecv(datos[10:])
		elif opcion == '#cSala':
			self.cambioAutoSala(datos[10:])
		elif opcion == '#cR':
			if datos[10:] == 'False':
				mensaje = '<p style="color:yellow;text-align:left;">(ADVERTENCIA!)<b> LA SALA DIGITADA YA EXISTE!...</b></p>'
				self.chat.append(mensaje)
			else:
				self.salaActual.setText(datos[10:])
				self.chat.clear()
		elif opcion == '#gR':
			if datos[10:] == 'False':
				mensaje = '<p style="color:green;text-align:left;">(ADVERTENCIA!)<b> LA SALA DIGITADA NO EXISTE!...</b></p>'
				self.chat.append(mensaje)
			else:
				self.salaActual.setText(datos[10:])
				self.chat.clear()

		else:
			if len(datos):
				print("entro al else")
				print(len(datos))
				print(type(len(datos)))
				mensajeun = json.loads(datos)
				if 'privado' in mensajeun:
					mensaje = '<p style="color:red;text-align:left;">(PRIVADO!)<b> {}:</b> {}</p>'.format(mensajeun['username'],mensajeun['mensaje'])
				else:
					mensaje = '<p style="color:blue;text-align:left;"><b>{}:</b> {}</p>'.format(mensajeun['username'],mensajeun['mensaje'])
				self.chat.append(mensaje)

	def enviar(self):
		try:

			mensaje = self.campoTexto.toPlainText()
			mensaje2 = '<p style="text-align:right;">{}</p>'.format(mensaje)
			self.campoTexto.clear()
			self.chat.append(mensaje2)
			cliente.sendall(mensaje.encode('utf-8'))
		except:
			cliente.close()

	def crearSala(self):
		nombreSala, ok = QInputDialog.getText(self, 'Crear Sala', 'Nombre de la Sala: ')
		if ok:
			datos = '#cR<{}>'.format(nombreSala)
			cliente.sendall(datos.encode('utf-8'))
			

	def cambiarSala(self):
		nombreSala, ok = QInputDialog.getText(self, 'Cambiar de Sala', 'Nombre de la Sala: ')
		if ok:
			datos = '#gR<{}>'.format(nombreSala)
			cliente.sendall(datos.encode('utf-8'))

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
		vistaListar.listarSalas(salasDisponibles)
		vistaListar.show()

	def showUsers(self):
		cliente.sendall('#showUsers'.encode('utf-8'))

	def listarUsuariosRecv(self, mensaje):
		usuariosDisponibles = json.loads(mensaje)
		vistaListar = Dialog(self)
		vistaListar.listarUsuarios(usuariosDisponibles)
		vistaListar.show()

	def mensajePrivado(self):
		self.msjPrivado.show()

	def mostrarPrivado(self, mensaje):
		self.chat.append(mensaje)


	def cambioAutoSala(self, sala):
		mensaje = '<p style="color:red;text-align:left;"><b>Sala eliminada por su creador.</b> Transferido automaticamente a la sala: DEFECTO</p>'
		self.salaActual.setText(sala)
		self.chat.clear()
		self.chat.append(mensaje)





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
			mensaje																										= 'Sala: {} : Usuarios conectatos({})'.format(sala, num)
			self.listaDeDatos.addItem(mensaje)
		layout.addWidget(self.listaDeDatos)
		self.setLayout(layout)

	def listarUsuarios(self, usuarios):
		layout = QVBoxLayout()																																																																																																																																																																																				
		for usuario in usuarios:
			self.listaDeDatos.addItem(usuario)
		layout.addWidget(self.listaDeDatos)
		self.setLayout(layout)
		self.setWindowTitle("Usuarios conectados")

	def opcionesDeUsuario(self):
		item = self.listaDeDatos.currentItem()
		print(item.text())


class DialogMsg(QDialog):
	def __init__(self, parent=None):
		super(DialogMsg, self).__init__(parent=parent)
		self.setWindowTitle("Mensaje Privado")
		self.setFixedSize(200, 150)
		self.labelUser = QLabel('Nombre del usuario: ')
		self.usuario = QLineEdit()
		self.labelMsg = QLabel('Mensaje: ')
		self.mensaje = QLineEdit()
		self.mensaje.selectAll()
		self.button = QPushButton('Enviar')
		self.button.clicked.connect(self.enviarMensaje)
		layout = QVBoxLayout()
		layout.addWidget(self.labelUser)
		layout.addWidget(self.usuario)
		layout.addWidget(self.labelMsg)
		layout.addWidget(self.mensaje)
		layout.addWidget(self.button)
		self.setLayout(layout)

	def enviarMensaje(self):
		try:
			usuario = self.usuario.text()
			mensaje = self.mensaje.text()
			mensaje2 = '<p style="color:red;text-align:left;">(Msj Privado Enviado)<b>Para</b>: {}. <b>Mensaje:</b> {}</p>.'.format(usuario, mensaje)			
			datos = '#private<{}><{}>'.format(usuario, mensaje)			
			cliente.sendall(datos.encode('utf-8'))
			self.parent().mostrarPrivado(mensaje2)
			self.close()
		except:
			self.close()
			cliente.close()


cliente = socket.socket()
app = QApplication(sys.argv)
mainWindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainWindow)
widget.setFixedWidth(640)
widget.setFixedHeight(456)
widget.show()
app.exec()

