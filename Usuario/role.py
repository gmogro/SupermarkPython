class Role:

    def __init__(self, id, name, description = "", status = True):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__status = status

    @property
    def Id(self):
        return self.__id

    @Id.setter
    def Id(self, id):
        self.__id = id

    @property
    def Name(self):
        return self.__name
    
    @Name.setter
    def Name(self, name):
        self.__name = name
    
    @property
    def Description(self):
        return self.__description
    
    @Description.setter
    def Description(self, description):
        self.__description = description
    
    @property
    def Status(self):
        return self.__status
    
    @Status.setter
    def Status(self, status):
        self.__status = status
    
    def crearRole(self):
        self.__id = input("Ingrese el ID del role: ")
        self.__name = input("Ingrese el nombre del role: ")
        self.__description = input("Ingrese la descripcion del role: ")

    def eliminarRole(self):
        self.__status = False
    
    def modificarRole(self):
        self.__name = input("Ingrese el nombre del role: ")
        self.__description = input("Ingrese la descripcion del role: ")
    
    def mostrarRole(self):
        print("ID: " + self.__id)
        print("Nombre: " + self.__name)
        print("Descripcion: " + self.__description)
        print("Estado: " + str(self.__status))
    
    def __str__(self):
        return self.__id + " - " + self.__name + " - " + self.__description + " - " + str(self.__status)
    
        