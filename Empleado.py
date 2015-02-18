__author__ = 'Jimmy Banegas'


def validarCorreo():
    pass


def validarIdentidad():
    pass


def getNextCodigo(self):
    return 0


def validarTelefono():
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
        if validarCorreo():
            ""
        else:
            return "Correo incorrecto o ya existe"

        if validarIdentidad():
            ""
        else:
            return "Identidad incorrecta o ya existe"

        if validarTelefono():
            ""
        else:
            return "Telfono incorrecto o repetido"

        return "Agregado"


emp1=Empleado()
emp1.inicializar('001','Juan','j.ramos@affisa.hn',3500,'1806','94621230')
emp1.imprimirDatos()


