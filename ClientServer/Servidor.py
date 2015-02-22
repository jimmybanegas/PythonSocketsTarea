from urllib import request

__author__ = 'Jimmy Banegas'

import socket
import time
import os
from ClientServer.Archivo import *


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


while True:
    client_data = client_socket.recv(1024)
    d = client_data.decode('utf-8')
    tokens = d.split(",")
    if (client_data.decode('utf-8'))=='listar':
        enc=listar()
        client_socket.send(enc.encode('utf-8'))
        continue
    if len(tokens)==2:
        print(tokens[0])
        print(tokens[1])
        editar(tokens[0],tokens[1])
        continue
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
