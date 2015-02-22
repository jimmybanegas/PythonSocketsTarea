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


def listar(empleados):
    cambio=tasas().split(',')
    venta = cambio[1]
    todos=empleados.split(',')
    for i, val in enumerate(todos):
        if len(val.split(' '))>4:
          #print (i, val.split(' '))
          emp = val.split(' ')
          print(Empleado.dolares(emp[0],emp[1]+' '+emp[2],emp[3],emp[5],emp[4],emp[6].replace("\n", ""),venta))


def tasas():
    return getTasas()

def modificar(codigo):
    nombre = input('Ingrese el nombre y apellidos: ')
    correo = input('Ingrese el correo: ')
    salario = input('Ingrese el salario: ')
    identidad = input('Ingrese la identidad: ')
    telefono = input('Ingrese el teléfono: ')
    return Empleado.agregarEmpleado(codigo,nombre,correo,salario,identidad,telefono)

