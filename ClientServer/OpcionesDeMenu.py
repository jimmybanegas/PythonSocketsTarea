from ClientServer import Empleado
from ClientServer.TasaCambio import *

__author__ = 'Jimmy Banegas'


def agregar():
    codigo = Empleado.getNextCodigo(Empleado)
    print('Código: '+ codigo)
    nombre = input('Ingrese el nombre y apellidos: ')
    correo = input('Ingrese el correo: ')
    salario = input('Ingrese el salario: ')
    identidad = input('Ingrese la identidad: ')
    telefono = input('Ingrese el teléfono: ')
    return Empleado.agregarEmpleado(codigo,nombre,correo,salario,identidad,telefono)

def buscar(codigo):
    return Empleado.buscarEmpleado(codigo)

def tasas():
    return getTasas()

def modificar(codigo):
    nombre = input('Ingrese el nombre y apellidos: ')
    correo = input('Ingrese el correo: ')
    salario = input('Ingrese el salario: ')
    identidad = input('Ingrese la identidad: ')
    telefono = input('Ingrese el teléfono: ')
    return Empleado.agregarEmpleado(codigo,nombre,correo,salario,identidad,telefono)