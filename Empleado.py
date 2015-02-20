import random
import socket
import string


__author__ = 'Jimmy Banegas'

import re
import json


def correoEsValido(correo):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$', correo.lower()):
        return True;
    else:
        return False;


def identidadEsValida(identidad):
    if re.match('^[0-9]{13}$', identidad):
        return True;
    else:
        return False;


def telefonoEsValido(telefono):
    if re.match('^[0-9]{8}$', telefono):
        return True;
    else:
        return False;


def salarioEsvalido(salario):
    if re.match('[+-]?\d+(\.\d+)?', salario):
        return True;
    else:
        return False;


def codigoEsValido(codigo):
    if re.match('^[A-Z]{2}[0-9]{2}$', codigo):
        return True;
    else:
        return False;


def nombreEsValido(nombre):
    if re.match('^[A-Za-záéíóúñ]{2,}([\s][A-Za-záéíóúñ]{2,})+$', string.capwords(nombre)):
        return True;
    else:
        return False;


def random_char(y):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))


class Empleado:
    def inicializar(self, cod, nom, email, suel, id, tel):
        self.codigo = cod
        self.nombre = nom
        self.correo = email
        self.sueldo = suel
        self.identidad = id
        self.telefono = tel

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def getNextCodigo(self):
        codigo=(random_char(2)+ str(random.randint(0,9))+str(random.randint(0,9)))
        return str(codigo)

    def imprimirDatos(self):
        print(self.codigo
              + ' - ' + self.nombre
              + ' - ' + self.correo
              + ' - ' + self.identidad
              + ' - ' + "{0:.2f}".format(self.sueldo)
              + ' - ' + self.telefono)

    def __str__(self):
        return (self.codigo,self.nombre,self.correo,self.identidad,str(self.sueldo),self.telefono)

    @classmethod
    def agregarEmpleado(self, codigo, nombre, correo, salario, identidad, telefono):
        if not codigoEsValido(codigo):
            return "Codigo incorrecto o repetido"

        if not correoEsValido(correo):
            return "Correo incorrecto o ya existe"

        if not identidadEsValida(identidad):
            return "Identidad incorrecta o ya existe"

        if not nombreEsValido(nombre):
            return "Formato de nombre no válido"

        if not salarioEsvalido(salario):
            return "Formato de salario no válido"

        if not telefonoEsValido(telefono):
            return "Telefono incorrecto o repetido"

        empleado= Empleado()
        empleado.inicializar(self,codigo,nombre,correo,identidad,telefono)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 2222

        print('Connecting to the server...')
        s.connect((host, port))
        print('Connection established...')

        s.recv(1024)

        s.sendall(str(empleado.__str__()).encode('utf-8'))

        return "Agregado"

    @classmethod
    def buscarEmpleado(cls, codigo):
        if not codigoEsValido(codigo):
            return None
        else:
            return Empleado()

    @classmethod
    def editarEmpleado(cls, codigo, nombre, correo, salario, identidad, telefono):
        pass

emp1=Empleado()
emp1.inicializar('001','Juan','j.ramos@affisa.hn',3500,'1806','94621230')
emp1.imprimirDatos()
print(emp1.__str__())