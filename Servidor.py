__author__ = 'Jimmy Banegas'

import socket
import time


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
client_socket.send(msg.encode('ascii'))

while True:
    client_data = client_socket.recv(1024)
    if client_data:
        print('[CLIENT] {}'.format(client_data.decode('ascii')))
        continue
    print('Closing connection with the client...')
    client_socket.close()
