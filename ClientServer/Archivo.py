import os

__author__ = 'Jimmy Banegas'

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
    archi.seek(0,2)
    archi.write(empleado+'\n')

    archi.close()

def esRepetido(parametro):
    creartxt()
    fn = os.path.join(os.path.abspath('datos.txt'))
    with open(fn, 'r') as inF:
        for line in inF:
            if parametro in line:
                return True
    return False

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


def listar():
    fn = os.path.join(os.path.abspath('datos.txt'))
    lista=' '
    with open(fn, 'r') as inF:
        for line in inF:
            lista+=line+','
    return lista