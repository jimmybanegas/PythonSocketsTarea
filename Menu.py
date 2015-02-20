__author__ = 'Jimmy Banegas'

from Empleado import *

ans=True

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


def modificar():
    codigo = Empleado.getNextCodigo(Empleado)
    print('Código: '+ codigo)
    nombre = input('Ingrese el nombre y apellidos: ')
    correo = input('Ingrese el correo: ')
    salario = input('Ingrese el salario: ')
    identidad = input('Ingrese la identidad: ')
    telefono = input('Ingrese el teléfono: ')
    return Empleado.editarEmpleado(codigo,nombre,correo,salario,identidad,telefono)


while ans:
    print ("""
    1.Insertar Empleado
    2.Modificar Empleado
    3.Buscar Empleado
    4.Listar Empleados
    4.Salir """)
    ans= input("Elija su opción: ")
    if ans=="1":
        respuesta = agregar()
        print(respuesta)
    elif ans=="2":
        codigo = input('Ingrese el código del empleado que quiere modificar: ')
        empleado=buscar(codigo)
        empleado.imprimirDatos()
        respuesta = modificar()
        print("\n Empleado modificado")
    elif ans=="3":
        codigo = input('Ingrese el código del empleado que quiere buscar: ')
        empleado=buscar(codigo)
        empleado.imprimirDatos()
        print("\n Encontrado")
    elif ans=="3":
        print("\n Listado")
    elif ans=="4":
        print("\n Goodbye")
        break
    elif ans !="":
        print("\n Opción no válida")




