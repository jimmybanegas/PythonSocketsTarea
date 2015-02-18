__author__ = 'Jimmy Banegas'

from Empleado import *

ans=True


def agregar():
    codigo = Empleado.getNextCodigo(Empleado)
    nombre = input('Ingrese el nombre: ')
    correo = input('Ingrese el correo: ')
    salario = input('Ingrese el salirio: ')
    identidad = input('Ingrese la identidad: ')
    telefono = input('Ingrese el telefono: ')
    return Empleado.agregarEmpleado(codigo,nombre,correo,salario,identidad,telefono)


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
        print("\n Empleado modificado")
    elif ans=="3":
        print("\n Found")
    elif ans=="3":
        print("\n Listado")
    elif ans=="4":
        print("\n Goodbye")
        break
    elif ans !="":
        print("\n Opción no válida")




