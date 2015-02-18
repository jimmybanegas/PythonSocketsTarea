__author__ = 'Jimmy Banegas'

import re

def correoEsValido(correo):
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,4}$',correo.lower()):
        return True;
    else:
        return False;


def identidadEsValida(identidad):
    pass


def getNextCodigo(self):
    return 0


def telefonoEsValido(telefono):
    pass


def salarioEsvalido(salario):
    pass


class Empleado:
    def inicializar(self,cod,nom,email,suel,id,tel):
        self.codigo=cod
        self.nombre=nom
        self.correo=email
        self.sueldo=suel
        self.identidad=id
        self.telefono=tel

    def imprimirDatos(self):
        print (self.codigo
               +' - '+self.nombre
               +' - '+self.correo
               +' - '+self.identidad
               +' - '+"{0:.2f}".format(self.sueldo)
               +' - '+self.telefono)

    @classmethod
    def agregarEmpleado(self,codigo,nombre,correo,salario,identidad,telefono):
        if not correoEsValido(correo):
            return "Correo incorrecto o ya existe"

        if not identidadEsValida(identidad):
            return "Identidad incorrecta o ya existe"

        if not salarioEsvalido(salario):
            return "Formato de salario no válido"

        if not telefonoEsValido(telefono):
            return "Telfono incorrecto o repetido"

        return "Agregado"


emp1=Empleado()
emp1.inicializar('001','Juan','j.ramos@affisa.hn',3500,'1806','94621230')
emp1.imprimirDatos()


