from Productos.producto import Producto
from Ventas.Cliente import Cliente
from Ventas.detalle_venta import DetalleVenta


class Venta:

    def __init__(self, cliente, fecha, total, detalle):
        self.___cliente = cliente
        self.__fecha = fecha
        self.__total = total
        self.__detalle = detalle
    
    @property
    def Cliente(self):
        return self.__cliente
    
    @Cliente.setter
    def Cliente(self, cliente):
        self.__cliente = cliente
    
    @property
    def Fecha(self):
        return self.__fecha
    
    @Fecha.setter
    def Fecha(self, fecha):
        self.__fecha = fecha
    
    @property
    def Total(self):
        return self.__total
    
    @Total.setter
    def Total(self, total):
        self.__total = total
    
    @property
    def Detalle(self):
        return self.__detalle
    
    @Detalle.setter
    def Detalle(self, detalle):
        self.__detalle = detalle
    
    def __str__(self):
        return self.__cliente + " - " + self.__fecha + " - " + str(self.__total)
    
    def crearVenta(self):
        cliente1 = Cliente()
        cliente1.crearCliente()
        cliente2 = Cliente()
        cliente2.crearCliente()
        cliente = [cliente1,cliente2]
        cliente2.listarClientes(cliente)
        id_cliente = int(input("Ingrese el id del cliente: "))
        print("### Seleccione el Producto ####")
        i = 0
        while True:
            producto1 = Producto()
            producto1.crearProducto()
            producto2 = Producto()
            producto2.crearProducto()
            producto = [producto1,producto2]
            producto2.listarProductos(producto)
            id_producto = int(input("Ingrese el id del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            subtotal = producto[id_producto].Precio * cantidad
            detalle = DetalleVenta(i,self.__idventa, id_producto, cantidad,subtotal)

        