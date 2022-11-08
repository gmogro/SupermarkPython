class Producto:

    def __init__(self, id = "", nombre = "", precio = "", stock = "", id_categoria = 0):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__idcategoria = id_categoria

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
    def Precio(self):
        return self.__precio
    
    @Precio.setter
    def Precio(self, precio):
        self.__precio = precio
    
    @property
    def Stock(self):
        return self.__stock
    
    @Stock.setter
    def Stock(self, stock):
        self.__stock = stock
    
    @property
    def Idcategoria(self):
        return self.__idcategoria
    
    @Idcategoria.setter
    def Idcategoria(self, categoria):
        self.__idcategoria = categoria
    
    def __str__(self):
        return self.__nombre + " - " + str(self.__precio) + " - " + str(self.__stock) + " - " + str(self.__idcategoria)


    def crearProducto(self):
        self.__id = input("Ingrese el ID del producto: ")
        self.__nombre = input("Ingrese el nombre del producto: ")
        self.__precio = float(input("Ingrese el precio del producto: "))
        self.__stock = int(input("Ingrese el stock del producto: "))
        self.__idcategoria = input("Ingrese la categoria del producto: ")

    
    def mostrarProducto(self):
        print("ID: " + self.__id)
        print("Nombre: " + self.__nombre)
        print("Precio: " + str(self.__precio))
        print("Stock: " + str(self.__stock))
        print("Categoria: " + str(self.__idcategoria))
        print("--------------------------------------------------")
    
    def actualizarProducto(self):
        self.__nombre = input("Ingrese el nuevo nombre del producto: ")
        self.__precio = float(input("Ingrese el nuevo precio del producto: "))
        self.__stock = int(input("Ingrese el nuevo stock del producto: "))
        self.__idcategoria = input("Ingrese la nueva categoria del producto: ")
    
    def eliminarProducto(self):
        self.__id = ""
        self.__nombre = ""
        self.__precio = 0
        self.__stock = 0
        self.__idcategoria = ""
    
    def listarProducto(self, lista_productos):
        for producto in lista_productos:
            producto.mostrarProducto()