# Clase de servidor
import socket                 
import threading
import pickle
import sys
import json

CLIENTES = []
SALAS = {
    'DEFECTO': []
}

class Cliente(threading.Thread):
    def __init__(self, conexion, direccion):                       
        super(Cliente, self).__init__()                      
        self.conexion = conexion          
        self.direccion = direccion
        self.UserName = ''
        self.sala = 'DEFECTO' 

    def difusion(self, datos):
        datosEnviados={'username': self.UserName, 'mensaje': datos.decode('utf-8')}
        datosEnviados = json.dumps(datosEnviados)
        print(datosEnviados)
        for cliente in SALAS[self.sala]:
            if cliente.conexion != self.conexion:
                cliente.conexion.sendall(datosEnviados.encode('utf-8'))

    def crearSala(self, datos):
        print('creando sala...')
        lista = datos.split("<")
        nombreSala = lista[1].split('>')[0]
        SALAS[nombreSala] = [self]
        SALAS[self.sala].remove(self)
        self.sala = nombreSala

        print(SALAS)
        print('sala creada!..')
    
    def cambiarSala(self, datos):
        lista = datos.split("<")
        nombreSala = lista[1].split('>')[0]
        SALAS[self.sala].remove(self)
        self.sala = nombreSala
        SALAS[nombreSala].append(self)

    def salirSala(self):
        SALAS[self.sala].remove(self)
        self.sala = 'DEFECTO'
        SALAS['DEFECTO'].append(self)
        mensaje = 'Se ha salido con exito de la sala!..\nSala actual DEFECTO... '

    def desconectar(self):
        SALAS[self.sala].remove(self)
        self.conexion.close()
        mensaje = 'Se ha desconectado con exito del servidor!..\n'

    def listarSalas(self):
        salasDisponibles={}
        for sala, num in SALAS.items():
            salasDisponibles[sala]=len(num)
        datos = json.dumps(salasDisponibles)
        datos = f"{'#lR':<{10}}"+datos
        self.conexion.sendall(datos.encode('utf-8'))

    def setUserName(self, datos):
        lista = datos.split("<")
        self.UserName = lista[1].split('>')[0]


    def run(self):   
        print('...conectado desde:',self.direccion) 
        while True:
            print('Sala actual: '+self.sala)
            datos=self.conexion.recv(1024)
            print(datos.decode('utf-8'))
            opciones = datos.decode('utf-8')
            print(opciones)   
            if opciones[0] == '#':
                if opciones[:3] == '#cR':
                    self.crearSala(opciones)
                elif opciones[:3] == '#gR':
                    self.cambiarSala(opciones)
                elif opciones[:3] == '#eR':
                    self.salirSala()
                elif opciones[:3] == '#exit':
                    self.desconectar()
                    break
                elif opciones[:3] == '#lR':
                    self.listarSalas()
                elif opciones[:3] == '#nM':
                    self.setUserName(opciones)

            else:
                print(datos.decode('utf-8'))
                self.difusion(datos)
             
        print('...Desconectado cliente:',self.direccion) 
        self.conexion.close()


class Servidor():
    def __init__(self, ip, puerto):
        self.ip = ip
        self.puerto = puerto
        self.servidor = None

    def crearSocket(self):
        self.servidor = socket.socket()
        self.servidor.bind((self.ip, self.puerto))
        self.servidor.listen(5)
    
    def iniciarSocket(self):
        self.crearSocket()                                                                                                                                                                                                                                                                                                                              
        print ("Servidor arriba, pero triste porque no tengo conexiones. pero sigo escuchando!!!...")
        while True:
            conexion, direccion = self.servidor.accept()
            cliente = Cliente(conexion, direccion)
            cliente.start()
            SALAS['DEFECTO'].append(cliente)

        for t in SALAS['DEFECTO']:
            t.join()

        self.servidor.close() 


if __name__ == '__main__':

    servidor = Servidor('localhost', 8004)  
    servidor.iniciarSocket()
     

    
    
