class Categoria:

    def __init__(self, nombre, descripcion):
        self.__nombre = nombre
        self.__descripcion = descripcion
    
    @property
    def Nombre(self):
        return self.__nombre

    @Nombre.setter
    def Nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def Descripcion(self):
        return self.__descripcion
    
    @Descripcion.setter
    def Descripcion(self, descripcion):
        self.__descripcion = descripcion
    
    def __str__(self):
        return self.__nombre + " - " + self.__descripcion

    