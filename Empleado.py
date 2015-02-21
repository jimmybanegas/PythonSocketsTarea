import random
import socket
import string

__author__ = 'Jimmy Banegas'

import re

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
        self.sueldo = str(suel)
        self.identidad = id
        self.telefono = tel

    def getNextCodigo(self):
        codigo=(random_char(2)+ str(random.randint(0,9))+str(random.randint(0,9)))
        return str(codigo)


    def toString(self):
        return (self.codigo+' '+self.nombre+' '+self.correo+' '+self.identidad+' '+
                self.sueldo+' '+self.telefono)

    @classmethod
    def agregarEmpleado(self, codigo, nombre, correo, salario, identidad, telefono):
        if not codigoEsValido(codigo):
            return ("Codigo incorrecto o repetido",False)

        if not correoEsValido(correo):
            return ("Correo incorrecto o ya existe",False)

        if not identidadEsValida(identidad):
            return ("Identidad incorrecta o ya existe",False)

        if not nombreEsValido(nombre):
            return ("Formato de nombre no válido",False)

        if not salarioEsvalido(salario):
            return ("Formato de salario no válido",False)

        if not telefonoEsValido(telefono):
            return ("Telefono incorrecto o repetido",False)

        empleado= Empleado()
        empleado.inicializar(codigo,nombre,correo,salario,identidad,telefono)
        return (empleado.toString(),True)
