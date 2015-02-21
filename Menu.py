__author__ = 'Jimmy Banegas'

from Empleado import *

ans=True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2222

print('Connecting to the server...')
s.connect((host, port))
print('Connection established...')

msg = s.recv(1024)

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

def modificar(codigo):
    nombre = input('Ingrese el nombre y apellidos: ')
    correo = input('Ingrese el correo: ')
    salario = input('Ingrese el salario: ')
    identidad = input('Ingrese la identidad: ')
    telefono = input('Ingrese el teléfono: ')
    return Empleado.agregarEmpleado(codigo,nombre,correo,salario,identidad,telefono)

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
        print(enc.decode('utf-8'))
    elif ans=="5":
        print("\n Goodbye")
        break
    elif ans !="":
        print("\n Opción no válida")




