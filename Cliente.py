__author__ = 'Jimmy Banegas'

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 2222

print('Connecting to the server...')
s.connect((host, port))
print('Connection established...')

msg = s.recv(1024)
print('[SERVER] {}'.format(msg.decode('ascii')))

while True:
    msg = input('Type something: ')
    if not msg:
        s.close()
        break
    s.send(msg.encode('ascii'))
