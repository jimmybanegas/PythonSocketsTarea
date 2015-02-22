import random
import re
import string
from ClientServer.Archivo import *
__author__ = 'Jimmy Banegas'


def correoEsValido(correo):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$', correo.lower()) and not esRepetido(correo):
        return True;
    else:
        return False;


def identidadEsValida(identidad):
    if re.match('^[0-9]{13}$', identidad) and not esRepetido(identidad):
        return True;
    else:
        return False;


def telefonoEsValido(telefono):
    if re.match('^[0-9]{8}$', telefono) and not esRepetido(telefono):
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