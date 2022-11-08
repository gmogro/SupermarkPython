from Ventas.Persona import Persona


class Cliente(Persona):

    def __init__(self,id = 0, nombre = "", apellido="", direccion="", telefono="", fecha_nacimiento="", dni="", email="", tipo_responsabilidad=""):
        self.__id = id
        super().__init__(nombre, apellido, direccion, telefono, fecha_nacimiento,dni)
        self.__email = email
        self.__tipo_responsabilidad = tipo_responsabilidad
        self.__estado = True

    @property
    def Id(self):
        return self.__id
    
    @Id.setter
    def Id(self, id):
        self.__id = id
    
    @property
    def Email(self):
        return self.__email
    
    @Email.setter
    def Email(self, email):
        self.__email = email
    
    @property
    def Tipo_responsabilidad(self):
        return self.__tipo_responsabilidad
    
    @Tipo_responsabilidad.setter
    def Tipo_responsabilidad(self, tipo_responsabilidad):
        self.__tipo_responsabilidad = tipo_responsabilidad
    
    @property
    def Estado(self):
        return self.__estado
    
    @Estado.setter
    def Estado(self, estado):
        self.__estado = estado
    
    def __str__(self):
        return super().__str__() + " - " + self.__email + " - " + self.__tipo_responsabilidad + " - " + self.__estado
    
    def crearCliente(self):
        super().Nombre    = input("Ingrese el nombre del cliente: ")
        super().Apellido  = input("Ingrese el apellido del cliente: ")
        super().Direccion = input("Ingrese la direccion del cliente: ")
        super().Telefono  = input("Ingrese el telefono del cliente: ")
        super().Fecha_nacimiento = input("Ingrese la fecha de nacimiento del cliente: ")
        super().Dni = input("Ingrese el dni del cliente: ")
        self.__email = input("Ingrese el email del cliente: ")
        self.__tipo_responsabilidad = input("Ingrese el tipo de responsabilidad del cliente: ")
        self.__estado = input("Ingrese el estado del cliente: ")
    
    def mostrarCliente(self):
        print("Nombre: ", super().Nombre)
        print("Apellido: ", super().Apellido)
        print("Direccion: ", super().Direccion)
        print("Telefono: ", super().Telefono)
        print("Fecha de nacimiento: ", super().Fecha_nacimiento)
        print("Dni: ", super().Dni)
        print("Email: ", self.__email)
        print("Tipo de responsabilidad: ", self.__tipo_responsabilidad)
        print("Estado: ", self.__estado)

    def modificarCliente(self):
        super().Nombre    = input("Ingrese el nombre del cliente: ")
        super().Apellido  = input("Ingrese el apellido del cliente: ")
        super().Direccion = input("Ingrese la direccion del cliente: ")
        super().Telefono  = input("Ingrese el telefono del cliente: ")
        super().Fecha_nacimiento = input("Ingrese la fecha de nacimiento del cliente: ")
        super().Dni = input("Ingrese el dni del cliente: ")
        self.__email = input("Ingrese el email del cliente: ")
        self.__tipo_responsabilidad = input("Ingrese el tipo de responsabilidad del cliente: ")
        
    
    def eliminarCliente(self):
        self.__estado = False

    
    def listarClientes(self, clientes):
        for cliente in clientes:
            print(cliente.Id)
            print(cliente.Nombre)
            print(cliente.Apellido)
            print(cliente.Direccion)
            print(cliente.Dni)