import socket

__author__ = 'Jimmy Banegas'

def iniciarCliente():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 2222

    print('Connecting to the server...')
    s.connect((host, port))
    print('Connection established...')

    msg = s.recv(1024)

    return s,msg