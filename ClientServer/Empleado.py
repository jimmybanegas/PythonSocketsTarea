from ClientServer.Validaciones import *
__author__ = 'Jimmy Banegas'


def getNextCodigo(self):
    codigo=(random_char(2)+ str(random.randint(0,9))+str(random.randint(0,9)))
    return str(codigo)

def agregarEmpleado(codigo, nombre, correo, salario, identidad, telefono):
    if not codigoEsValido(codigo):
        return ("Codigo incorrecto o repetido",False)

    if not correoEsValido(correo):
        return ("Correo incorrecto o ya existe",False)

    if not identidadEsValida(identidad):
        return ("Identidad incorrecta o ya existe",False)

    if not nombreEsValido(nombre):
        return ("Formato de nombre no válido",False)

    if not salarioEsvalido(salario):
        return ("Formato de salario no válido",False)

    if not telefonoEsValido(telefono):
        return ("Telefono incorrecto o repetido",False)

    empleado= Empleado()
    empleado.inicializar(codigo,nombre,correo,salario,identidad,telefono)
    return (empleado.toString(),True)

class Empleado:
    def inicializar(self, cod, nom, email, suel, id, tel):
        self.codigo = cod
        self.nombre = nom
        self.correo = email
        self.sueldo = str(suel)
        self.identidad = id
        self.telefono = tel

    def toString(self):
        return (self.codigo+' '+self.nombre+' '+self.correo+' '+self.identidad+' '+
                self.sueldo+' '+self.telefono)


