__author__ = 'Jimmy Banegas'

from ClientServer.OpcionesDeMenu import *
from ClientServer.Cliente import *

ans=True

s,msg=iniciarCliente()

while ans:
    print ("""
    1.Insertar Empleado
    2.Modificar Empleado
    3.Buscar Empleado
    4.Listar Empleados
    5.Salir """)
    ans= input("Elija su opción: ")
    if ans=="1":
        respuesta,tof = agregar()
        if not tof:
          print(respuesta)
        elif tof:
         s.send(respuesta.encode('utf-8'))
         print("\n Agregado")
    elif ans=="2":
        codigo = input('Ingrese el código del empleado que quiere modificar: ')
        s.send(codigo.encode('utf-8'))
        enc = s.recv(1024)
        res=enc.decode('utf-8')
        if res != ' ':
            print(res)
            respuesta,tof =  modificar(codigo)
            if not tof:
                print(respuesta)
            elif tof:
                s.send(str((codigo+','+respuesta)).encode('utf-8'))
                print("\n Empleado modificado")
        elif res == ' ':
            print('No econtrado')

    elif ans=="3":
        codigo = input('Ingrese el código del empleado que quiere buscar: ')
        s.send(codigo.encode('utf-8'))
        enc = s.recv(1024)
        res=enc.decode('utf-8')
        if res != '':
            print(res)
        elif res:
            print('No econtrado')
    elif ans=="4":
        codigo='listar'
        s.send(codigo.encode('utf-8'))
        enc = s.recv(1024)
        listar(enc.decode('utf-8'))
    elif ans=="5":
        print("\n Saliste!")
        break
    elif ans !="":
        print("\n Opción no válida")




