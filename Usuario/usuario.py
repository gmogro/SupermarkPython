class Usuario:

    def __init__(self, id, nombre, apellido, edad, email, password,estado):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__email = email
        self.__password = password
        self.__estado = estado

    @property
    def Id(self):
        return self.__id

    @Id.setter
    def Id(self, id):
        self.__id = id

    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def Apellido(self):
        return self.__apellido
    
    @Apellido.setter
    def Apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def Edad(self):
        return self.__edad
    
    @Edad.setter
    def Edad(self, edad):
        self.__edad = edad
    
    @property
    def Email(self):
        return self.__email
    
    @Email.setter
    def Email(self, email):
        self.__email = email
    
    @property
    def Password(self):
        return self.__password
    
    @Password.setter
    def Password(self, password):
        self.__password = password
    
    @property
    def Estado(self):
        return self.__estado
    
    @Estado.setter
    def Estado(self, estado):
        self.__estado = estado
    
    def __str__(self):
        return self.__nombre + " - " + self.__apellido + " - " + str(self.__edad) + " - " + self.__email + " - " + self.__password

    def crearUsuario(self):
        self.__nombre = input("Ingrese el nombre del usuario: ")
        self.__apellido = input("Ingrese el apellido del usuario: ")
        self.__edad = int(input("Ingrese la edad del usuario: "))
        self.__email = input("Ingrese el email del usuario: ")
        self.__password = input("Ingrese el password del usuario: ")

    def login(self):
        self.__email = input("Ingrese el email del usuario: ")
        self.__password = input("Ingrese el password del usuario: ")

    def logout(self):
        self.__email = ""
        self.__password = ""
    
    def modificarUsuario(self):
        self.__nombre = input("Ingrese el nombre del usuario: ")
        self.__apellido = input("Ingrese el apellido del usuario: ")
        self.__edad = int(input("Ingrese la edad del usuario: "))
        self.__email = input("Ingrese el email del usuario: ")
        self.__password = input("Ingrese el password del usuario: ")
    
    def eliminarUsuario(self):
        self.__nombre = ""
        self.__apellido = ""
        self.__edad = 0
        self.__email = ""
        self.__password = ""
    
    def mostrarUsuario(self):
        print("Nombre: " + self.__nombre)
        print("Apellido: " + self.__apellido)
        print("Edad: " + str(self.__edad))
        print("Email: " + self.__email)
        print("Password: " + self.__password)

