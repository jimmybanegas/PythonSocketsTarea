from urllib import request

__author__ = 'Jimmy Banegas'

import socket
import time
import os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2222

server_socket.bind((host, port))
server_socket.listen(1)

print('Awaiting connection...')
client_socket, addr = server_socket.accept()

print('Connection established...')
current_time = time.ctime(time.time())
msg = '[{}] You are connected to the server!'.format(current_time)
client_socket.send(msg.encode('utf-8'))

def creartxt():
    try:
        temp = os.path.join(os.path.abspath('datos.txt'))
        archi = open(temp,'r')
        archi.close()
    except:
        temp = os.path.join(os.path.abspath('datos.txt'))
        archi=open(temp,'w')
        archi.write('0\n')
        archi.close()

def grabartxt(empleado):
    fn = os.path.join(os.path.abspath('datos.txt'))
    archi=open(fn,'r+')
    numero_de_registros = archi.readline()
    number = int(numero_de_registros)+1

    pos_ultimo = 6

    if number != 1:
        archi.seek(0,2)
        pos_ultimo = archi.tell()

    archi.seek(0,0)
    archi.write( str(number) + '\n' )
    archi.write(str(pos_ultimo)+'\n')

    archi.seek(pos_ultimo,0)
    archi.write(empleado+'\n')

    archi.close()

def buscar(codigo):
    creartxt()
    fn = os.path.join(os.path.abspath('datos.txt'))
    with open(fn, 'r') as inF:
        for line in inF:
            if codigo in line:
             return line
    return ' '

def editar(codigo,nuevo):
    creartxt()
    fn = os.path.join(os.path.abspath('datos.txt'))
    f = open(fn,'r')
    filedata = f.read()
    f.close()
    ant = buscar(codigo)

    if ant == None:
        return False

    newdata = filedata.replace(ant,nuevo+'\n')

    f = open(fn,'w')
    f.write(newdata)
    f.close()

    return True


while True:
    client_data = client_socket.recv(1024)
    if len(client_data.decode('utf-8'))==4:
        enc=buscar(client_data.decode('utf-8'))
        client_socket.send(enc.encode('utf-8'))
        continue
    if client_data:
        creartxt()
        grabartxt(client_data.decode('utf-8'))
        print('[CLIENT] {}'.format(client_data.decode('utf-8')))
        continue
    print('Closing connection with the client...')
    client_socket.close()
